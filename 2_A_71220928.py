jeneng = input("masukkan nama : ")

q = 0

for i in range(len(jeneng)):
    q += 1
    print(jeneng[:q])

for i in range(len(jeneng)):
    q -= 1
    print(jeneng[:q])






