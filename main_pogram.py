from string import *
from Tkinter import *
from datetime import date
import couchdb
couch = couchdb.Server('http://admin:admin@localhost:5984')
loop=True
import re
from tkinter import messagebox



def seladmin():
    admin=Tk()
    admin.geometry('500x500')
    label = Label(admin, text="welcome admin", font=("bold", 30)).place(x=50, y=50)
    Label(admin, text="useer-name", font=("bold", 30)).place(x=120, y=120)
    Label(admin, text="password", font=("bold", 30)).place(x=120, y=260)
    e1 = Entry(admin)
    e2 = Entry(admin)
    e1.place(x=340, y=140)
    e2.place(x=340, y=280)
    def adminpage():
        user = e1.get()
        password = e2.get()
        db = couch['admins']
        for item in db.view('_design/admin/_view/new-view'):
            if (item.key == user):
                if (item.value == password):
                    adop=Tk()
                    adop.geometry('500x500')
                    def modifydriver():
                        db = couch['driver']
                        i = 1;
                        print("########all available drivers###########")
                        for item in db.view('_design/view2/_view/new-view'):
                            print(i, item.key, item.value['name'], item.value['location'], item.value['phone'])
                            i = i + 1

                        print("############# driver operetions ###############")
                        print("1. add new driver")
                        print("2.remove a driver")
                        print("3.update a driver")

                        c = input("select your choice(driver id)")
                        if (c == "1"):
                            dateofbirth = input("enter the dob of driver")
                            name = input("enter the name of the driver")
                            driverid = input("enter the id of the driver")
                            status = input("enter the status of driver")
                            phone = input("enter the phone no of the driver")
                            location = input("enter the location of driver")
                            password = input("enter the password(driver)")
                            doc = {'dob': dateofbirth, 'name': name, 'did': driverid, 'stat': status, 'phone': phone,
                                   'loc': location, "password": password}
                            db.save(doc)
                            print("succefully added driver")
                        if (c == "2"):
                            did = input("enter the driver id to be deleted")
                            for item in db.view('_design/view2/_view/new-view'):
                                if (item.key == did):
                                    id = item.id
                            doc = db[id]
                            db.delete(doc)
                            print("successfully deleted driver with id ", did)

                        if (c == "3"):
                            did = input("enter the driver id to update")
                            for item in db.view('_design/view2/_view/new-view'):
                                if (item.key == did):
                                    id = item.id
                            doc = db[id]
                            print("enter the new values")
                            dateofbirth = input("enter the dob of driver")
                            name = input("enter the name of the driver")
                            status = input("enter the status of driver")
                            phone = input("enter the phone no of the driver")
                            location = input("enter the location of driver")
                            password = input("enter the password(driver)")
                            db.delete(doc)
                            doc = {'dob': dateofbirth, 'name': name, 'did': did, 'stat': status, 'phone': phone,
                                   'loc': location, "password": password}
                            db.save(doc)
                            print("sucessfully updated the driver details")

                    def modifypassenger():
                        print("############# all available passengers ############")
                        db = couch['passenger']
                        for item in db.view('_design/pass/_view/new-view'):
                            print(item.key, item.value['fname'], item.value['lname'], item.value['phone'],
                                  item.value['password'])

                        print("########## admin passenger operetions ###############")
                        print("1.add new passenger")
                        print("2.remove a passengerr")
                        print("3.update a passenger")
                        c = input("enter your choice")

                        if (c == "1"):
                            fname = input("enter  first name:")
                            lname = input("enter  last name")
                            password = input("enter  password")
                            phone = input("enter  phone number")
                            eid = input("enter your email id")
                            mat = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', eid)
                            if (mat == None):
                                print("invalid email")


                            else:
                                db = couch['passenger']
                                doc = {'first_name': fname, 'last_name': lname, 'password': password, 'phone': phone,
                                       'eid': eid}
                                db.save(doc)
                                print("passenger added sucessfulfully")

                        if (c == "2"):
                            eid = input("enter the email id of the passenger to be removed")
                            for item in db.view('_design/pass/_view/new-view'):
                                if (item.key == eid):
                                    id = item.id
                            doc = db[id]
                            db.delete(doc)
                            print("sucessfully deleted the passenger with email id", eid)
                        if (c == "3"):
                            eid = input("enter the email id of passenger to be updated")
                            for item in db.view('_design/pass/_view/new-view'):
                                if (item.key == eid):
                                    id = item.id

                            print("enter the updated details")
                            fname = input("enter  first name:")
                            lname = input("enter  last name")
                            password = input("enter password")
                            phone = input("enter  phone number")
                            doc = {'first_name': fname, 'last_name': lname, 'password': password, 'phone': phone,
                                   'eid': eid}
                            db.save(doc)
                            print("sucessufully updated the passenger with email id ", eid)

                    def modifyadmins():
                        db = couch['admins']
                        for item in db.view('_design/admin/_view/new-view'):
                            print("###### all available admins")
                            print("user name:", item.key, "password:", item.value)
                        print("################")
                        print("1.add a new admin")
                        print("2.remove a admin")
                        print("3.change password of a admin")
                        c = input("enter your choice")
                        if (c == "1"):
                            user = input("user name of the new admin   :")
                            password = input("password of the new admin  :")
                            doc = {'username': user, "passwoord": password}
                            db.save(doc)
                            print("sucessfully added admiin")

                        if (c == "2"):
                            user = input("user name of the admin to be removed")
                            for item in db.view('_design/admin/_view/new-view'):
                                if (item.key == user):
                                    id = item.id

                            doc = db[id]
                            db.delete(doc)
                            print("successfully deleted the admin eith username : ", user)

                        if (c == "3"):
                            user = input("user name of the admin to change the password of  :")
                            for item in db.view('_design/admin/_view/new-view'):
                                if (item.key == user):
                                    id = item.id

                            password = input("password of the new admin  :")
                            doc = {'username': user, "passwoord": password}
                            db.delete(id)
                            db.save(doc)
                            print("successfully updated the admin with username  :", user)

                    def modifufinal():
                        db = couch['final-ride']
                        i = 1;
                        print("########all current rides###########")
                        for item in db.view('_design/dv/_view/new-view'):
                            print(i, item.key, item.value['driverid'], item.value['driverphone'], item.value['regno'],
                                  item.value['time'])
                            i = i + 1

                        print("############# ride operetions ###############")
                        print("1. add new ride")
                        print("2.remove a ride")
                        print("3.update a ride")

                        c = input("select your choice")
                        if (c == "1"):
                            passsengerid = input("passengerid: ")
                            driverid = input("driverid")
                            time = input("time")
                            regno = input("reg-no")
                            driverphone = input("DRIVER PHONE")
                            source = input("source")
                            destination = input("destination")
                            doc = {'passengerid': passengerid, 'driverid': driverid, 'time': time, 'regno': regno,
                                   'driverphone': driverphone, 'src': source, 'destination': destination}
                            db.save(doc)
                            print("succefully added new ride")
                        if (c == "2"):
                            did = input("enter the ride id to be deleted")
                            for item in db.view('_design/dv/_view/new-view'):
                                if (item.key == did):
                                    id = item.key
                            doc = db[id]
                            db.delete(doc)
                            print("successfully deleted ride with id ", did)

                        if (c == "3"):
                            did = input("enter the ride id to update")
                            for item in db.view('_design/view2/_view/new-view'):
                                if (item.key == did):
                                    id = item.id
                            doc1 = db[id]
                            print("enter the new values")
                            passsengerid = input("passengerid: ")
                            driverid = input("driverid")
                            time = input("time")
                            regno = input("reg-no")
                            driverphone = input("DRIVER PHONE")
                            source = input("source")
                            destination = input("destination")
                            doc = {'passengerid': passengerid, 'driverid': driverid, 'time': time, 'regno': regno,
                                   'driverphone': driverphone, 'src': source, 'destination': destination}
                            db.delete(doc1)

                            db.save(doc)
                            print("sucessfully ride details")




                    Button(adop, text='modify Driver', width=20, bg='brown', fg='white',command=modifydriver).place(x=180, y=180)
                    Button(adop, text='modify Passenger', width=20, bg='brown', fg='white',command=modifypassenger).place(x=180,y=380)
                    Button(adop, text='modify Admin', width=20, bg='brown', fg='white',command=modifyadmins).place(x=180, y=280)
                    Button(adop, text='modify final-ride', width=20, bg='brown', fg='white',command=modifufinal).place(x=180,y=480)


                    print("sucessfully logined as administrator")





    Button(admin, text='submit', width=20, bg='brown', fg='white',command=adminpage).place(x=180, y=400)




def passsignup():
    passsu = Tk()
    passsu.geometry('500x500')
    Label(passsu, text="Welcome passenger", font=("bold", 30)).place(x=80, y=50)
    Label(passsu, text="first anme", font=("bold", 10)).place(x=120, y=120)
    Label(passsu, text="lastname", font=("bold", 10)).place(x=120, y=160)
    Label(passsu, text="password", font=("bold", 10)).place(x=120, y=200)
    Label(passsu, text="phone", font=("bold", 10)).place(x=120, y=240)
    Label(passsu, text="email", font=("bold", 10)).place(x=120, y=280)

    e1 = Entry(passsu)
    e2 = Entry(passsu)
    e3 = Entry(passsu)
    e4 = Entry(passsu)
    e5 = Entry(passsu)

    e1.place(x=240, y=140)
    e2.place(x=240, y=180)
    e3.place(x=240, y=220)
    e4.place(x=240, y=260)
    e5.place(x=240, y=300)
    def passsnp():
        fname = e1.get()
        lname = e2.get()
        password = e3.get()
        phone = e4.get()
        eid = e5.get()
        mat = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', eid)
        if (mat == None):
            print("invalid email")


        else:
            db = couch['passenger']
            doc = {'first_name': fname, 'last_name': lname, 'password': password, 'phone': phone, 'eid': eid}
            db.save(doc)
            output ="you have successfully signedup, please login to complete your cab booking "
            messagebox.showinfo("sucessfull",output)



    Button(passsu, text='submit', width=20, bg='brown', fg='white', command=passsnp).place(x=180, y=380)


def passenger():
    passe=Tk()
    passe.geometry('500x500')
    Label(passe, text="welcome passenger", font=("bold", 30)).place(x=90, y=40)
    def login():
        plogin=Tk()
        plogin.geometry('500x500')
        Label(plogin, text="Welcome passenger", font=("bold", 30)).place(x=80, y=50)
        Label(plogin, text="passenger id", font=("bold", 10)).place(x=120, y=120)
        Label(plogin, text="password", font=("bold", 10)).place(x=120, y=160)
        Label(plogin, text="source", font=("bold", 10)).place(x=120, y=200)
        Label(plogin, text="destination", font=("bold", 10)).place(x=120, y=240)
        Label(plogin, text="time", font=("bold", 10)).place(x=120, y=280)
        Label(plogin, text="model", font=("bold", 10)).place(x=120, y=320)
        e1 = Entry(plogin)
        e2 = Entry(plogin)
        e3 = Entry(plogin)
        e4 = Entry(plogin)
        e5 = Entry(plogin)
        e6 = Entry(plogin)
        e1.place(x=240, y=120)
        e2.place(x=240, y=160)
        e3.place(x=240, y=200)
        e4.place(x=240, y=240)
        e5.place(x=240, y=280)
        e6.place(x=240, y=320)

        def passlogin():

            email = e1.get()

            password = e2.get()
            db = couch['passenger']
            e = 0
            for item in db.view('_design/pass/_view/new-view'):

                if (item.key == email):
                    e = 1

                    if (item.value['password'] == password):
                        passw = 1

                        print('successfully logined')
                        passid = item.key

                        print("first name:", item.value['fname'], "    last name :", item.value['lname'])
                        db = couch['locations']
                        print("our available locations")
                        for item in db.view('_design/loc/_view/new-view'):
                            print(item.key)
                        source = e3.get()
                        dest = e4.get()
                        for item in db.view('_design/loc/_view/new-view'):
                            if (source == item.key):
                                sourcedist = item.value

                        for item in db.view('_design/loc/_view/new-view'):
                            if (dest == item.key):
                                destdist = item.value

                        if (source == dest):
                            print("cant choose same locations for both sourcr and destination")

                        else:
                            print("choose the type of ride you want")
                            print("#####################")
                            db = couch['models']
                            for item in db.view('_design/car/_view/new-view'):
                                print(item.key, "  price per km  ", item.value)
                            car = e6.get()
                            for item in db.view('_design/car/_view/new-view'):
                                if (item.key == car):
                                    price = item.value
                                    model = item.key
                            total_distance = destdist - sourcedist
                            print("total distance is  ", total_distance)
                            priceto = total_distance * price
                            print("price is ", priceto)
                            time = e5.get()
                            print("--------confirm payment-----------")
                            print("yes [Y] or No [N]")

                            pay ="Y"
                            if (pay == "Y"):
                                db = couch['payment-details']
                                payid = passid
                                doc = {'paymentid': payid, 'time': time}
                                db.save(doc)
                            if (pay != "Y"):
                                print("payment unsucessful")
                    else:
                        print("invalid password")
                        passw = 0
                        exit()

            if (e == 0):
                print("wrong emnail")

            driup = 0
            if (pay == "Y"):
                db = couch['driver']
                d = 0
                for item in db.view('_design/update/_view/new-view'):

                    if (item.value['status'] == "AVAILABLE" and item.value['location'] == source):
                        d = 1
                        did = item.value['did']
                        id = item.key
                        doc1 = db[id]
                        name = item.value['name']
                        dob = item.value['dob']
                        phone = item.value['phone']
                        loc = dest
                        password = item.value['password']
                        doc = {'dob': dob, 'name': name, 'did': did, 'stat': "BUSY", 'phone': phone, 'loc': loc,
                               'password': password}
                        db.delete(doc1)
                        db.save(doc)
                        driup = 1
                        break

                # \\taxi \\
                db = couch['taxi']

                if (driup == 1):
                    for item in db.view('_design/reg/_view/new-view'):
                        m = 0
                        if (item.value['model'] == model and item.value['status'] == "AVAILABLE"):
                            regno = item.value['regno']
                            id = item.key
                            m = 1
                            ty = item.value['model']
                            sta = "BUSY"
                            doc = {'type': ty, 'regno': regno, 'Sta': sta}
                            doc1 = db[id]
                            db.delete(doc1)
                            db.save(doc)

                            # \\adding to final ride|\\
                            doc = {'passsengerid': passid, 'driverid': did, 'time': time, 'regno': regno,
                                   'driverphone': phone, 'source': source, 'destination': dest}
                            db = couch['final-ride']
                            db.save(doc)
                            print("your driver id and number are  ", did, phone)
                            print("your car no is ", regno)
                            output = "your driver id and number are  %s " %(did)
                            output +=" %s " %(phone)
                            output +="your car no is %s" %(regno)
                            messagebox.showinfo("sucessfully boooked", output)
                            break

                    if (m == 0):
                        print("Sorry, the recquired model of vehicle is not available")
                        db = couch['driver']
                        for item in db.view('_design/update/_view/new-view'):
                            if (did == item.value['did']):
                                did = item.value['did']
                                id = item.key
                                doc1 = db[id]
                                name = item.value['name']
                                dob = item.value['dob']
                                phone = item.value['phone']
                                loc = source
                                password = item.value['password']
                                doc = {'dob': dob, 'name': name, 'did': did, 'stat': "AVAILABLE", 'phone': phone,
                                       'loc': loc,
                                       'password': password}
                                db.delete(doc1)
                                db.save(doc)



                else:
                    print("Sorry,no driver available at the given locatrion")

            else:
                print("payment unsucessfull")

        Button(plogin, text='login', width=20, bg='brown', fg='white', command=passlogin).place(x=180, y=440)




    Button(passe, text='login', width=20, bg='brown', fg='white',command=login).place(x=180, y=180)
    Button(passe, text='signup', width=20, bg='brown', fg='white',command=passsignup).place(x=180, y=380)



def driver():



    dr = Tk()
    dr.geometry('500x500')
    dr.title("Driver section")

    input1=StringVar()
    input2=StringVar()
    Label(dr ,text="welcome driver",font=("bold",30)).place(x=90,y=40)
    Label(dr,text="driver id",font=("bold",20)).place(x=120,y=120)
    Label(dr,text="password",font=("bold",20)).place(x=120,y=240)
    def test():
        did = e1.get()
        password = e2.get()
        print(did)
        print(password)
        db = couch['driver']
        dc = 0
        p = 0
        for item in db.view('_design/view2/_view/new-view'):
            if (item.key == did):
                if (item.value['password'] == password):
                    print("succefully logined")
                    did = item.key
                    dc = 1
                    db = couch['final-ride']
                    dm = 0
                    p = 1
                    break
        for item in db.view('_design/dv/_view/new-view'):
            if item.value['driverid'] == did:
                dm = 1








                print("you are booked and the details are")
                print("time is ", item.value['time'])
                print("destination", item.value['destination'])
                print("car no is ", item.value['regno'])
                output = "you are booked and the details are"
                output +="    time is %s" %(item.value['time'])
                output +="    destination is %s" %(item.value['destination'])
                output +="    car no is %s  " %(item.value['regno'])
                messagebox.showinfo("driver", output)



        if (dm == "0"):
            print("you are not booked")

        if (p == 0):
            print("wrong password")

        if (dc == "0"):
            print("wrong driver id")







    e1=Entry(dr)
    e2=Entry(dr)
    e1.place(x=240,y=140)
    e2.place(x=240,y=260)


    Button(dr, text='submit', width=20, bg='brown', fg='white',command=test).place(x=180, y=380)
    e1.get()
    e2.get()




root = Tk()
root.geometry('500x500')
root.title("SMART CABS")
label = Label(root, text="welcome to smart cabs",font=("bold",30)).place(x=50,y=100)
Button(root, text='Driver',width=20,bg='brown',fg='white',command=driver).place(x=180,y=180)
Button(root, text='Passenger',width=20,bg='brown',fg='white',command=passenger).place(x=180,y=380)
Button(root, text='Admin',width=20,bg='brown',fg='white',command=seladmin).place(x=180,y=280)
print("test")
root.mainloop()
