import math
kujund = input("Kas romb või kolmnurk?")
if kujund == "romb":
        külg = float(input("Sisesta külje pikkus"))
        kõrgus = float(input("Sisesta kõrgus"))
        ümbermõõt = külg * 4
        pindala = külg * kõrgus
        if külg >= kõrgus :
            print("Rombi ümbermööt on",ümbermõõt ,"cm")
            print("Rombi pindala on" ,pindala,"cm2")
        else:
            print("Sisesta korrektsed mõõdud")
elif kujund =="kolmnurk":
    külg = float(input("Sisesta esimese külje pikkus"))
    kõrgus = float(input("Sisesta kolmnurga kõrgus"))
    ümbermõõt = külg + (math.sqrt(float((külg)/2)**2 + float(kõrgus)**2)) *2
    pindala = (külg * kõrgus)/2
    print("Kolmnurga ümbermõõt on" ,ümbermõõt ,"cm")
    print("Kolmnurga pindala on" ,pindala, "cm2")
else:
    print("Sisestasid vale kujundi")
    