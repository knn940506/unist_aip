
(define (domain deliver)
    (:predicates 
        (customer ?c)
        (store ?s)
        (food ?f) 
        (location ?l)

        (driver-at ?location)
        (obj-at ?obj ?l)
        (menu ?s-STORE ?f-FOOD)
    )
                  
    (:functions 
        (total-distance)
        (total-carrying)
        (food-cart ?f)
        (order ?customer ?food)
        (distance ?from ?to)
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
            ;;(driver-at ?location)
            (<= (total-carrying) 7)
        )
        :effect (and 
            (increase (total-carrying) 1)
            (forall (?food - FOOD) (when (menu ?store ?food) (increase (food-cart ?food) 1)))
        )
    )
                  
    (:action deliver 
        :parameters (?customer ?food)
        :precondition (and
            ;;(driver-at ?location)
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
