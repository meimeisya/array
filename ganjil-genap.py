#Mengimout angka
angka = int(input("Masukan Angka: "))

#jika Habis Dibagi Nol,maka Genap
if (angka % 2) == 0:
    print("{0}adalah bilangan genap".format(angka))

#jika tidak habis dibagi nol,maka ganjil
else:
    print("{0}adalah bilangan ganjil".format(angka))