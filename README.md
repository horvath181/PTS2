# Terminálové Človeče
Vítam Vás v hre Terminálové Človeče, ktorá je zjednodušenou terminálovou verziou tejto hry.  
Hra je pre 2 - 6 hráčov, každý má 4 figúrky a hracia plocha má 40 políčok. Prvý, ktorý prejde všetky políčka vyhráva.  
V hre samozrejme existujú i kolízie, a preto, keď sa na nejakom polčkou stretnú dve figúrky, tak tá, čo tam prišla neskôr, tú druhú nemilosrdne vyhodí.

## Manuál k hre
*Výber hráčov
Na začiatku si vyberiete počet hráčov od 2 - 6

*Hra
Hrajú hráči v poradí od 0 až po početHráčov-1.

*Ťah jedného hráča
Hod kockou reprezentuje pseudonáhodné číslo z intervalu 1 - 6, pričom, ak sa hodí 6, tak sa, narozdiel od pôvodnej verzie, NEJDE znova.  
Potom si hráč vyberie, ktorou figúrkou sa chce o daný počet pohnúť.  
Možno nastane kolízia.
Keď už potiahli všetci hráči, zobrazia sa výsledky po novom kole.

*Výhra
Vyhráva ten, kto prešiel ako prvý všetky políčka. Potom sa hra končí.

## Zoznam funkcií v hre
*collision(mojaPoloha)
Kontroluje, či nenastala kolízia. Ak hej, pošle figúrku, čo tam bola skôr, na políčko O.

args: mojaPoloha - poloha, na ktorej sa má zistiť kolízia
