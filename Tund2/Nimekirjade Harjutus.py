thislist = ["Tere" , 5, 7.9,4,6,8]
print (thislist)
print (thislist[0])#võtab esimese
print (thislist[-1])#võtab viimase
print (thislist[2:5])#vahemiku määramine
positsioon = 1
print (thislist[positsioon])
arv =(thislist[-1])#muutuja omistus nimekirjaga
thislist[2] = 100
print (thislist)
print(len(thislist))#kontrollime listi pikkust
thislist.append("Lisamine lõppu")
thislist.insert(1, "täpne lisamine")
print (thislist)
thislist.remove(6)
print (thislist)
thislist.pop(0)#kui pop() ontühi,siis võtab viimase elemendi
print(thislist)