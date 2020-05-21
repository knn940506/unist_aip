import os
import requests
from pprint import pprint

from aip.utils.io import *

WEB_EXAMPLE_BASE = 'http://api.planning.domains'
WEB_SOLVER_BASE = 'http://solver.planning.domains/solve'
WEB_VALIDATE_BASE = 'http://solver.planning.domains/validate'
    
def query(url):
    res = requests.get(url).json()

    if res['error']:
        print("Error: %s" % res['message'])
        return []
    else:
        return res['result']

def get_domain(id):
    """Return the domain for a given domain id"""
    return query(WEB_EXAMPLE_BASE + f"/classical/domain/{id}")

def get_problem(id):
    """Return the problem for a given problem id"""
    return query(WEB_EXAMPLE_BASE + f"/classical/problem/{id}")

def request_solve(domain_path, problem_path, detail=False):
    data = {
        'domain': read_file(domain_path),
        'problem': read_file(problem_path)
        }

    res = requests.post(WEB_SOLVER_BASE, verify=False, json=data).json()

    if res['status'] != 'ok':
        raise RuntimeError('Plan fail')

    if detail:
        return res
    else:
        return [act['name'] for act in res['result']['plan']]

def download_example_set(dir, id):
    res = get_problem(id)

    file_name = os.path.basename(res['domain_path'])
    write_file_from_url(dir, file_name, res['domain_url'])

    file_name = os.path.basename(res['problem_path'])
    write_file_from_url(dir, file_name, res['problem_url'])

def solve_problem(domain_path, problem_path, save_path):
    res = request_solve(domain_path, problem_path, detail=False)

    with open(save_path, 'w') as fp:
        fp.write('\n'.join(res))

if __name__ == '__main__':
    download_example_set(r'C:\Users\kjw940506\source\repos\unist_aip\aip\solver\example', 50)

    dpath = r'C:\Users\kjw940506\source\repos\unist_aip\aip\solver\example\p13-domain.pddl'
    ppath = r'C:\Users\kjw940506\source\repos\unist_aip\aip\solver\example\p13.pddl'
    save_path = ppath.replace('.pddl', '-result.pddl')

    solve_problem(dpath, ppath, save_path)
