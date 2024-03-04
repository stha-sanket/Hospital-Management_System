
#! Importing class and libraries
 #? to import admin
from Admin import Admin 
#? to importing the tkinter for GUI as tk btw
import tkinter as tk  
#? for messagebox from tkinter
from tkinter import messagebox  

def main():
    """
    The main function to be executed when the program runs.
    """
    #* Creating the main window for the login screen

    root = tk.Tk() #? using tinker constructor
    root.geometry('330x250')  #? to define dimension of main screen for login purpose
    root.configure(bg='limegreen')

    #* Creating and configuring the label for 'Login'

    label = tk.Label(root, text='Login', bg= 'white', fg='#333333')
    label.config(font=('Arial', 24, 'bold'))
    label.pack(pady=10)

    #* Creating label and input field for username

    user_name_lb = tk.Label(root, text='Enter username', bg='white', fg='#333333')
    user_name_lb.pack()

    user_name_input = tk.Entry(root)
    user_name_input.pack(pady=(0, 10))

    #* Creating label and input field for password

    password_lb = tk.Label(root, text='Enter password', bg='white', fg='#333333')
    password_lb.pack(pady=(30, 0))

    password_input = tk.Entry(root, show='*')
    password_input.pack(pady=(0, 10))

    #* login button

    def login():
        #? getting username and password entered by the user
        username = user_name_input.get()
        password = password_input.get()

        #? checking wheather both username and password are entered
        #! username and password cannot be empty
        if len(username) == 0 and len(password) == 0:
            #* shows error message if fields are empty
            messagebox.showerror('Error', 'Please enter username and password')

        else:
            #! checking wheather the entered username and password is correct or not
            if username == 'admin' and password == '123':
                #* display successfully login
                messagebox.showinfo('Success', 'Login Successful')
                #* end the login window
                root.destroy()  
                #* opening admin class
                Admin().home_window()  

            else:
                #* display error if incorrect
                messagebox.showerror('Error', 'Incorrect username or password')

    #* login button
    login_btn = tk.Button(root, text='Log In',bg='white',fg='black', command=login)
    login_btn.pack(pady=10)
    #* running the Tkinter in loop
    root.mainloop()
if __name__ == '__main__':
    main()
