
:- use_module(library(clpfd)).

left(A, B) :- A #< B.
next_to(A, B) :- B #= A+1.
far(A, B, X) :- (B #= A-X; B #=A+X).

even(X) :- 0 #= mod(X, 2).
odd(X) :- 1 #= mod(X, 2).


check(A, B, C, D, E, F, G, H) :- 
    all_distinct([A, B, C, D, E, F, G, H]),
    [A, B, C, D, E, F, G, H] ins 1..8
.

solve(A, B, C, D, E, F, G, H) :-
    check(A, B, C, D, E, F, G, H),
    even(F),
    left(H, D),
    far(A, E, 5),
    left(G, H),
    far(G, C, 3),
    left(C, F),
    even(D),
    even(C),
    left(E, H),
    left(D, F),
    far(D, C, 2),
    left(B, H)
.