sõnastik = {
    "Audi" : 2007,
    "Bmw" : "suunatuli katki" ,
    "Ford" : 1967
    }

print (sõnastik)
sõnastik["Audi"] = 1980
print (sõnastik["Audi"])

for x in sõnastik.values():#kasutades .values()saame objektide väärtused
    print(x)
    
for x,y in sõnastik.items():#x tähistab objekt ja y selle väärtust
    print(x, y)
    print(len(sõnastik))
    
del sõnastik["Bmw"]#objekti ja ta väärtuse eemaldamine
print(sõnastik)
sõnastik["Mazda"] = "roostetab palju"
print(sõnastik)