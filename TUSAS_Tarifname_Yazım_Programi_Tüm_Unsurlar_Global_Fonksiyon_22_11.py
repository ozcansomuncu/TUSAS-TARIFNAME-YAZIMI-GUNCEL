# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:58:30 2021

@author: Pc
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import scrolledtext

root = Tk()

root.title("TUSAŞ Tarifname Yazım Programı Toplam Unsur Sayısı Girişi")
root.iconbitmap('C:/Users/Pc/Desktop/Python Guncel/MMU_JPG-4.ico')
root.geometry("500x300")

#Fotoğrafı tanımladık.
bg = ImageTk.PhotoImage(Image.open("kasim.jpg")) #PIL Solution

#Arkaplanda gradyan geçişli görseller olunca label ların text lerin renginin sırıtmaması için canvas kullanıcaz.
my_canvas = Canvas(root, width=500, height=300)
my_canvas.pack(fill="both", expand=True)

#Canvas içerisinde arkaplan fotoğrafını ayarla.
my_canvas.create_image(0,0, image=bg, anchor="nw")

#Canvas'a Label ekliyoruz.
my_canvas.create_text(250, 200, text= "Patentlendin!", font= ("Helvetica", 75), fill="black")

#resizer fonksiyonunu yazıyoruz sayfayı büyüttüğümüzde background image'ın da büyümesi için.
def resizer(e):
    global bg1, resized_bg, new_bg
    #Open our image
    bg1 = Image.open("kasim.jpg")
    #Resize the image
    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
    #Define our image again
    new_bg = ImageTk.PhotoImage(resized_bg)
    #Add it back to canvas
    my_canvas.create_image(0,0, image=new_bg, anchor="nw")
    #Readd text
    my_canvas.create_text(250, 200, text= "Patentlendin!", font= ("Helvetica", 60), fill="black")

Label_1= Label(root, text="Toplam Unsur Sayısını Giriniz:") #.grid(row=0, column=1) (Alternatif yöntem)
label_1_window = my_canvas.create_window(35, 10, anchor="nw", window= Label_1) 

# Toplam Unsur Sayısı unsurunu depola

toplam_unsur_sayisi_intvar = IntVar()

toplam_unsur_sayisi_entry = Entry(root, textvariable=toplam_unsur_sayisi_intvar)

toplam_unsur_sayisi_entry_window= my_canvas.create_window(60, 30, anchor="nw", window= toplam_unsur_sayisi_entry) 

#toplam_unsur_sayisi_entry.grid(row=1, column=1)

def show_entry_fields(): #Bu fonksiyon, GUI'de girilen unsur sayısını kullanıcıya göstermek içindir.
    girilen_unsur_sayisi_text = my_canvas.create_text(250, 250, text= "Girilen toplam unsur sayisi: %s" % (toplam_unsur_sayisi_entry.get()), font= ("Helvetica", 20), fill="black")
    my_canvas.delete(girilen_unsur_sayisi_text)
    girilen_unsur_sayisi_text = my_canvas.create_text(250, 250, text= "Girilen toplam unsur sayisi: %s" % (toplam_unsur_sayisi_entry.get()), font= ("Helvetica", 20), fill="black")
    print("Girilen toplam unsur sayisi: %s" % (toplam_unsur_sayisi_entry.get())) #Bu kodu eğer "konsolda da" yazdırmak istiyorsan kullanabilirsin. 
    #Ama zaten GUI'de yazdığı için buna gerek yok.

Button_1 = Button(root, text='Toplam Unsur Sayisini Göster', command=show_entry_fields) #.grid(row=3, column=0, sticky=W, pady=4)

Button_1_window= my_canvas.create_window(20, 50, anchor="nw", window= Button_1) 

def open():   
    
    global unsur_isimleri_listesi, unsur_tanimlari_listesi
    
    master = Toplevel(root)
    master.grab_set() #to allow it to receive events andprevent users from interacting with the main window:
    master.title("TUSAŞ Tarifname Yazım Programı Unsur Referansları, İsimleri ve Tanımları Girişi")
    master.iconbitmap('C:/Users/Pc/Desktop/Python Guncel/MMU_JPG-4.ico')
    master.geometry("700x500")
    
    unsur_sayilari_listesi = []

    #Yukarıda unsur sayıları listesini oluşturmak için boş bir liste atadık. Daha sonra buraya 1'den n'e kadar unsur sayilarini atayacağız.
    
    #global toplam_unsur_sayisi, my_entries_unsur_isimleri, my_entries_unsur_tanimlari, unsur_isimleri_listesi,unsur_tanimlari_listesi, final_istem_cümlesi
    #problem globalden dolayı değilmiş. Şuan problem 1. GUI'de tuşa basınca 2. fonksiyonun otomatik çalışması!
    toplam_unsur_sayisi = toplam_unsur_sayisi_intvar.get()

    for i in range (1,toplam_unsur_sayisi+1):
        unsur_sayilari_listesi.append (i)
    
    #Yukarıda unsur sayiları listemizi 1'den n'e kadar boş listeye ekleye ekleye oluşturduk.

    #master = Tk()

    Label(master, text="Referans ").grid(row=0, column=1)
    Label(master, text="İsim ").grid(row=0, column=2)
    Label(master, text="Tanım ").grid(row=0, column=3)

    for z in range (1,toplam_unsur_sayisi+1):
       if z+1 == toplam_unsur_sayisi+1:
          Label(master, text= "1. unsur ").grid(row=z, column=0)
    
    my_entries_unsur_referanslari = StringVar()
    
    my_entries_unsur_referanslari= []
    
    my_entries_unsur_isimleri = StringVar()
    
    my_entries_unsur_isimleri= []
    
    my_entries_unsur_tanimlari = StringVar()
    
    my_entries_unsur_tanimlari= []
    
    #Harici Unsur Referansları Sütunu - Row Loop
    for x in range (1, toplam_unsur_sayisi+1):  
       my_entries_unsur_referanslari_entry = Entry (master)
       my_entries_unsur_referanslari_entry.grid(row=x, column=1, pady=20, padx=5)
       my_entries_unsur_referanslari.append(my_entries_unsur_referanslari_entry)
       
    #Harici Unsur İsimleri Sütunu - Row Loop
    for y in range (1, toplam_unsur_sayisi+1):  
       my_entries_unsur_isimleri_entry = Entry (master)
       my_entries_unsur_isimleri_entry.grid(row=y, column=2, pady=20, padx=5)
       my_entries_unsur_isimleri.append(my_entries_unsur_isimleri_entry)
        
    #Harici Unsur Tanımları Sütunu - Row Loop
    for z in range (1, toplam_unsur_sayisi):  
       my_entries_unsur_tanimlari_entry = Entry (master)
       my_entries_unsur_tanimlari_entry.grid(row=z, column=3, pady=20, padx=5, ipadx=50, ipady=10)
       my_entries_unsur_tanimlari.append(my_entries_unsur_tanimlari_entry)

    
    def show_values ():
        entry_list = ''
        
        for entries in my_entries_unsur_referanslari:
            entry_list = entry_list + str(entries.get()) + '\n'
            my_label.config(text=entry_list)
        
        for q in range(toplam_unsur_sayisi):
           print(my_entries_unsur_referanslari [q].get())
           
        for entries in my_entries_unsur_isimleri:
            entry_list = entry_list + str(entries.get()) + '\n'
            my_label.config(text=entry_list)
        
        for w in range(toplam_unsur_sayisi):
           print(my_entries_unsur_isimleri [w].get())
           
        for entries in my_entries_unsur_tanimlari:
            entry_list = entry_list + str(entries.get()) + '\n'
            my_label.config(text=entry_list)
        
        for w in range(toplam_unsur_sayisi-1):
           print(my_entries_unsur_tanimlari [w].get())
    
    
        ###-----------------------------------------------------------------------------###
        
        unsur_referanslari_listesi = StringVar ()
        
        unsur_referanslari_listesi = []
        #Yukarıda unsur isimleri listesini oluşturmak için boş bir liste atadık. Daha sonra buraya unsur isimlerini atayacağız.
            
        for i in range (0, toplam_unsur_sayisi):
            unsur_referanslari_listesi.append (i)
            
        #unsur_sayilari_listesi ile aynı üyeleri olan listeyi oluşturduk ki boş listemizde aynı sayıda unsurlar olsun. 
        #Daha sonra bu unsurları değiştireceğiz.
            
        for i in range (0, toplam_unsur_sayisi):
            unsur_referanslari_listesi [i] = my_entries_unsur_referanslari [i].get()
            
            #Yukarıda, my_entries listesinden değerleri unsur referanslarını atadık.    
               
        print ('Unsur Referansları Sırası ile aşağıdaki gibidir: ')
        print (unsur_referanslari_listesi)
        
        ###------------------------------------------------------------------------------###
        unsur_isimleri_listesi = StringVar ()
        
        unsur_isimleri_listesi = []
            
        #Yukarıda, unsur tanımları için boş liste tanımlanmışır.
            
        for i in range (0, toplam_unsur_sayisi):
            unsur_isimleri_listesi.append (i)
            
        #unsur_sayilari_listesi ile aynı üyeleri olan listeyi oluşturduk ki boş listemizde aynı sayıda unsur tanımları olsun. 
        #Daha sonra gerçek unsur tanımlarını gireceğiz.
            
        for i in range (0, (toplam_unsur_sayisi)):    
            unsur_isimleri_listesi [i] = my_entries_unsur_isimleri [i].get()
                  
            #Yukarıdaki for döngüsü ile 1. indexten n. idexe kadar, yani 2. unsurdan n. unsura kadar unsur tanımlarını aldık.
            
        print ('Unsur İsimleri Sırası ile aşağıdaki gibidir: ')
        print (unsur_isimleri_listesi)
        
        ###-----------------------------------------------------------------------------------###
       
        unsur_tanimlari_listesi = StringVar ()
       
        unsur_tanimlari_listesi = []
            
        #Yukarıda, unsur tanımları için boş liste tanımlanmışır.
            
        for i in range (0, toplam_unsur_sayisi-1):
            unsur_tanimlari_listesi.append (i)
            
        #unsur_sayilari_listesi ile aynı üyeleri olan listeyi oluşturduk ki boş listemizde aynı sayıda unsur tanımları olsun. 
        #Daha sonra gerçek unsur tanımlarını gireceğiz.
            
        for i in range (0, (toplam_unsur_sayisi-1)):    
            unsur_tanimlari_listesi [i] = my_entries_unsur_tanimlari [i].get()
                  
            #Yukarıdaki for döngüsü ile 1. indexten n. idexe kadar, yani 2. unsurdan n. unsura kadar unsur tanımlarını aldık.
            
        print ('Unsur Tanımları Sırası ile aşağıdaki gibidir: ')
        print (unsur_tanimlari_listesi)
        
        
        #print(my_entries [24].get()) #Konsolda yazılmasını istediğin şeyi böyle yazabilirsin, 
        #örneğin 5e5lik bir matris için 24 yazarsan son hücreyi yazdırır.  
        
        unsurlar = StringVar ()
        
        unsurlar = []
        
        for i in range (toplam_unsur_sayisi):
            unsurlar.append(toplam_unsur_sayisi)
        
        referans = 'referans'
        isim = 'isim'
        tanim = 'tanim'
        
        for i in range (0, toplam_unsur_sayisi-1):
            unsurlar [i] = {
                referans: unsur_referanslari_listesi [i],
                isim: unsur_isimleri_listesi [i],
                tanim: unsur_tanimlari_listesi [i]
        }
        
        for i in range (toplam_unsur_sayisi-1, toplam_unsur_sayisi):
            unsurlar [i] = {
                referans: unsur_referanslari_listesi [i],
                isim: unsur_isimleri_listesi [i]
        }
        
        for i in range (toplam_unsur_sayisi):
            print (unsurlar [i].get(referans))
            print (unsurlar [i].get(isim))
        
        for i in range (toplam_unsur_sayisi-1):
            print (unsurlar [i].get(tanim))
        
        ###---------------------------------------------------------------------------------###
        
        #Buradan aşağıdaki kodlar önceki hazır kodlardan direkt geldi.
            
        unsur_tanimlari_listesi_split = []
            
        #Yukarıdaki kod ile istem cümlesi için boş bir liste atadık, böylelikle her bir unsur cümlesini aşağıda yazılan kodla ekleyip
        #sonrasında bu ana istem cümlesinden index ile çekip cümleyi oluşturacağım.
            
        for i in range (0, toplam_unsur_sayisi-1):
            unsur_tanimlari_listesi_split.append (i)
            
        for i in range (0,toplam_unsur_sayisi-1):
            unsur_tanimlari_listesi_split [i] = unsur_tanimlari_listesi [i].split ()
        
        ### unsurlar [i].get(tanim)
        
        #unsur_referanslari_listesi = ["u1","u2","u3","u4","u5","u6","u7","u8","u9","u10","u11","u12","u13","u14","u15","u16","u17","u18","u19","u20"]
        '''    
        for i in range (0, toplam_unsur_sayisi-1):
           for l, item_3 in enumerate (unsur_tanimlari_listesi_split [i]):
              if unsur_tanimlari_listesi_split [i] [l].startswith (unsurlar [i].get(referans)):
                 unsur_tanimlari_listesi_split [i] [l] = item_3 + (unsurlar [i].get(referans))
              else:
                 unsur_tanimlari_listesi_split [i] [l] = item_3
        '''   
        
        '''
        #Buradan aşağıdaki kodlar önceki hazır kodlardan direkt geldi.
            
        unsur_tanimlari_listesi_split = []
            
        #Yukarıdaki kod ile istem cümlesi için boş bir liste atadık, böylelikle her bir unsur cümlesini aşağıda yazılan kodla ekleyip
        #sonrasında bu ana istem cümlesinden index ile çekip cümleyi oluşturacağım.
            
        for i in range (1, toplam_unsur_sayisi+1):
            unsur_tanimlari_listesi_split.append (i)
            
        for i in range (1,toplam_unsur_sayisi):
            unsur_tanimlari_listesi_split [i] = unsur_tanimlari_listesi [i].split ()
            
        unsur_tanimlari_listesi_split [0] = unsur_tanimlari_listesi [0]
            
        ###----BİR ÜSTTEKİ KISIMDAN BURAYA KADAR OLAN KISIMDA NE YAPTIĞIMI ANLAMAYA ÇALIŞ :D
            
        unsur_isimleri_listesi_unsuz_yumusamasi_hali = []
            
        for i in range (0,toplam_unsur_sayisi):
            unsur_isimleri_listesi_unsuz_yumusamasi_hali.append(unsur_isimleri_listesi [i])
            
        unsuz_yumusamasi_harfleri_listesi_initial = ['ç', 'k', 'p', 't']
            
        unsuz_yumusamasi_harfleri_listesi_modified = ['c','ğ','b','d']
            
        gecici = ['']
            
        for i in range (1, toplam_unsur_sayisi):
            if unsur_isimleri_listesi_unsuz_yumusamasi_hali [i].endswith (unsuz_yumusamasi_harfleri_listesi_initial [0]):
                gecici = list(unsur_isimleri_listesi_unsuz_yumusamasi_hali [i])
                gecici [-1] = unsuz_yumusamasi_harfleri_listesi_modified [0]
                unsur_isimleri_listesi_unsuz_yumusamasi_hali [i] = ''.join(gecici)
            elif unsur_isimleri_listesi_unsuz_yumusamasi_hali [i].endswith (unsuz_yumusamasi_harfleri_listesi_initial [1]):
                gecici = list(unsur_isimleri_listesi_unsuz_yumusamasi_hali [i])
                gecici [-1] = unsuz_yumusamasi_harfleri_listesi_modified [1]
                unsur_isimleri_listesi_unsuz_yumusamasi_hali [i] = ''.join(gecici)
            elif unsur_isimleri_listesi_unsuz_yumusamasi_hali [i].endswith (unsuz_yumusamasi_harfleri_listesi_initial [2]):
                gecici = list(unsur_isimleri_listesi_unsuz_yumusamasi_hali [i])
                gecici [-1] = unsuz_yumusamasi_harfleri_listesi_modified [2]
                unsur_isimleri_listesi_unsuz_yumusamasi_hali [i] = ''.join(gecici)
            elif unsur_isimleri_listesi_unsuz_yumusamasi_hali [i].endswith (unsuz_yumusamasi_harfleri_listesi_initial [3]):
                gecici = list(unsur_isimleri_listesi_unsuz_yumusamasi_hali [i])
                gecici [-1] = unsuz_yumusamasi_harfleri_listesi_modified [3]
                unsur_isimleri_listesi_unsuz_yumusamasi_hali [i] = ''.join(gecici)
            
        #-------------------UNSUR İSİMLERİNİN UNSUZ YUMUSAMASI HALLERİ LİSTESİNİN OLUŞTURULDUĞU KISIM BURAYA KADARKİ KISIM---------------
                    
        #-------ARTIK GEREKLİ TÜM LİSTE HAZIR, UNSUZ YUMUSAMASI İÇİN GEREKEN TÜM KOŞULLARI İF VE AND İLE AYNI KOMUTTA GİRİP UNSUZ YUMUSAMASI
        #OLUP OLMADIĞINI TESPİT EDİCEZ, VARSA UNSUZ YUMUSAMALI LİSTEDEKİ HALİNDEN AL DİYECEĞİZ.
            
            
            
        #-YUKARIDAKİ KODA EK İÇİN İLK HARFİN SESLİ HARF GELİP GELMEMESİ KOŞULU EKLENECEK. ÇÜNKÜ "DÖNER ÇUBUĞA" DA DEĞİŞMESİNİ İSTERİZ AMA "DÖNER ÇUBUKTAN" DA DEĞİŞMESİNİ İSTEMEYİZ. ÜNSÜZ YUMUŞAMASI EKİN İLK HARFİ ÜNLÜ HARF OLDUĞUNDA GERÇEKLEŞTİGİ İÇİN BUNU DA KODA KATMAM GEREKİYOR.
            
        unsur_referanslari_listesi = ["u1","u2","u3","u4","u5","u6","u7","u8","u9","u10","u11","u12","u13","u14","u15","u16","u17","u18","u19","u20"]
            
        for i in range (1, toplam_unsur_sayisi):
           for l, item_3 in enumerate (unsur_tanimlari_listesi_split [i]):
              if unsur_tanimlari_listesi_split [i] [l].startswith (unsur_referanslari_listesi [0]):
                 unsur_tanimlari_listesi_split [i] [l] = item_3 + ' (1).'
              elif unsur_tanimlari_listesi_split [i] [l].startswith (unsur_referanslari_listesi [1]):
                 unsur_tanimlari_listesi_split [i] [l] = item_3 + ' (2)'
              elif unsur_tanimlari_listesi_split [i] [l].startswith (unsur_referanslari_listesi [2]):
                 unsur_tanimlari_listesi_split [i] [l] = item_3 + ' (3)'
              elif unsur_tanimlari_listesi_split [i] [l].startswith (unsur_referanslari_listesi [3]):
                 unsur_tanimlari_listesi_split [i] [l] = item_3 + ' (4)'
              elif unsur_tanimlari_listesi_split [i] [l].startswith (unsur_referanslari_listesi [4]):
                 unsur_tanimlari_listesi_split [i] [l] = item_3 + ' (5)'
              else:
                 unsur_tanimlari_listesi_split [i] [l] = item_3
            
        #-YUKARIDAKİ KOD İLE UNSUR TANIMLARININ SPLIT VERSIYONU LISTESİNE YANİ UNSURLARA PARANTEZLİ REFERANS NUMARALARI ATANDI.
        #-DAHA SONRA BU KISMI BİR J YA DA K FOR DÖNGÜSÜ İLE TEK KODLU YAPMAYA ÇALIŞ.
            
        unsur_tanimlari_listesi_split_son = []
            
        unsur_tanimlari_listesi_split_son.append('')
        for k in range (1, len(unsur_tanimlari_listesi_split)):
            unsur_tanimlari_listesi_split_son.append(unsur_tanimlari_listesi_split [k])
            
        sesli_harfler = ['a','e','ı','i','o','ö','u','ü']
            
        #-Aşağıdaki kod ile kullanıcıya ünsüz yumuşaması ile ilgili bilgi verilmektedir.
            
        for i, item in enumerate(unsur_isimleri_listesi):
            for j, item_2 in enumerate(unsuz_yumusamasi_harfleri_listesi_initial):
                if item [-1].endswith (item_2):
                   print ("'{}.' unsur olan '{}' unsuru '{}'".format(i+1,item, item_2) + ' harfi ile bitmektedir ve ünsüz yumuşaması gerekebilir.') 
                else:
                    continue
            
        #-Yukarıdaki kodun amacı kullanıcıya ünsüz yumuşaması konusunda bilgi vermektir. Hangi unsur isimlerinin son harfine göre unsuz yumuşamasına
        #- uğrayabileceği söylenmektedir.
            
        for k in range (1, len(unsur_tanimlari_listesi_split)):
            for l, item_3 in enumerate(unsur_tanimlari_listesi_split [k]):
                for n in range (0,8):
                    if unsur_tanimlari_listesi_split [k] [l] [1].isdigit() and unsur_tanimlari_listesi_split [k] [l] [2] == sesli_harfler [n]:
                        print ("Unsur tanımlarında '[{}] [{}]' indexinde olan '{}' unsuru, unsur adından sonra '{}'".format(k,l,item_3,sesli_harfler [n]) + ' sesli harfi aldığı için ünsüz yumuşaması gerekebilir.')
                    else:
                       continue
            
        #-Yukarıdaki kodun amacı kullanıcıya ünsüz yumuşaması konusunda bilgi vermektir. Unsur tanımında u(n)'deki n sayısının olup olmadığına ve 
        #-n rakamından sonra sesli harf gelip gelmemesine göre unsuz yumuşaması ihtimatilini kullanıcıya söylüyor.
        #-Asıl değişim aşağıdaki kodlar ile yapılacaktır.
            
        for i, item in enumerate(unsur_isimleri_listesi):
           for j, item_2 in enumerate(unsuz_yumusamasi_harfleri_listesi_initial):
               for k in range (1, len(unsur_tanimlari_listesi_split_son)):
                    for l, item_3 in enumerate(unsur_tanimlari_listesi_split_son [k]):
                       for n in range (0,8):                
                           if unsur_isimleri_listesi [i] [-1].endswith (unsuz_yumusamasi_harfleri_listesi_initial [j]): #Buradan 3.(i=2) ve 5. (i=4) unsur isimleri geçecek
                               if unsur_tanimlari_listesi_split [k] [l].startswith (unsur_referanslari_listesi [i]): # [k] [l] = [3] [5] ve [3] [9] geçti.
                                  if unsur_tanimlari_listesi_split [k] [l] [2] == sesli_harfler [n]:
                                     unsur_tanimlari_listesi_split_son [k] [l] = unsur_tanimlari_listesi_split_son [k] [l].replace (unsur_referanslari_listesi [i], unsur_isimleri_listesi_unsuz_yumusamasi_hali [i])
                                  else:
                                      continue
                               else: 
                                   continue
                           else:
                               continue
            
        #-Yukarıdaki kodlar ile sadece unsuz yumusaması değişimlerini gerçekleştiriyoruz.
            
        for i, item in enumerate(unsur_isimleri_listesi):
            for k in range (1, len(unsur_tanimlari_listesi_split_son)):
                for l, item_3 in enumerate(unsur_tanimlari_listesi_split_son [k]):
                    if unsur_tanimlari_listesi_split [k] [l].startswith (unsur_referanslari_listesi [i]): # [k] [l] = [3] [5] ve [3] [9] geçti.
                       unsur_tanimlari_listesi_split_son [k] [l] = unsur_tanimlari_listesi_split_son [k] [l].replace (unsur_referanslari_listesi [i], unsur_isimleri_listesi [i])
                    else:
                        continue
            
        #- Yukarıdaki kod ile unsur referanslarını yerlerine yerleştirdik. Bir önceki kodda sadece unsuz yumusamasını değiştirdiğimiz için
        #-kalan tüm değişimleri bu kodlar ile gerçekleştirdik.
            
        unsur_tanimlari_listesi_string = []
            
        for i in range (0,toplam_unsur_sayisi):
            unsur_tanimlari_listesi_string.append(unsur_tanimlari_listesi_split_son [i])
            
        #-UNSUR TANIMI LİSTESİNİN STRING HALİNE ÇEVİRMEMİZ GEREKİYOR REPLACE FONK. İÇİN. BURADA BUNUN İÇİN BOŞ LİSTE ATAYIP DOLDURDUK
        #-DAHA SONRA DEĞİŞTİRMEK ÜZERE.
            
        for i in range (1, toplam_unsur_sayisi):
           unsur_tanimlari_listesi_string [i] = ' '.join(unsur_tanimlari_listesi_split_son [i])
            
        #- REPLACE FONKSİYONUNU GERÇEKLEŞTİREBİLMEK İÇİN TÜM İFADEYİ LİST'TEN STRING FORMATINA GERİ ÇEVİRDİK JOİN FONKSİYONU İLE.
            
        ###---BURAYA KADAR İŞİN KODSAL KISMI VAR, UNSUR İSİMLERİNİN ALINMASI, UNSUR TANIMLARININ ALINMASI, UNSUZ YUMUSAMASI YAPILMASI GİBİ GİBİ.###
        ###---AŞAĞIDAKİ KISIMLARDA TAMAMEN NİHAİ İSTEM CÜMLESİNİ YAZMAYA YÖNELİK KODLAR.###
        '''
        #-YUKARIDAKİ KOD İLE UNSUR TANIMLARININ SPLIT VERSIYONU LISTESİNE YANİ UNSURLARA PARANTEZLİ REFERANS NUMARALARI ATANDI.
        #-DAHA SONRA BU KISMI BİR J YA DA K FOR DÖNGÜSÜ İLE TEK KODLU YAPMAYA ÇALIŞ.
        
        unsur_tanimlari_listesi_string = []
            
        for i in range (0,toplam_unsur_sayisi-1):
            unsur_tanimlari_listesi_string.append(unsur_tanimlari_listesi_split [i])
            
        #-UNSUR TANIMI LİSTESİNİN STRING HALİNE ÇEVİRMEMİZ GEREKİYOR REPLACE FONK. İÇİN. BURADA BUNUN İÇİN BOŞ LİSTE ATAYIP DOLDURDUK
        #-DAHA SONRA DEĞİŞTİRMEK ÜZERE.
            
        for i in range (0, toplam_unsur_sayisi-1):
           unsur_tanimlari_listesi_string [i] = ' '.join(unsur_tanimlari_listesi_split [i])
            
        #- REPLACE FONKSİYONUNU GERÇEKLEŞTİREBİLMEK İÇİN TÜM İFADEYİ LİST'TEN STRING FORMATINA GERİ ÇEVİRDİK JOİN FONKSİYONU İLE.
        
        for i in range (toplam_unsur_sayisi-1):
            unsurlar [i].get(tanim) == unsur_tanimlari_listesi_string [i]
        
        ###---------------------------------------------------------------------------------###
        
        istem_cümlesi = []
            
        #Yukarıdaki kod ile istem cümlesi için boş bir liste atadık, böylelikle her bir unsur cümlesini aşağıda yazılan kodla ekleyip
        #sonrasında bu ana istem cümlesinden index ile çekip cümleyi oluşturacağım.
            
        for i in range (0, toplam_unsur_sayisi):
            istem_cümlesi.append (i)
            
        #unsur_sayilari_listesi ile aynı üyeleri olan listeyi oluşturduk ki boş listemizde aynı sayıda unsur tanımları olsun. 
        #Sonrasında asıl istem cümlesi girilecek.
            
        for i in range (0,toplam_unsur_sayisi):
            if i+2 < toplam_unsur_sayisi:
                istem_cümlesi [i]=  str(unsurlar [i].get(tanim)) + ' en az bir ' + str(unsurlar [i].get(isim)) + ' (' + str(((unsurlar [i].get(referans)).capitalize())) + '), '
            elif i+2 == toplam_unsur_sayisi:
                istem_cümlesi [i]=  str(unsurlar [i].get(tanim)) + ' en az bir ' + str(unsurlar [i].get(isim)) + ' (' + str(((unsurlar [i].get(referans)).capitalize())) + ') '
            else:
                istem_cümlesi [i]=  'ile karakterize edilen en az bir ' + str(unsurlar [i].get(isim)) + ' (' + str(((unsurlar [i].get(referans)).capitalize())) + '). '
            
        #Yukarıdaki kod ile for döngüsüyle tüm istemin cümlelerini indexleyerek birleştirdik tek bir list istem cümlesinde.
        #Ayrıca elif kısmının eklenmesinin sebebi karakterize edilen kısmından hemen önce yani son unsurdan sonra virgül koymamak. 
        #Ama şuanlık çalışmıyor, üzerinde çalış.
        
        final_istem_cümlesi = ['']
            
        for i in range (0,toplam_unsur_sayisi):
            final_istem_cümlesi [0] = final_istem_cümlesi [0] + (''.join(istem_cümlesi [i]))
            
        #tüm istem cümlesini for döngüsü ile bir değişkene atadık nihai olarak.
        
        print (str(final_istem_cümlesi [0]))
            
        #nihai istem cümlesini yazdırdık.  
        
    def text_editor():
        T.delete('1.0', END)
        T.insert(INSERT, str(final_istem_cümlesi [0]))
        
    show_value_button = Button (master, text="Girilen Verileri Göster", command=show_values)
    show_value_button.grid(row=15, column=0, pady=20)
    
    T = Text(master, height = 20, width = 100)
    T.place(x=600,y=400)
    
    my_label = Label (master, text= "")
    my_label.grid(row=1, column=4, pady=20)
    
    text_editor_button = Button (master, text="Text Editore Geç", command=text_editor) 
    text_editor_button.grid(row=15, column=1, pady=20)
    
    exit_button_2 = Button(master, text='Çıkış Yap', command=master.destroy)
    exit_button_2.grid(row=15, column=2, pady=20)
    
    master.mainloop()

Button_2 = Button(root, text='Unsur Referansları, İsimleri ve Tanımlamalarına Geç', command=open) #command=root.quit  #.grid(row=3, column=1, sticky=W, pady=4)

Button_2_window= my_canvas.create_window(200, 50, anchor="nw", window= Button_2) 

Button_3 = Button(root, text='Çıkış Yap', command=root.destroy)

Button_3_window= my_canvas.create_window(40, 100, anchor="nw", window= Button_3) 

root.bind('<Configure>', resizer)

root.mainloop()

'''
toplam_unsur_sayisi = 3

unsur_tanimlari_listesi_split = []

for i in range (0, toplam_unsur_sayisi):
    unsur_tanimlari_listesi_split.append (i)

unsur_tanimlari_listesi =["hava aracından hedefine taarruz etmek amacıyla gönderilen", "Ma basınç uygulayarak stabilitesini sağlayan", "teknisyen tarafından Pları döndürmek için kullanılan, Pa dönmesi için gerekli hareketi sağlayan"]

for i in range (0,toplam_unsur_sayisi):
    unsur_tanimlari_listesi_split [i] = unsur_tanimlari_listesi [i].split ()

unsurlar = []
        
for i in range (toplam_unsur_sayisi):
   unsurlar.append(toplam_unsur_sayisi)
        
referans = 'referans'
isim = 'isim'
tanim = 'tanim'
        
unsurlar [0] = {
   referans: "M",
   isim: "mühimmat",
   tanim: unsur_tanimlari_listesi [0]
   }

unsurlar [1] = {
   referans: "P",
   isim: "pabuç",
   tanim: unsur_tanimlari_listesi [1] 
   }

unsurlar [2] = {
   referans: "A",
   isim: "alyan",
   tanim: unsur_tanimlari_listesi [2]
   }

print (unsurlar)
      

###--------------------------------------###

unsur_isimleri_listesi_unsuz_yumusamasi_hali = []
            
for i in range (0,toplam_unsur_sayisi):
   unsur_isimleri_listesi_unsuz_yumusamasi_hali.append(unsurlar [i].get(isim))
            
unsuz_yumusamasi_harfleri_listesi_initial = ['ç', 'k', 'p', 't']
            
unsuz_yumusamasi_harfleri_listesi_modified = ['c','ğ','b','d']
            
gecici = ['']
            
for i in range (1, toplam_unsur_sayisi):
   if unsur_isimleri_listesi_unsuz_yumusamasi_hali [i].endswith (unsuz_yumusamasi_harfleri_listesi_initial [0]):
      gecici = list(unsur_isimleri_listesi_unsuz_yumusamasi_hali [i])
      gecici [-1] = unsuz_yumusamasi_harfleri_listesi_modified [0]
      unsur_isimleri_listesi_unsuz_yumusamasi_hali [i] = ''.join(gecici)
   elif unsur_isimleri_listesi_unsuz_yumusamasi_hali [i].endswith (unsuz_yumusamasi_harfleri_listesi_initial [1]):
      gecici = list(unsur_isimleri_listesi_unsuz_yumusamasi_hali [i])
      gecici [-1] = unsuz_yumusamasi_harfleri_listesi_modified [1]
      unsur_isimleri_listesi_unsuz_yumusamasi_hali [i] = ''.join(gecici)
   elif unsur_isimleri_listesi_unsuz_yumusamasi_hali [i].endswith (unsuz_yumusamasi_harfleri_listesi_initial [2]):
      gecici = list(unsur_isimleri_listesi_unsuz_yumusamasi_hali [i])
      gecici [-1] = unsuz_yumusamasi_harfleri_listesi_modified [2]
      unsur_isimleri_listesi_unsuz_yumusamasi_hali [i] = ''.join(gecici)
   elif unsur_isimleri_listesi_unsuz_yumusamasi_hali [i].endswith (unsuz_yumusamasi_harfleri_listesi_initial [3]):
      gecici = list(unsur_isimleri_listesi_unsuz_yumusamasi_hali [i])
      gecici [-1] = unsuz_yumusamasi_harfleri_listesi_modified [3]
      unsur_isimleri_listesi_unsuz_yumusamasi_hali [i] = ''.join(gecici)
            
#-------------------UNSUR İSİMLERİNİN UNSUZ YUMUSAMASI HALLERİ LİSTESİNİN OLUŞTURULDUĞU KISIM BURAYA KADARKİ KISIM---------------
                    
#-------ARTIK GEREKLİ TÜM LİSTE HAZIR, UNSUZ YUMUSAMASI İÇİN GEREKEN TÜM KOŞULLARI İF VE AND İLE AYNI KOMUTTA GİRİP UNSUZ YUMUSAMASI
#OLUP OLMADIĞINI TESPİT EDİCEZ, VARSA UNSUZ YUMUSAMALI LİSTEDEKİ HALİNDEN AL DİYECEĞİZ.
            
for i in range (0, toplam_unsur_sayisi):
   for l, item_3 in enumerate (unsur_tanimlari_listesi_split [i]):
       print (unsur_tanimlari_listesi_split [i] [l])
            
#-YUKARIDAKİ KODA EK İÇİN İLK HARFİN SESLİ HARF GELİP GELMEMESİ KOŞULU EKLENECEK. ÇÜNKÜ "DÖNER ÇUBUĞA" DA DEĞİŞMESİNİ İSTERİZ AMA "DÖNER ÇUBUKTAN" DA DEĞİŞMESİNİ İSTEMEYİZ. ÜNSÜZ YUMUŞAMASI EKİN İLK HARFİ ÜNLÜ HARF OLDUĞUNDA GERÇEKLEŞTİGİ İÇİN BUNU DA KODA KATMAM GEREKİYOR.
            
#unsur_referanslari_listesi = ["u1","u2","u3","u4","u5","u6","u7","u8","u9","u10","u11","u12","u13","u14","u15","u16","u17","u18","u19","u20"]
            
for i in range (1, toplam_unsur_sayisi):
   for l, item_3 in enumerate (unsur_tanimlari_listesi_split [i]):
      for k in range (0, toplam_unsur_sayisi):
         if unsur_tanimlari_listesi_split [i] [l].startswith (unsurlar [k].get(referans)):
            unsur_tanimlari_listesi_split [i] [l] = item_3 + ' (' + (unsurlar [k].get(referans)) + ')'
         else:
            continue

            
#-YUKARIDAKİ KOD İLE UNSUR TANIMLARININ SPLIT VERSIYONU LISTESİNE YANİ UNSURLARA PARANTEZLİ REFERANS NUMARALARI ATANDI.
#-DAHA SONRA BU KISMI BİR J YA DA K FOR DÖNGÜSÜ İLE TEK KODLU YAPMAYA ÇALIŞ.
            
unsur_tanimlari_listesi_split_son = []


for k in range (0, len(unsur_tanimlari_listesi_split)):
   unsur_tanimlari_listesi_split_son.append(unsur_tanimlari_listesi_split [k])
   
            
#-Aşağıdaki kod ile kullanıcıya ünsüz yumuşaması ile ilgili bilgi verilmektedir.
            
for k in range (0,toplam_unsur_sayisi):
   for j, item_2 in enumerate(unsuz_yumusamasi_harfleri_listesi_initial):
       if unsurlar [k].get(isim) [-1].endswith (item_2):
          print (" '{}' unsuru '{}'".format(unsurlar [k].get(isim), item_2) + ' harfi ile bitmektedir ve ünsüz yumuşaması gerekebilir.') 
       else:
          continue

sesli_harfler = ['a','e','ı','i','o','ö','u','ü']

#-Yukarıdaki kodun amacı kullanıcıya ünsüz yumuşaması konusunda bilgi vermektir. Hangi unsur isimlerinin son harfine göre unsuz yumuşamasına
 #- uğrayabileceği söylenmektedir.
            
for z in range (0,toplam_unsur_sayisi):
    for k in range (0, len(unsur_tanimlari_listesi_split)):
       for l, item_3 in enumerate(unsur_tanimlari_listesi_split [k]):
          for n in range (0,8): #sesli_harflerin toplam adedinden dolayı 8.
             if unsur_tanimlari_listesi_split [k] [l] [0] == unsurlar [z].get(referans) and unsur_tanimlari_listesi_split [k] [l] [1] == sesli_harfler [n]:
                print (" Unsur tanımlarında '[{}] [{}]' indexinde olan '{}' unsuru, unsur adından sonra '{}' ".format(k,l,item_3,sesli_harfler [n]) + ' sesli harfi aldığı için ünsüz yumuşaması gerekebilir.')
             else:
                continue
 
            
#-Yukarıdaki kodun amacı kullanıcıya ünsüz yumuşaması konusunda bilgi vermektir. Unsur tanımında başka unsura atıf yapılan unsur referansı olup olmadığına ve 
#unsur referansından sonra sesli harf gelip gelmemesine göre unsuz yumuşaması ihtimatilini kullanıcıya söylüyor.
#-Asıl değişim aşağıdaki kodlar ile yapılacaktır.

for z in range (0,toplam_unsur_sayisi):            
   for j, item_2 in enumerate(unsuz_yumusamasi_harfleri_listesi_initial):
      for k in range (0, len(unsur_tanimlari_listesi_split_son)):
         for l, item_3 in enumerate(unsur_tanimlari_listesi_split_son [k]):
            for n in range (0,8):   #sesli_harflerin toplam adedinden dolayı 8.             
               if unsurlar [z].get(isim) [-1] == (unsuz_yumusamasi_harfleri_listesi_initial [j]): #Buradan 3.(i=2) ve 5. (i=4) unsur isimleri geçecek
                  if unsur_tanimlari_listesi_split [k] [l] [0] == (unsurlar [z].get(referans)): # [k] [l] = [3] [5] ve [3] [9] geçti.
                     if unsur_tanimlari_listesi_split [k] [l] [1] == sesli_harfler [n]:
                        unsur_tanimlari_listesi_split_son [k] [l] = list(unsur_tanimlari_listesi_split_son [k] [l])
                        unsur_tanimlari_listesi_split_son [k] [l] [0] = unsur_isimleri_listesi_unsuz_yumusamasi_hali [z]
                        unsur_tanimlari_listesi_split_son [k] [l] = "".join(unsur_tanimlari_listesi_split_son [k] [l])
                     else:
                         continue
                  else: 
                     continue
               else:
                  continue
            
#-Yukarıdaki kodlar ile sadece unsuz yumusaması değişimlerini gerçekleştiriyoruz.


for z in range (0,toplam_unsur_sayisi):  
  for k in range (0, len(unsur_tanimlari_listesi_split_son)):
     for l, item_3 in enumerate(unsur_tanimlari_listesi_split_son [k]):
        if unsur_tanimlari_listesi_split [k] [l] [0] == (unsurlar [z].get(referans)): # [k] [l] = [3] [5] ve [3] [9] geçti.
           unsur_tanimlari_listesi_split_son [k] [l] = list(unsur_tanimlari_listesi_split_son [k] [l])
           unsur_tanimlari_listesi_split_son [k] [l] [0] = unsurlar [z].get(isim)
           unsur_tanimlari_listesi_split_son [k] [l] = "".join(unsur_tanimlari_listesi_split_son [k] [l])
        else:
           continue
            
#- Yukarıdaki kod ile unsur referanslarını yerlerine yerleştirdik. Bir önceki kodda sadece unsuz yumusamasını değiştirdiğimiz için
#-kalan tüm değişimleri bu kodlar ile gerçekleştirdik.

         
unsur_tanimlari_listesi_string = []
            
for i in range (0,toplam_unsur_sayisi):
    unsur_tanimlari_listesi_string.append(unsur_tanimlari_listesi_split [i])
            
#-UNSUR TANIMI LİSTESİNİN STRING HALİNE ÇEVİRMEMİZ GEREKİYOR REPLACE FONK. İÇİN. BURADA BUNUN İÇİN BOŞ LİSTE ATAYIP DOLDURDUK
#-DAHA SONRA DEĞİŞTİRMEK ÜZERE.
            
for i in range (0, toplam_unsur_sayisi):
   unsur_tanimlari_listesi_string [i] = ' '.join(unsur_tanimlari_listesi_split_son [i])
            
#- REPLACE FONKSİYONUNU GERÇEKLEŞTİREBİLMEK İÇİN TÜM İFADEYİ LİST'TEN STRING FORMATINA GERİ ÇEVİRDİK JOİN FONKSİYONU İLE.
            
###---BURAYA KADAR İŞİN KODSAL KISMI VAR, UNSUR İSİMLERİNİN ALINMASI, UNSUR TANIMLARININ ALINMASI, UNSUZ YUMUSAMASI YAPILMASI GİBİ GİBİ.###
###---AŞAĞIDAKİ KISIMLARDA TAMAMEN NİHAİ İSTEM CÜMLESİNİ YAZMAYA YÖNELİK KODLAR.###
            
istem_cümlesi = []
            
#Yukarıdaki kod ile istem cümlesi için boş bir liste atadık, böylelikle her bir unsur cümlesini aşağıda yazılan kodla ekleyip
#sonrasında bu ana istem cümlesinden index ile çekip cümleyi oluşturacağım.
            
for i in range (0, toplam_unsur_sayisi):
   istem_cümlesi.append (i)
            
#unsur_sayilari_listesi ile aynı üyeleri olan listeyi oluşturduk ki boş listemizde aynı sayıda unsur tanımları olsun. 
#Sonrasında asıl istem cümlesi girilecek.
            
for i in range (0,toplam_unsur_sayisi):
   if i+1 < toplam_unsur_sayisi:
      istem_cümlesi [i] =  unsur_tanimlari_listesi_string [i] + ' en az bir ' + unsurlar [i].get(isim) + ' (' + str(unsurlar [i].get(referans)) + '), '
   elif i+1 == toplam_unsur_sayisi:
      istem_cümlesi [i] =  unsur_tanimlari_listesi_string [i] + ' en az bir ' + unsurlar [i].get(isim) + ' (' + str(unsurlar [i].get(referans)) + ') '
   else:
      break
            
#Yukarıdaki kod ile for döngüsüyle tüm istemin cümlelerini indexleyerek birleştirdik tek bir list istem cümlesinde.
#Ayrıca elif kısmının eklenmesinin sebebi karakterize edilen kısmından hemen önce yani son unsurdan sonra virgül koymamak. 
#Ama şuanlık çalışmıyor, üzerinde çalış.
            
final_istem_cümlesi = ['']
            
for i in range (0,toplam_unsur_sayisi):
   final_istem_cümlesi [0] = final_istem_cümlesi [0] + (''.join(istem_cümlesi [i]))

print (final_istem_cümlesi [0])
'''