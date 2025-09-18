#### expense tracker
#project done by soban sai M
import time
import random
import datetime
import string

def greet():
    print("Hello welcome to Verna Expense tracker")
    print("1.Verna Expense tracker will record all your expenses.\n2.if you want to you can filter the expenses.\n3.if you want you can sum up the expenses.\n4.All the best.")
    print("Go ahead , you will have fun.")
    print("=======================================")


def user_details():
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    gen_choices={
        1:"Male",
        2:"Female",
        3:"other"
        }
    for i , j in gen_choices.items():
        print(f"{i}:{j}")
    while True:
        gen=int(input("Enter your choice of gender:"))
        if gen in gen_choices:
            gender=gen_choices.get(gen)
            break
        else:
            print("Invalid choice")
    
    print("you will recieve EXPIN .\nRemember the EXPIN for future use.")
    EX="".join(random.choices(string.digits,k=4))
    import time
    print("wait a moment")
    time.sleep(2)
    print("EXPIN is generated....⏳")
    EXPIN = EX
    print(f"━━━ ✦{EXPIN}✦━━━")
    
    details={
        "NAME":name,
        "AGE":age,
        "GENDER":gender,
        "EXPIN":EXPIN
    }
    import time
    print("wait a moment")
    time.sleep(3)
    print("Generating details...⌛")
    print("━━━ ━━━ ━━━ ━━━ ━━━ ━━━")
    for i , j in details.items():
        print(f"{i}:{j}")
    print("━━━ ━━━ ━━━ ━━━ ━━━ ━━━")
    
    return details


def category_list():
    cat_list={
        1:"food",
        2:"travel",
        3:"accessories",
        4:"utensils",
        5:"electronics"
    }
    print("════════════════════")
    for i , j in cat_list.items():
        print(f"{i}:{j}")
    print("════════════════════")
    return cat_list

def printing_exp(expense):
    print("===================================")
    for i , j in expense.items():
        print(f"{i}:{j}")
    print("===================================")

def manual_exp(details):
    while True:
        pin=input("Enter the EXPIN")
        if pin == details.get("EXPIN"):
            print("valid pin details")
            
            print("following are the examples of categories")
            category_list()
            time.sleep(3)
            category=input("Enter the category manually:")
            dat=input("Enter the date using[,] in 🟢year, 🔵month, 🔴date format").strip(",")
            date="-".join(dat.split(","))
            time.sleep(2)              
            amount=0
            while True:
                try:
                    amt=float(input(f"Enter the amount you spent on the  {category} :"))
                    if amt > 0:
                        amount=amt
                        break
                    else:
                        print("amount should be more than zero")
                except ValueError:
                    print("amount should not be negative and should have only numbers")
            time.sleep(2)
            descript=input("Enter the description about the expense:")
            a=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            timestamp=a
            manual_list={
                "CATEGORY":category,
                "DATE":date,
                "AMOUNT":amount,
                "DESCRIPTION":descript,
                "TIMESTAMP":timestamp
            }
            print("wait a moment")
            time.sleep(3)
            printing_exp(manual_list)
            return manual_list
            
        else:
            print("Not valid pin")

def auto_list():
    main_list={
        1:"food",
        2:"travel",
        3:"utensils",
        4:"medicals",
        5:"education",
        6:"others"
    }
    food={
        1:"break fast",
        2:"lunch",
        3:"dinner"
    }
    travel={
        1:"daily travel",
        2:"other travel"
    }
    utensils={
        1:"plastic ware",
        2:"steel ware",
        3:"bronze ware",
        4:"other ware"
    }
    medicals={
        1:"baby care",
        2:"adult care",
        3:"emergency"
    }
    education={
        1:"children fees",
        2:"education loans",
        3:"others"
    }
    others={
        1:"misceleneous"
    }
    return main_list , food , travel , utensils , medicals , education , others
        

def  auto_exp(details):
    print("✨━━✨━━✨━━✨✨━━✨━━✨━━✨")
    print("good to see you choosing auto expense tracker")
    print("following are the list of categories")
    print("you can simply select from the list")
    print("✨━━✨━━✨━━✨✨━━✨━━✨━━✨")

    main_list , food , travel , utensils , medicals , education , others=auto_list()
    sub_cat={
        1:food,
        2:travel,
        3:utensils,
        4:medicals,
        5:education,
        6:others
    }
    while True:
        time.sleep(2)
        user_pin=input("Enter the pin:")
        if user_pin == details.get("EXPIN"):
            print("valid pin 🟢")
            break
        else:
            print("pin not valid🔴")
    print("wait a moment")
    time.sleep(2)      
    print("------------------------------")
    dat=input("Enter the date using[,] in 🟢year, 🔵month, 🔴date format").strip(",")
    date="-".join(dat.split(","))
    print("wait a moment")
    time.sleep(2)
    print("main categories as follows:")
    for i , j in main_list.items():
        print(f"{i}:{j}")

    while True:
        try:
            main_choice=int(input("select the main catgeory:"))
            if main_choice in main_list:
                main_category=main_list[main_choice]
                sub_cats=sub_cat[main_choice]
                break
            else:
                print("invalid choice, if you can , try again")
        except ValueError:
            print("only numbers")
    time.sleep(2)
    print("════════════════════════════════════════")
    print("subcategories:")
    for i , j in sub_cats.items():
        print(f"{i}:{j}")
    print("════════════════════════════════════════")

    while True: 
        try:
            time.sleep(2)
            sub_choice=int(input("Enter your sub cat choice:"))
            if sub_choice in sub_cats:
                sub_category=sub_cats[sub_choice]
                break
            else:
                print("invalid choice, if you can , try again")
        except ValueError:
            print("only numbers")
    amount=0
    while True:
        try:
            amt=float(input(f"Enter the amount you spent on the  expenses :"))
            if amt > 0:
                amount=amt
                break
            else:
                print("amount should be more than zero")
        except ValueError:
            print("amount should not be negative and should have only numbers")

    descript=input("Enter the description about the expense:")
    
    a=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamp=a

    auto_expense={
        "MAIN CATEGORY":main_category,
        "SUB CATEGORY":sub_category,
        "DATE":date,
        "AMOUNT":amount,
        "DESCRIPTION":descript,
        "TIMESTAMP":timestamp
    }
    print("wait a moment")
    time.sleep(2)
    printing_exp(auto_expense)
    return auto_expense


def choice_of_exp(details):
    
    print("━━ ━━ ━━ ━━ ━━ ━━ ━━━━ ━━ ━━ ━━ ━━ ━━ ━━")
    print("we have two type of exp tracker.\nFirst you can enter the category manually.\nSecond you can choose the category from the list.\nThank you.")
    print("━━ ━━ ━━ ━━ ━━ ━━ ━━━━ ━━ ━━ ━━ ━━ ━━ ━━")
    choices={
        1:"Manual Expense Tracker",
        2:"Auto Expense Tracker",
        0:"EXIT"
    }
    expenses=[]
    while True:
        time.sleep(2)
        print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
        print("1.Manual Expense Tracker ,\n2.Auto Expense Tracker,\n0.finish or exit")
        user=int(input("Enter the choice:"))
        if user ==0:
            print("OK thank you")
            break
        if user in choices:
            time.sleep(2)
            print(f"You have selected the {choices.get(user)}")
            if user==1:
                expenses.append(manual_exp(details))
            elif user==2:
                expenses.append(auto_exp(details))
           
        else:
            print("you have selected wrong input")
    time.sleep(2)
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    for idx,exp in enumerate(expenses,start=1):
        print(f"the expenses are {idx}:")
        for i , j in exp.items():
            print(f"{i}:{j}")
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    return expenses


def filter_sum(expenses):
    import datetime
    if not expenses:
        print("no expenses found")
        return
    time.sleep(2)
    print("here we can use filtering in two ways.\n1.single date \n2.multiple dates")
    choice=input("Enter your choice")
    filtering=[]
    total_sum=0

    if choice=="1":
        time.sleep(2)
        date_str=input("Enter the date in 🟢year, 🔵month, 🔴date format:")
        date_str="-".join(date_str.split(","))
        for exp in expenses:
            expense_date=exp.get("DATE")
            if expense_date == date_str:
                filtering.append(exp)
                total_sum+=exp.get("AMOUNT",0)
        if not filtering:
            print("NO more expenses found")
            return
        print(f"Expenses on the date{date_str}")
    elif choice=="2":
        start_date_s=input("Enter the date start in 🟢year, 🔵month, 🔴date format :").strip()
        end_date_e=input("Enter the date end in 🟢year, 🔵month, 🔴date format:").strip()

        start_date="-".join(start_date_s.split(","))
        end_date="-".join(end_date_e.split(","))
        try:
            start_date_dt=datetime.datetime.strptime(start_date,"%Y-%m-%d")
            end_date_dt=datetime.datetime.strptime(end_date,"%Y-%m-%d")

            
        except ValueError:
            print("Invalid")
            return
        for exp in expenses:
            expense_date=exp.get("DATE")
            exp_date=datetime.datetime.strptime(expense_date,"%Y-%m-%d")
            if start_date_dt<=exp_date<=end_date_dt:
                filtering.append(exp)
                total_sum+=exp.get("AMOUNT",0)
        if not filtering:
            print("no exp found")
            return
            
        time.sleep(2)
        print(f"expenses from {start_date} to {end_date} is :")
    else:
        print("invalid choice")
        return
    time.sleep(2)
    print("=====================================")
    for i, j in enumerate(filtering,start=1):
        print(f"Expenses of {i} is :")
        for m ,n in j.items():
            print(f"{m}:{n}")
    print(f"total expenses are :{total_sum}")
    print("=====================================")



    
greet()
details=user_details()
expenses=choice_of_exp(details)
filter_sum(expenses)
   