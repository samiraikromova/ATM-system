
import math
import random
from datetime import datetime

import  DateTime


class ATM_FUNCTION():
    bills = {100000:0, 50000:0, 10000:0,5000:0}
    def __init__(self):
        pass
    def split_bills(self, sum, bills):
        count = math.floor(sum / 165000)
        remainder = sum % 165000
        if remainder == 0:
            for i in bills.keys():
                bills[i] += count
        else:
            for i in bills.keys():
                bills[i] += count + math.floor(remainder / i)
                remainder = remainder % i
        return bills, remainder

    def createATM(self, location, status, balance, bills):
        bills, reminder = ATM_FUNCTION().split_bills(balance, bills)
        balance -= reminder
        f = open("atm_list.txt",'+r')
        list_of_atm = f.readlines()
        f.close()
        if len(list_of_atm) == 0:
            print("No ATM found")
            f = open("atm_list.txt",'+w')
            f.write('1'+' ' + location+ ' '+status+ ' '+str(balance)+ ' '+str(bills)+'\n')
            f.close()
        else:
            id = int(list_of_atm[len(list_of_atm)-1].split(' ')[0])
            f = open("atm_list.txt", '+a')
            f.write( str(id+1) + ' ' + location + ' ' + status + ' ' + str(balance) + ' ' + str(bills) + '\n')
            f.close()
        return reminder
    def getATM_BALANCE(self):
        try:
            total_balance = 0
            f = open("atm_list.txt","r")
            list_of_atm = f.readlines()
            f.close()
            for atm in list_of_atm:
                total_balance += int(atm.split(' ')[3])
        except Exception as e:
            print("No ATM found", e)

        return total_balance

    def checkPhoneNumber(self, phoneNumber):
        if phoneNumber == 'yuq':
            return True
        elif phoneNumber.isdigit() and len(phoneNumber) ==9:
            return True
        else: return False
    def getCardNumber(self):
        f = open("user_data.txt",'+r')
        list_of_user = f.readlines()
        f.close()
        check = True
        while check:
            newCardNumber = random.randint(10000,99999)
            if (len(list_of_user)>0):
                for user in list_of_user:
                    if int(newCardNumber) == int(user.split(' ')[2]):
                        check =True
                        break
                    else:
                        check = False
            elif (len(list_of_user)==0):
                return newCardNumber
            return newCardNumber

    def creatUser ( self, user_name, phoneNumber, cardNumber, pin, experationDate, balance):
        f = open('user_data.txt','+a')
        f.write( user_name.replace(' ','_')+' '+phoneNumber+' '+cardNumber+' '+pin+' '+str(experationDate)+' '+str(balance)+'\n')
        f.close()

    def updateUser(self, cardnumber, user_info):
        f = open('user_data.txt')
        list_of_user = f.readlines()
        f.close()
        count = 0
        for user in list_of_user:
            list_info = user.split(' ')
            count = count + 1
            if cardnumber == int(list_info[2]):
                if user_info.isdigit() and len(user_info) == 9:
                    list_info[1] = user_info
                    with open('user_data.txt') as file:
                      lines = file.readlines()
                      lines[count-1] = list_info[0] + ' ' + list_info[1] + ' ' + list_info[2]+ ' ' + list_info[3]+ ' ' + list_info[4]  +' ' +  list_info[5]
                    with open('user_data.txt','+w') as file:
                        for line in lines:
                            file.write(str(line))
                elif len(user_info) == 4 and user_info.isdigit():
                    self.__change_pin(cardnumber, user_info)
                return  True
        return False

    def update_balance(self, cardnumber, balance):
        found = False
        current_balance = 0
        f = open('user_data.txt')
        list_of_user = f.readlines()
        f.close()
        count = 0
        for user in list_of_user:
            list_info = user.split(' ')
            count = count + 1
            if cardnumber == int(list_info[2]):
                found = True
                current_balance = float(list_info[5])
                if balance >= 0:
                    current_balance += balance
                elif current_balance >= - (balance):
                    current_balance += balance
                else:
                    return False, current_balance, found
                list_info[5] = current_balance
                with open("user_data.txt") as file:
                        lines = file.readlines()
                        lines[count - 1] = list_info[0] + ' ' + list_info[1] + ' ' + list_info[2] + ' ' + list_info[3] + ' ' + list_info[4] + ' ' + str(list_info[5])+'\n'
                with open("user_data.txt", "w+") as file:
                        for line in lines:
                            file.write(str(line))
                return True, current_balance, found
        return False, current_balance, found
    def update_atm_balance(self, atmID, balance, userID):
        found = False
        current_balance = 0
        f = open('atm_list.txt')
        list_of_atm = f.readlines()
        f.close()
        count = 0
        for user in list_of_atm:
            atm_info = user.split('{')
            user_info = atm_info[0].split(' ')
            count = count + 1
            if atmID == int(user_info[0]):
                found = True
                current_balance = float(user_info[3])
                self.split_bills(float(user_info[3]))
                if balance >= 0:
                    current_balance += balance
                elif current_balance >= - (balance):
                    current_balance += balance
                else:
                    return False, current_balance, found
                print("Current Balance", current_balance)
                user_info[3] = current_balance
                bills, reminder = self.split_bills(current_balance, self.bills)
                atm_info[0] = user_info[0]+' '+ user_info[1]+' '+ user_info[2]+' '+ str(user_info[3])
                atm_info[1] = bills
                with open("atm_list.txt") as file:
                        lines = file.readlines()
                        lines[count - 1] = str(atm_info[0]) + ' ' + str(atm_info[1]) +'\n'
                with open("atm_list.txt", "w+") as file:
                        for line in lines:
                            file.write(str(line))
                return True, current_balance, found
        return False, current_balance, found


    def __change_pin(self, cardNumber, new_pin):
        f = open("user_data.txt", "r")
        list_of_user = f.readlines()
        f.close()
        count = 0
        for user in list_of_user:
            count += 1
            list_info = user.split(' ')
            if int(cardNumber) == int(user.split(' ')[2]):
                list_info[3] = new_pin
                with open("user_data.txt") as file:
                    lines = file.readlines()
                    lines[count - 1] = list_info[0] + ' ' + list_info[1] + ' ' + list_info[2] + ' ' + list_info[3] + ' ' + list_info[4] + ' ' + str(list_info[5])
                with open("user_data.txt", "w+") as file:
                    for line in lines:
                        file.write(str(line))

    def check_card(self, cardnumber, pin):

        f = open("user_data.txt", "r")
        list_of_user = f.readlines()
        f.close()
        for user in list_of_user:
            user_info = user.split(' ')
            if int(user_info[2]) == cardnumber and int(user_info[3]) == pin:
                return True
        return False

    def check_card2(self, cardnumber):

        f = open("user_data.txt", "r")
        list_of_user = f.readlines()
        f.close()
        for user in list_of_user:
            user_info = user.split(' ')
            if int(user_info[2]) == cardnumber:
                return True
        return False

    
