#setting variable
nim  = input("masukkan nim")
nama  = input("masukkan nama lengkap")
kelas = input("masukkan kelas")
prodi = input("masukkan nama prodi")

#setting variable nilai
b_id  = int(input("Nilai Bahasa indonesia  :"))
b_ig  = int(input("Nilai Bahasa Inggris    :"))
pd    = int(input("Nilai Pemrograman Dasar :  "))
mtk    = int(input("Nilai Matematika        :  "))
kal1   = int(input("Nilai Kalkulus          :   "))


if(b_id > 0 and b_id <=60):
    gind= ("C")
elif(b_id>60 and b_id <=75) :
    gind = ("B")
elif(b_id>75 and b_id <=85) :
    gind= ("AB")
elif(b_id >85 and b_id<=100) :
    gind= ("A")
else: 
    gind=("Grade Anda Tidak ditemukan! ")
    
if(b_ig> 0 and b_ig <=60):
    gind2= ("C")
elif(b_ig>60 and b_ig<=75) :
    gind2 = ("B")
elif(b_ig>75 and b_ig<=85) :
    gind2= ("AB")
elif(b_ig>85 and b_ig<=100) :
    gind2= ("A")
else: 
    gind2=("Grade Anda Tidak ditemukan! ")
  
if(pd> 0 and pd<=60):
    gind3= ("C")
elif(pd>60 and pd<=75) :
    gind3 = ("B")
elif(pd>75 and pd<=85) :
    gind3= ("AB")
elif(pd>85 and pd<=100) :
    gind3= ("A")
else: 
    gind3=("Grade Anda Tidak ditemukan! ")
   
if(mtk > 0 and mtk <=60):
   gind4 = ("C")
elif(mtk>60 and mtk <=75) :
    gind4=("B")
elif(mtk >75 and mtk<=85) :
    gind4= ("AB")
elif(mtk>85 and mtk<=100) :
    gind4= ("A")
else: 
    gind4=("Grade Anda Tidak ditemukan! ")
   
if(kal1> 0 and kal1 <=60):
    gind5= ("C")
elif(kal1>60 and kal1<=75) :
    gind5= ("B")
elif(kal1>75 and kal1<=85) :
    gind5= ("AB")
elif(kal1>85 and kal1<=100) :
    gind5= ("A")
else: 
    gind5=("Grade Anda Tidak ditemukan! ")
   
   
#perhitungan
rata = (b_id+b_ig+pd+mtk+kal1)/5

if(rata >0 and rata <=60) :
    grade_rata = ("c")
elif(rata >60 and rata <=75) :
    grade_rata = ("b")
elif(rata >75 and rata <=85) :
    grade_rata = ("AB")
elif(rata >85 and rata <=100) :
    grade_rata = ("A")
else: 
    grade_rata =("Grade Anda Tidak ditemukan! ")
   
#menampilkan
print("----------------------")
print("    kartu hasil studi     ")
print("----------------------")
print ("Nim           :",nim)
print ("nama lengkap  :",nama)
print ("kelas         :",kelas)
print ("program study :",prodi)
print ("----------------------")
print ("No  Nama Makul   Nilai   Grade  ")
print ("----------------------")
print ("1.  bahasa Indonesia  ",b_id,gind ), 
print ("2.  bahasa Inggris    ",b_ig,gind2 )
print ("3.  Pemrograman Dasar ",pd, gind3)
print ("4.  matematika        ",mtk, gind4)
print ("5.  Kalkulus 1        ",kal1, gind5 )
print ("----------------------")
print ("Rata-Rata             ",rata," ",grade_rata)
print ("----------------------")