

(define (problem problem1)
    (:domain deliver)
    (:objects 
        c1 c2 c3 - CUSTOMER
        s1 - STORE
        f1 - FOOD
        l1 l2 l3 - LOCATION
    )

    (:init 
        (customer c1)
        (store s1)
        (food f1)
        (menu s1 f1)

        (location l1)
        (location l2)

        (= (food-cart f1) 0)

        (driver-at l1)
        (obj-at c1 l1)
        (obj-at s1 l2)

        (= (distance l1 l1) 0)
        (= (distance l1 l2) 100)
        (= (distance l2 l1) 100)
        (= (distance l2 l2) 0)

        ( = (order c1 f1) 1)
    )

    (:goal 
        (and
            (= (order c1 f1) 0)
        )
    )
  
    (:metric minimize (total-distance))
)