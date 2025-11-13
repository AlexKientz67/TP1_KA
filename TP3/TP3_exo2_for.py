import time

n = int(input("Entrez un nombre : "))

for i in range(n, -1, -1):
    print(i)
    time.sleep(1)
