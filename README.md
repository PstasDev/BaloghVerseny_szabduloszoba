# Balogh Verseny szbadulószobai szoftver

Évekkel ezelőtti, fél óra alatt összedobott kis Tkinter program, ami egy rövid, számokból álló kódot vár, majd leállítja a visszaszámlálót. Mivel a program egy kifejezett versenyre készült ezért nem túlságosan dinamikus, nem lehet a programkód nagyobb átírása nélkül kis módosításokat végezni rajta pl.: hibalehetőségek, irányítás vagy más karakterek támogatása.

## Egész nagy hiba
A program integerként kezeli a kódot, ezért nem várhat olyan kódot ami pl.: `088` vagy `008`, mert ezekben az esetekben elvileg el fogja fogadni a `8`-as szám szimpla beütését, mint helyes kód.

Ma már nem így csinálnám, de régi kód és nem azért töltöttem GitHubra fel, hogy továbbra is legyen support, hanem hogy trackelve legyen legalább, de már nagyon rég írtam.
