import random
import string
import re
import time

def user_details():
    name=input("Enter Your Name :")
    age=int(input("Enter your Age:"))
    gender=""
    gen={
    1:"Male",
    2:"Female",
    3:"Others"
    }
    for i , j in gen.items():
        print(f"{i}:{j}")
    gen_choice=int(input("Enter your choice:"))
    if gen_choice in gen:
        gender=gen[gen_choice]
    else:
        print("invalid")
        gender=input("Enter the gender manually")
    rule={
        1:"phone number should have 10 digits",
        2:"Phone number should not start with 0",
        3:"Gmail should end with @gmail.com only"
    }
    while True:
        for i,j in rule.items():
            print(f"{i}:{j}")
        phone=input("Enter Phone number:")
        gmail=input("Enter the Gmail:")
        pincode=input("Enter the Pincode:")
        ph_str=r'^\d{10}$'
        gm_str=r'^.+gmail\.com$'
        pin_str=r'^\d{6}$'
        if re.fullmatch(ph_str,phone) and re.fullmatch(gm_str,gmail) and re.fullmatch(pin_str,pincode):
            time.sleep(1)
            print("verification processing.....")
            time.sleep(1)
            print("phone number verified✔️")
            time.sleep(1)
            print("gmail is verified✔️")
            time.sleep(1)
            print("pincode is verified✔️")
            break
        else:
            print("not verified❌")
    details={
            "NAME":name,
            "AGE":age,
            "GENDER":gender,
            "PHONE NUMBER":phone,
            "GMAIL":gmail,
            "PINCODE":pincode
        }
    return details

def generate_code():
    a="".join(random.choices(string.digits,k=3))
    b="".join(random.choices(string.ascii_uppercase,k=3))
    c=a+b
    print(f"code is being generated")
    time.sleep(2)
    print("almost there.....⏳")
    print("Enter this to get to complete the verification process")
    time.sleep(1)
    while True:
        print(f"Your code is {c}.")
        user_code=input("Enter the code:")
        if user_code==c:
            print("Verification processed......⏳")
            time.sleep(2)
            print("registered☑️")
            break
        else:
            print("sorry ,invalid input")

def BPIN(details):
    print("BPIN is being generated,please remeber this for future usage.")
    time.sleep(2)
    a="".join(random.choices(string.digits,k=4))
    print("📌📌📌📌📌📌📌📌📌")
    print(f"Your BPIN is :{a}")
    print("📌📌📌📌📌📌📌📌📌")
    details["BPIN"]=a

def check_details(details):
    B_pin=input("Enter the Bpin:")
    if B_pin == details.get("BPIN"):
        print("Your complete profile details are as :")
        for i , j in details.items():
            if i!="BPIN":
                print(f"👉{i}:{j}")

def acc_num():
    print("account number consists of 11 characters")
    a="".join(random.choices(string.digits,k=4))
    b="".join(random.choices(string.ascii_uppercase,k=3))
    c="".join(random.choices(string.digits,k=3))
    d="SS"
    acc=a+b+c+d
    print(f"your account number :{acc}")
    return acc

def ifsc_num():
    print("Ifsc number consists of 16 characters")
    a="".join(random.choices(string.digits,k=4))
    b="".join(random.choices(string.ascii_uppercase,k=4))
    c="".join(random.choices(string.digits,k=4))
    d="MSS7"
    ifsc=a+b+c+d
    print(f"your ifsc number :{ifsc}")
    return ifsc

def Bank_details(details):
    while True:
        user_bpin_entry=input("Enter the BPIN:")
        if user_bpin_entry == details.get("BPIN"):
            acc=acc_num()
            ifsc=ifsc_num()
            details["account number"]=acc
            details["ifsc code"]=ifsc
            print("Account number and IFSC code have been added to your profile.")
            break
        else:
            print("Not correct BPIN")

    return

def deposit(details):
    balance=0
    while True:
        user_bpin_entry=input("Enter the BPIN:")
        if user_bpin_entry == details.get("BPIN"):
            amount=float(input("enter the amount you want to add:"))
            if amount > 0:
                balance+=amount
                print(f"{amount} has been added to your account successfull")
                details["BALANCE"]=balance
                break
            else:
                print("sorry amount is not valid")
        else:
            print("Not valid BPIN")

def withdraw(details):
    balance=details.get("BALANCE")
    while True:
        user_bpin_entry=input("Enter the BPIN:")
        if user_bpin_entry == details.get("BPIN"):
            amount=float(input("enter the amount you want to withdraw:"))
            if amount > 0 and amount < balance:
                balance-=amount
                print(f"{amount} has been deducted from your account successfull")
                details["BALANCE"]=balance
                break
            else:
                print("sorry amount is not valid")
        else:
            print("Not valid BPIN")

def balance_check(details):
    balance=details.get("BALANCE",0)
    print(f"your balance amount is {balance}.")


def main():
    print("Welcome to VERNA BANK")
    client=None
    while True:
        options={
            1:"NEW REGISTRATION",
            2:"BANK DETAILS",
            3:"PROFILE INFO",
            4:"DEPOSIT",
            5:"WITHDRAW",
            6:"BALANCE",
            7:"EXIT"
        }
        for i,j in options.items():
            print(f"{i}:{j}")

        try:
            user_option=int(input("Enter your choice:"))
        except ValueError:
            print("INVALID INPUT")
            continue


        if user_option == 1:
            print("NEW REGISTRATION FORM")
            client = user_details()
            generate_code()
            BPIN(client)
            print("Successfully registered✔️")
        elif user_option==2:
            if client is not None:
                Bank_details(client)
            else:
                print("please register first")
        elif user_option == 3:
            if client is not None:
                check_details(client)
            else:
                print("please register first")
        elif user_option ==4:
            if client is not None:
                deposit(client)
            else:
                print("please register first")
        elif user_option ==5:
            if client is not None:
                withdraw(client)
            else:
                print("please register first")
        elif user_option ==6:
            if client is not None:
                balance_check(client)
            else:
                print("please register first")

        elif user_option ==7:
            print("Thank you bye")
            break
        else:
            print("Invalid option.")

main()