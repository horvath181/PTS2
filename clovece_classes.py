from random import randint

# Trieda reprezentujuca jehu hru clovece
class Clovece:
    fig = 4; plocha = 40  # pocet figuriek, velkost plochy

    status = ()

    # Konstruktor vytvori hru s danym poctom hracov z int <2, 6>
    def __init__(self, number):
        # Reprezentuje plochu clovece. Hodnoty typu (hrac, figurka)
        clovece = [(-1, -1) for i in range(40)]

        # Ulozime si, na ktorych polickach su jednotlive figurky hracov
        policko = {i: [0 for j in range(self.fig)] for i in range(number)}

        # Stav plochy, figuriek, pocet hracov, v ktorom kole sme, ktory hrac bol posledne na tahu
        self.status = (clovece, policko, number, 0, 0)

        # Funkcia na detekciu kolizii s inou figurkou
    def kolizia(self, mojaPoloha):
        if self.status[0][mojaPoloha] != (-1, -1):
            hrac = self.status[0][mojaPoloha][0]
            figurka = self.status[0][mojaPoloha][1]
            print("Kolizia s figurkou", figurka, "hraca", hrac)
            self.status[1][hrac][figurka] = 0  # ak tam uz je figurka, tak ta prva ide na 0

    # Tah jedneho hraca
    def tah(self):
        hrac = self.status[4]
        kolo = self.status[3]
        number = self.status[2]
        policko = self.status[1]
        clovece = self.status[0]
        print("Na tahu je hrac", hrac)
        hod = randint(1, 6) #hod kocky
        #hod = 2
        print("Hodili ste", hod)
        figurka = int(input("Chcem ist figurkou č. (0 - 3): ")) #hrac si vyberie figurku
        policko[hrac][figurka] += hod  # figurka sa posunie o hodeny pocet policok
        self.kolizia(policko[hrac][figurka])  # riesenie kolizii: druhy vyhrava
        clovece[policko[hrac][figurka]] = (hrac, figurka)  # nova na dane policko
        print(self.status[2])
        print()
        if policko[hrac][figurka] >= self.plocha:
            print("Hrac", hrac, "vyhral. Gratulujeme!")
            exit(0)
        self.status = (clovece, policko, number, kolo, hrac)

    def hraj(self):
        pocet = self.status[2]
        while True:  # kym niekto nevyhra
            for hrac in range(pocet):  # tah kazdeho hraca
                self.status = (self.status[0], self.status[1], self.status[2], self.status[3], hrac)
                self.tah()
            self.status = (self.status[0], self.status[1], self.status[2], self.status[3] + 1, self.status[4])
            print("Stav hracov po kole", str(self.status[3]) + ":")
            for i in range(pocet):
                print("Hrac", i, ":", end=' ')
                for j in range(self.fig):
                    print(self.status[1][i][j], end=' ')
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
