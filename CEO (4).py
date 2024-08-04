import DateTime.DateTime
from datetime import datetime

from ATM_FUNCTION import  *
class  CEO(ATM_FUNCTION):


    def load_menu(self):
        bills = {100000: 0, 50000: 0, 10000: 0, 5000: 0}
        print("\nHurmatli SEO, hush kelibsiz!")
        print("Iltimos operatsiyani tanlang: "
              "\n\t1) ATMni yaratish "
              "\n\t2) Foydalanuvchini kiritish "
              "\n\t3) Foydalanuvchi ma\'lumotlarini yangilash "
              "\n\t4) Balansni tekshirish "
              "\n\t5) Bank nomini o'zgartirish")

        opera = int(input("Iltimos operatsiyani tanlang: "))
        if opera == 1:
            location = input("\n\tATM manzilini kiriting")
            status = 'active'
            balance = int(input("\n\tBoshlang\'ich balansni kiriting"))
            reminder = ATM_FUNCTION().createATM(location,status, balance, bills)
            print("Reminder ", reminder,"")
        elif opera ==2:
            user_name = input("\n\tFoydalanuvchini FISH")
            phone_number = input("\n\tTelefon raqami:")
            card_number = str(ATM_FUNCTION().getCardNumber())
            pin = input("\n\tPin raqamini kiriting")
            balance = input("\n\tBoshlang\'ich balansni kiriting")
            experationDate = datetime.today().strftime("%m/%Y")
            ATM_FUNCTION().creatUser(user_name,phone_number,card_number,pin,experationDate, balance)
            print("Foydalanuvchi ", user_name,'ma\'lumotlar bazasiga kiritildi')
        elif opera ==3:
            card_number = int(input("\t Karta raqamini kiriting:"))
            user_info = (input("Foydalanuvchi ismini yoki raqami yoki pin yoki telefon raqami kiritiladi"))
            ATM_FUNCTION().updateUser(card_number,user_info)
        elif opera == 4:
            print("Barcha ATMdagi pullar miqdori : ",ATM_FUNCTION().getATM_BALANCE())
        elif opera == 5:
            print("Bank nomini uzgartirmaymiz ")













if __name__ == "__main__":

    CEO().load_menu()