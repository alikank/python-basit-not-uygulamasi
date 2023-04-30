from colorama import Fore, Back, Style

def karsila():
   print("Notlar : (notlar.txt)")
   try: # notlar.txt mevcutsa içeriğini yazdır.
    f = open("notlar.txt","r+",encoding="utf-8")
    print(f.read())
   except:
      print("İçerik yok, dosya boş!")
      f= open("notlar.txt","x",encoding="utf-8")
      
sira = 0
def notekle():
    global sira
    f = open("notlar.txt","r+",encoding="utf-8")
    son = f.readlines()
    try: # daha önce not yoksa sira 1 den başlar, daha önce not eklenmişse son eklenen notun numarasını çeker.
      if(int(son[-1][0])):
        sira = int(son[-1][0:2])
    except: pass   
    while True:
        note = input("Not girin , çıkış için --> q : ")
        if(note=="q"):
           f.close()
           karsila()
           break
        else:    
            sira += 1
        f.write(str(sira) + " " + note + "\n")    

def notsil():
    sil = input("Silmek istediğiniz notun başındaki sayıyı girin : ")
    f = open("notlar.txt","r+",encoding="utf-8")
    notes = f.readlines()
    for i in notes:
       if i[0:2] == sil or i[0] == sil:
          notes.remove(i) 
          f.close()
          break
    f = open("notlar.txt","w+",encoding="utf-8")  
    f.writelines(notes)   

while True:
   karsila()
   sayi = input(Fore.RED + "not eklemek için 1’e, not silmek için 2’ye ve çıkış için q’ya basın : "+ Style.RESET_ALL)
   if sayi=="q": break
   if 1==int(sayi): notekle()
   if 2==int(sayi): notsil()
