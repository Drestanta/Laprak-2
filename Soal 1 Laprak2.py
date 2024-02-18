def hitung_berat_badan(tinggi_badan, bmi_harap):
    berat_badan_diperlukan = bmi_harap / tinggi_badan**2
    return berat_badan_diperlukan

tinggi_badan = float(input("Masukkan tinggi badan (meter): "))
bmi_harap = float(input("Masukkan nilai BMI yang diharapkan: "))
berat_diperlukan = hitung_berat_badan(tinggi_badan, bmi_harap)

if berat_diperlukan < 18.5:
    print(f"Hasil dari perhitungan BMI adalah {berat_diperlukan:.2f} kg, termasuk Underweight")
elif berat_diperlukan >= 18.5 and berat_diperlukan <= 24.9:
    print(f"Hasil dari perhitungan BMI adalah {berat_diperlukan:.2f} kg, termasuk Normal")
elif berat_diperlukan >= 25 and berat_diperlukan <= 30:
    print(f"Hasil dari perhitungan BMI adalah {berat_diperlukan:.2f} kg, termasuk Overweight")
else:
    print(f"Hasil dari perhitungan BMI adalah {berat_diperlukan:.2f} kg, termasuk Obesitas")