# Program Sistem Rental Mobil

print("=== PROGRAM RENTAL MOBIL ===")
print("Daftar Mobil:")
print("1. Avanza - Rp300.000/hari")
print("2. Xenia  - Rp250.000/hari")
print("3. Innova - Rp400.000/hari")

while True:
    # Input jenis mobil
    mobil = input("\nMasukkan jenis mobil (Avanza/Xenia/Innova): ").capitalize()

    # Input durasi rental
    try:
        hari = int(input("Masukkan durasi rental (hari): "))
    except ValueError:
        print("Input durasi harus berupa angka!")
        continue

    # Penentuan harga berdasarkan jenis mobil
    if mobil == "Avanza":
        harga = 300000
    elif mobil == "Xenia":
        harga = 250000
    elif mobil == "Innova":
        harga = 400000
    else:
        print("Jenis mobil tidak tersedia!")
        continue

    # Hitung total biaya
    total = harga * hari
    print(f"Total biaya sewa {mobil} selama {hari} hari adalah: Rp{total:,}")

    # Tanya apakah ingin menyewa lagi
    ulang = input("\nApakah ingin menyewa mobil lain? (y/n): ").lower()
    if ulang != "y":
        print("\nTerima kasih telah menggunakan layanan rental kami!")
        break
