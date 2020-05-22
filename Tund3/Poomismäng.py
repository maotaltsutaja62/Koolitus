elu = 9
sisestus = input ("Sisesta sõna")
sisestuslist = list(sisestus)
pikkus = len(sisestuslist)
valmis = []
for x in range(pikkus):
    valmis.append("_")
while elu > 0:
    print(valmis)
    if valmis == list(sisestus):
        print ("Tubli,arvasid ära!")
        break
    täht = input("Paku tähte")
    counter = 0
    arvamus = 0
    for x in list(sisestus):
        if täht == x:
            valmis[counter] = täht
            arvamus += 1
        counter += 1
    if arvamus == 0:
        print("Tähte polnud")
        elu -= 1
        