tingimus = True#teine variant on False
if tingimus == True :
    print ("Vastab tõele")
    tingimus = False
if tingimus == True :
    print("Midagi on valesti")
else:
    print("Kõik on korras")
arv = 10
if arv < 5 :
    print (arv,"on väiksem kui viis")
elif arv>= 10 :#elif ei pea lisama enam else lõppu/kasutades >=
    print("Arv vastab soovile")
sõna ="Henri"
if sõna != "Henri Tammo":
    print ("Tere" , sõna)
else:
    print ("Sõna ei olnud see,mis arvasin")
arv_1 = 6
arv_2 = 20
if arv_1 > 2 and arv_2 < 100 :#and võib esineda nii mitu korda kui vaja
    print("Arvud sobivad")
if arv_1 == 100 or arv_2 == 20 :#or võib samuti kasutada nii mitu korda kui vaja
    if arv_2 < 30 :
        print("See ei ole väga suur arv")
    print("Vähemalt üks arv sobib")

    
    
