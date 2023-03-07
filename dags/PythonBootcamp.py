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
        elif kontrol == "h":
            print("Güle Güle")
            break
        else:
            print("Hatalı Tuşlama")

if __name__ == "__main__":
    main_func()