def hitung_pendapatan(gaji_per_jam, jam_kerja_per_minggu):
    pajak = 0.14
    belanja_pakaian = 0.10
    belanja_alat_tulis = 0.01
    sedekah = 0.25
    sedekah_anak_yatim = 0.30

    pendapatan_sebelum_pajak = gaji_per_jam * jam_kerja_per_minggu * 5
    pendapatan_setelah_pajak = pendapatan_sebelum_pajak * (1 - pajak)

    uang_belanja_pakaian = pendapatan_setelah_pajak * belanja_pakaian
    uang_belanja_alat_tulis = pendapatan_setelah_pajak * belanja_alat_tulis

    sisa_uang = pendapatan_setelah_pajak - (uang_belanja_pakaian + uang_belanja_alat_tulis)
    jumlah_sedekah = sisa_uang * sedekah

    jumlah_anak_yatim = jumlah_sedekah * sedekah_anak_yatim
    jumlah_dhuafa = jumlah_sedekah - jumlah_anak_yatim

    return pendapatan_sebelum_pajak, pendapatan_setelah_pajak, uang_belanja_pakaian, uang_belanja_alat_tulis, jumlah_sedekah, jumlah_anak_yatim, jumlah_dhuafa

gaji_per_jam = float(input("Masukkan gaji per jam yang diinginkan: "))
jam_kerja_per_minggu = float(input("Masukkan jumlah jam kerja per minggu: "))
hasil_perhitungan = hitung_pendapatan(gaji_per_jam, jam_kerja_per_minggu)

print("\nHasil Perhitungan:")
print(f"1. Pendapatan Budi sebelum pembayaran pajak: Rp {hasil_perhitungan[0]:,.2f}")
print(f"2. Pendapatan Budi setelah pembayaran pajak: Rp {hasil_perhitungan[1]:,.2f}")
print(f"3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris: Rp {hasil_perhitungan[2]:,.2f}")
print(f"4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis: Rp {hasil_perhitungan[3]:,.2f}")
print(f"5. Jumlah uang yang akan Budi sedekahkan: Rp {hasil_perhitungan[4]:,.2f}")
print(f"6. Jumlah uang yang akan diterima anak yatim: Rp {hasil_perhitungan[5]:,.2f}")
print(f"7. Jumlah uang yang akan diterima kaum dhuafa: Rp {hasil_perhitungan[6]:,.2f}")