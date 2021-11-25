#Cek String
a = input("Masukkan string : ")

def cekString(a):
	if a.replace(".","").isnumeric() == True:
		if float(a)%2 == 0:
			print(format(float(a)/2, ".0f"))
		else :
			print(format((round(float(a))+5)/2, ".0f"))
	else:
		print(a[::-1])

cekString(a)