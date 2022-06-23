#sistem ini bagi mempelajari nama dan bentuk poligon
# turtle untuk melukis grafik
#time untuk lengah

import turtle
import time

#memanggil turtle
cute=turtle.Turtle()
cute.shape("turtle")
cute.pensize(2)
cute.color("black")
cute.speed(1)

#proses melukis

def lukis_bentuk(bil_sisi):
    for x in range(bil_sisi):
        cute.forward(100)
        cute.left(360/bil_sisi)
    return lukis_bentuk

#proses menamakan poligon
        
def nama_poligon(bil_sisi):
    if bil_sisi == 3:
        print("segitiga")
    elif bil_sisi == 4:
        print("segi empat")
    elif bil_sisi == 5:
        print("pentagon")
    elif bil_sisi== 6:
        print("heksagon")
    elif bil_sisi==7:
        print("heptagon")
    elif bil_sisi==8:
        print ("Oktagon")
    elif bil_sisi==9:
        print("Nonagon")
    elif bil_sisi==10:
        print("Dekagon")
    else:
        print("Opps sorry i dont'know")
    return nama_poligon

      

#start kod
while True:
    bil_sisi = int(input("Masukkan bilangan bilangan sisi poligon yang ingin depelajari, 3 hingga 10 : "))

    nama_poligon(bil_sisi)
    time.sleep (3)
    lukis_bentuk(bil_sisi)

    pilih = input("Ada lagi (y/t)")
    if pilih =="t":
        break


    
turtle.done()
    
  

