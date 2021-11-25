#soal 4 Tebak cacah
Var = 0
def tabakangka():
	global Var
	print("Apakah 4?\nApakah tebakan sudah benar ?\nlebih kecil (0)\nlebih besar (1)\nbenar (2)")
	b = int(input(": "))
	Var += 1

	if b == 0:
		print("Apakah 2?\nApakah tebakan sudah benar ?\nlebih kecil (0)\nlebih besar (1)\nbenar (2)")
		c = int(input(": "))
		Var += 1

		if c == 2:
			print("Jumlah tebakan :", Var)
			print("Program Selesai !")

		elif c == 0:
			print("Hasil Penjumlahannya Pasti 1 !")
			Var +=1
			print("Jumlah tebakan :", Var)
			print("Program Selesai !")

		elif c == 1:
			print("Hasil Penjumlahannya pasti 3 !")
			Var +=1
			print("Jumlah tebakan :", Var)
			print("Program Selesai !")

	elif b == 1:
		print("Apakah 6?\nApakah tebakan sudah benar ?\nlebih kecil (0)\nlebih besar (1)\nbenar (2)")
		d = int(input(": "))
		Var += 1

		if d == 2:
			print("Jumlah tebakan :", Var)
			print("Program Selesai !")

		elif d == 0:
			print("Hasil Penjumlahannya Pasti 5 !")
			Var +=1
			print("Jumlah tebakan :", Var)
			print("Program Selesai !")

		elif d == 1:
			print("Hasil Penjumlahannya Pasti 7 !")
			Var +=1
			print("Jumlah tebakan :", Var)
			print("Program Selesai !")		

	elif b == 2:
		print("Jumlah tebakan : ", Var)
		print("Program Selesai !")
            


print("Untuk memulai program masukkan (-1) untuk mulai")


a = int(input(": "))
if a == -1 : 
	tabakangka()
else : 
	print("Program tidak berhasil dijalankan")