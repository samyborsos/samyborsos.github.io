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
        <img src="/mccpy/mcc.py.svg" alt="MCC Logo 2" style="width: 600px; height: auto;">
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

<p><a src="https://youtu.be/rjGGpfTARDA">Thonny telepítése</a></p>



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
  - [Indexelés](#indexelés)
    - [Mi az az indexelés?](#mi-az-az-indexelés)
    - [Példa: a `Python` szó](#példa-a-python-szó)
    - [Hogyan használjuk az indexelést?](#hogyan-használjuk-az-indexelést)
    - [Több betű kiválasztása](#több-betű-kiválasztása)
    - [Negatív indexelés](#negatív-indexelés)
    - [Több betű kiválasztása negatív indexeléssel](#több-betű-kiválasztása-negatív-indexeléssel)
    - [Összefoglalás](#összefoglalás)
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
  - [Listák](#listák)
    - [Listák létrehozása és kiíratása](#listák-létrehozása-és-kiíratása)
    - [Lista elemeinek összefűzése](#lista-elemeinek-összefűzése)
    - [A lista hossza](#a-lista-hossza)
    - [Lista elemek elérése indexekkel](#lista-elemek-elérése-indexekkel)
    - [Részletek a listából: Szeletek](#részletek-a-listából-szeletek)
    - [Utolsó elem elérése](#utolsó-elem-elérése)
    - [Listák bejárása](#listák-bejárása)
    - [Szövegek és listák](#szövegek-és-listák)
    - [Listák metódusai](#listák-metódusai)
- [Projektek (3. óra)](#projektek-3-óra)
    - [1. Számkitaláló játék](#1-számkitaláló-játék)
    - [2. Egyszerű kalkulátor](#2-egyszerű-kalkulátor)
    - [3. Egyszerű jelszógenerátor](#3-egyszerű-jelszógenerátor)
    - [4. Személyre szabott üdvözlés](#4-személyre-szabott-üdvözlés)
    - [5. Páros vagy páratlan szám?](#5-páros-vagy-páratlan-szám)
    - [6. Neptun kód generátor](#6-neptun-kód-generátor)
    - [7. Változó hosszúságú jelszó generátor](#7-változó-hosszúságú-jelszó-generátor)
    - [8. Fibonacci sorozat](#8-fibonacci-sorozat)

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

Innét kezdve az `x` változó értéke 5 lesz. A változóknak bármilyen nevet adhatunk, de nem kezdődhet számmal és nem tartalmazhat ékezetes betűket. Az ékezetes karakterek és különleges karakterek is használhatók, mint például `-` vagy `_`.

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

# Sztring -> T

izedes
tizedes = float('2.5')

# Szám -> Sztring
szam_sztring = str(100)
```

### Indexelés

#### Mi az az indexelés?

Az indexelés a sztringek és listák elemeinek elérését jelenti. Az indexek 0-tól kezdődnek, például:

```python
szoveg = "Python"
print(szoveg[0])  # Eredmény: P
```

#### Példa: a `Python` szó

A `Python` szó karaktereit indexeléssel érhetjük el:

- `P` a 0. index
- `y` az 1. index
- `t` a 2. index
- És így tovább


```
P    y    t    h    o    n
↑    ↑    ↑    ↑    ↑    ↑ 
0    1    2    3    4    5
```
#### Hogyan használjuk az indexelést?

Az indexelést arra használhatjuk, hogy egy sztring bármelyik karakterét elérjük:

```python
szoveg = "Python"
print(szoveg[0])  # P
print(szoveg[2])  # t
```

#### Több betű kiválasztása

Több karakter kiválasztásához szögletes zárójeleket használunk, például:

```python
szoveg = "Python"
print(szoveg[1:4])  # yth
```

Itt a karakterek az 1-es indexről kezdődnek és a 4-es indexig tartanak, a 4-es indexet nem tartalmazza.

#### Negatív indexelés

Negatív indexekkel visszafelé indexelhetünk:

```
 P    y    t    h    o    n
 ↑    ↑    ↑    ↑    ↑    ↑ 
-6   -5   -4   -3   -2   -1
```

```python
szoveg = "Python"
print(szoveg[-1])  # n
print(szoveg[-3])  # h
```

A -1 az utolsó karaktert jelöli, -2 az utolsó előtti karaktert, és így tovább.

#### Több betű kiválasztása negatív indexeléssel

Több karakter kiválasztása negatív indexeléssel:

```python
szoveg = "Python"
print(szoveg[-5:-2])  # tho
```

#### Összefoglalás

- **Változók:** Tárolnak értékeket és hivatkozhatunk rájuk a nevek segítségével.
- **Típusok:** `int`, `string`, `float`, `boolean`.
- **Átalakítás:** Típusok közötti konvertálás.
- **Indexelés:** Karakterek elérése egy sztringben.
- **Negatív indexelés:** Karakterek visszafelé történő elérése.

---

### Adatbekérés és műveletek

#### Adatbekérés

Adatbekéréshez használjuk a **`input()`** függvényt:

```python
nev = input("Hogy hívnak?")
print("Üdvözöllek, " + nev)
```

Az **`input()`** függvény a felhasználótól kér be adatot és az eredmény sztringként tárolódik.

#### Műveletek

Matematikai műveleteket végezhetünk a felhasználó által megadott számokon:

```python
szam1 = int(input("Adj meg egy számot: "))
szam2 = int(input("Adj meg egy másik számot: "))
eredmeny = szam1 + szam2
print("A két szám összege: " + str(eredmeny))
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
<h1>Számkitalálós játék (Guess The Number Game)</h1>

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

if szam == True:
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

### Listák

A listák kulcsfontosságúak a programozásban, mivel lehetővé teszik, hogy több különböző elemet (például szavakat, számokat) egyetlen csoportban, vagyis egy listában tároljunk. A Pythonban listát úgy hozhatunk létre, hogy az elemeket szögletes zárójelek [ ] közé helyezzük, és vesszővel választjuk el őket egymástól. 

Képzeljük el, mintha különféle szavakat **`(például: 'január', 'február', 'március', 'április')`** egy nagyobb dobozba (a **`honapok`** nevű listába) gyűjtenénk össze.

#### Listák létrehozása és kiíratása

Egy lista létrehozása egyszerű:

```python
honapok = ['január', 'február', 'március', 'április']
```

Ez a lista négy hónap nevét tartalmazza. Kiírathatjuk a listát a `print()` függvénnyel:

```python
print(honapok)
```

Ez a parancs kiírja a teljes listát, vagyis az összes hónapot.

#### Lista elemeinek összefűzése

A `join()` metódussal a lista elemeit egy sztringgé fűzhetjük össze, egy megadott elválasztó karakterrel tagolva:

```python
print(', '.join(honapok))
```

Ez a parancs egy szöveggé fűzi össze a hónapokat, vesszővel és szóközzel elválasztva őket: `január, február, március, április`.

#### A lista hossza

A `len()` függvénnyel megtudhatjuk, hány elem van a listában:

```python
print(len(honapok))
```

Ez kiírja, hogy a lista négy elemet tartalmaz.

#### Lista elemek elérése indexekkel

A listák elemeit az indexük alapján érhetjük el. Az indexek 0-tól kezdődnek, így az első elem indexe 0:

```python
print(honapok[0])
```

Ez kiírja az első elemet, azaz `január`-t.

Az utolsó elem indexe pedig 3 lesz, mivel összesen négy elem van a listában:

```python
print(honapok[3])
```

Ez kiírja az utolsó elemet, azaz `április`-t.

**Fontos:** Ha megpróbálnánk egy olyan indexet használni, ami nem létezik a listában, például a 4-es indexet, akkor hibát kapnánk, mert a listában csak négy elem van, és az utolsó elem indexe 3.

#### Részletek a listából: Szeletek

A listából kiválaszthatunk bizonyos elemeket is, úgynevezett "szeletek" használatával:

- Az 1-es és 2-es indexű elemek kiíratása:

    ```python
    print(honapok[1:3])
    ```

    Ez kiírja `február`-t és `március`-t.

- Az elejétől a 2-es indexű elemmel bezárólag:

    ```python
    print(honapok[:3])
    ```

    Ez kiírja `január`, `február` és `március` hónapokat.

- A 2-es indexű elemtől a végéig:

    ```python
    print(honapok[2:])
    ```

    Ez kiírja `március`-t és `április`-t.

#### Utolsó elem elérése

A listákban az utolsó elemet is könnyen elérhetjük, ha negatív indexet használunk:

```python
print(honapok[-1])
```

Ez kiírja az utolsó elemet, azaz `április`-t.

Ezek az alapvető műveletek segítenek abban, hogy hatékonyan tudj dolgozni a listákkal, és különböző módokon érhesd el az elemeket a programjaidban.
#### Listák bejárása

A lista bejárása azt jelenti, hogy minden elemet sorban megvizsgálunk. Ezt ciklus segítségével tehetjük meg. Például:

```python
for gyumolcs in gyumolcsok:
    print(gyumolcs)
```

Ez a program kiírja az összes gyümölcsöt a listából: "alma", "banán", "cseresznye".

#### Szövegek és listák

A szövegek is tekinthetők egyfajta listának, ahol minden egyes karakter egy elem. Ezért ugyanúgy bejárhatjuk őket, mint a listákat:

```python
szoveg = "Python"
for betu in szoveg:
    print(betu)
```

Ez kiírja a "Python" szó minden egyes betűjét külön sorban.

#### Listák metódusai

A listáknak vannak speciális "metódusai", amelyekkel műveleteket végezhetünk rajtuk. Például:

- **`append()`**: Új elemet ad a lista végéhez.

```python
gyumolcsok.append("dinnye")
print(gyumolcsok)
```

Ez hozzáadja a "dinnye" szót a lista végéhez.

- **`remove()`**: Eltávolít egy adott elemet a listából.

```python
gyumolcsok.remove("banán")
print(gyumolcsok)
```

Ez eltávolítja a "banán"-t a listából.


Ez a **for** ciklus kiírja az összes számot a listából.

A **while** ciklus hasonló feladatot tud végrehajtani, de rugalmasabban kezelheti a feltételeket:

```python
i = 0
while i < len(szamok):
    print(szamok[i])
    i += 1
```

Ez is kiírja az összes számot, de egy **while** ciklussal, amely addig fut, amíg az index (i) kisebb, mint a listában lévő elemek száma.

Példák:

A második óra kis projektjeinek összeállításakor fontos, hogy a feladatok játékosak és érdekesek legyenek, miközben erősítik a hallgatók által az első órán tanult alapvető Python fogalmakat. Mivel a ciklusok és listák még nem kerültek bevezetésre, ezek a projektek főként a változók, matematikai műveletek, logikai kifejezések, adatbekérés, és véletlenszám-generálás köré épülnek.

Persze, itt van a kiegészített szöveg minden projekthez, rövid leírással és mintakimenettel:

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

---





<div style="text-align: center; margin-bottom: 20px; margin-top: 20px; font-family: Arial, sans-serif; font-size: 1.2em; line-height: 1.5; color: #333;">
    <p style="margin: 0;">Készítette</p>
    <p style="margin: 0; font-weight: bold;">Borsos Samy & Herold Virág</p>
    <p style="margin: 0; font-style: italic;">2024</p>
    <p style="margin: 4; font-weight: bold;">MCC.py</p>
    <p style="margin: 0; font-weight: bold;"><img src="/mccpy/mcc.py.png" height=100px></p>
</div>

