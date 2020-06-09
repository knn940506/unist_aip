
(define (domain deliver)
    (:predicates 
        (store ?s)
        (food ?f) 
        (location ?l)

        (driver-at ?location)
        (obj-at ?obj ?l)
    )
                  
    (:functions 
        (total-distance)
        (total-carrying)
        (food-cart ?food)
        (order ?customer ?food)
        (distance ?from - LOCATION ?to - LOCATION)
    )

    (:action move 
        :parameters (?from ?to)
        :precondition (and
            (driver-at ?from)
        )
        :effect (and
            (increase (total-distance) (distance ?from ?to))
            (not (driver-at ?from))
            (driver-at ?to)
        )
    )

    (:action pick-up 
        :parameters (?store)
        :precondition (and
            (driver-at ?location)
            (<= (total-carrying) 7)
        )
        :effect (and 
            (increase (total-carrying) 1)
            (increase (food-cart ?food) 1)
        )
    )
                  
    (:action deliver 
        :parameters (?customer ?food)
        :precondition (and
            (driver-at ?location)
            (> (food-cart ?food) 0)
            (> (order ?customer ?food) 0)
        )
        :effect (and
            (decrease (total-carrying) 1)
            (decrease (food-cart ?food) 1)
            (decrease (order ?customer ?food) 1)
        )
    )
)
