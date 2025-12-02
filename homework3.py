# --- FAN KLASSI ---
class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

    def repr(self):
        return self.nomi


# --- SHAXS KLASSI ---
class Shaxs:
    def __init__(self, ism,  yosh):
        self.ism = ism
        self.yosh = yosh

    def get_info(self):
        return f"{self.ism}, {self.yosh} yosh"
#

# --- TALABA KLASSI ---
class Talaba(Shaxs):
    def __init__(self, ism, yosh):
        super().__init__(ism, yosh)
        self.fanlar = []      # parametr orqali uzatilmaydi

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            return "Siz bu fanga yozilmagansiz"

    def get_info(self):
        info = super().get_info()
        if self.fanlar:
            fanlar = ", ".join(f.nomi for f in self.fanlar)
        else:
            fanlar = "Fanlar yo‘q"
        return f"{info}. Fanlar: {fanlar}"


# --- BOSHQA VORIS KLASSLAR ---
class Professor(Shaxs):
    def __init__(self, ism, yosh, kafedra):
        super().__init__(ism, yosh)
        self.kafedra = kafedra

    def get_info(self):
        return f"Professor {self.ism} {self.kafedra} kafedrasi"


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, yosh, username):
        super().__init__(ism, yosh)
        self.username = username

    def get_info(self):
        return f"Foydalanuvchi: {self.username} ({self.ism})"





    f1 = Fan("Matematika")
    f2 = Fan("Fizika")
    f3 = Fan("Ingliz tili")


    t1 = Talaba("Ali", 20)

    t1.fanga_yozil(f1)
    t1.fanga_yozil(f2)

    print(t1.get_info())

    print(t1.remove_fan(f3))
    t1.remove_fan(f1)

    print(t1.get_info())
