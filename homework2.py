class Avto:
    def init(self, model, yil, yurgan_km, narx):
        self.model = model
        self.yil = yil
        self.yurgan_km = yurgan_km
        self.narx = narx

    def info(self):
        return (f"Model: {self.model}\n"
                f"Yil: {self.yil}\n"
                f"Yurgan km: {self.yurgan_km}\n"
                f"Narx: ${self.narx}")
    def yurish(self, km):
        if km < 0:
            print("Km manfiy bo'lishi mumkin emas!")
        else:
            self.yurgan_km += km
    def chegirma(self, foiz):
        self.narx = self.narx - (self.narx * foiz/100)

jentra = Avto("Jentra", "2018", "120000", "9000")
malibu = Avto("Malibu", 2020, 45000, 18000)
tracker = Avto("Tracker", 2022, 15000, 25000)

print(jentra.info())
print(malibu.info())
print(tracker.info())

malibu.yurish(500)
tracker.chegirma(15)

print("\nYangilangan ma'lumotlar:")
print(jentra.info())
print(malibu.info())
print(tracker.info())


class User:
    def init(self,ism,familiya,foydalanuvchi_nomi, email):
        self.ism = ism
        self.familiya = familiya
        self.foydalanuvchi_nomi = foydalanuvchi_nomi
        self.email = email

    def get_info(self):
        info = (f"Foydalanuvchi: {self.foydalanuvchi_nomi}\n"
                   f"Ismi: {self.ism} {self.familiya}\n"
                   f"Email manzili: {self.email}")
        return info

user1 = User("Behruz", "Davletov", "behruz_davletov", "behruzdavletov@gmail.com")
user2 = User("Ali", "Valiyev", "ali2025", "ali2025@gmail.com")
user3 = User("donyor", "baxodirov","donyor.baxodirov", "donyor555@gmail.com")
print(user1.get_info())
print(user2.get_info())
print(user3.get_info())