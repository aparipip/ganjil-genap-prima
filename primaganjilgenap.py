def is_prime(angka):
    if angka <= 1:
        return False
    if angka <= 3:
        return True
    if angka % 2 == 0 or angka % 3 == 0:
        return False
    i = 5
    while i * i <= angka:
        if angka % i == 0 or angka % (i + 2) == 0:
            return False
        i += 6
    return True


angka_str = input("Masukkan sejumlah angka (pisahkan dengan spasi): ")

angka_list = angka_str.split()

for angka_str in angka_list:
    angka = int(angka_str)
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap.")
    else:
        print(f"{angka} adalah bilangan ganjil.")
    if is_prime(angka):
        print(f"dan merupakan bilangan prima.")
    else:
        print(f"dan bukan bilangan prima.")
