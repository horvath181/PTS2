from random import randint

# Funkcia na detekciu kolizii s inou figurkou
def collision(mojaPoloha):
    if clovece[mojaPoloha] != (-1, -1):
        hrac = clovece[mojaPoloha][0]
        figurka = clovece[mojaPoloha][1]
        print("Kolizia s figurkou", hrac, "hraca", figurka)
        policko[hrac][figurka] = 0 # ak tam uz je figurka, tak ta prva ide naspat do domceka


# Na zaciatku sa spytame na pocet hracov. Ten musi byt z intervalu [1,4]
number = 0  # pocet hracov clovece
fig = 4
minp = 2
maxp = 6
plocha = 40
while number < minp or number > maxp:
    number = int(input("Zadajte pocet hracov (2 - 6):"))
    if number < minp or number > maxp: print("Neplatny pocet hracov!")

# Reprezentuje plochu clovece. Hodnoty typu (hrac, figurka)
clovece = [(-1, -1) for i in range(40)]

# Ulozime si, na ktorych polickach su jednotlive figurky hracov
policko = {i: [0 for j in range(fig)] for i in range(number)}

# Zacneme hrat clovece
tah = 0  # tah, v ktorom sme
hod = 0  # hod daneho hraca
while True:  # kym niekto nevyhra
    for hrac in range(number):  # tah kazdeho hraca
        print("Na tahu je hrac", hrac)
        hod = randint(1, 4)
        #hod = 2
        print("Hodili ste", hod)
        figurka = int(input("Chcem ist figurkou č. (0 - 3):"))
        policko[hrac][figurka] += hod  # figurka sa posunie o hodeny pocet policok
        collision(policko[hrac][figurka])  # riesenie kolizii: druhy vyhrava
        clovece[policko[hrac][figurka]] = (hrac, figurka)  # nova sa umiestni na dane policko
        if policko[hrac][figurka] >= plocha:
            print("Hrac", hrac, "vyhral. Gratulujeme!")
            exit(0)
    tah += 1
    #print(clovece)
    #o = input("Ak chcete ukoncit hru po tomto tahu, stlacte \'a\':")
    print("Stav hracov po tahu", str(tah) + ":")
    for i in range(number):
        print("Hrac", i, ":", end=' ')
        for j in range(fig):
            print(policko[i][j], end=' ')
        print()

    #if o == "a":
        #exit(0)
