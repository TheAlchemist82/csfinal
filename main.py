## Medical database
import random
from prettytable import PrettyTable 
import time
import os
import datetime
import sys
patient_list = []
table1 = PrettyTable()
table2 = PrettyTable()
table3 = PrettyTable()
ptable = PrettyTable()

drugs = {
        "Paracetamol": 50,
        "Ibuprofen": 160,
        "Antihistamine": 150, 
        "Anti-inflamatory": 170,
        "Hydrocortisone": 300,
        "Antacid": 30,
        "Cough Syrup": 140,
        "Asprin": 230,
        "Painkillers": 400,
        "Anti-biotic Ointment": 200,
    }
medical_appliances = {
        "Bandages" : 40,
        "Capsules" : 10,
        "Inhalors": 220,
        "Injections": 340,
        "Suppositories": 80,
        "Cotton Swabs": 20,
        "Gauss Tape": 100,  
        "Gloves": 190,
        "Masks": 310,
    }
cafeteria = {
    "Cup Noodles" : 50,
    "Aaloo Patties": 5,
    "Coffee": 70,
    "Tea": 60,
    "Dal Kachori": 15,
    "Samosa": 20, 
    "Soft Drinks": 10, 
    "Kathi Rolls": 40,
    "Sandwich": 80,
}

serial_number = 1
table1.field_names = ["Serial Number","General Medical Appliances", "Price"]
for i in medical_appliances:
    table1.add_row([serial_number, i, medical_appliances[i]])
    serial_number += 1
    
serial_number = 1
table2.field_names = ["Serial Number","Medication", "Price"]
for k in drugs:
    table2.add_row([serial_number, k, drugs[k]])
    serial_number += 1

serial_number = 1
table3.field_names = ["Serial Number","Food Items", "Price"]
for r in cafeteria:
    table3.add_row([serial_number, r, cafeteria[r]])
    serial_number += 1

def value_stripper(gstring):
    global int_value
    str_value = ""
    for l in gstring:
        if l in "1234567890":
            str_value += l
    int_value = int(str_value)

def name_stripper(nstring):
    global actual_med_value
    med_value = ""
    for g in nstring.lower():
        if g in "abcdefghijklmnopqrstuvwxzy":
            med_value += g
    if table_1_indicator:
        actual_med_value = med_value[24::].capitalize()
    elif table_2_indicator:
        actual_med_value = med_value[10::].capitalize()
    elif table_3_indicator:
        actual_med_value = med_value[9::].capitalize()

def pharmacy():
    del_ans_ind = False
    med_order_ind = False
    cart = []
    prices = []
    global table_1_indicator
    global table_2_indicator
    global table_3_indicator
    total = 0
    print("PLEASE NOTE: All prescription drugs must be authorized before consulting professional before being sold to the customer\n")

    while True:
        ctable = PrettyTable()
        for row in cart:
            ctable.add_row([cart.index(row), row, prices[cart.index(row)]])
        ctable.field_names = ["Serial Number", "Item", "Prices"]
        if med_order_ind:
            os.system("clear")
            break
        table_selection = input("Which section would you like to access?\n(1) General Medical Appliances\n(2) Drugs\n(3) Cafeteria\n\nType 'Cart' to view cart.\nType 'Delete' to remove items.\nType 'Done' when ready to check out.\nType 'Back' to Main Menu.\n>>> ")
        if table_selection == "done":
            if total == 0:
                print("Your total is 0\n")
                continue
            else:
                if len(patient_list) == 0:
                    print("No patients exist in the database.\n")
                    continue
                else:
                    print(f"{ctable}\n")
                    ans = input(f"Your total ${total}\nAre you sure you want to check out? (y or n): ").lower()
                    if ans == "y":
                        checkout_patient = input("Enter the last name of the patient: ")
                        for person in range(len(patient_list)):
                            if (patient_list[person].get("l_name")).lower() == checkout_patient.lower():
                                print("Please wait...\n\n")
                                loading= "LOADING\n"
                                bar = "[==========]"
                                print(loading)
                                for c in bar:
                                    time.sleep(0.3)
                                    sys.stdout.write(c)
                                    sys.stdout.flush()
                                print(f"\nTotal was sent to patient")
                                patient_list[person]["bill"] += total
                                time.sleep(4)
                            else:
                                print("No such patient exists in the database.")
                                break
                        os.system("clear")
                        del_answer_ind = True
                        med_order_ind = True
                        break
                    elif ans == "n":
                        os.system("clear")
                        continue

        elif (table_selection) == "1":
            os.system("clear")
            print(table1)
            table_1_indicator = True
            table_2_indicator = False
            table_3_indicator = False

        elif (table_selection)== "2":
            os.system("clear")
            print(table2)
            table_2_indicator = True
            table_1_indicator = False
            table_3_indicator = False

        elif (table_selection) == "3":
            os.system("clear")
            print(table3)
            table_1_indicator = False
            table_2_indicator = False
            table_3_indicator = True

        elif table_selection == "cart":
            print(ctable)
            print(f"Total: ${total}\n")
            continue
        elif table_selection == "delete": 
                while True:
                    os.system("clear")
                    print(ctable)
                    print(f"Total: ${total}\n")
                    del_ans = input("Which item would you like to delete: ")
                    if del_ans == "done":
                        del_ans_ind = True
                        break
                    elif del_ans in "1234567890":
                        ctable.del_row(int(del_ans))
                        print(f"{cart[int(del_ans)]} was removed from the total.\n")
                        total -= prices.pop(int(del_ans))
                        del cart[int(del_ans)]
                    ctable.clear()
                    for row in cart:
                        ctable.add_row([cart.index(row), row, prices[cart.index(row)]])
        elif table_selection == "back":
            os.system("clear")
            break
        else:
            print("Please enter a valid option.\n")
            continue
        while True:
            if del_ans_ind:
                os.system("clear")
                break
            usr_input = (input("Press (0) to go back\nEnter Serial Number of desired item.\n>>> "))
            if not usr_input:
                print("Please enter a valid number.\n")
                continue
            elif usr_input in "1234567890":
                usr_input = int(usr_input)
                if usr_input == 0:
                    os.system("clear")
                    break
                elif table_1_indicator:
                    if usr_input > len(medical_appliances):
                        print("Please enter a value within range.\n")
                    else:  
                        part_price = table1.get_string(fields=["Price"], start=usr_input - 1, end=usr_input).strip()
                        part_name = table1.get_string(fields=["General Medical Appliances"], start=usr_input - 1, end=usr_input).strip()
                        value_stripper(part_price)
                        name_stripper(part_name)
                        if actual_med_value not in cart:
                                cart.append(actual_med_value)
                                prices.append(int_value)
                                print(f"{actual_med_value} added to cart.\n")
                        else:
                            print(f"{actual_med_value} is already in cart.\n")
                        total += int_value

                elif table_2_indicator:
                    if usr_input > len(drugs):
                        print("Please enter a value within range.\n")
                    else:
                        part_price = table2.get_string(fields=["Price"], start=usr_input - 1, end=usr_input).strip()
                        part_name = table2.get_string(fields=["Medication"], start=usr_input - 1, end=usr_input).strip()
                        value_stripper(part_price)
                        name_stripper(part_name)
                        if actual_med_value not in cart:
                            cart.append(actual_med_value)
                            prices.append(int_value)
                            print(f"{actual_med_value} added to cart.\n")
                        else:
                            print(f"{actual_med_value} is already in cart.\n")
                        total += int_value

                elif table_3_indicator:
                    if usr_input > len(cafeteria):
                        print("Please enter a value within range.\n")
                    else:
                        part_price = table3.get_string(fields=["Price"], start=usr_input - 1, end=usr_input).strip()
                        part_name = table3.get_string(fields=["Food Items"], start=usr_input - 1, end=usr_input).strip()
                        value_stripper(part_price)
                        name_stripper(part_name)
                        if actual_med_value not in cart:
                            cart.append(actual_med_value)
                            prices.append(int_value)
                            print(f"{actual_med_value} added to cart.\n")
                        else:
                            print(f"{actual_med_value} is already in cart.\n")
                        total += int_value
            else:
                print("Please enter a valid number.\n")
                continue

def register():
    f_name = str(input("Please enter the first name of the patient: ")).strip()
    l_name = str(input("Please enter the last name of the patient: ")).strip()
    age = str(input("Please enter an age for the patient: ")).strip()
    sex = str(input("Please enter the sex (M/F) of the patient: ")).strip()
    fathers_name = str(input("Please enter the father's name: ")).strip()
    mothers_name = str(input("Please enter the mother's name: ")).strip()
    bill = 0
    room_number = random.randint(0,300)
    print(f"Patient has been assigned room number {room_number}")
    print("Patients data has been registered!")
    ptable.field_names = ["Patient First Name","Patient Last Name", "Age", "Sex", "F-Name", "M-Name", "Room Number", "Bill"]
    ptable.add_row([f_name.capitalize(), l_name.capitalize(), age.capitalize(), sex.capitalize(), fathers_name.capitalize(), mothers_name.capitalize(), room_number, bill])
    print(ptable)
    time.sleep(2)
    os.system("clear")
    patient = dict(f_name = f_name, l_name = l_name,  age = age, sex = sex, fathers_name = fathers_name, mothers_name = mothers_name, room = room_number, bill = bill)
    patient_list.append(patient)
    #print(patient_list)

def appointment():
    departments = {
        "a": "Caridiology",
        "b": "Orthopedics",
        "c": "Dermatology",
        "d": "Neurology",
        "e": "General Surgery",
        "f": "Urology",
        "g": "Ophthalmology",
        "h": "Gynecology and Obstetrics",
        "i": "Pediatric Surgery",
        "j": "Oncology"
    }
    Doctor_names = ["Lubowitz", "Mitchell", "Hermann", "Kumar", "Gauss", "Euclid", "Godrick", "Cooper", "Bisen", "Rao", "Holmes", "Banner", "Banerjee", "Subramaniam", "Lee", "Nimoy", "Kido", "Ivanov"]
    def appointment_booker(appointment_input):
        patient_exists = False
        if len(patient_list) == 0:
            print("No patients currently registered.\n")
        else:
            app_patient = input("Enter the last name of the patient name: ")
            for person in range(len(patient_list)):
                if (patient_list[person].get("l_name")).lower() == app_patient.lower():
                    patient_exists = True
                else:
                    print("No such patient exists")
                    continue
                if patient_exists:
                    date_app = input(f"Current date: {datetime.date.today()}\n\nWhat date should your appointment be scheduled for? (YYYY/MM/DD): ").split("/")
                    year, month, day = year, month, day = [int(item) for item in date_app]
                    print("Please wait...\n\n")
                    loading= "LOADING\n"
                    bar = "[==========]"
                    print(loading)
                    for c in bar:
                        time.sleep(0.3)
                        sys.stdout.write(c)
                        sys.stdout.flush()
                    print(f"\nYour appointment for {departments.get(appointment_input)} has been confirmed for {datetime.date(year, month, day)}, with Dr. {Doctor_names[random.randint(0, len(Doctor_names))]}.\n")
                    time.sleep(4)
                    os.system("clear")

    while True:
        print("PLEASE NOTE: The patient for whom the appointment is being booked, must be registered in the databse. \nType 'back' to go back to the main menu.\n\nWhich department would you like to be connected to?: ")
        for key, value in departments.items():
            print(f"({key.upper()}) {value}")
        app_input = input(">>> ").lower()
        if app_input == "back":
            os.system("clear")
            break
        elif app_input in "abcdefghij":
            app_ans = input(f"Confirm your appointment for {departments.get(app_input)} (y or n)?: ")
            if app_ans == "y":
                appointment_booker(app_input)
                break
            elif app_ans == "n":
                break
            else:
                print("Please enter a valid option.\n")
        else: 
            print("Please enter a valid option.\n")
while True:
    print("     CISCO MEDICAL PERSONAL TERMINAL       \n")
    main_input = input("Please choose an option to be directed to the sub-menu:\n(A) Register new patient\n(B) Order Medication\n(C) Book Appointment\n(D) View Patient List\n(E) More Information\n\n>>> ").lower()
    os.system("clear")
    if main_input == "a":
        register()
    elif main_input == "b":
        pharmacy()
    elif main_input == "c":
        appointment()
    elif main_input == "d":
        if len(patient_list) == 0:
            print("There are currently no patients registered.\n")
        else:
            ptable.clear()
            ptable.field_names = ["Patient First Name","Patient Last Name", "Age", "Sex", "F-Name", "M-Name", "Room Number", "Bill"]
            for k in patient_list:
                ptable.add_row([k.get("f_name"), k.get("l_name"), k.get("age"), k.get("sex"), k.get("fathers_name"), k.get("mothers_name"), k.get("room"), k.get("bill")])
            print(ptable)
    elif main_input == "e":
        os.system("clear")
        print("The Cisco Personal Medical Terminal is a specialised software designed for new patients to be integrated into the Cisco Hospitals Ecosystem for an easy and comfortable treatment.\n")