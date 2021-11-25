#SOAL 2 STRING INSERT
string = input("Masukkan sebuah kata atau kalimat :")
sisipan = input ("Masukkan karakter yang ingin disisipkan :")

def sisipHuruf(string,sisipan) :
    a = string.upper ()
    print(sisipan.join(list(a)))

def sisipKata(string,sisipan) :
    b = string.title()
    print (sisipan.join(b.split()))

sisipHuruf(string, sisipan)
sisipKata(string, sisipan)