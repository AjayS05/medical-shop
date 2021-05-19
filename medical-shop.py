from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox

db = sqlite3.connect('medical.db')
db.execute('create table if not exists customer(name text NOT NULL, phone_no text PRIMARY KEY NOT NULL,'
           'address text NOT NULL, password text NOT NULL)')
db.execute('create table if not exists orders(order_id integer PRIMARY KEY AUTOINCREMENT, item text not null,'
           'quantity integer not null, address text not null, price integer not null, phone_no text not null,'
           'FOREIGN KEY(phone_no) REFERENCES customer(phone_no))')


def fp():

    def rip():
        pas = e6.get()
        if 6 <= len(pas) <= 10:
            pass
        else:
            messagebox.showerror('error', 'password should be\n between 6-10 characters', master=root8)
            return None
        num = e5.get()
        if num.isnumeric():
            pass
        else:
            messagebox.showerror('error', 'phone number should only\n contain numbers', master=root8)
            return None
        if len(num) == 10:
            pass
        else:
            messagebox.showerror('error', 'phone number must\n be of 10 characters', master=root8)
            return None
        if pas == e7.get():
            pass
        else:
            messagebox.showerror('error', 'password does not match', master=root8)
            return None
        db.execute('update customer set password = ? where phone_no = ?', (pas, num))
        db.commit()
        root8.destroy()

    root8 = Tk()
    root8.geometry('500x500')
    root8.title("MEDICAL STORE ")
    root8.configure(bg="darkslategrey")

    label28 = Label(root8, text=" Enter Phone Number ", font="arial 11 bold", bg="white", fg="black")
    label28.place(x=70, y=50)
    label29 = Label(root8, text=" Enter New Password ", font="arial 11 bold", bg="white", fg="black")
    label29.place(x=70, y=100)
    label30 = Label(root8, text="Confirm New Password", font="arial 11 bold", bg="white", fg="black")
    label30.place(x=70, y=150)

    e5 = Entry(root8, font="arial 11 bold")
    e5.place(x=270, y=50)

    e6 = Entry(root8, font="arial 11 bold")
    e6.place(x=270, y=100)

    e7 = Entry(root8, font="arial 11 bold")
    e7.place(x=270, y=150)

    button14 = Button(root8, text="         Submit          ", font="arial 13 bold", bg="slateblue4", fg="white",
                      command=rip)
    button14.place(x=170, y=200)


def ca():

    def no_check():
        no = e8.get()
        if no.isnumeric():
            pass
        else:
            messagebox.showerror('error', 'phone number should only\n contain numbers', master=root7)
            return None
        if len(no) == 10:
            pass
        else:
            messagebox.showerror('error', 'phone number must\n be of 10 characters', master=root7)
            return None
        return True

    def permenant_ad():
        if e9.get() == '':
            messagebox.showerror('error', 'address should not be empty', master=root7)
            return None
        if no_check() is True:
            db.execute('update customer set address = ? where phone_no = ?', (e9.get(), e8.get()))
            db.commit()
            root7.destroy()
        else:
            return None

    def delivery_ad():
        global new_address
        if e9.get() == '':
            messagebox.showerror('error', 'address should not be empty', master=root7)
            return None
        if no_check() is True:
            new_address = e9.get()
            root7.destroy()
        else:
            return None

    root7 = Tk()
    root7.geometry('500x500')
    root7.title("MEDICAL STORE ")
    root7.configure(bg="darkslategrey")

    label31 = Label(root7, text=" Manage Address ", font="arial 15 bold", bg="midnightblue", fg="rosybrown1")
    label31.place(x=160, y=50)
    label32 = Label(root7, text=" Enter phone number ", font="arial 11 bold", bg="white", fg="black")
    label32.place(x=70, y=120)
    label33 = Label(root7, text="      Enter Address      ", font="arial 11 bold", bg="white", fg="black")
    label33.place(x=70, y=160)

    e8 = Entry(root7, font="arial 11 bold")
    e8.place(x=270, y=120)

    e9 = Entry(root7, font="arial 11 bold")
    e9.place(x=270, y=160)

    label26 = Label(root7, text=" Do you want to :", font="arial 18 bold", bg="darkslategrey", fg="white")
    label26.place(x=70, y=230)
    label27 = Label(root7, text="  OR  ", font="arial 18 bold", bg="darkslategrey", fg="white")
    label27.place(x=90, y=330)

    button15 = Button(root7, text=" set this as permenant Address? ", font="arial 13 bold", bg="slateblue4", fg="white",
                      command=permenant_ad)
    button15.place(x=70, y=280)
    button16 = Button(root7, text=" Use only for this Delivery? ", font="arial 13 bold", bg="slateblue4", fg="white",
                      command=delivery_ad)
    button16.place(x=70, y=380)


def lpg():
    global destroy
    global phone_num
    global new_address

    def oc():

        def sb():

            def mp():

                def pay():
                    global made_payment
                    root5.destroy()
                    made_payment = True
                    root6 = Tk()
                    root6.geometry('400x200')
                    root6.title("MEDICAL STORE ")
                    root6.configure(bg="darkslategrey")

                    label25 = Label(root6, text=" Thank you for shopping with us.\nYour product will be delivered in\n"
                                                "1-3 days.",
                                    font="arial 15 bold", bg="midnightblue", fg="rosybrown1")
                    label25.place(x=30, y=50)

                def cash():

                    cash_frame = Frame(root5, width=300, height=250, relief='sunken', bg='darkslategrey')
                    cash_frame.place(x=95, y=190)

                    label34 = Label(cash_frame, text="You have to tender exact\nchange and have to\nbe present"
                                                     " at the time\nof"
                                                     " delivery.", font="arial 15 bold", bg="darkslategrey", fg="white")
                    label34.place(x=20, y=10)

                    button13 = Button(cash_frame, text=" Agree and Confirm ", font="arial 13 bold", bg="slateblue4",
                                      fg="white",
                                      command=pay)
                    button13.place(x=50, y=150)

                def card():

                    def card_pay():
                        ab = e1.get()
                        ac = e2.get()
                        ad = e3.get()
                        if ab == '' or ac == '' or ad == '':
                            messagebox.showerror('error', 'no field must remain empty', master=root5)
                            return None
                        for letters in ab:
                            if letters == ' ':
                                continue
                            else:
                                if letters.isalpha():
                                    continue
                                else:
                                    messagebox.showerror('error', 'name must not contain\n symbols or numbers',
                                                         master=root5)
                                    return None
                        if ac.isnumeric() and len(ac) == 12:
                            pass
                        else:
                            messagebox.showerror('error', 'card number should contain only digits and must contain 12'
                                                          'numbers', master=root5)
                            return None
                        if ad.isnumeric() and len(ad) == 3:
                            pass
                        else:
                            messagebox.showerror('error', 'cvv must be a 3 digit number on back of your card',
                                                 master=root5)
                            return None
                        pay()

                    card_frame = Frame(root5, width=300, height=250, relief='sunken', bg='darkslategrey')
                    card_frame.place(x=95, y=190)

                    label21 = Label(card_frame, text="Name of Cardholder", font="arial 11 bold", bg="darkslategrey",
                                    fg="white")
                    label21.place(x=20, y=10)
                    e1 = Entry(card_frame)
                    e1.place(x=180, y=10)

                    label22 = Label(card_frame, text=" Card Number ", font="arial 11 bold", bg="darkslategrey",
                                    fg="white")
                    label22.place(x=20, y=50)
                    e2 = Entry(card_frame)
                    e2.place(x=180, y=50)

                    label23 = Label(card_frame, text=" Expiry Date ", font="arial 11 bold", bg="darkslategrey",
                                    fg="white")
                    label23.place(x=20, y=90)
                    monthspinner = Spinbox(card_frame, width=5, values=tuple(range(1, 13)))
                    yearspinner = Spinbox(card_frame, width=5, values=tuple(range(2021, 2030)))
                    monthspinner.place(x=180, y=90)
                    yearspinner.place(x=230, y=90)

                    label24 = Label(card_frame, text=" CVV ", font="arial 11 bold", bg="darkslategrey", fg="white")
                    label24.place(x=20, y=130)
                    e3 = Entry(card_frame)
                    e3.place(x=180, y=130)

                    button12 = Button(card_frame, text=" Submit and Pay ", font="arial 13 bold", bg="slateblue4",
                                      fg="white", command=card_pay)
                    button12.place(x=70, y=170)

                if new_address == '':
                    cur = db.execute('select address from customer where phone_no = ?', (phone_num, ))
                    add = cur.fetchone()
                    add = list(add)
                    add = add[0]
                else:
                    add = new_address
                for it in total_bill[1:len(total_bill) - 1]:
                    tot = int(it[2]) * int(item_price[it[0]])
                    db.execute('insert into orders(item, quantity, address, price, phone_no) values(?,?,?,?,?)',
                               (it[0], int(it[2]), add, tot, phone_num))
                    db.commit()
                root4.destroy()
                root5 = Tk()
                root5.geometry('500x500')
                root5.title("MEDICAL STORE ")
                root5.configure(bg="darkslategrey")

                label19 = Label(root5, text="   Make Payment via:   ", font="arial 18 bold", bg="midnightblue",
                                fg="rosybrown1")
                label19.place(x=115, y=50)

                button10 = Button(root5, text="      Cash       ", font="arial 13 bold", bg="slateblue4", fg="white",
                                  command=cash)
                button10.place(x=90, y=120)
                button11 = Button(root5, text="      Card       ", font="arial 13 bold", bg="slateblue4", fg="white",
                                  command=card)
                button11.place(x=290, y=120)

            def table(row, column, window, x, y):

                for j in range(row):

                    for k in range(column):

                        if x > 240:
                            y += 20
                            x = 120

                        e = Entry(window)
                        e.place(x=x, y=y)
                        x += 120
                        e.insert(END, total_bill[j][k])

            for i in total_bill:
                if item == i[0]:
                    messagebox.showerror('error', 'an item cannot be repeated\n purchase another item')
                    return None
            total_bill.append([item, current_total, quantity])

            root3.destroy()
            total_amount = 0
            for i in total_bill[1:]:
                total_amount += int(i[1])
            total_bill.append(['Total amount', str(total_amount)])
            root4 = Tk()
            root4.geometry('500x500')
            root4.title("MEDICAL STORE ")
            root4.configure(bg="darkslategrey")

            table(len(total_bill), 2, root4, 120, 120)

            label17 = Label(root4, text="               BILL                 ", font="arial 17 bold", bg="midnightblue",
                            fg="rosybrown1")
            label17.place(x=120, y=50)
            label18 = Label(root4, text="  OR  ", font="arial 11 bold", bg="darkslategrey", fg="white")
            label18.place(x=235, y=370)

            button8 = Button(root4, text="   Make Payment    ", font="arial 13 bold", bg="slateblue4", fg="white",
                             command=mp)
            button8.place(x=50, y=370)
            button9 = Button(root4, text="  Change Delivery\nAddress  ", font="arial 13 bold", bg="slateblue4",
                             fg="white",
                             command=ca)
            button9.place(x=300, y=360)
            root4.mainloop()

        def new_order():
            if len(total_bill) == 8:
                messagebox.showerror('error', 'maximum order limit of 8 reached', master=root3)
                return None

            for i in total_bill:
                if item == i[0]:
                    messagebox.showerror('error', 'an item cannot be repeated\n purchase another item')
                    return None
            root3.destroy()
            total_bill.append([item, current_total, quantity])
            lpg()

        def cancel():
            root3.destroy()
            lpg()

        item = cb0.get()
        quantity = cb1.get()
        if item == '':
            messagebox.showerror('error', 'select product before proceeding', master=root1)
            return None
        elif quantity == '':
            messagebox.showerror('error', 'select quantity before proceeding', master=root1)
            return None
        elif item not in v:
            messagebox.showerror('error', 'invalid product', master=root1)
            return None
        elif quantity not in w:
            messagebox.showerror('error', 'invalid quantity', master=root1)
            return None
        else:
            root1.destroy()
        root3 = Tk()
        root3.geometry('500x500')
        root3.title("MEDICAL STORE ")
        root3.configure(bg="darkslategrey")

        label12 = Label(root3, text="        ORDER CONFIRMATION         ", font="arial 17 bold", bg="midnightblue",
                        fg="rosybrown1")
        label12.place(x=55, y=70)
        label13 = Label(root3, text=" Item Selected ", font="arial 11 bold", bg="white", fg="black")
        label13.place(x=70, y=130)
        item_label = Label(root3, text='', font="arial 11 bold", bg="white", fg="black")
        item_label.place(x=260, y=130)
        label14 = Label(root3, text=" Quantity ", font="arial 11 bold", bg="white", fg="black")
        label14.place(x=70, y=170)
        quant_label = Label(root3, text='', font="arial 11 bold", bg="white", fg="black")
        quant_label.place(x=260, y=170)
        label15 = Label(root3, text=" Price ", font="arial 11 bold", bg="white", fg="black")
        label15.place(x=70, y=210)

        loc = ''
        if item == "Crocin":
            loc = 'crocin.png'
        elif item == 'Benadryl':
            loc = 'benadryl.png'
        elif item == 'Aspirin':
            loc = 'aspirin.png'
        elif item == 'Eye drop':
            loc = 'eyedrops.png'
        elif item == 'Ear drop':
            loc = 'ear drop.jpg'
        elif item == 'Moov':
            loc = 'moov.png'
        elif item == 'Vicks':
            loc = 'vicks.png'
        elif item == 'Thermometer':
            loc = 'thermometer .png'
              
        image1 = Image.open(loc)
        test = ImageTk.PhotoImage(image1, master=root3)
        label16 = Label(root3, image=test, width=150, height=175)
        label16.image = test
        label16.place(x=70, y=260)

        item_label.config(text=item)
        item_label.update()
        quant_label.config(text=quantity)
        item_label.update()
        current_total = str(int(item_price[item]) * int(quantity))
        price_lab = Label(root3, text=current_total, font="arial 11 bold", bg="white", fg="black")
        price_lab.place(x=260, y=210)
        cancel_button = Button(root3, text='  cancel  ', font="arial 13 bold", bg="slateblue4", fg="white",
                               command=cancel)
        cancel_button.place(x=260, y=280)
        button6 = Button(root3, text=" Add another Product ", font="arial 13 bold", bg="slateblue4", fg="white",
                         command=new_order)
        button6.place(x=260, y=330)
        button7 = Button(root3, text=" Proceed to Checkout ", font="arial 13 bold", bg="slateblue4", fg="white",
                         command=sb)
        button7.place(x=260, y=380)
        root3.mainloop()

    def price_set(self):
        product = cb0.get()
        pr = '-'
        if product == 'Crocin':
            pr = item_price['Crocin']
        elif product == 'Benadryl':
            pr = item_price['Benadryl']
        elif product == 'Aspirin':
            pr = item_price['Aspirin']
        elif product == 'Ear drop':
            pr = item_price['Ear drop']
        elif product == 'Eye drop':
            pr = item_price['Eye drop']
        elif product == 'Moov':
            pr = item_price['Moov']
        elif product == 'Vicks':
            pr = item_price['Vicks']
        elif product == 'Thermometer':
            pr = item_price['Thermometer']
        price_label.config(text=pr)
        price_label.update()

    if destroy is True:
        phone_num = textbox1.get()
        password = textbox2.get()
        if textbox1.get() == '' or textbox2.get() == '':
            messagebox.showerror('error', 'no field should remain empty', master=root)
            return None
        cursor = db.execute('select * from customer where phone_no=? and password=?', (phone_num, password))
        ro = cursor.fetchone()
        if ro:
            root.destroy()
            destroy = False
        else:
            messagebox.showerror('error', 'incorrect username or password', master=root)
            return None

    root1 = Tk()
    root1.geometry('500x500')
    root1.title("MEDICAL STORE ")
    root1.configure(bg="darkslategrey")

    label4 = Label(root1, text="                ORDER                ", font="arial 17 bold", bg="midnightblue",
                   fg="rosybrown1")
    label4.place(x=100, y=70)
    label5 = Label(root1, text=" Select the Item ", font="arial 11 bold", bg="white", fg="black")
    label5.place(x=70, y=160)
    label6 = Label(root1, text=" Select the Quantity ", font="arial 11 bold", bg="white", fg="black")
    label6.place(x=70, y=210)
    label7 = Label(root1, text=" Price per piece ", font="arial 11 bold", bg="white", fg="black")
    label7.place(x=70, y=260)

    v = ["Crocin", "Benadryl", "Aspirin", "Ear drop", "Eye drop", "Moov",
         "Vicks", "Thermometer"]
    cb0 = Combobox(root1, values=v, font="comic 14", width='13')
    cb0.place(x=250, y=160)
    cb0.bind("<<ComboboxSelected>>", price_set)

    w = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    cb1 = Combobox(root1, values=w, font="comic 14", width='13')
    cb1.place(x=250, y=208)

    item_price = {'Crocin': '50', 'Benadryl': '120', 'Aspirin': '250', 'Ear drop': '210', 'Eye drop': '500',
                  'Moov': '90', 'Vicks': '130', 'Thermometer': '300'}
    price_label = Label(root1, text='-', font="arial 11 bold", bg="white", fg="black")
    price_label.place(x=250, y=260)

    button4 = Button(root1, text="          ORDER CONFRIMATION          ", font="arial 13 bold", bg="slateblue4",
                     fg="white", command=oc)
    button4.place(x=90, y=340)

    root1.mainloop()


def spg():

    def sign_up():
        name = textbox8.get()
        n = textbox9.get()
        ad = textbox10.get()
        p = textbox11.get()

        if name == "" or n == "" or p == "" or ad == "":
            messagebox.showerror('error', 'no field must remain empty', master=root2)
            return None
        if n.isnumeric():
            pass
        else:
            messagebox.showerror('error', 'phone number should only\n contain numbers', master=root2)
            return None
        if len(n) == 10:
            pass
        else:
            messagebox.showerror('error', 'phone number must\n be of 10 characters', master=root2)
            return None
        for i in name:
            if i == ' ':
                continue
            else:
                if i.isalpha():
                    continue
                else:
                    messagebox.showerror('error', 'username should not contain \nspecial characters and must\n'
                                                  ' be between 6-16 characters', master=root2)
                return None
        if 6 <= len(name) <= 16:
            pass
        else:
            messagebox.showerror('error', 'username should not contain \nspecial characters and must\n'
                                          ' be between 6-16 characters', master=root2)
            return None
        if 6 <= len(p) <= 10:
            pass
        else:
            messagebox.showerror('error', 'password should be\n between 6-10 characters', master=root2)
            return None
        db.execute('insert into customer values(?,?,?,?)', (name, n, ad, p))
        db.commit()
        root2.destroy()

    root2 = Tk()
    root2.geometry('500x500')
    root2.title("MEDICAL STORE ")
    root2.configure(bg="darkslategrey")

    label7 = Label(root2, text="                SIGN UP                ", font="arial 17 bold", bg="midnightblue",
                   fg="rosybrown1")
    label7.place(x=100, y=70)
    label8 = Label(root2, text="  Customer Name  ", font="arial 11 bold", bg="white", fg="black")
    label8.place(x=80, y=180)
    label9 = Label(root2, text=" Enter the\nPhone Number ", font="arial 11 bold", bg="white", fg="black")
    label9.place(x=80, y=230)
    label10 = Label(root2, text=" Enter the Address ", font="arial 11 bold", bg="white", fg="black")
    label10.place(x=80, y=285)
    label11 = Label(root2, text="    Password    ", font="arial 11 bold", bg="white", fg="black")
    label11.place(x=80, y=340)

    textbox8 = Entry(root2, font="comic 14", width='15')
    textbox8.place(x=240, y=180)
    textbox9 = Entry(root2, font="comic 14", width='15')
    textbox9.place(x=240, y=235)
    textbox10 = Entry(root2, font="comic 14", width='15')
    textbox10.place(x=240, y=285)
    textbox11 = Entry(root2, font="comic 14", width='15', show='*')
    textbox11.place(x=240, y=340)

    button5 = Button(root2, text="                  SIGN IN                ", font="arial 13 bold", bg="slateblue4",
                     fg="white", command=sign_up)
    button5.place(x=113, y=390)

    root2.mainloop()


if __name__ == '__main__':
    made_payment = False
    new_address = ''
    total_bill = [['Name', 'Price']]
    phone_num = ''
    destroy = True

    root = Tk()
    root.title("MEDICAL STORE ")
    root.configure(bg="darkslategrey")
    root.geometry('500x500')

    label0 = Label(root, text="    Enter the details   ", font="arial 18 bold", bg="midnightblue", fg="rosybrown1")
    label0.place(x=130, y=70)

    label1 = Label(root, text=" Phone Number ", font="arial 13 bold", bg="white", fg="black")
    label1.place(x=95, y=160)

    textbox1 = Entry(root, font="comic 14", width='14')
    textbox1.place(x=250, y=160)

    label2 = Label(root, text="    Password    ", font="arial 13 bold", bg="white", fg="black")
    label2.place(x=95, y=210)

    textbox2 = Entry(root, font="comic 14", width='14', show='*')
    textbox2.place(x=250, y=210)

    button1 = Button(root, text="                     LOGIN                    ", font="arial 13 bold", bg="slateblue4",
                     fg="white", command=lpg)
    button1.place(x=113, y=260)

    label1 = Label(root, text="                     OR                    ", font="arial 13 bold",
                   bg="darkslategrey", fg="white")
    label1.place(x=130, y=305)

    button2 = Button(root, text="                   SIGN UP                   ", font="arial 13 bold", bg="slateblue4",
                     fg="white", command=spg)
    button2.place(x=113, y=340)

    button3 = Button(root, text="           Forgot Password?           ", font="arial 13 bold", bg="slateblue4",
                     fg="white", command=fp)
    button3.place(x=113, y=450)

    root.mainloop()

    db.close()
    print(total_bill)
