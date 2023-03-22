#1.Feladat: Eljárással bekérünk 5db városnevet, tároljuk 
#a.) Írjuk ki hány darab város van a listában
#b.) Hányszor szerepel a Debrecen
#c.) A Debrecen hanyadik helyen van

def elj():
    
    lista = []
    
    for x in range(1,6,1):
        varos = str(input("Kérem a várost: "))
        lista.append(varos)
        
    lista_db = len(lista)
    print("A lista elemeinek darabja: ", lista)
    
    db = 0
    
    for x in lista:
        if x == "Debrecen":
            db += 1
            
    print("A Debrecen nevű város darabja: ",db)
    
    hely = lista.index("Debrecen")
    print("A Debrecen nevű város helye: ",hely + 1)
    
#elj()
        



#2.Feladat: Eljárással megkap 3db egész számot és vizsgáljuk meg hogy egyformák-e vagy sem
    
def megk(szam1,szam2,szam3):
    
    if szam1 == szam2 == szam3:
        print("A három szám egyenlő")
    else:
        print("A 3 szám különböző")
    
#megk(5,5,5)    
    
    
    
    
#3.Feladat: függvénnyel bekér 5db számot tároljuk listába és a legnagyobb értékrt kapjuk
        
def fugg():
    
    lista = []
    
    for x in range(1,6,1):
        szam = int(input("Kérem a számot: "))
        lista.append(szam)
        
    legnagyobb = max(lista)
    return "A lista legnagyobb száma: ",legnagyobb
    
#print(fugg())
        
        
        
        
#4.Feladat: függvénnyel megkap 2db egész számot ennek segítségével kiszámoljuk a kerület értéket

def kerulet():
    
    a = int(input("Kérem a számot: "))
    b = int(input("Kérem a számot: "))
    
    ker = a + b
    
    return ker

#print("A terület: ",kerulet())







#5.Feladat: eljárással megkap egy stringet és megkellene vizsgálnunk h 5karakternál hosszabb vagy rovidebb

def st(szo):
    
    szo_hossz = len(szo)
    print("A szó hossza:", szo_hossz)
    
    if szo_hossz <= 5:
    
        print("A szám rövidebb min 5 karakter")
        
    if szo_hossz >= 5:
        
        print("A szám hoszabb mint 5 karakter")
        
    
#st("alma")








