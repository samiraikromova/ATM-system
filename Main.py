from USER import  *
class Main():
    def __init__(self):
        pass

    def load(self):  # Ilk kirish oynasi: User yoki Admin tanlanadi
        print("Loading ... ")
        servise = input("Foydalanuvchi turini tanlang: \n 1. Admin \n 2. User \n")
        if servise == "1":
            print("Admin menyuni ochish ")

        elif servise == "2":
            while True:
                card = int(input("Enter card number"))
                pin = int(input("Enter pin number"))
                user = USER(card, pin)
                if (user.check_card(card,pin)):
                    print("Hush kelibsiz ", user.getName(card))
                    user.load_menu()
                else:
                    print("Notug'ri karta raqami yoki pin ")

        else:
            print("""T'g'ri sarvis tanlang! """)
if __name__ == '__main__':
    while True:
        Main().load()