# 1. user_data(first_name, last_name, age)
def user_data():
    first_name = input("Ismni kiriting: ")
    last_name = input("Familiyani kiriting: ")
    age = input("Yoshni kiriting: ")

    print(f"Ism: {first_name}")
    print(f"Familiya: {last_name}")
    print(f"Yosh: {age}")

user_data()

# 2. find_max(a, b, c)
def find_max():
    a = int(input("1-sonni kiriting: "))
    b = int(input("2-sonni kiriting: "))
    c = int(input("3-sonni kiriting: "))

    print("Eng katta son =", max(a, b, c))

find_max()


# 3. find_letter_count(word, letter)
def find_letter_count():
    word = input("So‘zni kiriting: ")
    letter = input("Harf kiriting: ")

    count = word.count(letter)
    print(f'"{word}" so‘zida "{letter}" harfi {count} marta bor.')

find_letter_count()



# 4. list_sum(myList)
def list_sum(myList):
    print(f"Listning elementlar yig'indisi = {sum(myList)}")

list_sum([5, 7, 10, 10])


# 5. daraja(a, b)
def daraja(a, b):
    print(a ** b)

daraja(6,2)


# 6. daraja4(a, b, c, d)
def daraja4(a, b, c, d):
    print(a ** b)
    print(a ** c)
    print(a ** d)

daraja4(89, 4, 76, 1)


# 7. digit_count_and_sum(word)



# 8. add_right(a, b)
def add_right(a, b):
    print(str(a) + str(b))

add_right(4,9)

# 9. add_left(a, b)
def add_left(a, b):
    print(str(b) + str(a))

add_left(6,1)

# 10. work_with_list(a)



# 11. big_sales(sales)
def big_sales(sales):
    return max(sales, key=sales.get)


sales = {
    "yanvar": 32000,
    "mart": 7000,
    "aprel": 15000,
    "sentabr": 5010,
    "dekabr": 1632487,
}

print("Eng ko‘p sotuv bo‘lgan oy:",big_sales(sales))

# 12. min_max(numbers, max_num, min_num)


# 13. expensiveProduct(products)
def expensiveProduct(products):
    expensive = max(products, key=lambda x: x["price"])
    print("Eng qimmat telefon:", expensive["name"])

products = [
    {
        "name": "Iphone X",
        "price": 600
    },
    {
        "name": "Iphone 12",
        "price": 1500
    },
    {
        "name": "Samsung Note 9",
        "price": 800
    },
    {
        "name": "Samsung S10",
        "price": 1100
    },
]
expensiveProduct(products)