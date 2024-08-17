
## Tartalomjegyzék

- [Python Alapok (1. Óra)](#python-alapok-1-óra)
  - [Első lépések](#első-lépések)
    - [Python Alapok: Kód és Kimenet](#python-alapok-kód-és-kimenet)
    - [Hibák és Hibaüzenetek](#hibák-és-hibaüzenetek)
    - [Matematikai Kifejezések](#matematikai-kifejezések)
    - [Sztringek Összefűzése](#sztringek-összefűzése)
    - [Sztringek Összeadása](#sztringek-összeadása)
    - [Kommentek (Megjegyzések)](#kommentek-megjegyzések)
    - [Üres Sorok](#üres-sorok)
    - [Összefoglaló](#összefoglaló)
  - [Változók (Tárolás és Hivatkozás)](#változók-tárolás-és-hivatkozás)
    - [Típusok](#típusok)
    - [Átalakítás](#átalakítás)
  - [Adatbekérés és Műveletek](#adatbekérés-és-műveletek)
    - [Adatbekérés](#adatbekérés)
    - [Műveletek](#műveletek)
    - [Maradékos Osztás (Modulo)](#maradékos-osztás-modulo)
  - [Logikai Kifejezések](#logikai-kifejezések)
    - [Összehasonlító Operátorok](#összehasonlító-operátorok)
    - [Logikai Operátorok](#logikai-operátorok)
    - [Példák](#példák)
  - [Véletlen Számok Generálása Pythonban](#véletlen-számok-generálása-pythonban)
    - [Példa: 1 és 10 Közötti Véletlenszám Generálása](#példa-1-és-10-közötti-véletlenszám-generálása)
    - [Miért Fontosak a Véletlenszámok?](#miért-fontosak-a-véletlenszámok)
- [Projektek (2. Óra)](#projektek-2-óra)
- [Projektek (3. Óra)](#projektek-3-óra)



# Python Alapok (1. Óra)

## Első lépések

### Python Alapok: Kód és Kimenet

A Python kód két fő részből áll: a kódot író rész és a kimenet (output). Szöveg megjelenítéséhez használjuk a `print()` függvényt:

```python
print("Samy")
print('Samy')
```

A szöveget (sztringet) idézőjelek (" ") vagy aposztrófok (' ') között kell megadni, és az eredmény azonos lesz.

```python
print('almafa')
```

### Hibák és Hibaüzenetek

Ha hibát találunk a kódban, ne ijedjünk meg! A hibaüzenet gyakran pontos információval szolgál a problémáról, és néha egy nyíllal jelzi a hiba helyét.

### Matematikai Kifejezések

A Python képes matematikai műveletek végrehajtására is. Például:

```python
print(4 + 5)
```

Ez az utasítás `9`-et eredményez, mivel a Python elvégzi az összeadást.

### Sztringek Összefűzése

Sztringeket is össze tudunk fűzni:

```python
print("alma" + "banan")  # Szövegösszefűzés
print("alma", "banan")   # Egymás mellé kiírás
```

- Az első példa `almabanan`-t ad vissza.
- A második példa `alma banan`-t ad vissza, mivel a `print` függvény szóközökkel választja el az elemeket.

### Sztringek Összeadása

A következő kód eredménye:

```python
print('4' + '5')
```

Mivel a `4` és `5` sztringek, az eredmény `45` lesz, nem pedig `9`. Ez a sztringek összefűzésére vonatkozik.

### Kommentek (Megjegyzések)

Kommentekkel dokumentálhatjuk a kódot anélkül, hogy az befolyásolná a végrehajtást:

```python
# Ez csak egy megjegyzés
print("Samy")  # Megjegyzés
```

A kettőskereszt (`#`) jelzi, hogy a sor figyelmen kívül lesz hagyva a program végrehajtása során.

### Üres Sorok

Az üres sorok növelik a kód olvashatóságát, de nem befolyásolják a kód végrehajtását.

### Összefoglaló

- **Szöveg kiírása:** `print("szöveg")` vagy `print('szöveg')`.
- **Matematikai műveletek:** Alapvető aritmetikai műveletek, mint az összeadás.
- **Sztringek összefűzése:** `print("szöveg1" + " szöveg2")`.
- **Sztringek összeadása:** Az idézőjelek között lévő számok szövegként kezelendők.
- **Kommentek:** `#` jel után következő szöveg, amely nem befolyásolja a kódot.
- **Üres sorok:** Az olvashatóságot javítják.

---

## Változók (Tárolás és Hivatkozás)

A programozás során változókra van szükségünk, amelyeket úgy kell elképzelnünk, mint dobozokat, amelyekben különböző értékeket tárolhatunk. Például:

```python
x = 5
```

Innét kezdve az `x` változó értéke 5 lesz. A változóknak bármilyen nevet adhatunk, de nem kezdődhet számmal és nem tartalmazhat ékezetes betűket. Az ékezetes karakterek és különleges karakterek is használhatók, mint például `-` vagy `_`.

### Típusok

A Python négy fő változótípust támogat:

1. **int**: Egész számok (pl. `5`)
2. **string**: Szöveg (pl. `Alma`)
3. **float**: Tizedes tört (pl. `0.75`)
4. **boolean**: Logikai érték, amely lehet **`True`** vagy **`False`**

### Átalakítás

A Pythonban a típusok közötti átalakításhoz használhatjuk az átalakító függvényeket, mint **`int()`**, **`float()`** és **`str()`**:

```python
# Sztring -> Szám
szam = int('17')

# Sztring -> Tizedes tört
tizedes_tort = float('0.5')

# Szám -> Sztring
szoveg = str(17)
```

---

## Adatbekérés és Műveletek

### Adatbekérés

Adatok bekéréséhez használjuk az `input()` függvényt:

```python
x = input('Add meg a korodat! ')
print('A te korod: ', x)
```

Ez a kód lehetővé teszi, hogy a felhasználó megadja az életkorát, amit egy változóba tárolunk, majd visszajelzést adunk róla.

### Műveletek

Alapvető matematikai műveletek a Pythonban:

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

### Maradékos Osztás (Modulo)

A maradékos osztás (`%`) a következőképpen működik:

```python
print(15 % 4)  # Eredmény: 3
```

Ez a művelet megmutatja, hogy egy szám osztásakor mi marad hátra.

---

## Logikai Kifejezések



### Összehasonlító Operátorok

Az összehasonlító operátorok segítenek a számok és szövegek összehasonlításában:

- `==` – egyenlőség
- `!=` – nem egyenlőség
- `>` – nagyobb
- `<` – kisebb
- `>=` – nagyobb vagy egyenlő
- `<=` – kisebb vagy egyenlő

Példa:

```python
x = 10
y = 5
if x > y:
    print("X nagyobb mint Y")
```

### Logikai Operátorok

A logikai operátorokkal több feltételt kombinálhatunk:

- `and` – logikai és (mindkét feltétel igaz)
- `or` – logikai vagy (legalább az egyik feltétel igaz)
- `not` – logikai negálás (a feltétel ellenkezője)

Példa:

```python
x = 5
if x > 0 and x < 10:
    print("X egy 1 és 10 közötti szám")
```

### Példák

Példa logikai kifejezésre:

```python
x = 5
if x > 0 and x < 10:
    print("X egy 1 és 10 közötti szám")
```

Ez a kód ellenőrzi, hogy `x` 1 és 10 közötti szám-e, és ha igen, kiírja a megfelelő üzenetet.

---

## Véletlen Számok Generálása Pythonban

### Példa: 1 és 10 Közötti Véletlenszám Generálása

A véletlen számok generálásához a `random` modult használhatjuk:

```python
import random
print(random.randint(1, 10))
```

Ez a kód egy véletlenszerű számot generál 1 és 10 között.

### Miért Fontosak a Véletlenszámok?

A véletlenszámok sok alkalmazásban hasznosak, például játékokban, szimulációkban és biztonsági alkalmazásokban. A randomizáció növeli a rendszer biztonságát és funkcionalitását azáltal, hogy előre nem látható kimeneteket biztosít.

---

# Projektek (2. Óra)
# Projektek (3. Óra)

