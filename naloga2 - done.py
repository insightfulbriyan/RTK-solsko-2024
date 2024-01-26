def permutate(plesalci: list[int], filter: list[int]) -> list[int]:
    returned_arr = []
    for i in filter:
        returned_arr.append(plesalci[i - 1])
    return returned_arr

def izvedi_ples(plesalci: list[int], filtes: list[list[int]]) -> list[int]:
    for filter in filtes:
        plesalci = permutate(plesalci, filter)
    
    return plesalci

n = 5
start = list(range(1, n + 1))
plesalci = list(range(1, n +1))
seznami = [[3, 4, 1, 5, 2], [4, 3, 2, 1, 5]]
i = 0

while True:
    plesalci = izvedi_ples(plesalci, seznami)
    i += 1
    if plesalci == start:
        print(i)
        break

#funkcija permutate izvede eno dejanje plesa, funkcija izvedi ples pa vsa dejanja enega plesa
#v while true zanki izvajamo ples dokler postavitev plesalcev ni enaka začetni postavitvi