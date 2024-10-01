

<body style="color: #1f2937; font-family: 'Inter', sans-serif">
    <div style="color: white;">
    <div style="color: white;">
    <div style="max-width: 1280px; margin: 0 auto; padding: 16px 32px; display: flex; justify-content: center; align-items: flex-start; flex-wrap: nowrap;">
    <!-- <div style="display: flex; align-items: flex-start;">
        <img src="https://mcc.hu/images/mcc-logo-kek.svg" alt="MCC Logo 1" style="max-width: 100%; height: auto; width: 200px;">
    </div>
    <div style="display: flex; align-items: center;">
        <div style="border-left: 2px solid #d1d5db; height: 100px; margin-left: 40px; margin-right: 40px;"></div>
    </div> -->
    <div style="display: flex; align-items: flex-start; padding: 0; margin: 0;">
        <img src="/mccpy/mccpy.svg" alt="MCC Logo 2" style="width: 600px; height: auto;">
    </div>
</div>




</div>
    </div>
    <!-- Hero szekció -->
    <section style="padding: 0px 0;">
        <div style="max-width: 1280px; margin: 0 auto; text-align: center;">
            <p style="font-size: 2.25rem; font-weight: 700;">MCC.py órai anyag</p>
        </div>
    </section>

</body>


[Thonny telepítése](https://youtu.be/rjGGpfTARDA)



## Tartalomjegyzék

- [Tartalomjegyzék](#tartalomjegyzék)
- [Python alapok (1. óra)](#python-alapok-1-óra)
  - [Első lépések](#első-lépések)
    - [Python alapok: kód és kimenet](#python-alapok-kód-és-kimenet)
    - [Hibák és hibaüzenetek](#hibák-és-hibaüzenetek)
    - [Matematikai kifejezések](#matematikai-kifejezések)
    - [Sztringek összefűzése](#sztringek-összefűzése)
    - [Sztringek összeadása](#sztringek-összeadása)
    - [Kommentek (megjegyzések)](#kommentek-megjegyzések)
    - [Üres sorok](#üres-sorok)
    - [Összefoglaló](#összefoglaló)
  - [Változók (tárolás és hivatkozás)](#változók-tárolás-és-hivatkozás)
    - [Típusok](#típusok)
    - [Átalakítás](#átalakítás)
  - [Adatbekérés és műveletek](#adatbekérés-és-műveletek)
    - [Adatbekérés](#adatbekérés)
    - [Műveletek](#műveletek)
    - [Maradékos osztás (modulo)](#maradékos-osztás-modulo)
  - [Véletlen számok generálása pythonban](#véletlen-számok-generálása-pythonban)
    - [Példa: 1 és 10 közötti véletlenszám generálása](#példa-1-és-10-közötti-véletlenszám-generálása)
- [Python alapok v2 (2. óra)](#python-alapok-v2-2-óra)
    - [Miért fontosak a véletlenszámok?](#miért-fontosak-a-véletlenszámok)
  - [Logikai kifejezések](#logikai-kifejezések)
    - [Feltételes utasítás (if)](#feltételes-utasítás-if)
    - [További feltételek (else)](#további-feltételek-else)
    - [Összehasonlító operátorok](#összehasonlító-operátorok)
    - [Logikai operátorok](#logikai-operátorok)
  - [Ciklusok](#ciklusok)
    - [While ciklus](#while-ciklus)
    - [Ciklusok egymásba ágyazása](#ciklusok-egymásba-ágyazása)
- [Projektek (3. óra)](#projektek-3-óra)
    - [1. Számkitaláló játék](#1-számkitaláló-játék)
    - [2. Egyszerű kalkulátor](#2-egyszerű-kalkulátor)
    - [3. Egyszerű jelszógenerátor](#3-egyszerű-jelszógenerátor)
    - [4. Személyre szabott üdvözlés](#4-személyre-szabott-üdvözlés)
    - [5. Páros vagy páratlan szám?](#5-páros-vagy-páratlan-szám)
    - [6. Neptun kód generátor](#6-neptun-kód-generátor)
    - [7. Változó hosszúságú jelszó generátor](#7-változó-hosszúságú-jelszó-generátor)
    - [8. Fibonacci sorozat](#8-fibonacci-sorozat)
    - [9. Kő, Papír, Olló](#9-kő-papír-olló)

---

## Python alapok (1. óra)

### Első lépések

#### Python alapok: kód és kimenet

A Python kód két fő részből áll: a kódot író rész és a kimenet (output). Szöveg megjelenítéséhez használjuk a `print()` függvényt:

```python
print("Samy")
print('Samy')
```

A szöveget (sztringet) idézőjelek (" ") vagy aposztrófok (' ') között kell megadni, és az eredmény azonos lesz.

```python
print('almafa')
```

#### Hibák és hibaüzenetek

Ha hibát találunk a kódban, ne ijedjünk meg! A hibaüzenet gyakran pontos információval szolgál a problémáról, és néha egy nyíllal jelzi a hiba helyét.

#### Matematikai kifejezések

A Python képes matematikai műveletek végrehajtására is. Például:

```python
print(4 + 5)
```

Ez az utasítás `9`-et eredményez, mivel a Python elvégzi az összeadást.

#### Sztringek összefűzése

Sztringeket is össze tudunk fűzni:

```python
print("alma" + "banan")  # Szövegösszefűzés
print("alma", "banan")   # Egymás mellé kiírás
```

- Az első példa `almabanan`-t ad vissza.
- A második példa `alma banan`-t ad vissza, mivel a `print` függvény szóközökkel választja el az elemeket.

#### Sztringek összeadása

A következő kód eredménye:

```python
print('4' + '5')
```

Mivel a `4` és `5` sztringek, az eredmény `45` lesz, nem pedig `9`. Ez a sztringek összefűzésére vonatkozik.

#### Kommentek (megjegyzések)

Kommentekkel dokumentálhatjuk a kódot anélkül, hogy az befolyásolná a végrehajtást:

```python
# Ez csak egy megjegyzés
print("Samy")  # Megjegyzés
```

A kettőskereszt (`#`) jelzi, hogy a sor figyelmen kívül lesz hagyva a program végrehajtása során.

#### Üres sorok

Az üres sorok növelik a kód olvashatóságát, de nem befolyásolják a kód végrehajtását.

#### Összefoglaló

- **Szöveg kiírása:** `print("szöveg")` vagy `print('szöveg')`.
- **Matematikai műveletek:** Alapvető aritmetikai műveletek, mint az összeadás.
- **Sztringek összefűzése:** `print("szöveg1" + " szöveg2")`.
- **Sztringek összeadása:** Az idézőjelek között lévő számok szövegként kezelendők.
- **Kommentek:** `#` jel után következő szöveg, amely nem befolyásolja a kódot.
- **Üres sorok:** Az olvashatóságot javítják.

---

### Változók (tárolás és hivatkozás)

A programozás során változókra van szükségünk, amelyeket úgy kell elképzelnünk, mint dobozokat, amelyekben különböző értékeket tárolhatunk. Például:

```python
x = 5
```

Innét kezdve az `x` változó értéke 5 lesz. A változóknak bármilyen nevet adhatunk, de nem kezdődhet számmal és nem tartalmazhat ékezetes betűket. Az ékezetes karakterek és különleges karakterek nem lehet használni, de léteznek kivételek mint például `-` vagy `_`.

#### Típusok

A Python négy fő változótípust támogat:

1. **int**: Egész számok (pl. `5`)
2. **string**: Szöveg (pl. `Alma`)
3. **float**: Tizedes tört (pl. `0.75`)
4. **boolean**: Logikai érték, amely lehet **`True`** vagy **`False`**

#### Átalakítás

A Pythonban a típusok közötti átalakításhoz használhatjuk az átalakító függvényeket, mint **`int()`**, **`float()`** és **`str()`**:

```python
# Sztring -> Szám
szam = int('17')

# Sztring -> Tizedes
tizedes = float('2.5')


# Szám -> Sztring
szam_sztring = str(100)
```

### Adatbekérés és műveletek

#### Adatbekérés

Adatbekéréshez használjuk a **`input()`** függvényt:

```python
nev = input("Hogy hívnak?")
print("Üdvözöllek,", nev)
```

Az **`input()`** függvény a felhasználótól kér be adatot és az eredmény sztringként tárolódik.

#### Műveletek

Matematikai műveleteket végezhetünk a felhasználó által megadott számokon:

```python
szam1 = int(input("Adj meg egy számot: "))
szam2 = int(input("Adj meg egy másik számot: "))
eredmeny = szam1 + szam2
print("A két szám összege: ", eredmeny)
print("A két szám összege: ", eredmeny)
```

#### Maradékos osztás (modulo)

A modulo operátor (**`%`**) az osztás maradékát adja vissza:

```python
maradek = 7 % 3
print(maradek)  # Eredmény: 1
```

---

### Véletlen számok generálása pythonban

#### Példa: 1 és 10 közötti véletlenszám generálása

A **`random`** modul segítségével véletlen számokat generálhatunk:

```python
import random
veletlen_szam = random.randint(1, 10)
print(veletlen_szam)
```



## Python alapok v2 (2. óra)
#### Miért fontosak a véletlenszámok?

A véletlenszámok hasznosak játékokban, statisztikai elemzésekben és más területeken, ahol a véletlen események modellezése szükséges.

### Logikai kifejezések

#### Feltételes utasítás (if)

Az **`if`** utasítással feltételes logikai ellenőrzéseket végezhetünk:

```python
szam = 10
if szam > 5:
    print("A szám nagyobb mint 5")
```

#### További feltételek (else)

Az **`else`** lehetőséget ad arra, hogy más kódot futtassunk, ha a feltétel nem teljesül:

```python
szam = 3
if szam > 5:
    print("A szám nagyobb mint 5")
else:
    print("A szám nem nagyobb mint 5")
```

#### Összehasonlító operátorok

Az összehasonlító operátorok segítenek a feltételek meghatározásában:

- **`==`**: Egyenlőség
- **`!=`**: Nem egyenlőség
- **`>`**: Nagyobb mint
- **`<`**: Kisebb mint
- **`>=`**: Nagyobb vagy egyenlő
- **`<=`**: Kisebb vagy egyenlő

#### Logikai operátorok

A logikai operátorok kombinálhatják a feltételeket:

- **`and`**: Ha mindkét feltétel igaz
- **`or`**: Ha bármelyik feltétel igaz
- **`not`**: Ha a feltétel nem igaz


A dupla egyenlőség jellel (**==**) össze lehet hasonlítani 2 értéket.

```python
engedely = True

if engedely == True:
  print("Kaptál engedélyt, ezért mehetsz nyaralni!")
else:
    print("Nem kaptál engedélyt :(")
```

```python
szam = 3

if szam >= 1 and szam <= 5:
    print("A szám 1 és 5 között van")
else:
    print("A szám nincsen 1 és 5 között")
```



```python
erdemjegy = 5

if erdemjegy not 5:
  print("Sajnos nem vagy jeles :(")
else:
    print("Jeles!!")
```


---



---




### Ciklusok
```python
'''
A print függvény a megadott szöveg kiírása után sort emel, 
vagyis a következő print függvény már egy újabb sorba ír.
Az alapértelmezett viselkedés azonban felülírható a "t" paraméterrel.
'''
# a kiírást követően a kurzor egy tabulátornyit ugrik
print('Teszt', end='\t')
# a kiírást követően a kurzor a kiírás végén marad
print('Teszt', end='')       
```
A ciklusok alapvető fontosságúak a programozásban, mert lehetővé teszik, hogy egy adott kódrészletet többször is végrehajtsunk. Gondolj rájuk úgy, mint egy ismétlődő feladat elvégzésére, például egy listában szereplő összes szám hozzáadására.

#### While ciklus

A **while** ciklus addig ismétel egy kódrészletet, amíg egy bizonyos feltétel igaz marad. Képzeld el, hogy egy dobozban addig teszel almát, amíg a doboz meg nem telik. A while ciklus addig fut, amíg a feltétel igaz.

Például:

```python
# while magyarul azt jelenti: amíg
  
  szam = 1
  while szam <= 10:
    print(szam)
    szam = szam + 1   
```

Ez a ciklus addig írja ki a számokat 1-től 5-ig, amíg a **szam** változó értéke el nem éri a 6-ot. A feltétel itt az, hogy a **szam** kisebb vagy egyenlő legyen 5-tel.

**Egyszerű magyarázat:**

1. A ciklus indul a **szam = 1** értékkel.
2. Ha a **szam** kisebb vagy egyenlő 5-tel (ami az első futtatáskor igaz), kiírja a számot.
3. Ezután növeli a **szam** értékét eggyel (pl. 2 lesz).
4. Újra ellenőrzi a feltételt, és folytatja a ciklust, amíg a feltétel nem lesz hamis (amikor **szam** 6 lesz, a ciklus megáll).

#### Ciklusok egymásba ágyazása

Egymásba ágyazott ciklusokat akkor használunk, ha egy cikluson belül még egy ciklust szeretnénk futtatni. Képzeld el ezt úgy, mintha több dobozt is megtöltenél almával, de minden dobozban van egy kisebb doboz, amit szintén meg kell tölteni.

Például, ha van egy rács (mint egy sakktábla), és ki szeretnéd írni az összes sor és oszlop kombinációját:

```python
sor = 1
  while sor <= 3:
      oszlop = 1
      while oszlop <= 5:
          print('O ', end='')
          oszlop = oszlop + 1
      print('')
      sor = sor + 1 
```

Ez a program egy 3x5-as rácsot ír ki. Az első ciklus végigmegy a sorokon, a belső ciklus pedig minden sorhoz végigmegy az oszlopokon.

---


## Projektek (3. óra)

#### 1. Számkitaláló játék

**Leírás**:
Ez a program egy egyszerű, szórakoztató játékot valósít meg, ahol a felhasználónak ki kell találnia a számítógép által véletlenszerűen generált számot 1 és 10 között. A program addig kéri a felhasználót, amíg el nem találja a számot, és visszajelzést ad minden próbálkozás után.

**Példa kód**:

```python
import random

szam = random.randint(1, 10)
tipp = None

while tipp != szam:
    tipp = int(input("Találd ki a számot 1 és 10 között: "))
    if tipp == szam:
        print("Gratulálok, eltaláltad!")
    else:
        print("Sajnálom, próbáld újra!")

print(">> Program vége <<")
```

**Minta kimenet**:

```
Találd ki a számot 1 és 10 között: 3
Sajnálom, próbáld újra!
Találd ki a számot 1 és 10 között: 7
Gratulálok, eltaláltad!
>> Program vége <<
```

---

#### 2. Egyszerű kalkulátor

**Leírás**:
Ez a kalkulátor program lehetővé teszi a felhasználó számára, hogy két szám között végezzen egyszerű matematikai műveleteket: összeadás, kivonás, szorzás és osztás. A program ellenőrzi az osztás esetén a nullával való osztást is.

**Példa kód**:

```python
szam1 = float(input("Add meg az első számot: "))
szam2 = float(input("Add meg a második számot: "))

muvelet = input("Milyen műveletet szeretnél elvégezni (+, -, *, /): ")

if muvelet == '+':
    eredmeny = szam1 + szam2
elif muvelet == '-':
    eredmeny = szam1 - szam2
elif muvelet == '*':
    eredmeny = szam1 * szam2
elif muvelet == '/':
    if szam2 != 0:
        eredmeny = szam1 / szam2
    else:
        eredmeny = "Hiba! Nullával való osztás."
else:
    eredmeny = "Ismeretlen művelet"

print("Az eredmény:", eredmeny)
```

**Minta kimenet**:

```
Add meg az első számot: 10
Add meg a második számot: 5
Milyen műveletet szeretnél elvégezni (+, -, *, /): *
Az eredmény: 50.0
```

---

#### 3. Egyszerű jelszógenerátor

**Leírás**:
Ez a jelszógeneráló program véletlenszerűen generál egy rövid jelszót kisbetűkből és számokból. Használhatjuk az egyszerű véletlenszerű választást és a string manipulációt.

**Példa kód**:

```python
import random

karakterek = "abcdefghijklmnopqrstuvwxyz0123456789"
jelszo = ""

for _ in range(6):
    jelszo += random.choice(karakterek)

print("A generált jelszó:", jelszo)
```

**Minta kimenet**:

```
A generált jelszó: a5j8k2
```

---

#### 4. Személyre szabott üdvözlés

**Leírás**:
Ez a program személyre szabott üdvözlést ad a felhasználó életkorának megfelelően. A program megkülönbözteti a felnőtt és fiatal felhasználókat, és üdvözli őket az életkoruk alapján.

**Példa kód**:

```python
nev = input("Add meg a neved: ")
kor = int(input("Add meg a korod: "))

if kor >= 18:
    print("Üdvözlünk", nev ,"! Te már felnőtt vagy!")
else:
    print("Üdvözlünk", nev ,"! Még fiatal vagy, élvezd az életet!")
```

**Minta kimenet**:

```
Add meg a neved: Anna
Add meg a korod: 22
Üdvözlünk Anna! Te már felnőtt vagy!
```

---

#### 5. Páros vagy páratlan szám?

**Leírás**:
Ez a program megállapítja, hogy egy megadott szám páros vagy páratlan. Egyszerű példát nyújt a modulus operátor használatára és a feltételes logika alkalmazására.

**Példa kód**:

```python
szam = int(input("Adj meg egy számot: "))

if szam % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")
```

**Minta kimenet**:

```
Adj meg egy számot: 7
A szám páratlan.
```

---

#### 6. Neptun kód generátor

**Leírás**:
Ez a program véletlenszerű alfanumerikus kódot generál, amely lehet például egy diákazonosító. A kód generálása során nagybetűket és számokat használ, és hat karakterből áll.

**Példa kód**:

```python
import random

karakterek = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Nagybetűk és számok
neptun_kod = "" 

for _ in range(6):  # Hat karaktert adunk hozzá egymás után
    veletlen_karakter = random.choice(karakterek)  # Kiválasztunk egy véletlen karaktert
    neptun_kod += veletlen_karakter  # Hozzáadjuk a kódhoz

print("A generált Neptun-kód:", neptun_kod)
```

**Minta kimenet**:

```
A generált Neptun-kód: A4J7P2
```

---

#### 7. Változó hosszúságú jelszó generátor

**Leírás**:
Ez a jelszógeneráló program lehetővé teszi a felhasználó számára, hogy megadja a jelszó kívánt hosszát. A program dinamikusan generálja a jelszót, figyelembe véve a felhasználó által megadott hosszúságot.

**Példa kód**:

```python
import random
import string

def jelszo_generalo(hossz):
    karakterek = string.ascii_letters + string.digits
    jelszo = ''.join(random.choice(karakterek) for _ in range(hossz))
    return jelszo

hossz = int(input("Add meg a jelszó hosszát: "))
print("A generált jelszó:", jelszo_generalo(hossz))
```

**Minta kimenet**:

```
Add meg a jelszó hosszát: 8
A generált jelszó: vT3x9K1q
```

---

#### 8. Fibonacci sorozat

**Leírás**:
Ez a program generálja a Fibonacci sorozatot egy megadott hosszúságig. A program bemutatja a Fibonacci sorozat létrehozásának algoritmusát és a listakezelés alapjait.

**Példa kód**:

```python
n = int(input("Add meg a Fibonacci sorozat hosszát: "))

sorozat = [0, 1]
while len(sorozat) < n:
    sorozat.append(sorozat[-1] + sorozat[-2])

print("A Fibonacci sorozat:", sorozat)
```

**Minta kimenet**:

```
Add meg a Fibonacci sorozat hosszát: 7
A Fibonacci sorozat: [0, 1, 1, 2, 3, 5, 8]
```

#### 9. Kő, Papír, Olló

```python
import random

print("Üdv a Kő, Papír, Olló játékban!")

# A játék addig fut, amíg a játékos játszani akar
while True:
    lehetosegek = ('kő', 'papír', 'olló')
    gep_valasztasa = random.choice(lehetosegek)  # A számítógép véletlenszerűen választ
    jatekos_valasztasa = input("Válassz: kő, papír vagy olló? ")  # A játékos választ

    print("A számítógép választása:", gep_valasztasa)
    
    # Döntés, ki nyert
    if jatekos_valasztasa == gep_valasztasa:
        print("Döntetlen!")
    if (jatekos_valasztasa == 'kő' and gep_valasztasa == 'olló') or \
         (jatekos_valasztasa == 'olló' and gep_valasztasa == 'papír') or \
         (jatekos_valasztasa == 'papír' and gep_valasztasa == 'kő'):
        print("Nyertél!")
    else:
        print("Vesztettél!")
    
    # Kérdezzük meg a játékost, hogy akar-e újra játszani
    ujra_jatek = input("Szeretnél újra játszani? (igen/nem): ")
    if ujra_jatek != 'igen':
        print("Köszönöm a játékot! Viszlát!")
        break
```

---

</div>

<div style="text-align: center; margin-bottom: 20px; margin-top: 20px; font-family: Arial, sans-serif; font-size: 1.2em; line-height: 1.5; color: #333;">
<img src="./QRCode for MCC.py visszajelzési kérdőív.png">
</div>

<div style="text-align: center; margin-bottom: 20px; margin-top: 20px; font-family: Arial, sans-serif; font-size: 1.2em; line-height: 1.5; color: #333;">
    <p style="margin: 0;">Készítette</p>
    <p style="margin: 0; font-weight: bold;">Borsos Samy & Herold Virág</p>
    <p style="margin: 0; font-style: italic;">2024</p>
    <p style="margin: 4; font-weight: bold;">MCC.py</p>
    <p style="margin: 0; font-weight: bold;"><img src="/mccpy/mccpy.svg" height=100px></p>
</div>


