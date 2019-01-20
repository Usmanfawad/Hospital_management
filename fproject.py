from tkinter import*
import datetime
from tkinter import messagebox


def appointment_screen():
    doctors_dict = {"Dr Ali Khan": "ENT",
                   "Dr Mehmood Khan": "Regular Checkup",
                   "Dr Summera Kulsoom": "Dentist",
                   "Dr Mohammad Mustafa": "Neurologist"
                   }
    docs_list= list(doctors_dict.keys())
    docs_list_specialty= list(doctors_dict.values())
    def search_patient():
        if patient_id.get()=='':
            messagebox.showinfo('Warning', 'Please fill all the entries')
        else:

            patient_file = open('patient.txt','r')
            txt = patient_file.readlines()
            patient_file.close()

            patient_id_info = patient_id.get()
            found = 0
            for each_line in range(len(txt)):
                splitted_line = txt[each_line].split(' ')
                if patient_id_info+'\n' in splitted_line:
                    first_name = Label(screen3, text=txt[each_line+1],bg="white",width="20")
                    first_name.place(x=175,y=230)
                    middle_name= Label(screen3, text=txt[each_line+2],bg="white",width="20")
                    middle_name.place(x=175,y=260)
                    last_name  = Label(screen3, text=txt[each_line+3],bg="white",width="20")
                    last_name.place(x=175,y=290)
                    age        = Label(screen3, text=txt[each_line+4],bg="white",width="20")
                    age.place(x=175,y=320)
                    found +=1

            if found == 0 :
                not_available = Label(screen3, text="Patient not available! ",fg="white",bg="red")
                not_available.place( y=550)



        def clear_screen111():
            not_available.destroy()
            first_name.destroy()
            middle_name.destroy()
            last_name.destroy()
            age.destroy()


    screen3=Tk()
    screen3.geometry("500x600")
    screen3.title("Appointment")
    heading= Label(screen3,text="Appointment",bg="black",fg="white",font=("Lucida Console",12),width="300",height="3")
    heading.pack()
    patient_info_heading= Label(screen3,text="Patient Information",bg="grey",width="71")
    patient_info_heading.place(y=200)

    patient_id=StringVar()
    pat_id= Label(screen3,text="Patient ID* ",bg="grey",fg="black",width="500",font="arial")
    pat_id.pack()
    pat_id_label= Label(screen3,text="Enter Patient ID")
    pat_id_label.place(x=100,y=100)
    pat_id_box=Entry(screen3,textvariable= patient_id,width="15")
    pat_id_box.place(x=200,y=100)

    choose_dr_label= Label(screen3,text="Choose Doctor")
    choose_dr_label.place(x=100,y=140)

    search_but = Button(screen3,text="Search",width=10,height=1,command = search_patient)
    search_but.place(x=360,y=98)

    var=StringVar(screen3)
    option = OptionMenu(screen3, var, *docs_list)
    option.place(x=195,y=130)
    def back_to_main_1():
        screen3.destroy()
        main_menu_screen()

    back_to_main1= Button(screen3,text="Back to Main Menu",width="20",height="3",command=back_to_main_1)
    back_to_main1.place(x=185,y=535)

    def confirm_appointment():
        x=var.get()
        details= Label(screen3,text=("Doctor's Name:-"+str(x)),fg="black")
        details.place(x=160,y=390)
        now=datetime.datetime.now()
        date_label=Label(screen3,text=("Date- "+now.strftime("%Y-%m-%d")))
        date_label.place(x=160,y=410)
        day_label=Label(screen3,text=("Day- "+now.strftime("%H:%M")))
        day_label.place(x=160,y=430)


    confirm_appointment_button=Button(screen3,text="Confirm Appointment",width="20",height="3",command=confirm_appointment)
    confirm_appointment_button.place(x=340,y=535)


    def dr_get():
        print("The docter chosen is: "+str(var.get()))

    ok_button= Button(screen3,text="Confirm",width=10,command=dr_get)
    ok_button.place(x=360,y=133)


    app_details=Label(screen3,text="Appointment Details",width='70',bg="grey")
    app_details.place(y=360)
    screen3.mainloop()


def main_menu_screen():

    screen= Tk()

    screen.geometry("300x300")
    screen.title("Main Menu")

    heading= Label(screen,text="MAIN MENU",bg="black",fg="white",width="300",height="3",font=("Lucida Console",12))
    heading.pack()

    def leftClick(event):
        screen.destroy()
        pat_reg()


    addpat_button=Button(screen, text="Register New Patient", width="100", height="3",font=("Lucida Console",12))
    addpat_button.pack()
    addpat_button.bind('<Button-1>',leftClick)

    def leftClick2(event):
        screen.destroy()
        appointment_screen()


    apppat_button=Button(screen,text="Book An Appointment", width="100",height="3",font=("Lucida Console",12))
    apppat_button.pack()
    apppat_button.bind('<Button-1>',leftClick2)


    def close_main():
        screen.destroy()

    quit_button= Button(screen,text="QUIT",bg="black",fg="white",command=close_main)
    quit_button.place(x=255,y=270)
    screen.mainloop()


def pat_reg():
    def save_info(firstname,middlename,lastname,age):
        if firstname.get() == '' or lastname.get() == '' or age.get() == '':
            messagebox.showinfo('Warning','Please fill all the entries')
        else:
            counter = 0
            firstname_info = firstname.get()
            lastname_info = lastname.get()
            age_info = age.get()
            age_info = str(age_info)
            mname_info = middlename.get()
            file = open("patient.txt", "r")
            txt = file.readlines()
            file.close()

            if txt == []:

                patient_info = 'Patient_ID: '+str(counter)+'\nF.Name: ' + firstname_info + '\nM.Name: ' + mname_info + '\nL.Name: ' + lastname_info + '\nAge: ' + age_info + '\n\n'
                txt.append(patient_info)
            else:
                num_list = txt[-6].split(' ')
                counter = num_list[1][0:-1]

                print("User ID: "+str(int(counter)+1))
                patient_info = 'Patient_ID: ' + str(int(counter)+1) + '\nF.Name: ' + firstname_info + '\nM.Name: ' + mname_info + '\nL.Name: ' + lastname_info + '\nAge: ' + age_info + '\n\n'
                txt.append(patient_info)


            file_w = open("patient.txt", "w")
            file_w.writelines(txt)
            file_w.close()
            print("User:", firstname_info.title(), " has been registered successfully.")

            firstname_entry.delete(0, END)
            lastname_entry.delete(0, END)
            age_entry.delete(0, END)
            mname_entry.delete(0, END)


    screen1 = Tk()
    screen1.geometry("500x500")
    screen1.title("HOSPITAL MANAGEMENT")
    heading = Label(screen1,text="HOSPITAL MANAGEMENT", bg="black",fg="white", width="500", height="3", font=("Lucida Console",12))
    heading.pack()

    firstname_text = Label(screen1,text="First Name")
    lastname_text = Label(screen1,text="Last Name *" )
    age_text = Label(screen1,text="Age *")
    middlename_text = Label(screen1,text="Middle Name ", )

    firstname_text.place(x=100, y=70)
    lastname_text.place(x=100, y=210)
    age_text.place(x=100, y=280)
    middlename_text.place(x=100,y=140)


    firstname = StringVar()
    lastname = StringVar()
    age = IntVar()
    middlename= StringVar()

    firstname_entry = Entry(screen1,textvariable =firstname, width="30")
    lastname_entry = Entry(screen1,textvariable =lastname, width="30")
    age_entry = Entry(screen1,textvariable= age, width="15")
    mname_entry = Entry(screen1,textvariable =middlename, width="30")

    firstname_entry.place(x=100, y=100)
    lastname_entry.place(x=100, y=240)
    age_entry.place(x=100, y=310)
    mname_entry.place(x=100,y=170)
    def leftClick(event):
        save_info(firstname,middlename,lastname,age)

    def back_main(event):
        screen1.destroy()
        main_menu_screen()

    register = Button(screen1, text="Register", width="20", height="3")
    register.bind('<Button-1>', leftClick)
    register.place(x=335, y=430)
    back_to_main= Button(screen1,text="Back to Main Menu",width="20",height="3")
    back_to_main.bind('<Button-1>',back_main)
    back_to_main.place(x=180,y=430)

    print(firstname.get())
    screen1.mainloop()




def patient_reg():
    main_menu_screen()

patient_reg()








