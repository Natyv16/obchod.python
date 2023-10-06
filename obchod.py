kategorie = ["maso", "zelenina", "ovoce","odejit"]
produkty  =  [ ["kureci","veprovy","hovezi"],["paprika","rajce","okurka"],["jablko","banan","jahoda"]
]
price = [[120,130,150],[15,20,30],[15,25,35]]
vybrane = [[0,0,0],[0,0,0],[0,0,0]]
cena = 0
pocetproduktu = 0

print("Vítej v Lídlu")
print("------------")

while True:

    print("Vyber jednu z nasledujicách kategorií: ")
    product = 0
    poradi = 1
    for b in range(4):
             print(poradi,".",kategorie[b], sep="")
             poradi += 1
    poradi = 1
    choose = int(input("Zadej cislo kategorie: "))
    if choose == 4:
        for uctenka in range(3):
                for uctenka2 in range(3):
                    if(vybrane[uctenka][uctenka2] != 0):
                        print(produkty[uctenka][uctenka2], vybrane[uctenka][uctenka2],)
        print("Vase cena nákupu je:", cena)
        break
    poradi = 1
    if choose == 1:
        category = "maso"
        for a in range(3):
             print(poradi,".",produkty[0][a], sep="")
             poradi += 1
        product = int(input("Zadej číslo produktu: "))

    elif choose == 2:
        category = "zelenina"
        for a in range(3):
             print(poradi,".",produkty[1][a], sep="")
             poradi += 1
        product = int(input("Zadej číslo produktu: "))

    elif choose == 3:
        category = "ovoce"
        for a in range(3):
             print(poradi,".",produkty[2][a], sep="")
             poradi += 1
        product = int(input("Zadej číslo produktu: "))
    pocet = int(input("Zadej počet kusů: "))
    vybrane[choose-1][product-1] += pocet
    cena += price[choose-1][product-1]
    pocetproduktu += 1
