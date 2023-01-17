#menginput nilai Tugas,UTS,dan UAS
tugas = float(input("Masukan nilai Tugas: "))
uts = float(input("Masukan nilai UTS: "))
uas = float(input("Masukan nilai UAs: "))

#menghitung nilai akhir sesuai dengan bobot
nilai = (0.15 * tugas) + (0.35 * uts) + (0.50 * uas)

#menentukan grade berdasarkan nilai akhir
if nilai > 80:
    grade = "A"
elif nilai > 70:
    grade = "B"
elif nilai > 60:
    grade = "C"
elif nilai > 50:
    grade = "D"
else:
    grade = "E"
#Menentukan status kelulusan berdasarkan nilai akhie
if nilai > 60:
    status = "Lulus"
else:
    status = "Tidak lulus"

#Menampilkan nilai akhir,grade,dan status kelulusan
print("Nilai Akhir: %0.2f" % nilai)
print("Grade: {}".format(grade))
print("Status: {}".format(status))