# MCC.py orai anyag

# Lesson 1

## Első lépések

### Python Alapok: Kód és Kimenet

A Python kód általában két fő részből áll: a kódot író rész (felső) és a kimenet, azaz az output (alsó). Ha szöveget szeretnénk megjeleníteni, azt a következő módon tehetjük meg:

```python
print("Samy")
print('Samy')
```

Ez hasonló egy Excel-függvényhez: amit a zárójelbe írunk, azt fogja kiírni a program. A szöveget, amelyet a programozásban sztringnek nevezünk, idézőjelekkel vagy aposztrófokkal adhatjuk meg. Mindkettő használható, és az eredmény ugyanaz lesz.

```python
print('almafa')
```

### Hibák és hibaüzenetek

Ha hibát találunk a kódban, ne ijedjünk meg! A hibaüzenet gyakran pontos információt ad arról, hogy mi a probléma, és néha egy nyíllal is jelzi a hiba helyét.

### Matematikai kifejezések

A Python képes matematikai műveletek végrehajtására is. Például, az alábbi kóddal összeadunk két számot:

```python
print(4 + 5)
```

Ez az utasítás az `9` eredményt adja, mert a Python elvégzi az összeadást.

### Sztringek összefűzése

Sztringeket is össze tudunk fűzni. Például, ha a következő kódot futtatjuk le:


Ha azt írom hogy `alma + banan`, akkor azt hozza ki hogy `almabanan`.
Ha azt írom hogy `alma, banan`, akkor `alma banan`. *Mi a különbség?* Nem mindegy, hogy 45 vagy 4 5.

```python
print("alma" + "banan") # szövegösszfüzés
print("alma", "banan") # egymás mellé kiiratás
```

### Sztringek összeadása

Most nézzük meg, mi történik a következő kóddal:

```python
print('4' + '5')
```

Mivel a `4` és `5` sztringek (idézőjelek között vannak), a Python ezeket szövegként kezeli, ezért az eredmény `45` lesz, nem pedig `9`. Ez hasonlóan működik, mint a sztringek összefűzése.

### Kommentek (megjegyzések)

Kommentekkel kódunk egyes részeire utalhatunk anélkül, hogy azok befolyásolnák a kód futását. Például:

```python
# ez csak egy megjegyzés
print("Samy") # megjegyzés
```

A kettőskereszt (`#`) jelzi, hogy a sor a program végrehajtása során figyelmen kívül lesz hagyva. Kommentekkel információkat adhatunk a kódhoz anélkül, hogy az befolyásolná a kimenetet.

### Üres sorok

Az üres sorok hasonlóan működnek, mint a kommentek: nem befolyásolják a kód végrehajtását, viszont javítják a kód olvashatóságát.

### Összefoglaló

- **Szöveg kiírása:** `print("szöveg")` vagy `print('szöveg')`.
- **Matematikai műveletek:** Alapvető aritmetikai műveletek, mint az összeadás.
- **Sztringek összefűzése:** `print("szöveg1" + " szöveg2")`.
- **Sztringek összeadása:** Az idézőjelek között lévő számok szövegként kezelendők.
- **Kommentek:** `#` jel után következő szöveg, amely nem befolyásolja a kódot.
- **Üres sorok:** Az olvashatóságot javítják.




## Változók (tárolás és hivatkozás)

A programozás során szükségünk lesz úgynevezett "dobozokra", amelyekben különböző értékeket tárolhatunk. Ezeket **változóknak** nevezzük. Ezeket a változókat úgy kell elképzelnünk, mint amit középiskolában tanultunk: például `x = 5`. Innentől kezdve, ha később használjuk az `x` változót, a program tudja, hogy annak értéke 5.

Másképpen úgy gondolhatunk a változóra, mint egy felcímkézett doboz, melynek cimkéjén az áll, hogy `x`, benne pedig megtalálható az `5`.

Úgy is érthetjük, mint egy hivatkozás, a dokumentum elején megadom, hogy `x = 5`, ezért a dokumentum bármelyik pontján erre hivatkozhatok simán `x`-ként.

Fontos megjegyezni, hogy a változónak bármilyen nevet adhatunk, de nem kezdődhet számmal, és nem tartalmazhat ékezetes betűket. Különleges karaktereket is tartalmazhat, mint például `-` vagy `_`.

Például van egy hosszú számunk, ezzel a hosszú számmal műveleteket akarunk végezni, egyszer / 4, aztán + 88888. Ahhoz, hogy időt spóroljunk és csökkentsük a hibalehetőséget ezt eltároljuk. Ezzel egyszerűbb a kód és nem kell annyit írnunk.

```python
print('Ez egy hosszú szöveg')
```
Probléma: 
Triviális megoldásnak tűnik, hogy a kódot egyszerűen megduplázzuk, de ez **probléma**:

```python
print('Ez egy hosszú szöveg')
print('Ez egy hosszú szöveg')
```

Viszont, ha a szöveget később módosítani szeretnénk, minden egyes sorban egyenként kellene változtatni. Egyszerűbb, ha ezt a szöveget egy **változóba** tesszük, például `szoveg` néven, majd kiírjuk kétszer:

```python
szoveg = 'Ez egy hosszú szöveg'
print(szoveg)
print(szoveg)
```

Így, ha most módosítani szeretnénk a szövegünket, csak egy helyen kell változtatnunk.

A print fügvénnyel akár több változót is kiírathatunk azok összefűzése nélkül is.

```python
szoveg1 = 'Több változó kiiratása '
szoveg2 = 'összefüzés néllkül'
print(szoveg1, szoveg2)
```
  

### Típusok

A Python nyelvben négy fő változótípus van. Nézzünk egy példát:

- **int**: egész számok (integer) - `5`
- **string**: szöveg - `Alma`
- **float**: tizedes tört / lebegőpontos szám - `0.75`
- **boolean**: logikai érték, ami **`True`** vagy **`False`** lehet


### Átalakítás

A Pythonban a típusok között váltani átalakítási függvényekkel lehet. Az átalakítás a zárójelben megadott értékre történik. Példák az **int()**, **float()** és **str()** használatára:


Add meg az életkorodat, megadod azt, hogy 15. Ezt ő **szövegként** értelmezi, mint egy kérdésre adott válasz. Ahhoz, hogy később ezzel a számmal **műveleteket** tudjunk végezni, át kell alakítanunk **int** típusú változóvá, azaz **számmá**.

Gondoljunk a `print('4' + '5')` példájára, azért tettük időjezelek közé a számokat, mert szövegként szeretnék őket értelmezni, így nem a számok értéke adódik össze, hanem egymás mellé kerülnek, mint `45` **szövegként**.

Ez olyan, mintha azt írnátok le, `print('alma' + 'banan')`, amely eredménye `almabanan`.

```python
# sztring -> szám
szam = int('17')

# sztring -> tizedes tört
tizedes_tort = float('0.5')

# szám -> sztring
szoveg = str(17)
```




## Adatbekérés és műveletek

**Adatbekérés**
Szeretnék valakitől, valamilyen adatok megtudni. Ehhez kell egy inputot generálni, ami alkalmas arra, hogy válaszolni tudjanak rá, **válaszlehetőséget** a felhasználónak.

Az inputra csak **szövegként** lehet válaszolni, ezért azt át kell alakítani, ha később műveleteket akarunk vele végezni.
`input` mivel a felhasználótól kérünk be adatot, `' '` időzelejek, mivel szöveg és a szöveget mindig idézőjelek közé írjuk.

```python
input('Add meg a korodat!')
```
Ha a fenti kódot lefuttatjuk, nem ír ki semmit. Tudomásul vette, hogy hány éves vagy, de nem csinált vele semmit. Ha a felhasználó számára visszajelzést szeretnénk küldeni, akkor ezt az inputot el kell tárolni. *Megoldás:* **változó**.
Emlékeztek rá, amikor az előbb beszéltünk, hogy az `x` dobozban benne van az 5? itt az `x` dobozban az a szöveg lesz, ami az inputra válasz volt. 

```python
x = input('Add meg a korodat! ')
print(x)
```
Egy kis finomítással jobb tájékoztatást adunk a felhasználónak.
```python
x = input('Add meg a korodat!')
print('A te korod: ', x)
```

---
**Műveletek**
A Pythonban könnyedén végezhetünk alapvető matematikai műveleteket, mint például összeadás, kivonás, szorzás és osztás:

```python
# Összeadás
print(15 + 4)  # Eredmény: 19

# Kivonás
print(15 - 4)  # Eredmény: 11

# Szorzás
print(15 * 4)  # Eredmény: 60

# Osztás
print(15 / 4)  # Eredmény: 3.75
```

### Maradékos osztás (Modulo)

A maradékos osztás (`%`) olyan művelet, amely megadja, hogy egy számot elosztva egy másik számmal, mi marad az osztás után. Másképpen fogalmazva, megmutatja, hogy a két szám osztása után mennyi maradék marad.

Például:

```python
print(15 % 4)  # Eredmény: 3
```

#### Hogyan működik a maradékos osztás?

Vegyük például a `15 % 4` kifejezést. Itt azt vizsgáljuk, hogy 15-ben hányszor van meg a 4, és mi marad hátra az osztás után.

- **Számolás:** 15-ben a 4 háromszor van meg, mert 4 * 3 = 12.
- **Maradék:** 15 - 12 = 3.

Ezért a `15 % 4` eredménye 3, mivel a 15-ből a 12-t levonva 3 marad.

Egy másik példa:

```python
print(16 % 4)  # Eredmény: 0
```

Itt a 16 osztható 4-gyel maradék nélkül, így a maradék 0.

### Miért hasznos a maradékos osztás?

A későbbiekben sokat fogjuk használni, ezért fontos erről beszélni és megjegyezni.

Itt van a feltételes utasításokról szóló rész átdolgozott, érthetőbb változata:

---

## Feltételes utasítások

Egy program segítségével megvizsgálhatjuk a felhasználó életkorát, és eldönthetjük, hogy fogyaszthat-e alkoholt. Ehhez a korát kell ellenőriznünk.

### Példa: Alkohol fogyasztási korhatár

Az alábbi program bekéri a felhasználó életkorát, majd eldönti, hogy részt vehet-e a „party”-ban, azaz fogyaszthat-e alkoholt (például ha 18 éves vagy idősebb).

#### Alapvető kód:

```python
eletkor = int(input('Add meg a korodat! '))

print('Party!!!')

print('>> A program vége! <<')
```

**Probléma:** Ebben a kódban a `Party!!!` üzenet mindig megjelenik, függetlenül attól, hogy a felhasználó elérte-e a korhatárt. Ahhoz, hogy csak a 18 éves vagy idősebbek kapják meg a „party” üzenetet, feltételes utasítást kell használnunk.

### Feltételes utasítás (`if`):

Az if kulcsszó segítségével a programban feltételeket állíthatunk fel. Az if utasítás általában a következőképpen néz ki:

```python
if feltétel:
    # kód, amely akkor fut le, ha a feltétel igaz
```

Az `if` kulcsszóval ellenőrizhetjük, hogy a megadott életkor megfelel-e a feltételnek. A feltétel ebben az esetben az, hogy az életkor legyen 18 vagy több.




```python
eletkor = int(input('Add meg a korodat! '))

if eletkor >= 18:
    print('Party!!!')

print('>> A program vége! <<')
```

**Hogyan működik?**

- A program bekéri az életkorodat.
- Az `if eletkor >= 18` utasítás ellenőrzi, hogy az életkor nagyobb vagy egyenlő-e 18-nál.
- Ha igen, a program kiírja: „Party!!!”.
- Ha nem, a kód átugorja a `print('Party!!!')` utasítást, és folytatja a futást a következő sorral.

### Kezeljük azt az esetet is, ha valaki fiatalabb:

Ha azt is szeretnénk, hogy a program jelezze, ha valaki nem érte el a korhatárt, használhatjuk az `else` utasítást, amelyet közvetlenül az `if` után kell írni:

```python
eletkor = int(input('Add meg a korodat! '))

if eletkor >= 18:
    print('Party!!!')
else:
    print('Sajnos nincs party...')

print('>> A program vége! <<')
```

**Magyarázat:**

- Ha a `eletkor >= 18` feltétel nem teljesül, az `else` ágba lép a program.
- Itt a program kiírja: „Sajnos nincs party...”, jelezve, hogy a felhasználó túl fiatal az alkoholfogyasztáshoz.
- A végén a program lezárul az üzenettel: „>> A program vége! <<”.

Ez a feltételes utasítások egyszerű és hasznos módja annak, hogy különböző esetekre reagáljunk a programban.

## Logikai kifejezések

Logikai kifejezéseket a programozásban akkor használunk, amikor több feltételt szeretnénk összehasonlítani vagy kombinálni. Ezekhez különböző operátorokat használunk:

#### Összehasonlító operátorok:
- `==` : egyenlő, például `x == y` akkor igaz, ha x és y ugyanazt az értéket képviselik.
- `!=` : nem egyenlő, például `x != y` akkor igaz, ha x és y különböző értékek.
- `<` : kisebb, például `x < y` akkor igaz, ha x kisebb, mint y.
- `>` : nagyobb, például `x > y` akkor igaz, ha x nagyobb, mint y.
- `<=` : kisebb vagy egyenlő, például `x <= y` akkor igaz, ha x kisebb vagy egyenlő y-nal.
- `>=` : nagyobb vagy egyenlő, például `x >= y` akkor igaz, ha x nagyobb vagy egyenlő y-nal.

#### Logikai operátorok:
- `and` : és, akkor igaz, ha mindkét feltétel igaz.
- `or` : vagy, akkor igaz, ha legalább az egyik feltétel igaz.
- `not` : nem, akkor igaz, ha a feltétel hamis.

### Példák

Tegyük fel, hogy van két változónk, `x = 5` és `y = -3`:

```python
x = 5
y = -3
```

#### 1. Példa: Mindkettő negatív?

```python
if x < 0 and y < 0:
    print('mindkettő negatív')
```
Itt az `and` operátor azt jelenti, hogy a `print` utasítás csak akkor fut le, ha **mindkét feltétel igaz**. Mivel `x` nem negatív, ez az üzenet nem kerül kiírásra.

#### 2. Példa: Van köztük negatív?

```python
if x < 0 or y < 0:
    print('van köztük negatív')
```
Az `or` operátorral a feltétel akkor is igaz lesz, ha **csak az egyik** feltétel igaz. Ebben az esetben `y` negatív, így a program kiírja: „van köztük negatív”.

#### 3. Példa: `x` pozitív?

```python
if not x <= 0:
    print('x pozitív')
```
A `not` operátor megfordítja a feltétel értékét. Itt a `not x <= 0` kifejezés azt jelenti, hogy „x nem kisebb vagy egyenlő 0-val”, vagyis `x` pozitív, így a program kiírja: „x pozitív”.



## Véletlen Számok Generálása Pythonban

A véletlenszámok generálása számos programozási feladatban hasznos lehet, például játékokban, szimulációkban, vagy tesztadatok létrehozásakor. A Pythonban a `random` modul segítségével könnyen generálhatunk véletlen számokat.

#### Példa: 1 és 10 közötti véletlenszám generálása

Az alábbi kódban egy véletlenszámot generálunk az 1 és 10 közötti tartományban, beleértve a határokat is:

```python
import random

random_szam = random.randint(1, 10)
print(random_szam)
```

#### Hogyan Működik?

1. **`import random`**: A Python beépített `random` moduljának importálása. Ez a modul tartalmazza a véletlenszám-generáláshoz szükséges függvényeket.

2. **`random.randint(1, 10)`**: A `randint` függvény két argumentumot vár: egy alsó és egy felső határt. Ebben az esetben az 1 és 10 közötti egész számokból választ véletlenszerűen egyet, és visszaadja azt. Mind az alsó, mind a felső határ része a lehetséges értékeknek.

3. **`print(random_szam)`**: A generált véletlenszámot kiírja a konzolra.

#### Miért Fontosak a Véletlenszámok?

A véletlenszámok sokrétű felhasználási lehetőséget kínálnak:
- **Játékok**: A véletlenszerű események, például dobókocka eredmények vagy kártyahúzások szimulálására.
- **Szimulációk**: Olyan rendszerek modellezésére, ahol a véletlenszerűség fontos szerepet játszik, mint például a statisztikai mintavételezés.
- **Biztonság**: Kriptográfiai alkalmazásokban, például jelszavak generálásában, bár erre a `random` modul helyett a `secrets` modul ajánlott.

A `random` modulban sok más hasznos függvény is található, például véletlenszerű elemek kiválasztása listából (`random.choice`), vagy véletlenszám generálása a 0 és 1 közötti tartományban (`random.random`).