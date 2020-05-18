arv_1 = int(input("Sisesta esimene arv"))
arv_2 = int(input("Sisesta teine arv"))
arv_3 = int(input("Sisesta kolmas arv"))
if arv_1 > arv_2 and arv_1 > arv_3 :
    print(arv_1 **2)
if arv_3 > arv_1 and arv_3 > arv_2 :
    print(arv_3 **2)
if arv_2 > arv_1 and arv_2 > arv_3 :
    print(arv_2 - arv_1 - arv_3)