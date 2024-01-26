from itertools import permutations, combinations_with_replacement

s = "abcd"
k = 7
dolzina_ostanka = k - len(s)


permutacije_s = [''.join(p) for p in permutations(s)]
print(permutacije_s)

kombinacije_s_ponavlajanjem_ostanka = [''.join(p) for p in combinations_with_replacement(s, dolzina_ostanka)]
print(kombinacije_s_ponavlajanjem_ostanka)

for ostanek in kombinacije_s_ponavlajanjem_ostanka:
    for s_perm in permutacije_s:
        for i in range(dolzina_ostanka+1):
            ostanek_l = list(ostanek)
            ostanek_l.insert(i, s_perm)
            print(''.join(ostanek_l))


# program vse permutacije s-a in vse kombinacije ostanka (znaki iz s, dolžine k-len(s)) združi tako da permutacije vstavi med vsak znak ostanka (tudi na začetek in konec)