import time
import pyttsx3
import random
suplier_dic = {"kamal": "1234", "anu": "0011"
               }
suplier_dic_phone = [7864662693, 98879869,
                     ]
client_dic = {"rihan": {"name": "rihan", "amount": 500, "address": "kerala", "phone": 7853478, "password": 1234},
              "fathima": {"name": "fathima", "amount": 5000, "address": "kerala", "phone": 78897878, "password": 1234},
              "sakshi": {"name": "sakshi", "amount": 5678, "address": "nodia", "phone": 734547388, "password": 1234},
              "guru": {"name": "guru", "amount": 5678, "address": "Tamil nadu", "phone": 734547455, "password": 1234},
              "hari": {"name": "hari", "amount": 5788, "address": "Tamil nadu", "phone": 737687388, "password": 1234}}
def k():
    global engine
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 125)
k()
def say(a):
    engine.say(a)
    engine.runAndWait()
def client():
    try:
        while True:

            say("ENTER YOUR NAME")
            name = input(("ENTER YOUR NAME : "))
            say("ENTER YOUR PASSWORD")
            pass_word = int(input("ENTER YOUR PASSWORD : "))
            global items
            items = dict(client_dic.get((name)))
            pass_w = items.get("password")
            if pass_word == pass_w:

                while True:
                    print(f"----------------WELCOME {name.upper()} CLIENT---------------------")
                    print(
                        "------------------------------------- 1. VIEW YOUR DATA ------------------------------------------")
                    print(
                        "------------------------------------- 2. EDIT YOUR DATA ------------------------------------------")
                    print(
                        "------------------------------------- 3.   GO BACK  ----------------------------------------------")
                    say("ENTER YOUR CHOICE")
                    client_choice = input("ENTER YOUR CHOICE : ")
                    if client_choice == "1":
                        say("YOUR DATA IS ")
                        print("YOUR DATA IS ")

                        print(items, end="\n")
                        time.sleep(2)
                    elif client_choice == "2":
                        say("WHAT YOU WANT TO EDIT")
                        print("WHAT YOU WANT TO EDIT \n 1.NAME \n 2.AMOUNT \n 3.ADDRESS \n 4.PHONE \n 5.TO EXIT ")
                        say("ENTER YOUR CHOICE")
                        edit_choice = input(" : ")
                        if edit_choice == "1":
                            name = input("ENTER YOUR NAME TO EDIT: ")
                            items.update(({"name": name}))
                            print("DATA UPDATED ENTER 1 TO VIEW")
                        elif edit_choice == "2":
                            amount = input("ENTER YOUR AMOUNT TO EDIT: ")
                            items.update(({"amount": amount}))
                            print("DATA UPDATED ENTER 1 TO VIEW")
                        elif edit_choice == "3":
                            adrs = input("ENTER YOUR ADDRESS TO EDIT: ")
                            items.update(({"ADDRESS": adrs}))
                            print("DATA UPDATED ENTER 1 TO VIEW")
                        elif edit_choice == "4":
                            ph = input("ENTER YOUR PHONE TO EDIT: ")
                            items.update(({"phone": ph}))
                            print("DATA UPDATED ENTER 1 TO VIEW")
                        elif edit_choice == 5:
                            break

                        else:
                            say("NO DATA FOUND")
                            print()
                            break

                    elif client_choice == "3":
                        break
            print("ENTER 1 TO CONTINUE OR 0 TO EXIT ")
            exter_or_exit = int(input(":>"))
            if exter_or_exit == 0:
                break

    except:
        say("NO DATA FOUND")
        print("NO DATA FOUND")
def suplier():
    say("ENTER YOUR NAME")
    name = input("ENTER YOUR NAME : ")
    say("ENTER YOUR PASSWORD  ")
    password = input("ENTER YOUR PASSWORD : ")
    try:
        while True:
            if suplier_dic[name] == password:
                print()

                print(f"-----------------------WELCOME {name.upper()} (SUPPLIER)---------------------")
                print(
                    "----------------------------------------- 1. VIEW DATA ----------------------------------------------")
                print(
                    "----------------------------------------- 2. CRREATE NEW DATA ---------------------------------------")
                print(
                    '----------------------------------------- 3. EDIT DATAS ---------------------------------------------')
                print(
                    "----------------------------------------- 4. GO BACK ------------------------------------------------\n")
                say("ENTER YOUR CHOICE")
                input_choice = input("ENTER YOUR CHOICE:")
                if input_choice == "1":
                    say("YOUR CLIENT DATAS ARE")
                    print("YOUR CLIENT DATAS ARE : ")
                    for i in client_dic:
                        print(client_dic.get(i))
                        time.sleep(2)
                elif input_choice == "2":
                    say("ENTER THE CLIENT DETAILS")
                    print("ENTER THE CLIENT DETAILS")
                    nam = input("NAME : ")
                    amoun = int(input("AMOUNT : "))
                    addr = input("ADDRESS : ")
                    ph = int(input("PHONE : "))
                    passw = int(input("PASSWORD : "))
                    client_dic.update(
                        {nam: {"name": nam, "amount": amoun, "address": addr, "phone": ph, "password": passw}})
                    say("data updated")
                    print("DATA UPDATED")
                    print("ENTER CHOICE 1 TO VIEW IT")
                elif input_choice == "3":
                    say("ENTER THE NAME OF CLIENT TO CHANGE THE DATA")
                    get_name = input("ENTER THE NAME OF CLIENT TO CHANGE THE DATA : ")
                    items = client_dic.get(get_name)
                    if get_name == items["name"]:
                        while True:
                            say("WHAT YOU WANT TO EDIT ")
                            print("WHAT YOU WANT TO EDIT \n 1.NAME \n 2.AMOUNT \n 3.ADDRESS \n 4.PHONE \n 5.TO EXIT ")
                            say("ENTER YOUR CHOICE ")
                            edit_choice = input("ENTER YOUR CHOICE : ")
                            if edit_choice == "1":
                                name = input("ENTER YOUR NAME TO EDIT: ")
                                items.update(({"name": name}))
                                say("DATA UPDATED")
                                print("DATA UPDATED ENTER 1 TO VIEW\n")
                            elif edit_choice == "2":
                                amount = input("ENTER YOUR AMOUNT TO EDIT: ")
                                items.update(({"amount": amount}))
                                say("DATA UPDATED")
                                print("DATA UPDATED ENTER 1 TO VIEW\n")
                            elif edit_choice == "3":
                                adrs = input("ENTER YOUR ADDRESS TO EDIT: ")
                                items.update(({"ADDRESS": adrs}))
                                say("DATA UPDATED")
                                print("DATA UPDATED ENTER 1 TO VIEW")
                            elif edit_choice == "4":
                                ph = input("ENTER YOUR PHONE TO EDIT: ")
                                items.update(({"phone": ph}))
                                say("DATA UPDATED")
                                print("DATA UPDATED ENTER 1 TO VIEW\n")
                            elif edit_choice == "5":
                                break
                    else:
                        print("NO USER NAME FOUND")



                elif input_choice == "4":
                    break
            else:
                say("ENTER THE VALID OPTION \n")
                print("ENTER THE VALID OPTION \n")
    except:
        pass
        #say("ERROR OCCURRED")
        #print("ERROR OCCURRED")
def create_new_user():
    try:
        while True:
            print("-------------------------------- 1. FOR CLIENT   --------------------------------------------")
            print("-------------------------------- 2. FOR SUPPLIER --------------------------------------------")
            print("-------------------------------- 3. GO BACK      --------------------------------------------")
            say("ENTER CHOICE ")
            create_choice = input("ENTER CHOICE : ")
            if create_choice == "1":
                say("YOU CAN ALSO CONTACT OUR SUPPLIERS TOE CREATE CLIENT ACCOUNT OR ELSE ENTER 0 TO CREATE BY YOUR OWN ")
                print("YOU CAN ALSO CONTACT OUR SUPPLIERS TO CREATE CLIENT ACCOUNT ")
                c = input("OR ELSE ENTER 0 TO CREATE BY YOUR OWN : ")
                if c == "0":
                    print("--------------------------------- NEW SIGN-UP  ------------------------------------------")

                    print("------------      FOR CLIENT        ---------------")
                    say("ENTER THE YOUR DETAILS")
                    print("ENTER THE YOUR DETAILS")
                    nam = input("NAME : ")
                    amoun = int(input("AMOUNT : "))
                    addr = input("ADDRESS : ")
                    ph = int(input("PHONE : "))
                    passw = int(input("NEW PASSWORD (STRONG) : "))
                    client_dic.update(
                        {nam: {"name": nam, "amount": amoun, "address": addr, "phone": ph, "password": passw}})

                    say("WAIT FOR 5 SECONDS")
                    print("WAIT FOR 5 SECONDS ")

                    time.sleep(5)
                    say("DATA UPDATED")
                    print("DATA UPDATED")
                    say("GO BACK TO VIEW it")
                    print("GO BACK TO VIEW IT \n")
                    print("")
            elif create_choice == "2":
                print("--------------------------------- NEW SIGN-UP  ------------------------------------------")

                print("------------       FOR SUPPLIER       ---------------")
                say("ENTER THE FOLLOWING DETAILS CAREFULLY")
                print("-----------------ENTER THE FOLLOWING DETAILS CAREFULLY-----------------------------------")
                nam = input("NAME : ")
                email = (input("EMAIL : "))
                addr = input("ADDRESS : ")
                ph = int(input("PHONE : "))
                adhar = int(input("AADHAR FOR VERIFICATION : "))
                f_name = input("FATHER NAME : ")
                work_ex = input("WORK EXPERIENCE : ")
                say("WAIT FOR 15 SECONDS ")
                print("WAIT FOR 15 SECONDS ")
                time.sleep(15)
                pass_w = str(random.randint(1000, 9999))
                say("VERIFICATION DONE")
                print("VERIFICATION DONE ")
                say("YOUR CREDENTIALS")
                print(f"YOUR CREDENTIALS \n USER_NAME - {nam} \n PASSWORD - {pass_w}")
                suplier_dic.update({nam: pass_w})
                suplier_dic_phone.append(ph)
                print("PLEASE UPLOAD YOUR PHOTO IN OUR SITE WITH IN TWO DAYS FOR VERIFICATION")

            elif create_choice == "3":
                break
            else:
                say("ENTER THE VALID CHOICE")
                print("ENTER THE VALID CHOICE")
    except:
        say("PLEASE TRY AGAIN")
        print("PLEASE TRY AGAIN")
say("welcome")
while True:
    print("""
          --------------------------------------------------- WELCOME ------------------------------------------------------\n
          ---------------------------------------------------1. SUPPLIER ----------------------------------------------------
          ---------------------------------------------------2. CLIENT ------------------------------------------------------
          ---------------------------------------------------3. NEW USER ----------------------------------------------------
          ---------------------------------------------------4. HELP --------------------------------------------------------
          ---------------------------------------------------5. EXIT --------------------------------------------------------\n""")
    say(" ENTER YOUR OPTION  ")
    sup_or_cli = input(" ENTER YOUR OPTION : ")
    if sup_or_cli == "1":
        suplier()
    elif sup_or_cli == "2":
        client()
    elif sup_or_cli == "3":
        create_new_user()
    elif sup_or_cli == "4":
        say("CONTACT OUR SUPPLIERS")
        print("CONTACT OUR SUPPLIERS")
        k = suplier_dic.keys()

        for i in suplier_dic_phone:
            print(i)
    elif sup_or_cli == "5":
        say("THANK YOU ")
        print("THANK YOU ")
        break
    else:
        say("Please enter the correct choice ")
        print("Please enter the correct choice ><....")
