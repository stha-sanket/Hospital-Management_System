import tkinter as tk
from tkinter import NO
from tkinter import ttk
from tkinter import messagebox


class Admin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hospital Management System")
        self.root.geometry("400x300")
        self.root.resizable(0, 0)
        self.__doctors = [['John','Smith','Internal Med.'], ['Jone','Smith','Pediatrics'], ['Jone','Carlos','Cardiology']]
        self.__discharged_patient = []

    def refresh_page(self):
        table = ttk.Treeview(self.root, columns=('Id', 'first', 'last', 'speciality'), )
        table.heading('Id', text='ID',)
        table.heading('first', text='First name')
        table.heading('last', text='Surname')
        table.heading('speciality', text='Speciality')
        
        table.column('#0', width=0, stretch=False)
        table.column('Id', width=80)  
        table.column('first', width=165) 
        table.column('last', width=165)  
        table.column('speciality', width=185)
        table.grid(row = 1, column=1, padx=(40, 50))

        for index, i in enumerate(self.__doctors):
            table.insert(parent='',index=index, values=(index+1, *i))

    def home_window(self):
        self.clear_window()
        self.root.geometry("400x300")
        label = tk.Label(self.root, text="Welcome to Hospital Management System", font=("Arial", 12))
        label.pack(pady=5)

        doctor_btn = tk.Button(self.root, text="Doctor", command=self.doctor_window)
        doctor_btn.pack(pady=5)

        patient_btn = tk.Button(self.root, text="Patient", command=self.patient_window)
        patient_btn.pack(pady=5)

        admin_btn = tk.Button(self.root, text="Admin", command=self.admin_window)
        admin_btn.pack(pady=5)

        management_btn = tk.Button(self.root, text='Management', command=self.management)
        management_btn.pack(pady=5)

        settings_btn = tk.Button(self.root, text="Settings", command=self.settings_window)
        settings_btn.pack(pady=5)

    def doctor_window(self):
        self.clear_window()
        self.root.geometry('800x400')
        self.create_home_button()
        label = tk.Label(self.root, text="Doctor Window", font=("Arial", 20))
        label.grid(row=0, column=1, padx=(10, 5))

        doc_frame = tk.Frame(self.root)
        table = ttk.Treeview(self.root, columns=('Id', 'first', 'last', 'speciality'), )
        table.heading('Id', text='ID',)
        table.heading('first', text='First name')
        table.heading('last', text='Surname')
        table.heading('speciality', text='Speciality')
        
        table.column('#0', width=0, stretch=False)
        table.column('Id', width=80)  
        table.column('first', width=165) 
        table.column('last', width=165)  
        table.column('speciality', width=185)
        table.grid(column=1, padx=(40, 50))

        for index, i in enumerate(self.__doctors):
            table.insert(parent='',index=index, values=(index+1, *i))
        
        def delete_doctor():
            root = tk.Tk()
            root.geometry('220x300')

            label = tk.Label(root, text='Delete Doctor')
            label.config(font=('Aerial', 12, 'bold'))
            label.pack(pady=(5, 10))

            new_doctor_name = tk.Label(root, text='Enter doctor id')
            new_doctor_name.pack(padx=(10, 0))

            doctor_id = tk.Entry(root)
            doctor_id.pack(pady=5)

            def confirm():
                if len(doctor_id.get()) == 0:
                    messagebox.showerror('Error', 'Enter Doctor id')

                else:
                    given_id = int(doctor_id.get()) - 1
                    if given_id in range(len(self.__doctors)):
                        del self.__doctors[given_id]
                        messagebox.showinfo('Deletion Successful', 'The doctor has been successfully deleted.')

                        root.destroy()
                    
                    else:
                        messagebox.showerror('Error', 'No Id with Doctor')


            confirm_btn = tk.Button(root, text='Delete', command=confirm)
            confirm_btn.pack(pady=10)

            root.mainloop()


        def update_doctor():
            root = tk.Tk()
            root.geometry('220x300')

            label = tk.Label(root, text='Update Doctor')
            label.config(font=('Aerial', 12, 'bold'))
            label.pack(pady=(5, 10))

            new_doctor_name = tk.Label(root, text='Enter doctor id')
            new_doctor_name.pack(padx=(10, 0))

            doctor_id = tk.Entry(root)
            doctor_id.pack(pady=5)

            def search():
                if len(doctor_id.get()) == 0:
                    messagebox.showerror('Error', 'Please provide the doctor ID.')

                else:
                    given_id = int(doctor_id.get()) - 1

                    if given_id in range(len(self.__doctors)):
                        confirm_btn.config(state='disabled')
                        first_name = tk.Entry(root)
                        first_name.insert(0, self.__doctors[given_id][0])
                        first_name.pack(pady=5)

                        surname = tk.Entry(root)
                        surname.insert(0, self.__doctors[given_id][1])
                        surname.pack(pady=5)

                        speciality = tk.Entry(root)
                        speciality.insert(0, self.__doctors[given_id][2])
                        speciality.pack(pady=5)

                        def confirm():
                            self.__doctors[given_id][0] = first_name.get()
                            self.__doctors[given_id][1] = surname.get()
                            self.__doctors[given_id][2] = speciality.get()

                            messagebox.showinfo('Update Successful', 'The information has been updated successfully.')

                            root.destroy()

                        update_btn = tk.Button(root, text='Confirm', command=confirm)
                        update_btn.pack(pady=5)
                        
                    else:
                        messagebox.showerror('Error', 'No doctor with this id')
                        root.destroy()

            confirm_btn = tk.Button(root, text='Search', command=search)
            confirm_btn.pack(pady=10)

            root.mainloop()

        def add_doctor():
            root = tk.Tk()
            root.geometry('220x300')

            label = tk.Label(root, text='Add Doctor')
            label.config(font=('Aerial', 12, 'bold'))
            label.pack(pady=(5, 10))

            new_doctor_name_lb = tk.Label(root, text='Enter First Name')
            new_doctor_name_lb.pack(padx=(10, 0))

            new_doctor_name = tk.Entry(root)
            new_doctor_name.pack(pady=(0, 5))

            new_doctor_surname_lb = tk.Label(root, text='Enter Surname')
            new_doctor_surname_lb.pack(padx=(10, 0))

            new_doctor_surname = tk.Entry(root)
            new_doctor_surname.pack(pady=(0, 5))

            new_doctor_speciality_lb = tk.Label(root, text='Enter Speciality')
            new_doctor_speciality_lb.pack(padx=(10, 0))

            new_doctor_speciality = tk.Entry(root)
            new_doctor_speciality.pack(pady=(0, 5))

            def confirm_registration():
                new_doctor_list = [new_doctor_name.get(), new_doctor_surname.get(), new_doctor_speciality.get()]
                self.__doctors.append(new_doctor_list)
                new_doctor_list = []

                messagebox.showinfo('Registration Successful', 'The doctor has been registered successfully.')
                root.destroy()

            register_btn = tk.Button(root, text='Register', command=confirm_registration)
            register_btn.pack(pady=20)
        
        delete = tk.Button(doc_frame, text='Delete', command=delete_doctor)
        delete.grid(row = 0, column=0, padx=30)

        update = tk.Button(doc_frame, text='Update', command=update_doctor)
        update.grid(row = 0, column=1)

        add = tk.Button(doc_frame, text='Add', command=add_doctor)
        add.grid(row=0, column=2, padx=30)

        refresh = tk.Button(self.root, text='Refresh', command=self.refresh_page)
        refresh.grid(row=6, column=1, padx=30)
        
        doc_frame.place(x=90, y=300)

    
    def read_file(self):
        patient_info = []
    
        with open('patient.txt', 'r') as file:
            for i in file.readlines():
                patient_info.append(i.strip().split())
        
        return patient_info


    def patient_window(self):
        self.clear_window()
        self.root.geometry('800x600')
        self.create_home_button()

        label = tk.Label(self.root, text="Patient", font=("Arial", 20))
        label.grid(row=0, column=1, padx=(20, 5))

        patient_frame = tk.Frame(self.root)

        table = ttk.Treeview(self.root, columns=('Id', 'first', 'last', 'doc_name', 'age', 'mobile', 'code'), )
        table.heading('Id', text='ID',)
        table.heading('first', text='First name')
        table.heading('last', text='Surname')
        table.heading('doc_name', text = 'Doctor\'s Name')
        table.heading('age', text='age')
        table.heading('mobile', text='Mobile')
        table.heading('code', text="Postal Code")
        
        table.column('#0', width=0, stretch=False)
        table.column('Id', width=40) 
        table.column('first', width=150) 
        table.column('last', width=150)
        table.column('doc_name', width=150)
        table.column('age', width=40)
        table.column('mobile', width=100)
        table.column('code', width=80)

        patient_symptoms = []

        patient_info = self.read_file()

        for index, i in enumerate(patient_info):
            patient_symptoms.append(i[7:])
            code = i[5] + ' ' + i[6]
            table.insert(parent='', index=index, values=(index+1, *i[:5], code))

        table.grid(row=1, column=1, padx=0)
        
        def view_symptoms():
            symptoms_frame = tk.Frame(self.root)

            symptoms_table = ttk.Treeview(symptoms_frame, columns=('Id', 'Symptoms'))

            symptoms_table.heading('Id', text='Patient Id')
            symptoms_table.heading('Symptoms', text='Symptoms')

            symptoms_table.column('#0', width=0, stretch=False)
            symptoms_table.column('Id', width=150)
            symptoms_table.column('Symptoms', width=500)

            print(patient_symptoms)
            for index, i in enumerate(patient_symptoms):
                symptoms_table.insert(parent='',index=index, values=(index+1, ', '.join(i)))

            symptoms_table.grid(row=0, column=0, padx=(50, 50))

            symptoms_frame.place(x=1, y=350)


        symptoms = tk.Button(patient_frame, text='View Symptoms', command=view_symptoms)
        symptoms.grid(row = 0, column=0, padx=30)


        patient_frame.place(x=90, y=300)

    def admin_window(self):
        self.clear_window()
        self.root.geometry('330x350')
        self.create_home_button()
        label = tk.Label(self.root, text="Admin Window", font=("Arial", 15))
        label.grid( row=0,column=1,pady=(0,50))

        def assign():
            root = tk.Tk()
            root.geometry('200x300')

            label = tk.Label(root, text='Assign Doctor')
            label.config(font=('Aerial', 12, 'bold'))
            label.pack()

            doctor_id_lb = tk.Label(root, text='Enter Doctor Id')
            doctor_id_lb.pack(pady=(30, 0))

            doctor_id = tk.Entry(root, )
            doctor_id.pack(pady=(0, 20))

            patient_id_lb = tk.Label(root, text='Enter Patient Id')
            patient_id_lb.pack()

            patient_id = tk.Entry(root, )
            patient_id.pack()

            def confirm_assign():
                if len(doctor_id.get()) == 0 and len(patient_id.get()) == 0:
                    messagebox.showerror('Error', 'Please provide the ID.')
                
                else:
                    patient_info = self.read_file()
                    doctorId = int(doctor_id.get()) - 1
                    patientId = int(patient_id.get()) - 1
                    if doctorId in range(len(self.__doctors)) and patientId in range(len(patient_info)):
                        doctor_name = self.__doctors[doctorId][0] + '_' + self.__doctors[doctorId][1]
                        patient_info[patientId][2] = doctor_name
                        
                        with open('patient.txt', 'w') as file:
                            for i in patient_info:
                                file.write(' '.join(i) + '\n')
                        
                        messagebox.showinfo('Success', 'Doctor successfully assigned.')

                        root.destroy()
                    
                    else:
                        messagebox.showerror('Errot', 'Enter valid id')


            assign_btn = tk.Button(root, text='Assign', command=confirm_assign)
            assign_btn.pack(pady=10)

            root.mainloop()

        assign_doctor = tk.Button(self.root, text='Assign Doctor', command=assign)
        assign_doctor.grid(row=1, column=0)

        def patient_discharge():
            root = tk.Tk()
            root.geometry('200x300')

            label = tk.Label(root, text='Discharge Patient')
            label.config(font=('Aerial', 12, 'bold'))
            label.pack()

            patient_id_lb = tk.Label(root, text='Enter Patient Id')
            patient_id_lb.pack(pady=(30, 0))

            patient_id_1 = tk.Entry(root)
            patient_id_1.pack(pady=(0, 20))

            
            def confirm_discharge():
                if len(patient_id_1.get()) == 0:
                    messagebox.showerror('Error', 'Please provide id')
                
                else:
                    try:
                        patient_id = int(patient_id_1.get()) - 1
                        patient_info = self.read_file()
                        if patient_id in range(len(patient_info)):
                            self.__discharged_patient.append(patient_info[patient_id])
                            del patient_info[patient_id]

                            with open('patient.txt', 'w') as file:
                                for i in patient_info:
                                    file.write(' '.join(i) + '\n')

                            messagebox.showinfo('Success', 'Patient discharge successful.')
                        
                        else:
                            messagebox.showerror('Error', 'No patient found with this id')
                    
                    except:
                        messagebox.showerror('Error', 'Please provide id ')


            discharge_btn = tk.Button(root, text='Discharge', command=confirm_discharge)
            discharge_btn.pack(pady=10)

            root.mainloop()

        discharge_patient = tk.Button(self.root, text='Discharge Patient', command=patient_discharge)
        discharge_patient.grid(pady=10)

        def view_discharge_patient():
            discharge_window = tk.Toplevel()
            discharge_window.geometry('650x300')
            discharge_fm = tk.Frame(discharge_window)  
            label = tk.Label(discharge_fm, text='Discharged Patient')
            label.config(font=('Arial', 14, 'bold'))
            label.grid(pady=(20, 10), column=0)  

            discharged_table = ttk.Treeview(discharge_fm, columns=('Id', 'first', 'last', 'doc_name', 'age', 'mobile', 'code'), )
            discharged_table.heading('Id', text='ID',)
            discharged_table.heading('first', text='First name')
            discharged_table.heading('last', text='Surname')
            discharged_table.heading('doc_name', text='Doctor\'s Name')
            discharged_table.heading('age', text='age')
            discharged_table.heading('mobile', text='Mobile')
            discharged_table.heading('code', text="Postal Code")
            discharged_table.column('#0', width=0, stretch=False)
            discharged_table.column('Id', width=40)

            discharged_table.column('first', width=100)  
            discharged_table.column('last', width=100)
            discharged_table.column('doc_name', width=150)
            discharged_table.column('age', width=40)
            discharged_table.column('mobile', width=100)
            discharged_table.column('code', width=80)

            for index, i in enumerate(self.__discharged_patient):
                code = i[5] + ' ' + i[6]
                discharged_table.insert(parent='', index=index, values=(index+1, *i[:5], code))

            discharged_table.grid(row=1, pady=(10, 20), padx=(20, 0))  
            discharge_fm.pack(fill=tk.BOTH, expand=True) 
        view_discharge = tk.Button(self.root, text='View Discharged Patient', command=view_discharge_patient)
        view_discharge.grid(padx=5,pady=10)



        def view_patient():
            root = tk.Tk()
            root.geometry('500x300')

            patient_details = self.read_file()
            family_names = set([patient[1] for patient in patient_details])

            for family_name in family_names:
                label = tk.Label(root, text=f'{family_name} Family')
                label.pack(pady=(10, 10))

                table = ttk.Treeview(root, columns=('Id', 'first', 'second', 'doctor_name', 'age', 'mobile', 'postcode'), height=len(patient_details))
                table.heading('Id', text='ID',)
                table.heading('first', text='First Name')
                table.heading('second', text='Surname')
                table.heading('doctor_name', text='Doctor\'s Full Name')
                table.heading('age', text='Age')
                table.heading('mobile', text='Mobile')
                table.heading('postcode', text='Postcode')

                table.column('#0', width=0, stretch=NO)
                table.column('Id', width=40)
                table.column('first', width=85)
                table.column('second', width=100)
                table.column('doctor_name', width=150)
                table.column('age', width=40)
                table.column('mobile', width=100)
                table.column('postcode', width=80)

                for index, patient in enumerate(patient_details):
                    if patient[1] == family_name:
                        table.insert(parent='', index=index, values=(index+1, *patient))

                table.pack(pady=5)

            root.mainloop()

        view_patient_by_family_name = tk.Button(self.root, text='ViewFamily', command=view_patient)
        view_patient_by_family_name.grid(padx=5,pady=10)

    
    def management(self):
        self.clear_window()
        self.root.geometry('800x400')
        self.create_home_button()

        label = tk.Label(self.root, text='Management Report', font=('Arial', 20))
        label.grid(row=0, column=0, padx=(250, 5), columnspan=4)

        total_doctor = len(self.__doctors)
        total_patient = len(self.read_file())

        total_doctor_lb = tk.Label(self.root, text=f'Total No of Doctor: {total_doctor}')
        total_doctor_lb.config(font=('Aerial', 12, 'bold'))
        total_doctor_lb.grid(row=1, column=2, pady=10, columnspan=2)

        total_patient_lb = tk.Label(self.root, text=f'Total No of Patient: {total_patient}')
        total_patient_lb.config(font=('Aerial', 12, 'bold'))
        total_patient_lb.grid(row=2, pady=10, column=2, columnspan=2)


    def settings_window(self):
        self.clear_window()
        self.root.geometry('800x300')
        self.create_home_button()
        label = tk.Label(self.root, text="Settings Window", font=("Arial", 20))
        label.grid(row=0, column=1, padx=(250, 5))

        setting_fm = tk.Frame(self.root, height=200)

        new_username_lb = tk.Label(setting_fm, text='Enter new username')
        new_username_lb.grid()

        new_username = tk.Entry(setting_fm)
        new_username.grid()

        new_password_lb = tk.Label(setting_fm, text='Enter new password')
        new_password_lb.grid()

        new_password = tk.Entry(setting_fm)
        new_password.grid()

        new_address_lb = tk.Label(setting_fm, text='Enter new address')
        new_address_lb.grid()

        new_address = tk.Entry(setting_fm)
        new_address.grid()

        def confirm_update():
            if len(new_username.get()) == 0 and len(new_password.get()) == 0 and len(new_address.get()) == 0:
                messagebox.showerror('Error', 'Fields shouldd not be empty')
            
            else:
                messagebox.showinfo('Success', 'Update successfull')

        update_btn = tk.Button(setting_fm, text='Update', command=confirm_update)
        update_btn.grid(pady=10)
    
        setting_fm.place(x=350, y=50)

    def create_home_button(self):
        home_btn = tk.Button(self.root, text="Home", command=self.home_window)
        home_btn.grid(row=0, column=0, padx=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
