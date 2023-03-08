from datetime import datetime
import csv

class Pizza(object):

    def __init__(self,name,cost,explain) :
        self.name = name
        self.__cost = cost
        self.__explain = explain

    def get_cost(self):
        return self.__cost
    
    def get_explain(self):
        return self.__explain
    
class Decarator(Pizza):

    def __init__(self,name,cost,explain):
        self.name = name
        self.__cost = cost
        self.__explain = explain

    def get_cost(self,self1):
        return self.__cost + Pizza.get_cost(self1)
    
    def get_explain(self,self1):
        return self.__explain + " ve " + Pizza.get_explain(self1)

class ClassicPizza(Pizza):
    def __init__(self, name = "Klasik Pizza", cost = 50, explain = "Klasikten Şaşmayanların Pizzası"):
        super().__init__(name, cost, explain)

class MargaritaPizza(Pizza):
    def __init__(self, name = "Margarita Pizza", cost = 60 , explain = "Pizza Sevenler için"):
        super().__init__(name, cost, explain)

class TurkPizza(Pizza):
    def __init__(self, name = "Türk Pizza", cost = 75, explain = "Anadolu ve İtalyan lezzetleri bir arada"):
        super().__init__(name, cost, explain)

class SadePizza(Pizza):
    def __init__(self, name = "Sade Pizza", cost = 85, explain = "Sadelikte ihtişam vardır diyenler için"):
        super().__init__(name, cost, explain)

class ZeytinSos(Decarator):
    def __init__(self, name = "Zeytin Sos", cost = 20, explain = "Egenin eşsiz zeytinleri ile beraber"):
        super().__init__(name, cost, explain)
class MantarSos(Decarator):
    def __init__(self, name = "Mantar Sos", cost = 15, explain = "Mantar Sevenler İçin"):
        super().__init__(name, cost, explain)
class SoganSos(Decarator):
    def __init__(self, name = "Soğan Sosu", cost = 5, explain = "Soğan Severler"):
        super().__init__(name, cost, explain)
class KeciPeyniriSos(Decarator):
    def __init__(self, name = "Keçi Peyniri Sosu", cost = 40, explain = "İnatçıyım ben diyenler için"):
        super().__init__(name, cost, explain)
class EtSos(Decarator):
    def __init__(self, name = "Et Sos", cost = 35, explain = "Et Sevenler için"):
        super().__init__(name, cost, explain)
class MisirSos(Decarator):
    def __init__(self, name = "Mısır Sos", cost = 25, explain = "Mısır sevenler için"):
        super().__init__(name, cost, explain)

def main_func():
    while True:
        menu = open("/home/user/deneme/AkbankPythonBootcamp/dags/Menu.txt","r")
        print(f"{40*'/'} \n Pizza Sipariş Ekranına Hoşgeldiniz \n {40*'/'} \n {menu.read()}")
        kontrol = input("İşleme devam etmek istiyor musunuz e/h \n")
        if kontrol == "e":
            pizza_tabani = int(input("Pizza tabanı numaranızı seçiniz"))
            pizza_sosu = int(input("Pizza sosu numaranızı seçiniz"))
            siparis_detay =  siparis(pizza_sosu,pizza_tabani)
            ücret = siparis_detay[0]
            aciklama = siparis_detay[1]
            print(f" {aciklama} pizza siparişinizin fiyatı {ücret} tldir \n")
            ödeme_kontrol = input("Siparişinizi onaylıyor musunuz ? e/h \n")
            if ödeme_kontrol == "e":
                ad = input("Adınız :   ")
                kart_no = input("Kart Bilgilerinizi :   ")
                tc_no = input("TCK No :   ")
                kart_sifre = input("kart sifre :   ")
                müsteri_kayit(ad,ücret,aciklama,kart_no,tc_no,kart_sifre)
                break
        elif kontrol == "h":
            print("Güle Güle")
            break
        else:
            print("Hatalı Tuşlama")
def müsteri_kayit(ad, ücret, aciklama, kart_no, tc_no,kart_sifre, date = datetime.now()):
    f = open("/home/user/deneme/AkbankPythonBootcamp/dags/Orders_Database.csv","a")
    writer = csv.writer(f)
    row = [ad, ücret, aciklama, kart_no, tc_no,kart_sifre, date]
    writer.writerow(row)
    f.close()



def siparis(pizza_sosu,pizza_tabani):
    pizza_tabani_dict = {1 : ClassicPizza(), 2 : MargaritaPizza(), 3 : TurkPizza(), 4 : SadePizza()}
    pizza_sosu_dict = {11 : ZeytinSos(), 12 : MantarSos(), 13 : KeciPeyniriSos() , 14 : EtSos(), 15 : SoganSos(), 16 : MisirSos()}
    for key in pizza_tabani_dict.keys():
        if key == pizza_tabani:
            pizza_tabani = pizza_tabani_dict[key]
    for key in pizza_sosu_dict.keys():
        if key == pizza_sosu:
            pizza_sosu = pizza_sosu_dict[key]
    return Decarator.get_cost(pizza_sosu,pizza_tabani), Decarator.get_explain(pizza_sosu,pizza_tabani)
    
        
if __name__ == "__main__":
    main_func()