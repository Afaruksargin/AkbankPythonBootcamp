from datetime import datetime
import csv

class Pizza:
    def get_cost(self):
        return self.__class__.cost 
    def get_description(self):
        return self.__class__.description
    
class ClassicPizza(Pizza):
    cost = 50
    description = "Klasik Severler"

class MargaritaPizza(Pizza):
    cost = 60
    description = "Peynir Severler"

class TurkPizza(Pizza):
    cost = 70
    description = "Anadolu Lezzeti arayanlara"

class SadePizza(Pizza):
    cost = 40
    description = "Sade Severler"

class Decorator(Pizza):
    def __init__(self,pizza=ClassicPizza()):
        self.component = pizza

    def get_cost(self):
        return self.component.get_cost() + \
                Pizza.get_cost(self)
    def get_description(self):
        return self.component.get_description() + " " + \
            Pizza.get_description(self)

class ZeytinSos(Decorator):
    cost = 30
    description = "Zeytin sosu ile beraber"

class MantarSos(Decorator):
    cost =50
    description = "Mantar ile beraber"

class EtSos(Decorator):
    cost = 55
    description = "Et sosu ile beraber"

class SoganSos(Decorator):
    cost =15
    description = "Soğan ile beraber"

class KeciPeyniriSos(Decorator):
    cost = 40
    description = "Keçi Peyniri sosu ile beraber"

class MisirSos(Decorator):
    cost =10
    description = "Mısır ile beraber"


def main_func():
    menu = open("/home/user/deneme/AkbankPythonBootcamp/dags/Menu.txt","r")
    print(f"{40*'/'} \n Pizza Sipariş Ekranına Hoşgeldiniz \n {40*'/'} \n {menu.read()}")
    pizza = int(input("Pizza Seçiniz \n"))
    sos = int(input("Sos Seçiniz \n"))
    siparis = siparis_func(pizza,sos)
    print(f" Sipariş Açıklama : {siparis.get_description()} \n \
Sipariş Tutar : {siparis.get_cost()} ")
    #Müşteri Kayıt Bilgileri
    ad = input("Adınız :   ")
    kart_no = input("Kart Bilgilerinizi :   ")
    tc_no = input("TCK No :   ")
    kart_sifre = input("kart sifre :   ")
    müsteri_kayit(ad,siparis.get_cost(), siparis.get_description(),kart_no,tc_no,kart_sifre)


def müsteri_kayit(ad, ücret, aciklama, kart_no, tc_no,kart_sifre, date = datetime.now()):
    f = open("/home/user/deneme/AkbankPythonBootcamp/dags/Orders_Database.csv","a")
    writer = csv.writer(f)
    row = [ad, ücret, aciklama, kart_no, tc_no,kart_sifre, date]
    writer.writerow(row)
    f.close()

def siparis_func(pizza,sos):
    pizza_tabani_dict = {1 : ClassicPizza(), 2 : MargaritaPizza(), 3 : TurkPizza(), 4 : SadePizza()}
    for key in pizza_tabani_dict.keys():
        if key == pizza:
            pizza_tabani = pizza_tabani_dict[key]
    if sos == 11 :
        return ZeytinSos(pizza_tabani)
    if sos == 12:
        return MantarSos(pizza_tabani)
    if sos == 13 :
        return KeciPeyniriSos(pizza_tabani)
    if sos == 14:
        return EtSos(pizza_tabani)
    if sos == 15 :
        return SoganSos(pizza_tabani)
    if sos == 16:
        return MisirSos(pizza_tabani)
    else:
        print("Hatalı ürün girişi")


if __name__ == "__main__":
    main_func()
