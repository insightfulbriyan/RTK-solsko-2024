with open("vhod1.txt", "r") as f:
    f = f.read().split("\n")

    vrata_num = int(f[0])
    vrata_stanje = [0]*vrata_num
    vrata_man = [0]*vrata_num

    # tale for zanka za vsak dogodek spremeni stanje vrat v arrayu na trenutno stanje in zabeleži da so ta vrata spremenila stanje
    for dogodek in f[1:]:
        i, s = dogodek.split(" ")

        # če se odprejo odprta vrata li azaprejo zaprta vrata javi napako
        if vrata_stanje[int(i)] == int(s):
            raise Exception("Stanje vrat se je ponovilo")
        
        vrata_stanje[int(i)] = int(s)
        vrata_man[int(i)] = 1


    # ker se log pošlje šele ko se vhodna vrata zaprejo in ker vemo, da se zapiranje vhodnih vrat lahko pojavi le v zadnji vrstici vemo, da je zadnja vrstica zapiranje vhodnih vrat
    if vrata_stanje != [0]*vrata_num:
        raise Exception("Ob zaprtju vhodnih vrat so bila nekatera še odprta")

    for i in range(vrata_num):
        if vrata_man[i] == 1:
            print(i, end=" ")
    print()