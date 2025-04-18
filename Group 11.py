from sqlite3.dbapi2 import OperationalError
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
import sqlite3
import os

main = Tk()
main.title('Main Menu')
main.geometry('290x300')
main.iconbitmap("covid.ico")

           
# Sort Function
def treeview_sort_column(tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        try:
            l.sort(key=lambda t: int(t[0]), reverse=reverse)
        except ValueError:
            l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))

# Register User
def register():
    root = Tk()
    root.title('Registration')
    root.geometry("360x340")
    root.iconbitmap("covid.ico")

    #Database
    # Create a database or connect to one
    conn = sqlite3.connect('Register.db')

    # create cursor
    c = conn.cursor()

    # create table
    c.execute("""CREATE TABLE if not exists addresses(
            name text, 
            password text,
            id integer,
            phone_number integer,
            birth_date integer,
            age integer,
            postcode integer,
            address text,
            occupation text,
            disease text,
            rank integer,
            status text
            )""")

    # Create submit function for database
    def submit():
        # Create a database or connect to one
        conn = sqlite3.connect('Register.db')

        # create cursor
        c = conn.cursor()

        #Insert into table
        c.execute("INSERT INTO addresses VALUES (:name, :password, :id, :phone_number, :birth_date, :age, :postcode, :address, :occupation, :disease, :rank, :status)",
                {
                    'name': name.get(),
                    'password': password.get(),
                    'id': id.get(),
                    'phone_number': phone_number.get(),
                    'birth_date': birth_date.get(),
                    'age': age.get(),
                    'postcode': postcode.get(),
                    'address': address.get(),
                    'occupation': occupation.get(),
                    'disease': disease.get(),
                    'rank': rank.get(),
                    'status': status.get()
                })

        #commit changes
        conn.commit()

        # Close connection
        conn.close()

        #Clear the text boxes
        name.delete(0, END)
        password.delete(0, END)
        id.delete(0, END)
        phone_number.delete(0, END)
        birth_date.delete(0, END)
        age.delete(0, END)
        postcode.delete(0, END)
        address.delete(0, END)
        occupation.delete(0, END)
        disease.delete(0, END)
        rank.delete(0, END)
        status.delete(0, END)
        Label(root, text="Registration Successful", fg="saddle brown", font=("cambria", 10)).grid(columnspan=2)

    # Create text boxes
    name = Entry(root, width=30)
    name.grid(row=0, column=1, padx=20, pady=(10, 0))
    password = Entry(root, width=30, show='*')
    password.grid(row=1, column=1)
    id = Entry(root, width=30)
    id.grid(row=2, column=1)
    phone_number = Entry(root, width=30)
    phone_number.grid(row=3, column=1)
    birth_date = Entry(root, width=30)
    birth_date.grid(row=4, column=1)
    age = Entry(root, width=30)
    age.grid(row=5, column=1)
    postcode = Entry(root, width=30)
    postcode.grid(row=6, column=1)
    address = Entry(root, width=30)
    address.grid(row=7, column=1)
    occupation = Entry(root, width=30)
    occupation.grid(row=8, column=1)
    disease = Entry(root, width=30)
    disease.grid(row=9, column=1)
    rank = Entry(root, width=30, state=DISABLED, text='ADMIN')
    rank.grid(row=10, column=1)
    status = Entry(root, width=30, state=DISABLED, text='ADMIN')
    status.grid(row=11, column=1)


    # Create text box labels
    name_label = Label(root, text="Name :", fg="saddle brown", font=("Cambria", 10))
    name_label.grid(row=0, column=0, pady=(10, 0))
    password_label = Label(root, text="Password :", fg="saddle brown", font=("Cambria", 10))
    password_label.grid(row=1, column=0)
    id_label = Label(root, text="ID :", fg="saddle brown", font=("Cambria", 10))
    id_label.grid(row=2, column=0)
    phone_number_label = Label(root, text="Phone Number :", fg="saddle brown", font=("Cambria", 10))
    phone_number_label.grid(row=3, column=0)
    birth_date_label = Label(root, text="Birthdate (DD/MM/YY) :", fg="saddle brown", font=("Cambria", 10))
    birth_date_label.grid(row=4, column=0)
    age_label = Label(root, text="Age :", fg="saddle brown", font=("Cambria", 10))
    age_label.grid(row=5, column=0)
    postcode_label = Label(root, text="Postcode :", fg="saddle brown", font=("Cambria", 10))
    postcode_label.grid(row=6, column=0)
    address_label = Label(root, text="Address :", fg="saddle brown", font=("Cambria", 10))
    address_label.grid(row=7, column=0)
    occupation_label = Label(root, text="Occupation :", fg="saddle brown", font=("Cambria", 10))
    occupation_label.grid(row=8, column=0)
    disease_label = Label(root, text="Disease :", fg="saddle brown", font=("Cambria", 10))
    disease_label.grid(row=9, column=0)


    #Create Submit button
    submit_btn = Button(root, text="Register", command=submit ,bg="dark khaki", fg="saddle brown", font=("Cambria", 10))
    submit_btn.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    #commit changes
    conn.commit()

    # Close connection
    conn.close()

# Login User
def login():
    global login_screen
    login_screen = Toplevel(main)
    login_screen.title("User Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Fill in the details below to continue", width="300", height="2", bg="dark khaki", fg="saddle brown", font=("Cambria", 10)).pack()
    Label(login_screen, text="").pack()
    login_screen.iconbitmap("covid.ico")
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Name * ", fg="saddle brown", font=("Cambria", 10)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ",fg="saddle brown", font=("Cambria", 10)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify, bg="dark khaki",fg="saddle brown", font=("Cambria", 10)).pack()

# Login Admin
def admin_login():
    global login_screen
    login_screen = Toplevel(main)
    login_screen.title("Admin Login")
    login_screen.geometry("300x250")
    login_screen.iconbitmap("covid.ico")
    Label(login_screen, text="Please enter details below to login", width="300", height="2", bg="dark khaki", fg="saddle brown", font=("Cambria", 10)).pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Name * ",fg="saddle brown", font=("Cambria", 10)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ",fg="saddle brown", font=("Cambria", 10)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=20, height=1, command = admin_login_verify, bg="dark khaki", fg="saddle brown", font=("Cambria", 10)).pack()

# User Login Verify
def login_verify():
    # Create or Connect
    conn = sqlite3.connect('Register.db')
    # Create Cursor
    c = conn.cursor()
    # Query the database
    c.execute("SELECT * FROM addresses where name=? AND password=?"
                ,(username_verify.get(),password_verify.get()))
    row = c.fetchone()
    if row:
        messagebox.showinfo('Congrats', 'Login Successful')
        login_sucess()
    else:
        messagebox.showwarning('Error', ' Login Failed \n Name or Password Incorrect')

    #commit changes
    conn.commit()
    #close connection
    conn.close()

# Admin Login Verify
def admin_login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            admin_login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()

# User Menu
def login_sucess():
    # Create save Function
    def save():
        # Create or Connect
        conn = sqlite3.connect('Register.db')
        # Create Cursor
        c = conn.cursor()

        record_id = password_verify.get()
        c.execute("""UPDATE addresses SET
            name = :name,
            id = :id,
            phone_number = :phone_number,
            birth_date = :birth_date,
            age = :age,
            postcode = :postcode,
            address = :address,
            occupation = :occupation,
            disease = :disease,
            rank = :rank,
            status = :status
                
            WHERE password = :password""",
            {
            'name': name_update.get(),
            'id' : id_update.get(),
            'phone_number' : phone_number_update.get(),
            'birth_date' : birth_date_update.get(),
            'age' : age_update.get(),
            'postcode' : postcode_1_update.get(),
            'address' : address_update.get(),
            'occupation' : occupation_update.get(),
            'disease' : disease_update.get(),
            'rank' : rank_update.get(),
            'status' : status_update.get(),
            
            'password': record_id
            })

        #commit changes
        conn.commit()
        #close connection
        conn.close()

    # Create User Query Fuction
    def uquery1():
        global update
        update = Tk()
        update.title('User information')
        update.geometry('400x400')

        # Create or Connect
        conn = sqlite3.connect('Register.db')
        # Create Cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT * FROM addresses where name=? AND password=?"
                        ,(username_verify.get(),password_verify.get()))
        records = c.fetchall()
        
        # Create Global Variables for text box names
        global name_update
        global id_update
        global phone_number_update
        global birth_date_update
        global age_update
        global postcode_1_update
        global address_update
        global occupation_update
        global disease_update
        global rank_update
        global status_update

        #Create Text Box
        name_update = Entry(update, width=30)
        name_update.grid(row=0, column=1, padx=20, pady=(10, 0))
        id_update = Entry(update, width=30)
        id_update.grid(row=1, column=1)
        phone_number_update = Entry(update, width=30)
        phone_number_update.grid(row=2, column=1)
        birth_date_update = Entry(update, width=30)
        birth_date_update.grid(row=3, column=1)
        age_update = Entry(update, width=30)
        age_update.grid(row=4, column=1)
        postcode_1_update = Entry(update, width=30)
        postcode_1_update.grid(row=5, column=1)
        address_update = Entry(update, width=30)
        address_update.grid(row=6, column=1)
        occupation_update = Entry(update, width=30)
        occupation_update.grid(row=7, column=1)
        disease_update = Entry(update, width=30)
        disease_update.grid(row=8, column=1)
        rank_update = Entry(update, width=30)
        rank_update.grid(row=9, column=1)
        status_update = Entry(update, width=30)
        status_update.grid(row=10, column=1)
        oid_update = Entry(update, width=30,)
        oid_update.grid(row=11, column=1)

        # Create text Box Labels
        name_label = Label(update, text="Name :", fg="saddle brown", font=("Cambria", 10))
        name_label.grid(row=0, column=0, padx=20, pady=(10, 0))
        id_label = Label(update, text="ID :", fg="saddle brown", font=("Cambria", 10))
        id_label.grid(row=1, column=0)
        phone_number_label = Label(update, text="Phone Number :", fg="saddle brown", font=("Cambria", 10))
        phone_number_label.grid(row=2, column=0)
        birth_date_label = Label(update, text="Birthdate :", fg="saddle brown", font=("Cambria", 10))
        birth_date_label.grid(row=3, column=0)
        age_date_label = Label(update, text="Age :", fg="saddle brown", font=("Cambria", 10))
        age_date_label.grid(row=4, column=0)
        postcode_1_label = Label(update, text="Postcode :", fg="saddle brown", font=("Cambria", 10))
        postcode_1_label.grid(row=5, column=0)
        address_label = Label(update, text="Address :", fg="saddle brown", font=("Cambria", 10))
        address_label.grid(row=6, column=0)
        occupation_label = Label(update, text="Occupation :", fg="saddle brown", font=("Cambria", 10))
        occupation_label.grid(row=7, column=0)
        disease_label = Label(update, text="Disease :", fg="saddle brown", font=("Cambria", 10))
        disease_label.grid(row=8, column=0)
        rank_label = Label(update, text="Rank :", fg="saddle brown", font=("Cambria", 10))
        rank_label.grid(row=9, column=0)
        status_label = Label(update, text="Status :", fg="saddle brown", font=("Cambria", 10))
        status_label.grid(row=10, column=0)

        # Loop thru results
        for rec in records:
            name_update.insert(0, rec[0])
            id_update.insert(0, rec[2])
            phone_number_update.insert(0, rec[3])
            birth_date_update.insert(0, rec[4])
            age_update.insert(0, rec[5])
            postcode_1_update.insert(0, rec[6])
            address_update.insert(0, rec[7])
            occupation_update.insert(0, rec[8])
            disease_update.insert(0, rec[9])
            rank_update.insert(0, rec[10])
            status_update.insert(0, rec[11])

        # Create an Save Updated button
        save_btn=Button(update, text='Save records', command=save)
        save_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

        #commit changes
        conn.commit()
        #close connection
        conn.close()

    # Apointment Query Fuction
    def aquery1():
        top = Toplevel()
        top.title('Appointment List')
        top.iconbitmap("covid.ico")
        # Create or Connect
        conn = sqlite3.connect('Appointment.db')
        # Create Cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT *,oid FROM addresses")
        data = c.fetchall()

        columns = ('Center Name','Date','Time',"Users' Name",'ID','Phone Number','Age','Status','OID')
        my_tree = ttk.Treeview(top, columns=columns, show='headings')

        # Format our columns
        my_tree.column('#0', width=0, stretch=NO)
        my_tree.column('Center Name', anchor=W, width=120, minwidth=25)
        my_tree.column('Date', anchor=CENTER, width=120, minwidth=25)
        my_tree.column('Time', anchor=CENTER, width=120, minwidth=35)
        my_tree.column("Users' Name", anchor=CENTER, width=120, minwidth=25)
        my_tree.column('ID', anchor=CENTER, width=120, minwidth=25)
        my_tree.column('Phone Number', anchor=CENTER, width=80, minwidth=15)
        my_tree.column('Age', anchor=CENTER, width=80, minwidth=15)
        my_tree.column('Status', anchor=CENTER, width=80, minwidth=15)
        my_tree.column('OID', anchor=CENTER, width=80, minwidth=15)

        # Add Data
        count=0
        for record in data:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]))
            my_tree.grid(pady=20)
            count += 1

        # Sort Data
        for col in columns:
                my_tree.heading(col, text=col, command=lambda c=col: treeview_sort_column(my_tree, c, False))

        #commit changes
        conn.commit()
        #close connection
        conn.close()
 
    #ERROR
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("User Menu")
    login_success_screen.geometry("260x280")
    login_success_screen.iconbitmap("covid.ico")
    Label(login_success_screen, text="Welcome User", width=260, height=2, fg="saddle brown", bg="dark khaki", font=("Cambria", 12)).pack()    
    Button(login_success_screen, text="View User Info",height=3,width=30, command=uquery1, bg="dark khaki", fg="saddle brown", font=("Cambria", 10)).pack(padx=5, pady=5)
    Button(login_success_screen, text="Vaccination Appointment",height=3,width=30, command=aquery1, bg="dark khaki", fg="saddle brown", font=("Cambria", 10)).pack(padx=5, pady=5)
    Button(login_success_screen, text="Log Out",height=3,width=30, command=delete_login_success, bg="dark khaki", fg="saddle brown", font=("Cambria", 10)).pack(padx=5, pady=5)

# Admin Menu
def admin_login_sucess():

    # Create User Query Fuction
    def uquery():
        top = Toplevel()
        top.title('User List')
        top.iconbitmap("covid.ico")
        # Create or Connect
        conn = sqlite3.connect('Register.db')
        # Create Cursor
        c = conn.cursor()

        # Create treeview frame
        tree_frame = Frame(top, width=500)
        tree_frame.pack(pady=20)

        # Create Treeview Frame
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Query the database
        c.execute("SELECT *,oid FROM addresses")
        data = c.fetchall()

        columns = ('Name','ID','Phone Number','Birth Date','Age','Postcode','Address','Occupation','Disease','Rank','Status','OID')
        my_tree = ttk.Treeview(tree_frame, columns=columns, show='headings', yscrollcommand=tree_scroll.set)

        # Create save Function
        def save():
            # Create or Connect
            conn = sqlite3.connect('Register.db')
            # Create Cursor
            c = conn.cursor()

            record_id = oid.get()
            c.execute("""UPDATE addresses SET
                name = :name,
                id = :id,
                phone_number = :phone_number,
                birth_date = :birth_date,
                age = :age,
                postcode = :postcode,
                address = :address,
                occupation = :occupation,
                disease = :disease,
                rank = :rank,
                status = :status
                    
                WHERE oid = :oid""",
                {
                'name': name_update.get(),
                'id' : id_update.get(),
                'phone_number' : phone_number_update.get(),
                'birth_date' : birth_date_update.get(),
                'age' : age_update.get(),
                'postcode' : postcode_1_update.get(),
                'address' : address_update.get(),
                'occupation' : occupation_update.get(),
                'disease' : disease_update.get(),
                'rank' : rank_update.get(),
                'status' : status_update.get(),
                
                'oid': record_id
                })

            #commit changes
            conn.commit()
            #close connection
            conn.close()

        # Create edit Function
        def edit():
            try:
                global update
                update = Tk()
                update.title('Update User information')
                update.geometry('400x400')

                # Create or Connect
                conn = sqlite3.connect('Register.db')
                # Create Cursor
                c = conn.cursor()

                record_id = oid.get()
                # Query the database
                c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
                records = c.fetchall()
                
                # Create Global Variables for text box names
                global name_update
                global id_update
                global phone_number_update
                global birth_date_update
                global age_update
                global postcode_1_update
                global address_update
                global occupation_update
                global disease_update
                global rank_update
                global status_update

                #Create Text Box
                name_update = Entry(update, width=30)
                name_update.grid(row=0, column=1, padx=20, pady=(10, 0))
                id_update = Entry(update, width=30)
                id_update.grid(row=1, column=1)
                phone_number_update = Entry(update, width=30)
                phone_number_update.grid(row=2, column=1)
                birth_date_update = Entry(update, width=30)
                birth_date_update.grid(row=3, column=1)
                age_update = Entry(update, width=30)
                age_update.grid(row=4, column=1)
                postcode_1_update = Entry(update, width=30)
                postcode_1_update.grid(row=5, column=1)
                address_update = Entry(update, width=30)
                address_update.grid(row=6, column=1)
                occupation_update = Entry(update, width=30)
                occupation_update.grid(row=7, column=1)
                disease_update = Entry(update, width=30)
                disease_update.grid(row=8, column=1)
                rank_update = Entry(update, width=30)
                rank_update.grid(row=9, column=1)
                status_update = Entry(update, width=30)
                status_update.grid(row=10, column=1)

                # Create text Box Labels
                name_label = Label(update, text="Name :", fg="saddle brown", font=("Cambria", 10))
                name_label.grid(row=0, column=0, padx=20, pady=(10, 0))
                id_label = Label(update, text="ID :", fg="saddle brown", font=("Cambria", 10))
                id_label.grid(row=1, column=0)
                phone_number_label = Label(update, text="Phone Number :", fg="saddle brown", font=("Cambria", 10))
                phone_number_label.grid(row=2, column=0)
                birth_date_label = Label(update, text="Birthdate :", fg="saddle brown", font=("Cambria", 10))
                birth_date_label.grid(row=3, column=0)
                age_date_label = Label(update, text="Age :", fg="saddle brown", font=("Cambria", 10))
                age_date_label.grid(row=4, column=0)
                postcode_1_label = Label(update, text="Postcode :", fg="saddle brown", font=("Cambria", 10))
                postcode_1_label.grid(row=5, column=0)
                address_label = Label(update, text="Address :", fg="saddle brown", font=("Cambria", 10))
                address_label.grid(row=6, column=0)
                occupation_label = Label(update, text="Occupation :", fg="saddle brown", font=("Cambria", 10))
                occupation_label.grid(row=7, column=0)
                disease_label = Label(update, text="Disease :", fg="saddle brown", font=("Cambria", 10))
                disease_label.grid(row=8, column=0)
                rank_label = Label(update, text="Rank :", fg="saddle brown", font=("Cambria", 10))
                rank_label.grid(row=9, column=0)
                status_label = Label(update, text="Status :", fg="saddle brown", font=("Cambria", 10))
                status_label.grid(row=10, column=0)

                # Loop thru results
                for rec in records:
                    name_update.insert(0, rec[0])
                    id_update.insert(0, rec[2])
                    phone_number_update.insert(0, rec[3])
                    birth_date_update.insert(0, rec[4])
                    age_update.insert(0, rec[5])
                    postcode_1_update.insert(0, rec[6])
                    address_update.insert(0, rec[7])
                    occupation_update.insert(0, rec[8])
                    disease_update.insert(0, rec[9])
                    rank_update.insert(0, rec[10])
                    status_update.insert(0, rec[11])

                # Create an Save Updated button
                save_btn=Button(update, text='Save records', command=save)
                save_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

                #commit changes
                conn.commit()
                #close connection
                conn.close()
            except OperationalError:
                pass

        # Autofill
        def select_record(e):
            try:
                #clear entry box
                oid.delete(0, END)
                # Grab record number
                selected = my_tree.focus()
                # Grab record value
                values = my_tree.item(selected, 'values')
                # Output
                oid.insert(0, values[11])
            except IndexError:
                pass

        #Bind the treeview
        my_tree.bind("<ButtonRelease-1>", select_record, edit)

        #remove function
        def remove():
            try:
                x = my_tree.selection()[0]
                my_tree.delete(x)

                # Create or Connect
                conn = sqlite3.connect('Register.db')
                # Create Cursor
                c = conn.cursor()

                # Delete From Database
                c.execute("DELETE from addresses WHERE oid =" + oid.get())

                #commit changes
                conn.commit()
                #close connection
                conn.close()
            except IndexError:
                pass

        # Format our columns
        my_tree.column('#0', width=0, stretch=NO)
        my_tree.column('Name', anchor=W, width=120, minwidth=30)
        my_tree.column('ID', anchor=CENTER, width=80, minwidth=25)
        my_tree.column('Phone Number', anchor=CENTER, width=120, minwidth=15)
        my_tree.column('Birth Date', anchor=CENTER, width=120, minwidth=25)
        my_tree.column('Age', anchor=CENTER, width=40, minwidth=15)
        my_tree.column('Postcode', anchor=CENTER, width=100, minwidth=15)
        my_tree.column('Address', anchor=CENTER, width=120, minwidth=15)
        my_tree.column('OID', anchor=CENTER, width=40, minwidth=15)
        my_tree.column('Occupation', anchor=CENTER, width=120, minwidth=15)
        my_tree.column('Disease', anchor=CENTER, width=120, minwidth=15)
        my_tree.column('Rank', anchor=CENTER, width=40, minwidth=15)
        my_tree.column('Status', anchor=CENTER, width=100, minwidth=15)

        # Add Data
        count=0
        for record in data:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12]))
            my_tree.pack(pady=20)
            count += 1
            
        for col in columns:
                my_tree.heading(col, text=col, command=lambda c=col: treeview_sort_column(my_tree, c, False))
            
        # Delete
        oid_label = Label(top, text="Please Choose an OID from the list above:",fg="saddle brown", font=("Cambria", 10)).pack()
        oid = Entry(top, width=30, justify="center")
        oid.pack(pady=5)
        remove_one = Button(top, text="Remove Selected", bg="dark khaki", fg="saddle brown", font=("Cambria", 10), command=remove).pack(pady=5)
       
        # Add Menu
        my_menu = Menu(top)
        top.config(menu=my_menu)
        # Config menu
        my_menu.add_cascade(label="Update User Record", command=edit)

    # Create Place Query Fuction
    def pquery():
        global pvac
        pvac = Toplevel()
        pvac.title('Vaccine Center List')
        pvac.iconbitmap("covid.ico")


        # Create or Connect
        conn = sqlite3.connect('Vaccine_Center.db')
        # Create Cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT *,oid FROM addresses")
        data = c.fetchall()

        #commit changes
        conn.commit()
        #close connection
        conn.close()

        columns = ('Name','Postcode','Time','Date','Capacity Per Hour','OID')
        my_tree = ttk.Treeview(pvac, columns=columns, show='headings')

        # Create save Function
        def save():
            # Create or Connect
            conn = sqlite3.connect('Vaccine_Center.db')
            # Create Cursor
            c = conn.cursor()

            record_id = oid.get()
            c.execute("""UPDATE addresses SET
                center_name = :center,
                zipcode = :zipcode,
                time = :time,
                date = :date,
                capacity = :capacity

                WHERE oid = :oid""",
                {
                'center': c_name_update.get(),
                'zipcode' : zipcode_update.get(),
                'time' : time_update.get(),
                'date' : date_update.get(),
                'capacity' : capacity_update.get(),

                'oid': record_id
                })

            #commit changes
            conn.commit()
            #close connection
            conn.close()

        # Create Update Function
        def update():
            try:
                global update
                update = Tk()
                update.title('Update Place information')
                update.geometry('400x200')

                # Create or Connect
                conn = sqlite3.connect('Vaccine_Center.db')
                # Create Cursor
                c = conn.cursor()

                record_id = oid.get()
                # Query the database
                c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
                records = c.fetchall()
                
                # Create Global Variables for text box names
                global c_name_update
                global zipcode_update
                global time_update
                global date_update
                global capacity_update

                #Create Text Box
                c_name_update = Entry(update, width=30)
                c_name_update.grid(row=0, column=1, padx=20, pady=(10, 0))
                zipcode_update = Entry(update, width=30)
                zipcode_update.grid(row=1, column=1)
                time_update = Entry(update, width=30)
                time_update.grid(row=2, column=1)
                date_update = Entry(update, width=30)
                date_update.grid(row=3, column=1)
                capacity_update = Entry(update, width=30)
                capacity_update.grid(row=4, column=1)

                # Create text Box Labels
                c_name_label = Label(update, text="Center Name :",fg="saddle brown", font=("Cambria", 10)).grid(row=0, column=0, padx=20, pady=(10, 0))
                zipcode_label = Label(update, text="Postcode :",fg="saddle brown", font=("Cambria", 10)).grid(row=1, column=0)
                time_label = Label(update, text="Time :",fg="saddle brown", font=("Cambria", 10)).grid(row=2, column=0)
                date_label = Label(update, text="Date :",fg="saddle brown", font=("Cambria", 10)).grid(row=3, column=0)
                capacity_label = Label(update, text="Capacity Per Hour :",fg="saddle brown", font=("Cambria", 10)).grid(row=4, column=0)

                # Loop thru results
                for rec in records:
                    c_name_update.insert(0, rec[0])
                    zipcode_update.insert(0, rec[1])
                    time_update.insert(0, rec[2])
                    date_update.insert(0, rec[3])
                    capacity_update.insert(0, rec[4])

                # Create an Save Updated button
                save_btn=Button(update, text='Save records', command=save).grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

                #commit changes
                conn.commit()
                #close connection
                conn.close()
            except OperationalError:
                pass

        def select_record(e):
            try:
                #clear entry box
                oid.delete(0, END)
                # Grab record number
                select = my_tree.focus()
                # Grab record value
                values = my_tree.item(select, 'values')
                # Output
                oid.insert(0, values[5])
            except IndexError:
                pass

        #Bind the treeview
        my_tree.bind("<ButtonRelease-1>", select_record)

        #remove function
        def remove():
            try:
                x = my_tree.selection()[0]
                my_tree.delete(x)

                # Create or Connect
                conn = sqlite3.connect('Vaccine_Center.db')
                # Create Cursor
                c = conn.cursor()

                # Delete From Database
                c.execute("DELETE from addresses WHERE oid =" + oid.get())

                #commit changes
                conn.commit()
                #close connection
                conn.close()
            except IndexError:
                pass

        # Format our columns
        my_tree.column('#0', width=0, stretch=NO)
        my_tree.column('Name', anchor=W, width=120, minwidth=30)
        my_tree.column('Postcode', anchor=CENTER, width=120, minwidth=25)
        my_tree.column('Time', anchor=CENTER, width=120, minwidth=30)
        my_tree.column('Date', anchor=CENTER, width=120, minwidth=30)
        my_tree.column('Capacity Per Hour', anchor=CENTER, width=120, minwidth=30)
        my_tree.column('OID', anchor=CENTER, width=80, minwidth=15)

        # Add Data
        count=0
        for record in data:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]))
            my_tree.grid(pady=20)
            count += 1

        # Sort Data
        for col in columns:
                my_tree.heading(col, text=col, command=lambda c=col: treeview_sort_column(my_tree, c, False))

        # Delete
        oid_label = Label(pvac, text="Please choose an OID from the list above :",fg="saddle brown", font=("Cambria", 10)).grid()
        oid = Entry(pvac, width=30, justify="center")
        oid.grid(pady=5)
        remove_one = Button(pvac, text="Remove Selected", bg="dark khaki", fg="saddle brown", font=("Cambria", 10), command=remove).grid(pady=5)

        # Add Menu
        my_menu = Menu(pvac)
        pvac.config(menu=my_menu)
        # Config menu
        my_menu.add_cascade(label="Update Vaccine Center Records", command=update)

    # Define Vaccination Place
    def vaccination():
        vacc = Tk()
        vacc.title('Vaccination Center Menu')
        vacc.geometry('360x300')
        vacc.iconbitmap("covid.ico")

        # Create or Connect
        conn = sqlite3.connect('Vaccine_Center.db')
        # Create Cursor
        c = conn.cursor()

        # Create table
        c.execute(""" CREATE TABLE if not exists addresses (
                center_name text,
                zipcode integer,
                time text,
                date text,
                capacity integer
                )""")

        # Create Submit fuction
        def submit():
            # Create or Connect
            conn = sqlite3.connect('Vaccine_Center.db')
            # Create Cursor
            c = conn.cursor()

            # insert into Table
            c.execute("INSERT INTO addresses VALUES (:c_name, :zipcode, :time, :date, :capacity)",
                    {
                        'c_name':c_name.get(),
                        'zipcode':zipcode.get(),
                        'time':time.get(),
                        'date':date.get(),
                        'capacity':capacity.get()
                    })

            #commit changes
            conn.commit()
            #close connection
            conn.close()

            # Clear Textboxes
            c_name.delete(0, END)
            zipcode.delete(0, END)
            time.delete(0, END)
            date.delete(0, END)
            capacity.delete(0, END)

        #Create Text Box
        c_name = Entry(vacc, width=30)
        c_name.grid(row=0, column=1, padx=20, pady=(10, 0))
        zipcode = Entry(vacc, width=30)
        zipcode.grid(row=1, column=1)
        time = Entry(vacc, width=30)
        time.grid(row=2, column=1)
        date = Entry(vacc, width=30)
        date.grid(row=3, column=1)
        capacity = Entry(vacc, width=30)
        capacity.grid(row=4, column=1)

        # Create text Box Labels
        c_name_label = Label(vacc, text="Center Name :",fg="saddle brown", font=("Cambria", 10)).grid(row=0, column=0, padx=20, pady=(10, 0))
        zipcode_label = Label(vacc, text="Postcode :",fg="saddle brown", font=("Cambria", 10)).grid(row=1, column=0)
        time_label = Label(vacc, text="Time :",fg="saddle brown", font=("Cambria", 10)).grid(row=2, column=0)
        date_label = Label(vacc, text="Date :",fg="saddle brown", font=("Cambria", 10)).grid(row=3, column=0)
        capacity_label = Label(vacc, text="Capacity Per Hour :",fg="saddle brown", font=("Cambria", 10)).grid(row=4, column=0)

        # Create Submit Button
        submit_btn = Button(vacc, text="Add To Vaccine Center List", command=submit,width=2, bg="dark khaki", fg="saddle brown", font=("Cambria", 10)).grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=133)

        # Create a Place Query Button
        pquery_btn=Button(vacc, text='Show Vaccine Center List', command=pquery,width=2, bg="dark khaki", fg="saddle brown", font=("Cambria", 10)).grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=134)

        '''# Create an Update button
        edit_btn=Button(vacc, text='Update Vaccine Center List', command=update,width=2, bg="dark khaki", fg="saddle brown", font=("Cambria", 10)).grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=131)'''

        #commit changes
        conn.commit()
        #close connection
        conn.close()

        vacc.mainloop()

    # Define Assign Appointment
    def appointment():
        root = Tk()
        root.title('Assign Appointment Menu')
        root.geometry('400x400')
        root.iconbitmap("covid.ico")


        # Databases
        # Create or Connect
        conn = sqlite3.connect('Appointment.db')
        # Create Cursor
        c = conn.cursor()

        # Create table
        c.execute(""" CREATE TABLE if not exists addresses (
                center_name text,
                date text,
                time text,
                name text,
                id integer,
                phone_number integer,
                age integer,
                status text       
                )""")
        # Create Submit fuction
        def submit():
            # Create or Connect
            conn = sqlite3.connect('Appointment.db')
            # Create Cursor
            c = conn.cursor()

            # insert into Table
            c.execute("INSERT INTO addresses VALUES (:c_name, :date, :time, :name, :id, :number, :age, :status)",
                    {
                        'c_name':c_name.get(),
                        'date':date.get(),
                        'time':time.get(),
                        'name':name.get(),
                        'id':id.get(),
                        'number':number.get(),
                        'age':age.get(),
                        'status':status.get()
                    })

            #commit changes
            conn.commit()
            #close connection
            conn.close()


            # Clear Textboxes
            c_name.delete(0, END)
            date.delete(0, END)
            time.delete(0, END)
            name.delete(0, END)
            id.delete(0, END)
            number.delete(0, END)
            age.delete(0, END)
            status.delete(0, END)
        # Apointment Query Fuction
        def aquery():
            top = Toplevel()
            top.title('Appointment List')
            top.iconbitmap("covid.ico")

            # Create or Connect
            conn = sqlite3.connect('Appointment.db')
            # Create Cursor
            c = conn.cursor()

            # Query the database
            c.execute("SELECT *,oid FROM addresses")
            data = c.fetchall()

            columns = ('Center Name','Date','Time',"Users' Name",'ID','Phone Number','Age','Status','OID')
            my_tree = ttk.Treeview(top, columns=columns, show='headings')

            def select_record(e):
                try:
                    #clear entry box
                    oid.delete(0, END)
                    # Grab record number
                    select = my_tree.focus()
                    # Grab record value
                    values = my_tree.item(select, 'values')
                    # Output
                    oid.insert(0, values[8])
                except IndexError:
                    pass

            #Bind the treeview
            my_tree.bind("<ButtonRelease-1>", select_record)

            #remove function
            def remove():
                try:
                    x = my_tree.selection()[0]
                    my_tree.delete(x)

                    # Create or Connect
                    conn = sqlite3.connect('Appointment.db')
                    # Create Cursor
                    c = conn.cursor()

                    # Delete From Database
                    c.execute("DELETE from addresses WHERE oid =" + oid.get())

                    #commit changes
                    conn.commit()
                    #close connection
                    conn.close()
                except IndexError:
                    pass
            
            # Csv function
            def write_to_csv(data):
                try:
                    fields = ['Center Name', 'Date', 'Time', "Users' Name", 'ID', 'Phone Number', 'Age', 'Status']
                    with open('Appointment.csv','a',newline='') as f:
                        w = csv.writer(f, dialect='excel')
                        w.writerow(fields)
                        w.writerows(data)
                except PermissionError:
                    pass
                
            # csv update
            def update_to_csv(data):
                try:
                    os.remove('Appointment.csv')
                    write_to_csv(data)
                except PermissionError:
                    pass
                
            # Format our columns
            my_tree.column('#0', width=0, stretch=NO)
            my_tree.column('Center Name', anchor=W, width=120, minwidth=25)
            my_tree.column('Date', anchor=CENTER, width=120, minwidth=25)
            my_tree.column('Time', anchor=CENTER, width=120, minwidth=35)
            my_tree.column("Users' Name", anchor=CENTER, width=120, minwidth=25)
            my_tree.column('ID', anchor=CENTER, width=120, minwidth=25)
            my_tree.column('Phone Number', anchor=CENTER, width=80, minwidth=15)
            my_tree.column('Age', anchor=CENTER, width=80, minwidth=15)
            my_tree.column('Status', anchor=CENTER, width=80, minwidth=15)
            my_tree.column('OID', anchor=CENTER, width=80, minwidth=15)

            # Add Data
            count=0
            for record in data:
                my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]))
                my_tree.grid(pady=20)
                count += 1

            # Sort Data
            for col in columns:
                    my_tree.heading(col, text=col, command=lambda c=col: treeview_sort_column(my_tree, c, False))

            # Delete
            oid_label = Label(top, text="Please choose an OID from the list above :",fg="saddle brown", font=("Cambria", 10)).grid()
            oid = Entry(top, width=30, justify="center")
            oid.grid(pady=5)
            remove_one = Button(top, text="Remove Selected", bg="dark khaki", fg="saddle brown", font=("Cambria", 10),width=8, command=remove).grid(pady=5, ipadx=20)
            # WARNING
            warn_label = Label(top, text="WARNING: 1) If Adding has been made, close the excel file before update. \n 2) If remove is done, Please close the Appointment List together with excel file. \n Open it back and then click update", fg="saddle brown", font=("Cambria", 10)).grid(pady=10)

            # Add Menu
            my_menu = Menu(top)
            top.config(menu=my_menu)
            # Config menu
            option_menu = Menu(my_menu, tearoff=0)
            my_menu.add_cascade(label="Options", menu=option_menu)
            # Drop down Menu
            option_menu.add_command(label="Save To Excel", command=lambda: write_to_csv(data))
            option_menu.add_separator()
            option_menu.add_command(label="Update To Excel", command=lambda: update_to_csv(data))

            #commit changes
            conn.commit()
            #close connection
            conn.close()
        

        #Create Text Box
        c_name = Entry(root, width=30)
        c_name.grid(row=0, column=1, padx=20, pady=(10, 0))
        date = Entry(root, width=30)
        date.grid(row=1, column=1)
        time = Entry(root, width=30)
        time.grid(row=2, column=1)
        name = Entry(root, width=30)
        name.grid(row=3, column=1)
        id = Entry(root, width=30)
        id.grid(row=4, column=1)
        number = Entry(root, width=30)
        number.grid(row=5, column=1)
        age = Entry(root, width=30)
        age.grid(row=6, column=1)
        status = Entry(root, width=30)
        status.grid(row=7, column=1)

        # Create text Box Labels
        c_name_label = Label(root, text="Center Name :",fg="saddle brown", font=("Cambria", 10)).grid(row=0, column=0, padx=20, pady=(10, 0))
        date_label = Label(root, text="Date :",fg="saddle brown", font=("Cambria", 10)).grid(row=1, column=0)
        time_label = Label(root, text="Time :",fg="saddle brown", font=("Cambria", 10)).grid(row=2, column=0)
        name_label = Label(root, text="Users Name :",fg="saddle brown", font=("Cambria", 10)).grid(row=3, column=0)
        id_label = Label(root, text="ID :",fg="saddle brown", font=("Cambria", 10)).grid(row=4, column=0)
        number_label = Label(root, text="Number :",fg="saddle brown", font=("Cambria", 10)).grid(row=5, column=0)
        age_label = Label(root, text="Age :",fg="saddle brown", font=("Cambria", 10)).grid(row=6, column=0)
        status_label = Label(root, text="Status :",fg="saddle brown", font=("Cambria", 10)).grid(row=7, column=0)

        # Create Submit Button
        submit_btn = Button(root, text="Add To Appointment List", command=submit, bg="dark khaki", fg="saddle brown", font=("Cambria", 10)).grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=93)

        # Create a Apoinment Query Button
        aquery_btn=Button(root, text='Show Appointment List', command=aquery, bg="dark khaki", fg="saddle brown", font=("Cambria", 10)).grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=95)

        # Create a Place Query Button
        pquery_btn=Button(root, text='Show Vaccine Center List', command=pquery, bg="dark khaki", fg="saddle brown", font=("Cambria", 10)).grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=93)

        # Create a User Query Button
        uquery_btn=Button(root, text='Show User List', command=uquery, bg="dark khaki", fg="saddle brown", font=("Cambria", 10)).grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=118)

        #commit changes
        conn.commit()
        #close connection
        conn.close()

        root.mainloop()


    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Admin Menu")
    login_success_screen.geometry("260x340")
    login_success_screen.iconbitmap("covid.ico")
    Label(login_success_screen, text="Admin Menu", width=260, height=2,bg="dark khaki", fg="saddle brown", font=("Cambria", 15)).pack()
    Button(login_success_screen, text="View All User", fg="saddle brown", bg="dark khaki", font=("Cambria", 10),height=3,width=40, command=uquery).pack(padx=5, pady=5)
    Button(login_success_screen, text="Add New Vaccination Centre", fg="saddle brown", bg="dark khaki", font=("Cambria", 10),height=3,width=40, command=vaccination).pack(padx=5, pady=5)
    Button(login_success_screen, text="Assign Appointment", fg="saddle brown", bg="dark khaki", font=("Cambria", 10),height=3,width=40, command=appointment).pack(padx=5, pady=5)
    Button(login_success_screen, text="Log Out", fg="saddle brown", bg="dark khaki", font=("Cambria", 10),height=3,width=40, command=delete_login_success).pack(padx=5, pady=5)
 
# Password Not Recognised
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("ERROR")
    password_not_recog_screen.geometry("200x200")
    password_not_recog_screen.iconbitmap("covid.ico")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",bg="dark khaki", fg="saddle brown", font=("Cambria", 10), command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Error")
    user_not_found_screen.geometry("200x200")
    user_not_found_screen.iconbitmap("covid.ico")
    Label(user_not_found_screen, text="User Not Found", fg="saddle brown", font=("Cambria", 10)).pack()
    Button(user_not_found_screen, text="OK",bg="dark khaki", fg="saddle brown", font=("Cambria", 10), command=delete_user_not_found_screen).pack()

# Log out
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

Label(main, text="Welcome To BioVax", width=180, height=2,bg="dark khaki", fg="saddle brown", font=("Cambria", 15)).pack()
register_btn = Button(main, text='Register', command=register, width=50, height=3, fg="saddle brown", bg="dark khaki", font=("Cambria", 10)).pack(padx=10, pady=10)
login_btn = Button(main, text='Login', command=login, width=50, height=3, fg="saddle brown", bg="dark khaki", font=("Cambria", 10)).pack(padx=10, pady=10)
admin_btn = Button(main, text='Admin', command = admin_login, width=50, height=3, fg="saddle brown", bg="dark khaki", font=("Cambria", 10)).pack(padx=10, pady=10)


main.mainloop()