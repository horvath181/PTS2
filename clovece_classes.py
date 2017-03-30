from random import randint

# Trieda reprezentujuca jehu hru clovece
class Clovece:
    fig = 4; plocha = 40  # pocet figuriek, velkost plochy
    kolo = 0 #pocitadlo kol
    status = ()

    # Konstruktor vytvori hru s danym poctom hracov z int <2, 6>
    def __init__(self, number):
        self.number = number

        # Reprezentuje plochu clovece. Hodnoty typu (hrac, figurka)
        self.clovece = [(-1, -1) for i in range(40)]

        # Ulozime si, na ktorych polickach su jednotlive figurky hracov
        self.policko = {i: [0 for j in range(self.fig)] for i in range(number)}

        # Ulozi stav plochy, pocet hracov, v ktorom kole sme,
        # ktory hrac bol posledne na tahu
        status = (self.clovece, number, 0, 0)

        # Funkcia na detekciu kolizii s inou figurkou
    def kolizia(self, mojaPoloha):
        if self.clovece[mojaPoloha] != (-1, -1):
            hrac = self.clovece[mojaPoloha][0]
            figurka = self.clovece[mojaPoloha][1]
            print("Kolizia s figurkou", figurka, "hraca", hrac)
            self.policko[hrac][figurka] = 0  # ak tam uz je figurka, tak ta prva ide na 0

    #Tah jedneho hraca
    def tah(self, hrac):
        print("Na tahu je hrac", hrac)
        #hod = randint(1, 6) #hod kocky
        hod = 2
        print("Hodili ste", hod)
        figurka = int(input("Chcem ist figurkou č. (0 - 3): ")) #hrac si vyberie figurku
        self.policko[hrac][figurka] += hod  # figurka sa posunie o hodeny pocet policok
        self.kolizia(self.policko[hrac][figurka])  # riesenie kolizii: druhy vyhrava
        self.clovece[self.policko[hrac][figurka]] = (hrac, figurka)  # nova na dane policko
        print(self.clovece)
        print()
        if self.policko[hrac][figurka] >= self.plocha:
            print("Hrac", hrac, "vyhral. Gratulujeme!")
            exit(0)
        self.status = (self.clovece, self.number, self.kolo, hrac)

    def hraj(self):
        while True:  # kym niekto nevyhra
            for hrac in range(self.number):  # tah kazdeho hraca
                self.tah(hrac)
            self.kolo += 1
            print("Stav hracov po kole", str(self.kolo) + ":")
            for i in range(self.number):
                print("Hrac", i, ":", end=' ')
                for j in range(self.fig):
                    print(self.policko[i][j], end=' ')
                print()
            print("\n")

    def ziskajStatus(self):
        return [self.status[i] for i in range(3)]

# Spyta sa na pocet hracov a vytvori novu hru
def novaHra():
    # Na zaciatku sa spytame na pocet hracov. Ten musi byt z intervalu [1,4]
    number = 0  # pocet hracov clovece
    minp = 2
    maxp = 6
    while number < minp or number > maxp:
        number = int(input("Zadajte pocet hracov (2 - 6): "))
        if number < minp or number > maxp: print("Neplatny pocet hracov!")
        return Clovece(number)

clovece = novaHra()
clovece.hraj()
status = clovece.ziskajStatus()
