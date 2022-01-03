# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 10:42:03 2021

@author: t22375
"""
#20 ve üzerindeki unsurlarda çalışmıyor, ancak buna zaten gerek de yok. Çünkü gerçekte max 10-20 arasında unsur oluyor.
#Ancak yine de ileride futureworks olarak gerçekleştirilecek.



####---###

unsur_referanslari_listesi = []

unsur_referanslari_listesi.append ("M")

unsur_referanslari_listesi.append ("P")

unsur_referanslari_listesi.append ("2")

unsur_referanslari_listesi.append ("3")

unsur_referanslari_listesi.append ("310")

unsur_referanslari_listesi.append ("320")

unsur_referanslari_listesi.append ("11")

unsur_referanslari_listesi.append ("12")

unsur_referanslari_listesi.append ("1")

'''
unsur_referanslari_listesi.append ("M")

unsur_referanslari_listesi.append ("P")

unsur_referanslari_listesi.append ("2")

unsur_referanslari_listesi.append ("30")

unsur_referanslari_listesi.append ("420")

unsur_referanslari_listesi.append ("1")
'''

'''
unsur_referanslari_listesi.append ("2")

unsur_referanslari_listesi.append ("3")

unsur_referanslari_listesi.append ("E")

unsur_referanslari_listesi.append ("310")

unsur_referanslari_listesi.append ("320")

unsur_referanslari_listesi.append ("4")

unsur_referanslari_listesi.append ("410")

unsur_referanslari_listesi.append ("420")

unsur_referanslari_listesi.append ("1")
'''

toplam_unsur_sayisi = len (unsur_referanslari_listesi)

#toplam_unsur_sayisi = 6 Tkinter'da bunu kullanıyorum, o yüzden aktif değil.


####---###


unsur_isimleri_listesi = []

unsur_isimleri_listesi.append ("mühimmat")

unsur_isimleri_listesi.append ("pabuç")

unsur_isimleri_listesi.append ("gövde")

unsur_isimleri_listesi.append ("çubuk")

unsur_isimleri_listesi.append ("döner çubuk")

unsur_isimleri_listesi.append ("iletim çubuğu")

unsur_isimleri_listesi.append ("alyan")

unsur_isimleri_listesi.append ("bağlayıcı")

unsur_isimleri_listesi.append ("ayarlanabilir ekipman montaj sistemi")

'''
unsur_isimleri_listesi.append ("mühimmat")

unsur_isimleri_listesi.append ("pabuç")

unsur_isimleri_listesi.append ("gövde")

unsur_isimleri_listesi.append ("döner çubuk")

unsur_isimleri_listesi.append ("iletim çubuğu")

unsur_isimleri_listesi.append ("mühimmat destek sistemi")
'''

'''
unsur_isimleri_listesi.append ("gövde")

unsur_isimleri_listesi.append ("boru")

unsur_isimleri_listesi.append ("ekipman")

unsur_isimleri_listesi.append ("bükümlü boru")

unsur_isimleri_listesi.append ("kıvrımlı boru")

unsur_isimleri_listesi.append ("yapısal parça")

unsur_isimleri_listesi.append ("birinci yapısal parça")

unsur_isimleri_listesi.append ("ikinci yapısal parça")

unsur_isimleri_listesi.append ("ayarlanabilir ekipman montaj sistemi")
'''

###

unsur_tanimlari_listesi = []

unsur_tanimlari_listesi.append("hava aracından hedefine taarruz etmek amacıyla gönderilen")

unsur_tanimlari_listesi.append("Ma basınç uygulayarak stabilitesini sağlayan")

unsur_tanimlari_listesi.append("hava aracı yapısalı olan")

unsur_tanimlari_listesi.append("2 üzerinde hareket edebilir şekilde yer alan ve yapısal parça olan ")

unsur_tanimlari_listesi.append("2 üzerinde çıkarılabilir şekilde yer alan ve dönebilir şekilde hareket eden")

unsur_tanimlari_listesi.append("2ye mesnetlendiği eksen etrafında dönebilir şekilde 310un ucunda yer alan, 310un döner hareketini doğrusal harekete çeviren, üzerinde bulunan Pu hareket ettiren")

unsur_tanimlari_listesi.append("teknisyen tarafından Pları döndürmek için kullanılan alet olan, 320nun ayarlanmasını sağlayan")

unsur_tanimlari_listesi.append("Ma çıkarılabilir şekilde takılan, Mı 2ye çıkarılabilir şekilde takılmasını sağlayan, teknisyen tarafından 11 vasıtası ile takılan")

'''
unsur_tanimlari_listesi.append("hava aracından hedefine taarruz etmek amacıyla gönderilen")

unsur_tanimlari_listesi.append("Ma basınç uygulayarak stabilitesini sağlayan")

unsur_tanimlari_listesi.append("hava aracı yapısalı olan")

unsur_tanimlari_listesi.append("2 üzerinde çıkarılabilir şekilde yer alan ve döner hareket yapan")

unsur_tanimlari_listesi.append("2ye mesnetlendiği eksen etrafında dönen, 30 üzerinde yer alan, 30un döner hareketini doğrusal harekete çeviren, üzerinde bulunan Pu hareket ettiren")
'''

'''
unsur_tanimlari_listesi.append("hava aracı yapısalı olan")

unsur_tanimlari_listesi.append("2 üzerinde çıkarılabilir şekilde yer alan ve kendi ekseni etrafında döndürülen")

unsur_tanimlari_listesi.append("3ya çıkarılabilir şekilde takılan")

unsur_tanimlari_listesi.append("2ye çıkarılabilir şekilde takılan, hemen hemen tamamen boylu boyunca uzanan")

unsur_tanimlari_listesi.append("3 üzerinde yer alan, 310nun devamında yer alan, en az bir bükümü bulunan, Eın takıldığı")

unsur_tanimlari_listesi.append("320ya çıkarılabilir şekilde takılan, yapısal mukavemet sağlayan")

unsur_tanimlari_listesi.append("320ya eksenel yüklere karşı mukavemet sağlayan")

unsur_tanimlari_listesi.append("320ya kesme yüklerine karşı mukavemet sağlayan")
'''


istisnai_unsuz_yumusamasi_kelimeleri = ["mühimmat","tek","alt","ak","yakıt","anıt","kesit","yarıçap","ip","sap", "tazyik","sürat","iç","gözet","beklet"] #Yabancı dillerden dilimize geçen kelimelerde, birçok tek heceli kelimelerde genelde ünsüz yumuşaması görülmez.

###---###


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

# unsur_tanimlari_listesi.append (' ')  Döngü dönebilsin diye eklediğim satır.
        
for i in range (toplam_unsur_sayisi):
    print (unsurlar [i].get(referans))
    print (unsurlar [i].get(isim))

for i in range (toplam_unsur_sayisi-1):
    print (unsurlar [i].get(tanim))

###---------------------------------------------------------------------------------### 

#Bu kısım numarasız kısım için ayrıca hazırlanmıştır. Hazır koddan referans eklenmemiş halinin çekilmesiyle elde edilmiştir.

global unsur_tanimlari_listesi_split_referanssiz

unsur_tanimlari_listesi_split_referanssiz = []

for i in range (0, toplam_unsur_sayisi-1):
    unsur_tanimlari_listesi_split_referanssiz.append (i)
    
for i in range (0,toplam_unsur_sayisi-1):
    unsur_tanimlari_listesi_split_referanssiz [i] = unsur_tanimlari_listesi [i].split ()
    
print ("\n Unsur tanımlarının referanssız kelimelere ayrılmış referanssız hali: " + str(unsur_tanimlari_listesi_split_referanssiz))
    
#Yukarıdaki kod ile istem cümlesi için boş bir liste atadık, böylelikle her bir unsur cümlesini aşağıda yazılan kodla ekleyip
#sonrasında bu ana istem cümlesinden index ile çekip cümleyi oluşturacağım.
 
#Buradan aşağıdaki kodlar önceki hazır kodlardan direkt geldi.
    
unsur_tanimlari_listesi_split_referansli = []

for i in range (0, toplam_unsur_sayisi-1):
    unsur_tanimlari_listesi_split_referansli.append (i)
    
for i in range (0,toplam_unsur_sayisi-1):
    unsur_tanimlari_listesi_split_referansli [i] = unsur_tanimlari_listesi [i].split ()

alt_unsur_listesi = []

alt_unsuru_olan_ana_unsur_listesi = []

# Aşağıda kodla gerçekleştirilen, hangi unsurların hangi ana unsurun alt unsuru olduğunu tespit etmektir.

for ana_unsur_index, ana_unsur in enumerate(unsur_referanslari_listesi [0: -1]):
    for alt_unsur_index, alt_unsur in enumerate(unsur_referanslari_listesi [0: -1]):
        for i in range (0, toplam_unsur_sayisi-1): #Tüm unsur tanımı cümlelerine bakmak için bir i değişkeni ekledim.
            if len(alt_unsur) > len(ana_unsur): #320, 520'yi 3ün alt unsuru gibi algılayabilir, bu yüzden aşağıda startswith şartı getiriyoruz... # print ("'{}' alt unsuru '{}' ana unsurundan daha uzundur".format(alt_unsur,ana_unsur)) 
                if alt_unsur.startswith (ana_unsur): #320, 3'ün alt unsurudur. #Yapılacak: 1 ile 11, 12, 13' de böyle algılayabilir. Bunu önlemem gerek.
                   #print ("'{}' alt unsuru '{}' ana unsuru ile başlamaktadır".format(alt_unsur,ana_unsur))  
                   if len (alt_unsuru_olan_ana_unsur_listesi) == 0: #bool(alt_unsuru_olan_ana_unsur_listesi) ...#Yalnızca ilk liste oluşturulması için olan kısım.
                       alt_unsuru_olan_ana_unsur_listesi.append (ana_unsur)  #alt_unsuru_olan_ana_unsur_listesi = [[ana_unsur] for i in range(1)]
                       #print ("\n Ana unsur listesine, '{}' alt unsurunun ana unsuru olan '{}' ana unsuru eklenmiştir".format(alt_unsur,ana_unsur))
                       alt_unsur_listesi = [[alt_unsur] for i in range(1)] #alt_unsur_listesi.append([[alt_unsur] for i in range(1)])
                       #print ("Alt unsur listesine, '{}' ana unsuruna ait olan '{}' alt unsuru eklenmiştir".format(ana_unsur,alt_unsur)) 
                   else: # İlk değerler girilmesinin ardından tüm caseler buraya gelecek.
                       if alt_unsur_listesi [-1] [-1] == alt_unsur: #Aynı 310, aynı 320 lerin tekrarlamaması, listeye sadece 1 kez girmesi için yapıldı.
                           continue
                       if alt_unsur.startswith (alt_unsuru_olan_ana_unsur_listesi [-1]): #...[-1] [-1] ...#3 ana unsuru, 310,320 alt unsuru gibi...
                           alt_unsur_listesi [-1].append (alt_unsur) #alt_unsur_listesi.append([[alt_unsur] for i in range(1)])  #alt_unsur_listesi [-1].append (alt_unsur)
                           #print ("Alt unsur listesine '{}' ana unsuruna ait olan '{}' alt unsuru eklenmiştir".format(ana_unsur,alt_unsur))
                       else: # 3 ana unsuruna 310,320 eklendikten sonra 4 ana unsuru ve 410 420 gibi yeni alt unsurların eklenmesi için olan kısım.
                           alt_unsuru_olan_ana_unsur_listesi.append (ana_unsur) #alt_unsuru_olan_ana_unsur_listesi.append (ana_unsur)
                           #print ("\n Ana unsur listesine, '{}' alt unsurunun ana unsuru olan '{}' ana unsuru eklenmiştir".format(alt_unsur,ana_unsur))  
                           alt_unsur_listesi.append ([alt_unsur for i in range(1)]) #alt_unsur_listesi.append ([[alt_unsur] for i in range(1)])  #alt_unsur_listesi = alt_unsur_listesi.append ([[alt_unsur] for i in range(1)])
                           #print ("\n Alt unsur listesine, '{}' ana unsuruna ait olan '{}' alt unsuru eklenmiştir".format(ana_unsur,alt_unsur)) 
                else:
                    continue 
            elif len(alt_unsur) == len (ana_unsur):
               #print ("\n '{}' alt unsur, '{}' ana unsurunun herhangi bir alakaları olmadığı için pas geçilmiştir.".format(alt_unsur,ana_unsur))
               continue 
            elif len(alt_unsur) < len (ana_unsur): # Yani alt unsur olmayan, yalnızca ana unsurlu durumlar. Normal bir şekilde değişimler gerçekleştirilecektir.
               continue

#print ('\n Alt unsurlar şunlardır: ' + str(alt_unsur_listesi))

#print ('\n Alt unsuru olan ana unsurlar şunlardır: ' + str(alt_unsuru_olan_ana_unsur_listesi))

print ("\n Ana unsur ve alt unsur eşleşmesi aşağıdaki gibidir: ")

for index, value in enumerate(alt_unsuru_olan_ana_unsur_listesi):
    print (str(value), str(" --> "), str(alt_unsur_listesi [index]))

alt_unsur_index_listesi = [] #Referanslardaki alt unsurların indexlerini kaydedeceğimiz liste.

for k, value in enumerate(alt_unsuru_olan_ana_unsur_listesi): #Referanslardaki alt unsurların indexlerini tespit etmemizi sağlayan kod.
    for l, alt_unsur in enumerate(alt_unsur_listesi [k]):
        index= unsur_referanslari_listesi.index(alt_unsur)
        alt_unsur_index_listesi.append (index)

print ("\n Alt unsur index listesi: " + str(alt_unsur_index_listesi))        

#Alt unsur indexlerini bildiğimiz için, ana unsur indexlerini elde etmek için tüm referans indexi listesinden alt unsur referans indexini çıkarıcaz.

ana_unsur_index_listesi = []

for index, referans in enumerate(unsur_referanslari_listesi):
    ana_unsur_index_listesi.append (index)

for random, alt_unsur_index in enumerate(alt_unsur_index_listesi):
    ana_unsur_index_listesi.remove (alt_unsur_index)
    
print ("\n Ana unsur index listesi: " + str(ana_unsur_index_listesi))


for i in range (0, toplam_unsur_sayisi-1): #Tüm unsur tanımı cümlelerine bakmak için bir i değişkeni ekledim.
    for unsur_tanim_referans_index, unsur_tanim_referans in enumerate(unsur_tanimlari_listesi_split_referanssiz [i]): #İlk cümleden itibaren değişmesi gerekenleri değiştire değiştire ilerlemesi için böyle yapıldı...#for alt_unsur_tanim_index, alt_unsur_tanimi in enumerate(unsur_tanimlari_listesi_split_referanssiz [i]): 
        if len (alt_unsur_index_listesi) > 0: #Alt unsur olması durumu.
           for temporary, alt_unsur_index in enumerate(alt_unsur_index_listesi):
              if unsur_tanimlari_listesi_split_referanssiz [i] [unsur_tanim_referans_index].startswith (unsur_referanslari_listesi [alt_unsur_index]):  #Alt unsurların referanslarının yerleştirilmesi.
                 #print ("\n '{} ' '{}' indexindeki unsur tanımı olan '{}' tanımı, '{}' alt unsuru ile başlamaktadır.".format(i,unsur_tanim_referans_index, unsur_tanimlari_listesi_split_referanssiz [i] [unsur_tanim_referans_index],unsur_referanslari_listesi [alt_unsur_index])) 
                 unsur_tanimlari_listesi_split_referansli [i] [unsur_tanim_referans_index] = unsur_tanim_referans + ' (' + str(unsur_referanslari_listesi [alt_unsur_index].capitalize()) + ')'
                 print ("\n '{} ' '{}' indexindeki unsur tanımı olan '{}' tanımı, '{}' referanslı tanımı ile değiştirilmiştir.".format(i,unsur_tanim_referans_index, unsur_tanimlari_listesi_split_referanssiz [i] [unsur_tanim_referans_index],unsur_tanimlari_listesi_split_referansli [i] [unsur_tanim_referans_index]))
              else:
                 for temporary_2, ana_unsur_index in enumerate(ana_unsur_index_listesi): #Ana unsurların referanslarının yerleştirilmesi.
                    if (unsur_tanimlari_listesi_split_referanssiz [i] [unsur_tanim_referans_index].startswith (unsur_referanslari_listesi [ana_unsur_index]) and (not unsur_tanimlari_listesi_split_referansli [i] [unsur_tanim_referans_index].endswith (')'))):
                        #print ("\n '{} ' '{}' indexindeki unsur tanımı olan '{}' tanımı, '{}' ana unsuru ile başlamaktadır.".format(i,unsur_tanim_referans_index, unsur_tanimlari_listesi_split_referanssiz [i] [unsur_tanim_referans_index],unsur_referanslari_listesi [ana_unsur_index])) 
                        unsur_tanimlari_listesi_split_referansli [i] [unsur_tanim_referans_index] = unsur_tanim_referans + ' (' + str(unsur_referanslari_listesi [ana_unsur_index].capitalize()) + ')'  
                        print ("\n '{} ' '{}' indexindeki unsur tanımı olan '{}' tanımı, '{}' referanslı tanımı ile değiştirilmiştir.".format(i,unsur_tanim_referans_index, unsur_tanimlari_listesi_split_referanssiz [i] [unsur_tanim_referans_index],unsur_tanimlari_listesi_split_referansli [i] [unsur_tanim_referans_index]))
                    else:
                       continue
        else: #Alt unsur olmaması durumu.
           for temporary_2, ana_unsur_index in enumerate(ana_unsur_index_listesi): #Ana unsurların referanslarının yerleştirilmesi.
             if (unsur_tanimlari_listesi_split_referanssiz [i] [unsur_tanim_referans_index].startswith (unsur_referanslari_listesi [ana_unsur_index]) and (not unsur_tanimlari_listesi_split_referansli [i] [unsur_tanim_referans_index].endswith (')'))):
                 #print ("\n '{} ' '{}' indexindeki unsur tanımı olan '{}' tanımı, '{}' ana unsuru ile başlamaktadır.".format(i,unsur_tanim_referans_index, unsur_tanimlari_listesi_split_referanssiz [i] [unsur_tanim_referans_index],unsur_referanslari_listesi [ana_unsur_index])) 
                 unsur_tanimlari_listesi_split_referansli [i] [unsur_tanim_referans_index] = unsur_tanim_referans + ' (' + str(unsur_referanslari_listesi [ana_unsur_index].capitalize()) + ')'  
                 print ("\n '{} ' '{}' indexindeki unsur tanımı olan '{}' tanımı, '{}' referanslı tanımı ile değiştirilmiştir.".format(i,unsur_tanim_referans_index, unsur_tanimlari_listesi_split_referanssiz [i] [unsur_tanim_referans_index],unsur_tanimlari_listesi_split_referansli [i] [unsur_tanim_referans_index]))
             else:
                continue
  
print ("\n Unsur tanımlarının referanslı kelimelere ayrılmış referanslı hali: " + str(unsur_tanimlari_listesi_split_referansli))

#-YUKARIDAKİ KOD İLE UNSUR TANIMLARININ SPLIT VERSIYONU LISTESİNE YANİ UNSURLARA PARANTEZLİ REFERANS NUMARALARI ATANMIŞTIR.

#Buradan aşağıdaki kodlar ünsüz yumuşaması ve tanımlardaki unsurların replace edilmesi fonksiyonu ile ilgilidir.

#Aşağıda ünsüz yumuşaması kod bloğu vardır.
    
unsur_isimleri_listesi_unsuz_yumusamasi_hali = []
    
for i in range (0,toplam_unsur_sayisi-1):
    unsur_isimleri_listesi_unsuz_yumusamasi_hali.append(unsur_isimleri_listesi [i])
    
unsuz_yumusamasi_harfleri_listesi_initial = ['ç', 'k', 'p', 't']
    
unsuz_yumusamasi_harfleri_listesi_modified = ['c','ğ','b','d']
    
gecici = ['']
    
for i in range (0, toplam_unsur_sayisi-1):
    for k in range (0,4):
        if unsur_isimleri_listesi_unsuz_yumusamasi_hali [i].endswith (unsuz_yumusamasi_harfleri_listesi_initial [k]):
            gecici = list(unsur_isimleri_listesi_unsuz_yumusamasi_hali [i])
            gecici [-1] = unsuz_yumusamasi_harfleri_listesi_modified [k]
            unsur_isimleri_listesi_unsuz_yumusamasi_hali [i] = ''.join(gecici)
        else:
            continue
    
#-------------------UNSUR İSİMLERİNİN UNSUZ YUMUSAMASI HALLERİ LİSTESİNİN OLUŞTURULDUĞU KISIM BURAYA KADARKİ KISIM---------------
            
#-------ARTIK GEREKLİ TÜM LİSTE HAZIR, UNSUZ YUMUSAMASI İÇİN GEREKEN TÜM KOŞULLARI İF VE AND İLE AYNI KOMUTTA GİRİP UNSUZ YUMUSAMASI
#OLUP OLMADIĞINI TESPİT EDECEĞİZ, VARSA İLGİLİ HARFİ UNSUZ YUMUSAMALI LİSTEDEKİ HALİNDEN AL DİYECEĞİZ.
    
unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis = []

for k in range (0, toplam_unsur_sayisi-1):
    unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis.append(unsur_tanimlari_listesi_split_referansli [k])
    
sesli_harfler = ['a','e','ı','i','o','ö','u','ü']
    
#-Aşağıdaki kod ile kullanıcıya ünsüz yumuşaması ile ilgili bilgi verilmektedir.
    
for i, item in enumerate(unsur_isimleri_listesi):
    for j, item_2 in enumerate(unsuz_yumusamasi_harfleri_listesi_initial):
        if unsur_isimleri_listesi [i].endswith (unsuz_yumusamasi_harfleri_listesi_initial [j]):
           print ("\n '{}.' unsur olan '{}' unsuru '{}'".format(i,item, item_2) + ' harfi ile bitmektedir ve ünsüz yumuşaması gerekebilir.') 
        else:
            continue
    
#-Yukarıdaki kodun amacı kullanıcıya ünsüz yumuşaması konusunda bilgi vermektir. Hangi unsur isimlerinin son harfine göre unsuz yumuşamasına
#- uğrayabileceği söylenmektedir.
    

for i in range (0, toplam_unsur_sayisi-1):
    for l, item_3 in enumerate(unsur_tanimlari_listesi_split_referansli [i]):
        for n in range (0,8):
            if unsur_tanimlari_listesi_split_referansli [i] [l] [0] == unsur_referanslari_listesi [i]:
                if unsur_tanimlari_listesi_split_referansli [i] [l] [1] == sesli_harfler [n]:
                    print ("\n Değişim öncesi Ön Bilgilendirme: Unsur tanımlarında '[{}] [{}]' indexinde olan '{}' kelimesi,'{}' referansına ve '{}' ismine sahiptir. Kelime; unsur isminden sonra '{}'".format(i,l,item_3,unsur_referanslari_listesi [i],unsur_isimleri_listesi [i],sesli_harfler [n]) + ' sesli harfi aldığı için ünsüz yumuşaması gerekebilir.')
                else:
                    continue
            else:
               continue

# BURAYA KADAR ALT UNSURLARIM NELER BİLDİĞİM İÇİN DOĞRUDAN ÖNCE ALT UNSURLAR, DAHA SONRA ANA UNSURLAR REPLACE EDİLECEKTİR.

global unsur_i_tanimi_her_bir_kelimenin_harf_listesi
unsur_i_tanimi_her_bir_kelimenin_harf_listesi = []

ilk_parantez_indexi = []


for temporary, alt_unsur_index in enumerate(alt_unsur_index_listesi):
   alt_unsur = unsur_referanslari_listesi [alt_unsur_index]
   for k in range (0,toplam_unsur_sayisi-1):
      for l, unsur_tanimi in enumerate (unsur_tanimlari_listesi_split_referansli [k]):
         if unsur_tanimlari_listesi_split_referansli [k] [l].startswith (alt_unsur): 
            print ("\n Unsur tanımlarında '[{}] [{}]' indexinde olan '{}' kelimesi,'{}' referansına ve '{}' ismine sahiptir.".format(k,l,unsur_tanimi,alt_unsur,unsur_isimleri_listesi [alt_unsur_index]))
            for j, item_2 in enumerate(unsuz_yumusamasi_harfleri_listesi_initial):
               if unsur_isimleri_listesi [alt_unsur_index].endswith (unsuz_yumusamasi_harfleri_listesi_initial [j]):
                  print (" \n Unsur tanımlarında '[{}] [{}]' indexindeki '{}' kelimesi, '{}' referanslı '{}' unsur ismi ile başlamaktadır + ayrıca '{}' unsur ismi, ünsüz yumuşaması harfleri listesindeki '[{}]' indexinde yer alan '{}' ünsüz yumuşaması harfi ile bitmektedir.".format(k,l,unsur_tanimi,alt_unsur,unsur_isimleri_listesi [alt_unsur_index],unsur_isimleri_listesi [alt_unsur_index],j,item_2))
                  #if unsur_tanimlari_listesi_split_referansli [k] [l].startswith (alt_unsur) and (not unsur_tanimlari_listesi_split_referansli [k] [l].endswith (")")): #Bu satırın tek amacı değişim gerçekleştikten sonra yine aynı işlemin gerçekleşmemesi. Çünkü Ma (M) ve mühimmat unsurunda 2 kere uc uca ekledi.
                  for z in range (0,len(istisnai_unsuz_yumusamasi_kelimeleri)): #İstisnai kelimelerin tümünün listesinde taraması için for döngüsü.    
                     if unsur_isimleri_listesi [alt_unsur_index] == istisnai_unsuz_yumusamasi_kelimeleri [z]: #İstisnai kelimelerin tümünün listesinde herhangi bir unsur ismimiz var mı bakıyor, varsa döngüyü kırıyor, yoksa devam ediyor. Normal devam etmek için bir ön geçit aslında
                       print ("'{} referanslı '{}' unsuru, '{}' istisnai ünsüz yumuşaması kelimesi olduğu için ünsüz yumuşaması uygulanmamıştır".format(unsur_referanslari_listesi [alt_unsur_index],unsur_isimleri_listesi [alt_unsur_index],istisnai_unsuz_yumusamasi_kelimeleri [z]))
                       if len(alt_unsur) == 1:
                           unsur_i_tanimi_her_bir_kelimenin_harf_listesi = list(unsur_tanimlari_listesi_split_referansli [k] [l])
                           unsur_i_tanimi_her_bir_kelimenin_harf_listesi [0] = unsur_isimleri_listesi [alt_unsur_index]
                           unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [k] [l] = ''.join(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)
                           print ('1) Geçici kelime değişkeni= ' + str(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)) 
                       elif len(alt_unsur) > 1:
                           unsur_i_tanimi_her_bir_kelimenin_harf_listesi = list(unsur_tanimlari_listesi_split_referansli [k] [l])   
                           unsur_i_tanimi_her_bir_kelimenin_harf_listesi [0] = unsur_isimleri_listesi [alt_unsur_index]
                           for w in range (1,len(unsur_referanslari_listesi [alt_unsur_index])):
                              unsur_i_tanimi_her_bir_kelimenin_harf_listesi [w] = ''
                              unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [k] [l] = ''.join(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)
                              print ('2) Geçici kelime değişkeni= ' + str(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)) 
                       else:
                           continue
                     else: # İstisnai kelime olmadığı normal durumlar
                        for n in range (0,8):  
                          if unsur_tanimlari_listesi_split_referansli [k] [l] [len(unsur_referanslari_listesi [alt_unsur_index])] == sesli_harfler [n]:
                             if unsur_tanimlari_listesi_split_referansli [k] [l].startswith (unsur_referanslari_listesi [alt_unsur_index]): #Bu satırın tek amacı değişim gerçekleştikten sonra yine aynı işlemin gerçekleşmemesi. Çünkü Ma (M) ve mühimmat unsurunda 2 kere uc uca ekledi.    
                                print ("\n ÜNSÜZ YUMUŞAMASI VARDIR! Ünsüz yumuşaması '[{}] [{}]' indexindeki '{}' kelimesine ait '{}' referansına ek olarak '{}'sesli harfi gelmiştir ve '{}' isimli unsur '{}' ünsüz yumuşaması harfi ile bitmektedir.".format(k,l,alt_unsur,unsur_referanslari_listesi [alt_unsur_index], sesli_harfler [n], unsur_isimleri_listesi [alt_unsur_index], unsuz_yumusamasi_harfleri_listesi_initial [j]))
                                if len(alt_unsur) == 1:
                                   unsur_i_tanimi_her_bir_kelimenin_harf_listesi = list(unsur_tanimlari_listesi_split_referansli [k] [l])
                                   unsur_i_tanimi_her_bir_kelimenin_harf_listesi [0] = unsur_isimleri_listesi_unsuz_yumusamasi_hali [alt_unsur_index]
                                   unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [k] [l] = ''.join(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)
                                   print ('3) Geçici kelime değişkeni= ' + str(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)) 
                                elif len(alt_unsur) > 1:
                                   unsur_i_tanimi_her_bir_kelimenin_harf_listesi = list(unsur_tanimlari_listesi_split_referansli [k] [l])   
                                   unsur_i_tanimi_her_bir_kelimenin_harf_listesi [0] = unsur_isimleri_listesi_unsuz_yumusamasi_hali [alt_unsur_index]
                                   for w in range (1,len(alt_unsur)):
                                      unsur_i_tanimi_her_bir_kelimenin_harf_listesi [w] = ''
                                      unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [k] [l] = ''.join(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)
                                      print ('4) Geçici kelime değişkeni= ' + str(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)) 
                                else:
                                   continue
                             else:
                                break #break yazdım çünkü hangi sesli harfle başladığını bulmak için foor döngüsü dönerken replace edeceği kelimeleri yan yana koyup tekrar etmesin diye.
                          else:
                             continue
                  else:
                     continue
               else: 
                    if unsur_isimleri_listesi [alt_unsur_index] [-1].count("ç") == 1: #item_2 != unsuz_yumusamasi_harfleri_listesi_initial [-1] or item_2 == unsuz_yumusamasi_harfleri_listesi_initial [-1]:
                       continue 
                    elif unsur_isimleri_listesi [alt_unsur_index] [-1].count("k"):
                       continue 
                    elif unsur_isimleri_listesi [alt_unsur_index] [-1].count("p"):
                       continue 
                    elif unsur_isimleri_listesi [alt_unsur_index] [-1].count("t"):
                       continue 
                    else:
                       unsur_i_tanimi_her_bir_kelimenin_harf_listesi = list(unsur_tanimlari_listesi_split_referansli [k] [l])   
                       unsur_i_tanimi_her_bir_kelimenin_harf_listesi [0] = unsur_isimleri_listesi [alt_unsur_index]
                       for w in range (1,len(alt_unsur)):
                          unsur_i_tanimi_her_bir_kelimenin_harf_listesi [w] = ''
                          unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [k] [l] = ''.join(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)
                          print ('5) Geçici kelime değişkeni= ' + str(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)) 
                       break
         else :
            continue 

# TANIMLARDA ALT UNSURLARIN REPLACE EDİLMESİ YUKARIDAKİ KOD BLOĞUNDA GERÇEKLEŞİYOR. HEM ÜNSÜZ YUMUŞAMASI OLANLAR HEM DE OLMAYANLAR.

for temporary, ana_unsur_index in enumerate(ana_unsur_index_listesi):
   ana_unsur = unsur_referanslari_listesi [ana_unsur_index]
   for k in range (0,toplam_unsur_sayisi-1):
      for l, unsur_tanimi in enumerate (unsur_tanimlari_listesi_split_referansli [k]):
         if unsur_tanimlari_listesi_split_referansli [k] [l].startswith (ana_unsur): 
            print ("\n Unsur tanımlarında '[{}] [{}]' indexinde olan '{}' kelimesi,'{}' referansına ve '{}' ismine sahiptir.".format(k,l,unsur_tanimi,ana_unsur,unsur_isimleri_listesi [ana_unsur_index]))
            for j, item_2 in enumerate(unsuz_yumusamasi_harfleri_listesi_initial):
               if unsur_isimleri_listesi [ana_unsur_index].endswith (unsuz_yumusamasi_harfleri_listesi_initial [j]):
                  print (" \n Unsur tanımlarında '[{}] [{}]' indexindeki '{}' kelimesi, '{}' referanslı '{}' unsur ismi ile başlamaktadır + ayrıca '{}' unsur ismi, ünsüz yumuşaması harfleri listesindeki '[{}]' indexinde yer alan '{}' ünsüz yumuşaması harfi ile bitmektedir.".format(k,l,unsur_tanimi,ana_unsur,unsur_isimleri_listesi [ana_unsur_index],unsur_isimleri_listesi [ana_unsur_index],j,item_2))
                  #if unsur_tanimlari_listesi_split_referansli [k] [l].startswith (ana_unsur): #and (not unsur_tanimlari_listesi_split_referansli [k] [l].endswith (")")): #Bu satırın tek amacı değişim gerçekleştikten sonra yine aynı işlemin gerçekleşmemesi. Çünkü Ma (M) ve mühimmat unsurunda 2 kere uc uca ekledi.
                  for z in range (0,len(istisnai_unsuz_yumusamasi_kelimeleri)): #İstisnai kelimelerin tümünün listesinde taraması için for döngüsü.    
                       if unsur_isimleri_listesi [ana_unsur_index] == istisnai_unsuz_yumusamasi_kelimeleri [z]: #İstisnai kelimelerin tümünün listesinde herhangi bir unsur ismimiz var mı bakıyor, varsa döngüyü kırıyor, yoksa devam ediyor. Normal devam etmek için bir ön geçit aslında
                          print ("'{} referanslı '{}' unsuru, '{}' istisnai ünsüz yumuşaması kelimesi olduğu için ünsüz yumuşaması uygulanmamıştır".format(unsur_referanslari_listesi [ana_unsur_index],unsur_isimleri_listesi [ana_unsur_index],istisnai_unsuz_yumusamasi_kelimeleri [z]))
                          if len(ana_unsur) == 1:
                               unsur_i_tanimi_her_bir_kelimenin_harf_listesi = list(unsur_tanimlari_listesi_split_referansli [k] [l])
                               unsur_i_tanimi_her_bir_kelimenin_harf_listesi [0] = unsur_isimleri_listesi [ana_unsur_index]
                               unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [k] [l] = ''.join(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)
                               print ('6) Geçici kelime değişkeni= ' + str(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)) 
                          elif len(ana_unsur) > 1:
                               unsur_i_tanimi_her_bir_kelimenin_harf_listesi = list(unsur_tanimlari_listesi_split_referansli [k] [l])   
                               unsur_i_tanimi_her_bir_kelimenin_harf_listesi [0] = unsur_isimleri_listesi [ana_unsur_index]
                               for w in range (1,len(ana_unsur)):
                                  unsur_i_tanimi_her_bir_kelimenin_harf_listesi [w] = ''
                                  unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [k] [l] = ''.join(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)
                                  print ('7) Geçici kelime değişkeni= ' + str(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)) 
                          else:
                               continue
                       else: # İstisnai kelime olmadığı normal durumlar
                           for n in range (0,8):  
                             if unsur_tanimlari_listesi_split_referansli [k] [l] [len(unsur_referanslari_listesi [ana_unsur_index])] == sesli_harfler [n]:
                                if unsur_tanimlari_listesi_split_referansli [k] [l].startswith (ana_unsur): #Bu satırın tek amacı değişim gerçekleştikten sonra yine aynı işlemin gerçekleşmemesi. Çünkü Ma (M) ve mühimmat unsurunda 2 kere uc uca ekledi.    
                                   print ("\n ÜNSÜZ YUMUŞAMASI VARDIR! Ünsüz yumuşaması '[{}] [{}]' indexindeki '{}' kelimesine ait '{}' referansına ek olarak '{}'sesli harfi gelmiştir ve '{}' isimli unsur '{}' ünsüz yumuşaması harfi ile bitmektedir.".format(k,l,ana_unsur,unsur_referanslari_listesi [ana_unsur_index], sesli_harfler [n], unsur_isimleri_listesi [ana_unsur_index], unsuz_yumusamasi_harfleri_listesi_initial [j]))
                                   if len(ana_unsur) == 1:
                                      unsur_i_tanimi_her_bir_kelimenin_harf_listesi = list(unsur_tanimlari_listesi_split_referansli [k] [l])
                                      unsur_i_tanimi_her_bir_kelimenin_harf_listesi [0] = unsur_isimleri_listesi_unsuz_yumusamasi_hali [ana_unsur_index]
                                      unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [k] [l] = ''.join(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)
                                      print ('8) Geçici kelime değişkeni= ' + str(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)) 
                                   elif len(ana_unsur) > 1:
                                      unsur_i_tanimi_her_bir_kelimenin_harf_listesi = list(unsur_tanimlari_listesi_split_referansli [k] [l])   
                                      unsur_i_tanimi_her_bir_kelimenin_harf_listesi [0] = unsur_isimleri_listesi_unsuz_yumusamasi_hali [ana_unsur_index]
                                      for w in range (1,len(ana_unsur)): #len(ana_unsur)
                                         unsur_i_tanimi_her_bir_kelimenin_harf_listesi [w] = ''
                                         unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [k] [l] = ''.join(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)
                                         print ('\n 9) Geçici kelime değişkeni= ' + str(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)) 
                                   else:
                                      continue
                                else:
                                   break #break yazdım çünkü hangi sesli harfle başladığını bulmak için foor döngüsü dönerken replace edeceği kelimeleri yan yana koyup tekrar etmesin diye.
                             elif unsur_tanimlari_listesi_split_referansli [k] [l] [len(unsur_referanslari_listesi [ana_unsur_index])].count(sesli_harfler [0]):
                                 continue
                             elif unsur_tanimlari_listesi_split_referansli [k] [l] [len(unsur_referanslari_listesi [ana_unsur_index])].count(sesli_harfler [1]):
                                 continue
                             elif unsur_tanimlari_listesi_split_referansli [k] [l] [len(unsur_referanslari_listesi [ana_unsur_index])].count(sesli_harfler [2]):
                                 continue
                             elif unsur_tanimlari_listesi_split_referansli [k] [l] [len(unsur_referanslari_listesi [ana_unsur_index])].count(sesli_harfler [3]):
                                 continue
                             elif unsur_tanimlari_listesi_split_referansli [k] [l] [len(unsur_referanslari_listesi [ana_unsur_index])].count(sesli_harfler [4]):
                                 continue
                             elif unsur_tanimlari_listesi_split_referansli [k] [l] [len(unsur_referanslari_listesi [ana_unsur_index])].count(sesli_harfler [5]):
                                 continue
                             elif unsur_tanimlari_listesi_split_referansli [k] [l] [len(unsur_referanslari_listesi [ana_unsur_index])].count(sesli_harfler [6]):
                                 continue
                             elif unsur_tanimlari_listesi_split_referansli [k] [l] [len(unsur_referanslari_listesi [ana_unsur_index])].count(sesli_harfler [7]):
                                 continue
                             else:
                                if len(ana_unsur) == 1:
                                   unsur_i_tanimi_her_bir_kelimenin_harf_listesi = list(unsur_tanimlari_listesi_split_referansli [k] [l])
                                   unsur_i_tanimi_her_bir_kelimenin_harf_listesi [0] = unsur_isimleri_listesi [ana_unsur_index]
                                   unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [k] [l] = ''.join(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)
                                   print ('12) Geçici kelime değişkeni= ' + str(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)) 
                                   break
                                elif len(ana_unsur) > 1:
                                   unsur_i_tanimi_her_bir_kelimenin_harf_listesi = list(unsur_tanimlari_listesi_split_referansli [k] [l])   
                                   unsur_i_tanimi_her_bir_kelimenin_harf_listesi [0] = unsur_isimleri_listesi [ana_unsur_index]
                                   for w in range (1,len(ana_unsur)):
                                      unsur_i_tanimi_her_bir_kelimenin_harf_listesi [w] = ''
                                      unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [k] [l] = ''.join(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)
                                      print ('13) Geçici kelime değişkeni= ' + str(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)) 
                                   break
                  else:
                     continue 
               else: 
                    if unsur_isimleri_listesi [ana_unsur_index] [-1].count("ç"): #item_2 != unsuz_yumusamasi_harfleri_listesi_initial [-1] or item_2 == unsuz_yumusamasi_harfleri_listesi_initial [-1]:
                       continue 
                    elif unsur_isimleri_listesi [ana_unsur_index] [-1].count("k"):
                       continue 
                    elif unsur_isimleri_listesi [ana_unsur_index] [-1].count("p"):
                       continue 
                    elif unsur_isimleri_listesi [ana_unsur_index] [-1].count("t"):
                       continue 
                    else:
                        if len(ana_unsur) == 1:
                           unsur_i_tanimi_her_bir_kelimenin_harf_listesi = list(unsur_tanimlari_listesi_split_referansli [k] [l])
                           unsur_i_tanimi_her_bir_kelimenin_harf_listesi [0] = unsur_isimleri_listesi [ana_unsur_index]
                           unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [k] [l] = ''.join(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)
                           print ('10) Geçici kelime değişkeni= ' + str(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)) 
                           break
                        elif len(ana_unsur) > 1:
                           unsur_i_tanimi_her_bir_kelimenin_harf_listesi = list(unsur_tanimlari_listesi_split_referansli [k] [l])   
                           unsur_i_tanimi_her_bir_kelimenin_harf_listesi [0] = unsur_isimleri_listesi [ana_unsur_index]
                           for w in range (1,len(ana_unsur)):
                              unsur_i_tanimi_her_bir_kelimenin_harf_listesi [w] = ''
                              unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [k] [l] = ''.join(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)
                              print ('11) Geçici kelime değişkeni= ' + str(unsur_i_tanimi_her_bir_kelimenin_harf_listesi)) 
                           break
         else :
            continue 

# TANIMLARDA ANA UNSURLARIN REPLACE EDİLMESİ YUKARIDAKİ KOD BLOĞUNDA GERÇEKLEŞİYOR. HEM ÜNSÜZ YUMUŞAMASI OLANLAR HEM DE OLMAYANLAR.
 

unsur_tanimlari_listesi_string = []
    
for i in range (0,toplam_unsur_sayisi-1):
    unsur_tanimlari_listesi_string.append(unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [i])
    
#-UNSUR TANIMI LİSTESİNİN STRING HALİNE ÇEVİRMEMİZ GEREKİYOR REPLACE FONK. İÇİN. BURADA BUNUN İÇİN BOŞ LİSTE ATAYIP DOLDURDUK
#-DAHA SONRA DEĞİŞTİRMEK ÜZERE.
    
for i in range (0, toplam_unsur_sayisi-1):
   unsur_tanimlari_listesi_string [i] = ' '.join(unsur_tanimlari_listesi_split_unsurlar_yerlestirilmis [i])
    
#- REPLACE FONKSİYONUNU GERÇEKLEŞTİREBİLMEK İÇİN TÜM İFADEYİ LİST'TEN STRING FORMATINA GERİ ÇEVİRDİK JOİN FONKSİYONU İLE.

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
        istem_cümlesi [i]=  str(unsur_tanimlari_listesi_string [i]) + ' en az bir ' + str(unsur_isimleri_listesi [i]) + ' (' + str(unsur_referanslari_listesi [i].capitalize()) + '), '
    elif i+2 == toplam_unsur_sayisi:
        istem_cümlesi [i]=  str(unsur_tanimlari_listesi_string [i]) + ' en az bir ' + str(unsur_isimleri_listesi [i]) + ' (' + str(unsur_referanslari_listesi [i].capitalize()) + ') '
    else:
        istem_cümlesi [i]=  'ile karakterize edilen en az bir ' + str(unsur_isimleri_listesi [i]) + ' (' + str(unsur_referanslari_listesi [i].capitalize()) + '). '
    
#Yukarıdaki kod ile for döngüsüyle tüm istemin cümlelerini indexleyerek birleştirdik tek bir list istem cümlesinde.
#Ayrıca elif kısmının eklenmesinin sebebi karakterize edilen kısmından hemen önce yani son unsurdan sonra virgül koymamak. 
#Ama şuanlık çalışmıyor, üzerinde çalış.

global final_istem_cümlesi

final_istem_cümlesi = ['']
    
for i in range (0,toplam_unsur_sayisi):
    final_istem_cümlesi [0] = final_istem_cümlesi [0] + (''.join(istem_cümlesi [i]))
    
#tüm istem cümlesini for döngüsü ile bir değişkene atadık nihai olarak.

final_istem_cümlesi [0] = final_istem_cümlesi [0].capitalize()

print ('\n' + str(final_istem_cümlesi [0]))
    
#nihai istem cümlesini yazdırdık.