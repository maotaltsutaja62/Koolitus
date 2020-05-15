kujund = input ("ruut või ristkülik")
if kujund == "ruut" :
    külg = float(input("Sisesta ruudu külg"))
    pindala = külg**2
    ümbermõõt = 4 * külg
    print ("Ruudu pindala on" , pindala, "cm,ning ümbermööt on", ümbermõõt,"cm")
elif kujund == "ristkülik":
    külg_1 = float(input("sisesta külg 1"))
    külg_2 = float(input("Sisesta külg2"))
    pindala = külg_1 * külg_2
    ümbermõõt = (külg_1+ külg_2)*2
    print("Ristküliku pindala on" ,pindala,"cm,ning ümbermõõt on" ,ümbermõõt, "cm")
else:
    print("Sisestasid tundmatu sõna")