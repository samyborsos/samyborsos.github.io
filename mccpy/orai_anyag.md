
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
  - [Logikai kifejezések](#logikai-kifejezések)
    - [Feltételes utasítás (if)](#feltételes-utasítás-if)
    - [További feltételek (else)](#további-feltételek-else)
    - [Összehasonlító operátorok](#összehasonlító-operátorok)
    - [Logikai operátorok](#logikai-operátorok)
  - [Véletlen számok generálása pythonban](#véletlen-számok-generálása-pythonban)
    - [Példa: 1 és 10 közötti véletlenszám generálása](#példa-1-és-10-közötti-véletlenszám-generálása)
    - [Miért fontosak a véletlenszámok?](#miért-fontosak-a-véletlenszámok)
  - [Projektek (2. óra)](#projektek-2-óra)
    - [1. óra ismétlése](#1-óra-ismétlése)
      - [Python alapok](#python-alapok)
      - [Változók](#változók)
      - [Indexelés](#indexelés-1)
      - [Adatbekérés és műveletek](#adatbekérés-és-műveletek-1)
      - [Logikai kifejezések](#logikai-kifejezések-1)
      - [Véletlen számok generálása](#véletlen-számok-generálása)
  - [Projektek (3. óra)](#projektek-3-óra)

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
- `h` a 3. index
- `o` a 4. index
- `n` az 5. index

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

---

### Véletlen számok generálása pythonban

#### Példa: 1 és 10 közötti véletlenszám generálása

A **`random`** modul segítségével véletlen számokat generálhatunk:

```python
import random
veletlen_szam = random.randint(1, 10)
print(veletlen_szam)
```

#### Miért fontosak a véletlenszámok?

A véletlenszámok hasznosak játékokban, statisztikai elemzésekben és más területeken, ahol a véletlen események modellezése szükséges.

---

### Projektek (2. óra)

#### 1. óra ismétlése

##### Python alapok

A Python alapok ismerete az első óra tartalmát képezi.

##### Változók

A változók kezelése, típusok és indexelés.

##### Indexelés

Az indelés bemutatása és variációi.

##### Adatbekérés és műveletek

Adatbekérés és matematikai műveletek végrehajtása.

##### Logikai kifejezések

Feltételes utasítások és logikai operátorok.

##### Véletlen számok generálása

Véletlen számok generálása Pythonban.

### Projektek (3. óra)

Az első és második óra tartalmának ismétlése és mélyebb projektek megvalósítása.

---