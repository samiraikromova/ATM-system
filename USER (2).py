from ATM_FUNCTION import  *
class USER(ATM_FUNCTION):
    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin


    def load_menu(self):
        print("Iltimos operatsiyani tanlang: "
              "\n\t1) Balansni tekshirish"
              "\n\t2) Pinni uzgartirish"
              "\n\t3) Telefon raqamini uzgartirish"
              "\n\t4) Deposit qo'yish"
              "\n\t5) Pul yechish"
              "\n\t6) Pul o'tkazish"
              "\n\t7) Keyingi menuga qaytish uchun 6 ni tanlang ")
        service = input()
        if service == "1":
            balance = self.getBalance(self.card_number)
            print(balance)
        elif  service == '2':
            pin = input("Enter the old pin")
            new_pin = input("Enter the new pin")
            if int(pin) == int(self.pin):
                self.change_pin(self.card_number, pin, new_pin)
                print("Pin muaffaqqiyatli o'zgartirildi")
            else:
                print("Noto'g'ri pin raqami  ")
        elif service == '3':
            phone = input("Yangi telefon raqamini kiriting")
            if (self.checkPhoneNumber(phone)):
                self.updateUser(self.card_number, phone)
                print("Telefon raqami muaffaqqiyatli o'zgartirildi")
            else:
                print("Notug'ri telefon raqami")
        elif service == '4':
            get_balance = int(input("Deposit summani kiriting"))
            self.update_balance(self.card_number, get_balance)
            print("Balans qo'shildi")
        elif service == '5':
            get_money = int(input("Summani kiriting"))
            status, current, found =self.update_balance(self.card_number, -get_money)
            if status == True:
                print("Naqt pul yechildi")
                print("Hozirgi balance", current)
            else:
                print("Balansda yetarli pul yo'q")
        elif service == '6':
            card_number = int(input("Pul utkazadigan karta raqamini kiriting"))
            if self.check_card2(card_number):
                print("Card found")
                summa = float(input("Pul utkazadigan summani kiriting"))
                if self.update_balance(self.card_number, - summa):
                    self.update_balance(card_number, summa)
                    print("Balance",self.getBalance(self.card_number))
                else:
                    print("Yetarli pul mavjud emas")
            else:
                print("Card not found")


        elif service =='7':
            exit(0)






    def getName(self, cardNumber):
        with open('user_data.txt') as file:
            list_of_users = file.readlines()
            for user in list_of_users:
                list_info = user.split(" ")
                if cardNumber == int(list_info[2]):
                    return list_info[0].replace('_', ' ')
            return None

    # getBalance function returns balance of the user if user provide card number
    def getBalance(self, cardNumber):
        with open('user_data.txt') as file:
            list_of_users = file.readlines()
            for user in list_of_users:
                list_info = user.split(" ")
                if cardNumber == int(list_info[2]):
                    return list_info[5]
            return None


    def change_pin(self, cardNumber, old_pin, new_pin):
        f = open("user_data.txt", "r")
        list_of_user = f.readlines()
        f.close()
        count = 0
        for user in list_of_user:
            count += 1
            list_info = user.split(' ')
            if int(cardNumber) == int(user.split(' ')[2]) and int(old_pin) == int(user.split(' ')[3]):
                list_info[3] = new_pin
                with open("user_data.txt") as file:
                    lines = file.readlines()
                    lines[count - 1] = list_info[0] + ' ' + list_info[1] + ' ' + list_info[2] + ' ' + list_info[3] + ' ' + \
                                       list_info[4] + ' ' + list_info[5]
                with open("user_data.txt", "w+") as file:
                    for line in lines:
                        file.write(str(line))


