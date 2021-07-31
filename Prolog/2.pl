
:- use_module(library(clpfd)).

left(A, B) :- A #< B.
next_to(A, B) :- B #= A+1.
far(A, B, X) :- (B #= A-X; B #=A+X).

even(X) :- 0 #= mod(X, 2).
odd(X) :- 1 #= mod(X, 2).


check(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y) :- 
    all_distinct([A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y]),
    [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y] ins 1..25
.

solve(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y) :-
    check(A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y),
    odd(J),
    far(M, I, 8),
    odd(D),
    even(P),
    far(A, C, 2),
    far(O, Y, 9),
    even(A),
    far(L, A, 4),
    even(I),
    odd(E),
    far(K, P, 9),
    left(R, U),
    far(K, D, 8),
    far(O, H, 5),
    even(T),
    far(T, H, 10),
    far(U, W, 17),
    even(S),
    odd(G),
    left(W, I),
    left(S, D),
    far(X, L, 19),
    left(C, U),
    far(G, B, 5),
    left(N, P),
    far(F, Y, 15),
    even(M),
    left(Q, G),
    far(E, N, 16),
    even(Y),
    far(Q, C, 3),
    left(S, J),
    far(L, Q, 1),
    left(Y, X),
    far(H, I, 12),
    left(Q, J),
    even(B),
    left(S, X),
    left(R, G),
    far(T, B, 6),
    odd(Q),
    far(E, U, 4),
    left(H, E),
    left(V, R),
    All = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y],
    label(All)
.

