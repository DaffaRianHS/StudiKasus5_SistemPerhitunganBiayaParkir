# Definisi hitungan total tarif parkir
def hitungan_parkir(tipe, jammasuk, jamkeluar):
    if tipe == "mobil":
        tarif = 5000
    elif tipe == "motor":
        tarif = 3000
    else:
        tarif = 0

    total_jam = jamkeluar - jammasuk
    total_tarif = tarif * total_jam
    return total_tarif

# Tipe kendaraan, jam kendaraan masuk dan keluar
tipe_kend = input("Masukkan tipe kendaraan: ")
masuk_jam = int(input("Masukkan jam berapa kendaraan masuk (0-23): "))
keluar_jam = int(input("Masukkan jam berapa kendaraan keluar (0-23): "))

# Output tipe kendaraan, jam kendaraan masuk, keluar, dan tarif parkir
hasil = hitungan_parkir(tipe_kend, masuk_jam, keluar_jam)
if hasil == 0:
    print("Tipe kendaraan: Tidak diketahui")
else:
    print("Tipe kendaraan", tipe_kend)
print(f"Jam kendaraan masuk: {masuk_jam}.00")
print(f"Jam kendaraan keluar: {keluar_jam}.00")
print("Tarif Parkir:", hasil)