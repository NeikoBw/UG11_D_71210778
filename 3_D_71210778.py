#SOAL 3 BANDING HASIL
import random 
tipe = input("Masukkan tipe yang ingin anda coba : ")

n1 = random.randint(1,20)
u = n1
n2 = random.randint(1,20)
k = n2
n3 = random.randint(1,20)
d = n3
n4 = random.randint(1,20)
w = n4
options = ["<",">","=="]
r_options = random.randint(0,2)
c_pick = options[r_options]

def generateSoal():
	print("(benar/salah) jika", end=" ")

	if tipe.lower()=="penjumlahan":
		print(n1,"+",n2,c_pick,n3,"+",n4, sep='')
	elif tipe.lower()=="pengurangan":
		print(n1,"-",n2,c_pick,n3,"-",n4, sep='')
		
	else:
		print("hanya ada tipe pengurangan/penjumlahan")

generateSoal()
jawaban = input("Masukkan Jawaban Anda: ")

def cekHasil():
	if c_pick == "<" and tipe.lower() == "penjumlahan":
		if ((u+k)<(d+w)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")

	elif c_pick == "<" and tipe.lower() == "pengurangan":
		if ((u-k)<(d-w)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")

	elif c_pick == ">" and tipe.lower() == "penjumlahan":
		if ((u+k)>(d+w)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")

	elif c_pick == ">" and tipe.lower() == "pengurangan":
		if ((u-k)>(d-w)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah!")

	elif c_pick == "==" and tipe.lower() == "penjumlahan":	
		if ((u+k)==(d+w)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")

	elif c_pick == "==" and tipe.lower() == "pengurangan":
		if ((u-k)==(d-w)) == True:
			if jawaban.lower() == "benar":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")	
		else: 
			if jawaban.lower() =="salah":
				print("Jawaban Anda Benar !")
			else:
				print("Jawaban Anda Masih Salah !")

cekHasil()