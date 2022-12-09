batesan = int(input("Masukkan Pembatas : "))
keri = int(input("Masukkan angka yang dilarang : "))

for i in range(batesan):
    if i == keri:
        continue
    print(i, end=' ')

