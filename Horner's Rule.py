# Program Python untuk
# implementasi metode Horner
# untuk Evaluasi Polinominal

# mengembalikan nilai poli[0]x(n-1)
# + poli[1]x(n-2) + .. + poli[n-1]
def horner(poli, n, x):

	# Inisialisasi hasil
	hasil = poli[0]

	# Evaluasi nilai polinominal
	# menggunakan metode Horner
	for i in range(1, n):

		hasil = hasil*x + poli[i]

	return hasil

# program driver untuk
# uji fungsi di atas.

# Mari kita evaluasi nilai dari
# 2x3 - 6x2 + 2x - 1 for x = 3
poli = [2, -6, 2, -1]
x = 3
n = len(poli)

print("Nilai dari Polinominal adalah" , horner(poli, n, x))
