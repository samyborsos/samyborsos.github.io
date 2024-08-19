import random

karakterek = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Nagybetűk és számok
neptun_kod = "" 

# Hat karaktert adunk hozzá egymás után
for i in range(6):  # A ciklus hatszor fog lefutni
    veletlen_karakter = random.choice(karakterek)  # Kiválasztunk egy véletlen karaktert
    neptun_kod += veletlen_karakter  # Hozzáadjuk a kódhoz

print("A generált Neptun-kód:", neptun_kod)