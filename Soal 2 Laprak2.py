def hitung_fungsi(x):
    return (2 * x**3 + 2 * x + 15) / x if x != 0 else None

x = int(input("Input nilai x (bilangan bulat): "))
hasil_fungsi = hitung_fungsi(x)

if hasil_fungsi is not None:
    print(f"Jika X = {x}, maka nilai yang dihasilan {hasil_fungsi:.2f}")
else:
    print("Nilai x tidak boleh sama dengan 0 karena menyebabkan pembagian dengan nol.")