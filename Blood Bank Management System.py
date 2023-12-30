#------------------------------------------------------------------------------------------------------------------------
#                                           BLOOD BANK MANAGEMANT SYSTEM
#------------------------------------------------------------------------------------------------------------------------
#BBMS Project
#By - Vedant Sudhir Patil
#------------------------------------------------------------------------------------------------------------------------


import mysql.connector

#options in the
#donor menu

def donor():
    print("-"*64+"\n"," "*30 + "MENU" + " "*30,"\n"+"-"*64,"\n"+
          " 1. Sign In / Make Profile\n",
          "2. View Profile\n",
          "3. Edit Profile\n",
          "4. Donate your Blood (Book an Appointment)\n",
          "5. Request for Blood\n",
          "6. Certificate/Proof of Blood Donation")
    opt=int(input("Enter Your Choice :"))
    if opt == 1:
        auth_donor()
        #sign up of user
    elif opt == 2:
        view_donor()
        #view donor
    elif opt == 3:
        edit_donor()
        #edit log in donor
    elif opt == 4:
        donate_donor()
        #donate donor
    elif opt == 5:
        request_donor()
        #request donor
    elif opt == 6:
        Proof_donor()
        """certificate for
        blood donation"""
    elif opt == 9:
        doclist()
    else:
        print("Choose a Valid Option")
        
#options in the
#doctor menu        

def doctor():
    print("-"*64+"\n"," "*30 + "MENU" + " "*30,"\n"+"-"*64,"\n"+
          " 1. Authorise Patients to Recieve Blood\n",
          "2. View Doctor's Profile\n",
          "3. Edit Doctor's Name\n")
    opt=int(input("Enter Your Choice :"))
    if opt == 1:
        approve_doctor()
    elif opt == 2:
        view_doctor()
    elif opt == 3:
        editname_doctor()
    elif opt == 9:
        print(".")    
    else:
        print("Choose a Valid Option")

#to authorise
#a doctor

def auth_donor():
    try:
        ans=input("Do you have a profile (Y/N) ?:")
        if ans.upper() == 'Y':
            donid = int(input(str("ID : ")))
            passw= input(str("Password : "))
            query_vals = (donid, passw )
            db=mysql.connector.connect(host="localhost",
                                       user="root",password="password",
                                       database="bloodbankcopy")
            cursor=db.cursor()
            cursor.execute("select * from don" )
            data=cursor.fetchall()
            for i in list(data):
                if i[0:2] == query_vals:
                    print("Welcome ", i[2])
                    break
        elif ans.upper()=='N':
            db=mysql.connector.connect(host="localhost",
                                       user="root",password="password",
                                       database="bloodbankcopy")
            cursor=db.cursor()
            cursor.execute("select donid from don order by donid desc" )
            data=cursor.fetchall()
            par=data[0:1]
            n=""
            for i in par:
                n=int(i[0])
            donid=n+1
            print("Your ID is ",donid)
            donpass=input(str("Enter a Password for your Profile:"))
            donname=input(str("Enter your Name :"))
            bloodgp=input(str("Enter your Blood Group :"))
            doncity=input(str("Enter your City Name :"))
            donstate=input(str("Enter your State / Union Territory Name :"))
            val=(str(donid),donpass,donname,bloodgp,doncity,donstate)
            cursor.execute("insert into don"
                           "(donid,donpass,donname,bloodgp,doncity,donstate)"
                           "values (%s,%s,%s,%s,%s,%s)",val)
            db.commit()
            print("Information submitted succesfully as :- \nID : ",donid,
                  "\nPassword : ",donpass,
                  "\nName : ",donname,
                  "\nBlood Group : ",bloodgp,
                  "\nCity : ",doncity,
                  "\nState : ",donstate)
        else:
            print("Enter a valid option")
    except:
        print("Try Again")

#to view donor
#from id

def view_donor():
    try:
        donid = int(input(str("ID : ")))
        db=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from don" )
        data=cursor.fetchall()
        flg=0
        for i in list(data):
            if i[0] == (donid):
                print("Information retrieved :- \nID : ",i[0],
                      "\nPassword : ",i[1],
                      "\nName : ",i[2],
                      "\nBlood Group : ",i[3],
                      "\nCity : ",i[4],
                      "\nState : ",i[5])
                flg=1
                break
            else:
                print("")
        if flg==0:
            print("Check your ID and Try Again")
    except:
        print("Try Again")
    main()

#to display
#list of doctors

def doclist():
    donid = int(input(str("ID : ")))
    db=mysql.connector.connect(host="localhost",
                               user="root",
                               password="password",
                               database="bloodbankcopy")
    cursor=db.cursor()
    cursor.execute("select * from doclist" )
    data=cursor.fetchall()
    print("Information retrieved :- \nID : ",i[0],
          "\nPassword : ",i[1],
          "nName : ",i[2])
    print("")  

#to edit name
#of the given donor    

def edit_donor():
    try:
        donid = int(input(str("ID : ")))
        donpass= input(str("Password : "))
        query_vals = (donid, donpass )
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from don" )
        data=cursor.fetchall()
        for i in list(data):
            if i[0:2] == query_vals:
                upd = "update don set donid = %s,"
                "donpass = %s, donname = %s,"
                "bloodgp = %s, doncity = %s,"
                "donstate = %s where donid = %s"
                donname=input(str("Enter new Name :"))
                bloodgp=input(str("Enter new Blood Group :"))
                doncity=input(str("Enter new City Name :"))
                donstate=input(str("Enter new State / Union Territory Name :"))
                input1=(donid, donpass, donname, bloodgp, doncity, donstate, donid)
                cursor.execute(upd, input1)
                db.commit()
                print("Information Updated Succesfully")
                break
    except:
        print("Check your Information and Try Again")
    main()    

#to donate blood
#for donor

def donate_donor():
    try:
        donid = int(input(str("ID : ")))
        passw= input(str("Password : "))
        query_vals = (donid, passw )
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from don" )
        dat=cursor.fetchall()
        info=""
        for i in list(dat):
            if i[0:2] == query_vals:
                info=i
                break
        did=info[0]
        dpass=info[1]
        dname=info[2]
        bloodgp=info[3]
        dcity=info[4]
        dstate=info[5]
        val=(str(did),dpass,dname,bloodgp,dcity,dstate)
        cursor.execute("insert into donlist"
                       "(did,dpass,dname,bloodgp,dcity,dstate)"
                       "values (%s,%s,%s,%s,%s,%s)",val)
        db.commit()
        print("Your information is stored for appointment")
        cursor.execute("select * from campadd ")
        exe=cursor.fetchall()
        for i in exe:
            if i[2].upper() == dcity.upper():
                print ("The nearest blood donation camp is :-\nCamp ID : ",i[0],
                       "\nCamp Adress : ",i[1],
                       "\nCamp City : ",i[2],
                       "\nCamp State : ",i[3])
    except:
        print("Check your Information and Try Again")
    main()    

#to request blood
#from donor

def request_donor():
    try:
        donid = int(input(str("ID : ")))
        passw= input(str("Password : "))
        query_vals = (donid, passw )
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from don" )
        dat=cursor.fetchall()
        info=""
        for i in list(dat):
            if i[0:2] == query_vals:
                info=i
                break
        nid=info[0]
        npass=info[1]
        nname=info[2]
        ncity=info[4]
        nstate=info[5]
        needgp=input(str("Enter the blood group you want :"))
        val=(str(nid),npass,nname,ncity,nstate,needgp)
        cursor.execute("insert into needlist"
                       "(nid,npass,nname,ncity,nstate,needgp)"
                       "values (%s,%s,%s,%s,%s,%s)",val)
        db.commit()
        print("Your information will be sent to doctor for approval")
        cursor.execute("select * from campadd ")
        exe=cursor.fetchall()
        for i in exe:
            if i[2].upper() == ncity.upper():
                print ("The nearest blood donation camp is :-\nCamp ID : ",i[0],
                       "\nCamp Adress :",i[1],
                       "\nCamp City :",i[2],
                       "\nCamp State : ",i[3])
    except:
        print("Check your Information and Try Again")
    main()    


#to print certificate
#of blood donation

def Proof_donor():
    try:
        donid = int(input(str("ID : ")))
        passw= input(str("Password : "))
        query_vals = (donid, passw )
        db=mysql.connector.connect(host="localhost",user="root",
                                   password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from donlist" )
        dat=cursor.fetchall()
        info=""
        for i in list(dat):
            if i[0:2] == query_vals:
                print("You have donated your blood.")
                print("-"*61+"\n"," "*25 + "CERTIFICATE" + " "*25,
                      "\n"+"-"*61,"\n"+"Sir/Madam ",i[2],
                      ", \nYou have succesfully donated your ",i[3],
                      " blood to a blood bank.\nThank You")
                break
    except:
        print("Check your information and Try Again")
    main()    

#to authorise doctors

def auth_doctor():
    try:
        global flag2
        flag2=0
        docid = input(str("ID : "))
        passw= input(str("Password : "))
        name=input(str("Name :"))
        query_vals = (docid, passw, name )
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from doclist" )
        data=cursor.fetchall()
        for i in list(data):
            if i == query_vals:
                print("Welcome Dr.",name) 
                flag2=1
            else :
                break
    except:
        print("Check your Information and Try Again")
    doctor()    


#to approve donor
#to donate blood

def approve_doctor():
    try:
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from needlist" )
        dat=cursor.fetchall()
        info=""
        for i in list(dat):
            if i[6]== None:
                print(i)
                inp=input("Approve ? (Y/N) :")
                if inp.upper()== "Y":
                    upd = "update needlist set nid = %s,npass = %s,"
                    "nname = %s,ncity = %s, nstate = %s,"
                    "needgp = %s,approve = %s where nid = %s"
                    nid=i[0]
                    npass=i[1]
                    nname=i[2]
                    ncity=i[3]
                    nstate=i[4]
                    needgp=i[5]
                    approve="YES"
                    input1=(nid, npass, nname, ncity, nstate, needgp, approve, nid)
                    cursor.execute(upd, input1)
                    db.commit()
                    print("Approved")
    except:
        print("Try Again")
    doctor()     


#to view the list
#of existing doctors by ID

def view_doctor():
    try:
        docid = input(str("Doctor's ID : "))
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from doclist" )
        data=cursor.fetchall()
        flg=0
        for i in list(data):
            if i[0] == (docid):
                print("Information retrieved :- \nID : ",i[0],
                      "\nPassword : ",i[1],
                      "\nName : ",i[2])
                flg=1
                break
            else:
                print("")
        if flg==0:
            print("Check your ID and Try Again")
    except:
        print("Try Again")
    doctor()     



#to edit the names
#of existing doctors
    
def editname_doctor():
    try:
        docid = input(str("Doctor's ID : "))
        docpass= input(str("Doctor's Password : "))
        query_vals = (docid, docpass )
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from doclist" )
        data=cursor.fetchall()
        for i in list(data):
            if i[0:2] == query_vals:
                upd = "update doclist set docid = %s,"
                "docpass = %s,"
                "docname = %s where docid = %s"
                docname=input(str("Enter your edited Name :"))
                input1=(docid, docpass, docname, docid)
                cursor.execute(upd, input1)
                db.commit()
                print("Information Updated Succesfully")
                break
    except:
        print("Try Again")
    doctor()

    

#main

def main():
    print("-"*64+"\n"," "*30 + "MENU" + " "*30,"\n"+"-"*64)
    ask=int(input("1. Donor\n2. Doctor\n\nYou are (1 or 2) :"))
    if ask == 1:
        donor()
    elif ask == 2:
        auth_doctor()
        if flag2==1:
            doctor()
        else :
            print("Try Again")
    elif ask == 9:
        verification()       
    else:
        print("Choose a valid option")

#verify the password
#and id of admin

def verification():
    user=input("Enter username :")
    passw=input("Enter password :")
    if user=="admin123" and passw=="pass123":
        admin()



#options in
#the admin menu

def admin():
    print("-"*64+"\n",
          " "*30 + "MENU" + " "*30,
          "\n"+"-"*64,
          "\n"+" 1. Add Camps\n",
          "2. Show all \n",
          "3. Remove Donors\n",
          "4. Add Doctors\n",
          "5. Remove Doctors\n",
          "6. Change Username and Password of Admin")
    loop="YES"
    while loop.upper()=="YES":
        opt=int(input("Enter Your Choice :"))
        if opt == 1:
            add_camps()
        elif opt == 2:
            show_all()
        elif opt == 3:
            remove_donors()
        elif opt == 4:
            add_doctors()
        elif opt == 5:
            remove_doctors()
        elif opt == 6:
            change_login_details()
        else:
            print("Choose a Valid Option")
        loop=input("Want to continue ? (YES / NO):")



#It will be for
#adding camps 

def add_camps():
    try:
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        rep=1
        while rep==1:
            cursor.execute("select campid from campadd order by campid desc" )
            data=cursor.fetchall()
            par=data[0:1]
            n=""
            for i in par:
                n=int(i[0])
                break
            campid=n+1
            camploc=input(str("Enter the location of Camp :"))
            campcity=input(str("Enter the City Name :"))
            campstate=input(str("Enter the State / Union Territory Name :"))
            val=(str(campid),camploc,campcity,campstate)
            cursor.execute("insert into campadd(campid,camploc,campcity,campstate)"
                           "values(%s,%s,%s,%s)",val)
            db.commit()
            print("Information submitted succesfully as :- \nID : ",campid,
                  "\nLocation : ",camploc,
                  "\nName : ",campcity,
                  "\nState : ",campstate)
            rep=int(input("Want to add more camps (1-->Yes,0-->No) :"))
    except:
        print("Try again")


#It will be for
#removing donors

def remove_donors():
    db=mysql.connector.connect(host="localhost",
                               user="root",password="password",
                               database="bloodbankcopy")
    cursor=db.cursor()
    cursor.execute("select * from don" )
    data=cursor.fetchall()
    for i in list(data):
        print(i[0],space(i[0]),i[1],space(i[1]),i[2],space(i[2]),i[3],space(i[3]),i[4],space(i[4]),i[5])
    delete=input("Enter ID of donor, you want to delete : ")
    cursor.execute("delete from don where donid=%s",delete)
    db.commit()
    print("Entry deleted successfully")




#It will be for
#removing doctors

def remove_doctors():
    db=mysql.connector.connect(host="localhost",
                               user="root",password="password",
                               database="bloodbankcopy")
    cursor=db.cursor()
    cursor.execute("select * from doclist" )
    data=cursor.fetchall()
    for i in list(data):
        print(i[0],
        space(i[0]),i[1],space(i[1]),i[2])
    delete=input("Enter ID of doctor, you want to delete (D 0XX):")
    condition="delete fron doclist where docid=%s"
    cursor.execute(condition,delete)
    db.commit()
    print("Entry deleted successfully")



#Adding doctors

def add_doctors():
    try:
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        rep=1
        while rep==1:
            cursor.execute("select campid from campadd order by campid desc" )
            data=cursor.fetchall()
            par=data[0:1]
            for i in par:
                print(i)
                break
            docid=input(str("Enter the ID of new doctor"
                            "(greater than the showed no.):"))
            docpass=input(str("Enter the Password of new doctor :"))
            docname=input(str("Enter the new Doctor's Name :"))
            val=(docid,docpass,docname)
            cursor.execute("insert into doclist (docid,docpass,docname) values (%s,%s,%s)",val)
            db.commit()
            print("Information submitted succesfully as :- \nID : ",docid,
                  "\nPassword : ",docpass,
                  "\nName : ",docname)
            rep=int(input("Want to add more doctors (1-->Yes,0-->No) :"))
    except:
        print("Try again")



#Changing admin's
#username & password

def change_login_details():
    global username_admin
    global password_admin
    new_user=input("Enter new username :")
    new_passw=input("Enter new password :")
    username_admin=new_user
    password_admin=new_passw




#Function to make
#space while display

def space(x):
    sp=""
    l=15-(len(str(x)))
    for i in range(l):
        sp+=" "
    return sp



#To show all
#the records

def show_all():
    print(" 1. Show all Donors\n",
          "2. Show all Doctors\n",
          "3. Show all Camps\n",
          "4. Show all the People who have donated\n",
          "5. Show all the People who need donations\n")
    k=int(input("Enter your choice :"))
    if k==1:
        show_all_donors()
    elif k==2:
        show_all_doctors()
    elif k==3:
        show_all_camps()
    elif k==4:
        show_donators()
    elif k==5:
        show_recievers()
    else:
        print("Choose from the above options ")


          
#To show records
#of all the donors

def show_all_donors():
    try:
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from don" )
        data=cursor.fetchall()
        for i in list(data):
            print(i[0],
                  space(i[0]),
                  i[1],space(i[1]),
                  i[2],space(i[2]),
                  i[3],space(i[3]),
                  i[4],space(i[4]),i[5])
    except:
        print("Try Again")



#To show records
#of all the doctors  

def show_all_doctors():
    try:
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from doclist" )
        data=cursor.fetchall()
        for i in list(data):
            print(i[0],
                  space(i[0]),
                  i[1],space(i[1]),
                  i[2])
    except:
        print("Try Again")



#To show records
#of all the camps

def show_all_camps():
    try:
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from campadd" )
        data=cursor.fetchall()
        for i in list(data):
            print(i[0],
                  space(i[0]),
                  i[1],space(i[1]),
                  i[2],space(i[2]),i[3])
    except:
        print("Try Again")



#To show records
#of all the people
#who have donated

def show_donators():
    try:
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from donlist" )
        data=cursor.fetchall()
        for i in list(data):
            print(i[0],
                  space(i[0]),
                  i[1],space(i[1]),
                  i[2],space(i[2]),
                  i[3],space(i[3]),
                  i[4],space(i[4]),i[5])
    except:
        print("Try Again")



#To show records
#of all the people
#who want donations 

def show_recievers():
    try:
        db=mysql.connector.connect(host="localhost",
                                   user="root",password="password",
                                   database="bloodbankcopy")
        cursor=db.cursor()
        cursor.execute("select * from don" )
        data=cursor.fetchall()
        for i in list(data):
            print(i[0],
                  space(i[0]),
                  i[1],space(i[1]),
                  i[2],space(i[2]),
                  i[3],space(i[3]),
                  i[4],space(i[4]),
                  i[5],i[6],space(i[6]))
    except:
        print("Try Again")        

main()

#------------------------------------------------------------------------------------------------------------------------
#                                           BLOOD BANK MANAGEMANT SYSTEM
#------------------------------------------------------------------------------------------------------------------------
#The Function Used Are :-
#donor()
#doctor()
#auth_donor()
#view_donor()
#donate_donor()
#edit_donor()
#request_donor()
#Proof_donor()
#view_doctor()
#auth_doctor()
#approve_doctor()
#editname_doctor()
#verification()
#admin()
#add_camps()
#remove_donors()
#remove_doctors()
#add_doctors()
#verification()
#show_all()
#show_recievers()
#show_donators()
#show_all_camps()
#------------------------------------------------------------------------------------------------------------------------
