#1
def kopaytma(*sonlar):
    natija = 1
    for s in sonlar:
        natija *= s
    return natija


#
print(kopaytma(2, 78, 4))
print(kopaytma(5, 14))
print(kopaytma(3, 6, 1, 7, 68))


#2
def talaba_info(ism, familiya, **qoshimcha):
    info = {
        "ism": ism,
        "familiya": familiya
    }
    info.update(qoshimcha)
    return info


# Funksiyani tekshiramiz
print(talaba_info("Ali", "Valiyev"))
print(talaba_info("Behruz", "Davletov", yil=2010, sinf=9))