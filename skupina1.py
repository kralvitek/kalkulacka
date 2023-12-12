x = input("zadejte proměnou x: ")
y = input("zadejte proměnou y: ")

x = int(x)
y = int(y)

print("hele Bráško pro sčítání zadej +")
print("hele Bráško pro odčítání zadej -")
print("hele Bráško pro násobení zadej *")
print("hele Bráško pro dělení zadej /")
print("hele Bráško pro mocnění zadej **")
print("hele Bráško pro odmocnění zadej /*")

znamenko = input("zvolte si operátora: ")

if znamenko == "+":
    vysledek = x + y
    vysledek = str(vysledek)
    print("vysledek je: " + vysledek)

elif znamenko == "-":
    vysledek = x - y
    vysledek = str(vysledek)
    print("vysledek je: " + vysledek)

elif znamenko == "*":
    vysledek = x * y
    vysledek = str(vysledek)
    print("vysledek je: " + vysledek)

elif znamenko == "/":
    if y != 0:
    vysledek = x / y
    vysledek = str(vysledek)
        print("vysledek je: " + vysledek)
    else:
    print("nemůžeš dělit nulou debile")
        
elif znamenko == "**":
    vysledek = x ** y
    vysledek = str(vysledek)
    rint("vysledek je: " + vysledek)

  elif znamenko == "/*":
    vysledek = x /* y
    vysledek = str(vysledek)
     print("vysledek je: " + vysledek)

