sõnastik = {
    "Audi" : 2007,
    "Bmw " : "suunatuli katki" ,
    "Ford" : 1967
    }

print (sõnastik)
sõnastik["Audi"] = 1980
print (sõnastik["Audi"])

for x in sõnastik.values():#kasutades .values()saame objektide väärtused
    print(x)