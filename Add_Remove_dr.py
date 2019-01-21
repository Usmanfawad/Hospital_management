from tkinter import *
from tkinter import messagebox

doctor_screen=Tk()
doctor_screen.geometry("300x600")

def add_doc_txt():
    if doc_name_entry.get()=='' or doc_last_name_entry.get()=='' or cnic_entry.get()=='':
        messagebox.showinfo('Warning', 'Please fill all the entries')
    else:
        counter = 0
        doc_fname_info= doc_name_entry.get()
        doc_lname_info=doc_last_name_entry.get()
        cnic_info=cnic_entry.get()
        file = open("doctor.txt", "r")
        txt = file.readlines()
        file.close()
        if txt == []:

            doc_info = 'Doctor_ID: ' + str(counter) + '\nF.Name: ' + doc_fname_info + '\nL.Name: ' + doc_lname_info + '\nCNIC#: '+cnic_info + '\n\n'
            txt.append(doc_info)
        else:
            numb_list = txt[-5].split(' ')
            counter = numb_list[1][0:-1]

            print("DR ID: " + str(int(counter)+1))
            doc_info= 'DR ID: ' + str(int(counter)+1) + '\nF.Name: ' + doc_fname_info + '\nL.Name: ' + doc_lname_info+'\nCNIC#: '+cnic_info +'\n\n'
            txt.append(doc_info)

        file_w = open("doctor.txt", "w")
        file_w.writelines(txt)
        file_w.close()
        print("Doctor:", doc_fname_info.title(), " has been registered successfully.")

        doc_name_entry.delete(0, END)
        doc_last_name_entry.delete(0, END)
        cnic_entry.delete(0, END)

doc_id = IntVar()
doc_fname=StringVar()
doc_lname=StringVar()
doc_cnic=IntVar()

screen_heading=Label(doctor_screen,text="Update Doctor",bg="black",fg="white",width=300,height=3,font=("Lucida console",12))
screen_heading.pack()

doc_name=Label(doctor_screen,text="First Name")
doc_last_name=Label(doctor_screen,text="Last Name")
doc_cnic_=Label(doctor_screen,text="CNIC#")
doc_name.place(x=30,y=70)
doc_last_name.place(x=30,y=125)
doc_cnic_.place(x=30,y=180)

doc_name_entry=Entry(doctor_screen,textvariable=doc_fname)
doc_last_name_entry=Entry(doctor_screen,textvariable=doc_lname)
cnic_entry=Entry(doctor_screen,textvariable=doc_cnic)
doc_name_entry.place(x=30,y=95)
doc_last_name_entry.place(x=30,y=150)
cnic_entry.place(x=30,y=205)



confirm_button_add_dr= Button(doctor_screen,text="Confirm",command=add_doc_txt)
confirm_button_add_dr.place(x=30,y=240)

remove_patient_header= Label(doctor_screen,text="Remove Doctor",width=30,height='3',bg="black",fg="white",font=("Lucida Console",12))
remove_patient_header.place(y=290)

dr_id_=IntVar()
dr_id=Label(doctor_screen,text="ID")
dr_id.place(x=30,y=360)
dr_id_entry= Entry(doctor_screen,textvariable=dr_id_)
dr_id_entry.place(x=30,y=385)
dr_removebutton= Button(doctor_screen,text="Remove")
dr_removebutton.place(x=30,y=420)



doctor_screen.mainloop()
