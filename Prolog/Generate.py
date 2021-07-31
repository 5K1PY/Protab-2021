f = open("2.in", encoding="utf-8")
g = open("2.pl", "w")

n = 25
g.write("""
:- use_module(library(clpfd)).

left(A, B) :- A #< B.
next_to(A, B) :- B #= A+1.
far(A, B, X) :- (B #= A-X; B #=A+X).

even(X) :- 0 #= mod(X, 2).
odd(X) :- 1 #= mod(X, 2).

"""
)

letters = ", ".join([chr(ord("A") + i) for i in range(n)])
g.write(f"""
check({letters}) :- 
    all_distinct([{letters}]),
    [{letters}] ins 1..{n}
.

solve({letters}) :-
    check({letters})"""
)

line = f.readline()
while line != "":
    line = line.split()
    g.write(",\n    ")
    if "sudé" in line:
        g.write(f"even({line[0]})")
    elif "liché" in line:
        g.write(f"odd({line[0]})")
    elif "nalevo" in line:
        g.write(f"left({line[0]}, {line[-1]})")
    elif "napravo" in line:
        g.write(f"left({line[-1]}, {line[0]})")
    else:
        g.write(f"far({line[0]}, {line[-1]}, {line[2]})")

    line = f.readline()

g.write(f""",
    All = [{letters}],
    label(All)
.

""")
f.close()
g.close()