admin = 'admin'
password = 'pass'
import  ATM_FUNCTION
def admin():
    SerLP = {"Ser1":"pass1", "Ser2":"pass2", "Ser3":"pass3", "Ser4":"pass4"}
    print("Admin oynasiga hush kelibsiz! Iltimos, ")
    login = input("Loginni kiriting: ")
    password = input("Parolni kiriting: ")
    if login == "CEO" and password == "pass":
        seo()

    elif login in SerLP and SerLP[login] == password:
        print("\nHurmatli Service, hush kelibsiz!")
        print("Iltimos operatsiyani tanlang: "
              "\n\t1) ATM balansini tekshirish "
              "\n\t2) ATM balansini o'zgartirish "
              "\n\t3) ATM transaksiyasi tarihini ko'rish")
    else:
        print("""Login yoki Parol noto'g'ri kiritildi. 
        Iltimos parolni tekchirib qaytadan kiriting! """)
        admin()





def admin():       # Admin oynasi: SEO yoki Service tanlanadi. Bu yerda SEO bitta va Service ko'p
    SerLP = {"Ser1":"pass1", "Ser2":"pass2", "Ser3":"pass3", "Ser4":"pass4"}    # Birqancha Service larni login va parollari
    print("Admin oynasiga hush kelibsiz! Iltimos, ")
    login = input("Loginni kiriting: ")
    password = input("Parolni kiriting: ")
    if login == "SEO" and password == "pass":
        seo()
#        print("\nHurmatli SEO, hush kelibsiz!")
#        print("Iltimos operatsiyani tanlang: \n1) ATMni yaratish \n2) Foydalanuvchini kiritish \n3) Foydalanuvchi ma\'lumotlarini yangilash \n4) Balansni tekshirish \n5) Bank nomini o'zgartirish")
    elif login in SerLP and SerLP[login] == password:
        ser()
#        print("\nHurmatli Service, hush kelibsiz!")
#        print("Iltimos operatsiyani tanlang: \n1) ATM balansini tekshirish \n2) ATM balansini o'zgartirish \n3) ATM transaksiyasi tarihini ko'rish")
    else:
        print("""Login yoki Parol noto'g'ri kiritildi. Iltimos parolni tekchirib qaytadan kiriting! """)
        admin()

def seo():          # SEO oynasi bilan ishlash
    print("seo")

def ser():          # Service oynasi bilan ishlash
    print("\nHurmatli Service, hush kelibsiz!")
    operation = {1:"ATM balansini tekshirish", 2:"ATM balansini o'zgartirish", 3:"ATM transaksiyasi tarihini ko'rish"}
    print("1) ATM balansini tekshirish \n2) ATM balansini o'zgartirish \n3) ATM transaksiyasi tarihini ko'rish")
    opera = int(input("\nIltimos operatsiyani tanlang: "))
    if opera in operation:
        print("\n", operation[opera], " oynasini ochish")
    else:
        print("\nTo'g'ri operatsiyani tanlang!")

def user():          # User oynasi bilan ishlash
# num 5 ta raqamdan iborat 1-bank nomi, 2-filial nomi, 3-UzKard (0) yoki Humo (1) 4-5-Foydalanuvchi ID raqami
    print("\nHurmatli Mijoz, hush kelibsiz!")
    card = int(input("Iltimos karta raqamini kiriting: "))
    pin = int(input("Iltimos maxfiy raqamini kiriting: "))
    user = {11101:"p11101", 11102:"p11102", 11103:"p11103"}
    if card in user.keys() and user[card] == pin:
        print("Hurmatli Mijoz, qanday operatsiyani tanlaysiz?")
#        Mijoz = User(name, cardNo, balance)




