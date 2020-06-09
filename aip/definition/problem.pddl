

(define (problem problem1)
    (:domain deliver)
    (:objects 
        c1 c2 c3 - CUSTOMER
        s1 s2 s3 - STORE
        f1 f2 f3 - FOOD
        l1 l2 l3 - LOCATION
    )

    (:init 
        (customer c1)
        (customer c2)
        (customer c3)

        (store s1)
        (store s2)
        (store s3)

        (food f1)
        (food f2)
        (food f3)

        (location l1)
        (location l2)
        (location l3)
        (location l4)
        (location l5)
        (location l6)

        (food-cart f1)
        (food-cart f2)
        (food-cart f3)

        (driver-at ?l1)
        (obj-at ?c1 ?l1)
        (obj-at ?c2 ?l2)
        (obj-at ?c3 ?l3)
        (obj-at ?s1 ?l4)
        (obj-at ?s2 ?l5)
        (obj-at ?s3 ?l6)

        (= (distance l1 l1) 0)
        (= (distance l1 l2) 100)
        (= (distance l1 l3) 100)
        (= (distance l1 l4) 100)
        (= (distance l1 l5) 100)
        (= (distance l1 l6) 100)

        (= (distance l2 l1) 100)
        (= (distance l2 l2) 0)
        (= (distance l2 l3) 100)
        (= (distance l2 l4) 100)
        (= (distance l2 l5) 100)
        (= (distance l2 l6) 100)

        (= (distance l3 l1) 100)
        (= (distance l3 l2) 100)
        (= (distance l3 l3) 0)
        (= (distance l3 l4) 100)
        (= (distance l3 l5) 100)
        (= (distance l3 l6) 100)

        (= (distance l4 l1) 100)
        (= (distance l4 l2) 100)
        (= (distance l4 l3) 100)
        (= (distance l4 l4) 0)
        (= (distance l4 l5) 100)
        (= (distance l4 l6) 100)

        (= (distance l5 l1) 100)
        (= (distance l5 l2) 100)
        (= (distance l5 l3) 100)
        (= (distance l5 l4) 100)
        (= (distance l5 l5) 0)
        (= (distance l5 l6) 100)

        (= (distance l6 l1) 100)
        (= (distance l6 l2) 100)
        (= (distance l6 l3) 100)
        (= (distance l6 l4) 100)
        (= (distance l6 l5) 100)
        (= (distance l6 l6) 0)

        ( = (order c1 f1) 1)
        ( = (order c2 f1) 1)
        ( = (order c3 f1) 1)
    )

    (:goal 
        (and
            (= (order c1 f1) 0)
            (= (order c2 f1) 0)
            (= (order c3 f1) 0)
        )
    )
  
    (:metric minimize (total-distance))
)