n = int(input("Add meg a Fibonacci sorozat hosszát: "))

sorozat = [0, 1]
while len(sorozat) < n:
    sorozat.append(sorozat[-1] + sorozat[-2])

print("A Fibonacci sorozat:", sorozat)