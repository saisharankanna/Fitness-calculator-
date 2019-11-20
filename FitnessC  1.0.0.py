#============Importing Tkinter===========================================================================================================
from tkinter import *
#============Importing Pillow============================================================================================================
from PIL import ImageTk,Image
#============Importing Sqlite3===========================================================================================================
import sqlite3
#============Importing Tkinter Message Box===============================================================================================
import tkinter.messagebox as m
#============Creating Database===========================================================================================================
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
class FitnessCalculator:
                def __init__(self):
                    calculator=Tk()
                    calculator.title('Fitness Calculator')
                    #calculator.resizable(0,0)
                    calculator.geometry('1600x800')
                    #frames defining                    
                    mann = Frame(calculator,width = 1600,height=700,relief=SUNKEN)
                    mann.pack(side=TOP)
                    manns1 = Frame(calculator,width = 1600,height=700,relief=SUNKEN)
                    manns1.pack()
                    manns2 = Frame(calculator,width = 1600,height=700,relief=SUNKEN)
                    #manns2.pack(side=BOTTOM)

                    #Main Label
                    #lblinfo = Label(mann, font=( 'aria' ,30, 'bold' ),text="FITNESS CALUCULATOR",fg="steel blue",bd=10)
                    #lblinfo.place(x=400,y=10)

                    #Name and Age Entry Fields 
                    name=StringVar()
                    age=IntVar()
                    Label(manns1,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='Name : ',width=10).grid(row=1,column=1)
                    Entry(manns1,font=( 'Bradley Hand ITC' ,14, 'bold' ),width=16,relief='ridge',bd=2,textvariable=name).grid(row=1,column=2)
                    Label(manns1,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='Age : ',width=10).grid(row=1,column=3)
                    Entry(manns1,font=( 'Bradley Hand ITC' ,14, 'bold' ),width=16,relief='ridge',bd=2,textvariable=age).grid(row=1,column=4)
                     
                    #The Gender Radio Button
                    v=IntVar()
                    Label(manns1,text='Gender : ',font=( 'Bradley Hand ITC' ,14, 'bold' )).grid(row=2,column=1)
                    Radiobutton(manns1,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='Male',variable=v,value=1).grid(row=2,column=2,padx=30)
                    Radiobutton(manns1,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='Female',variable=v,value=2).grid(row=2,column=4,padx=100)
                    
                    #Generating the fields for Entry Fields
                    fields=('Weight (Kg)','Height (Mts)','BP Low (Systolic) mm/Hg','BP High (Diastolic) mm/Hg','Pulse Rate','RBC Count (trillion Cells/L)','WBC Count (billions cells/L)','Platelets','HB','Uric Acid (mg/dL)','Cholestrol (mg/dL)')
                    r=3
                    entries=[]
                    for field in fields:
                        Label(manns1,font=( 'Bradley Hand ITC' ,14, 'bold' ),text=field+' : ',width=30,bg='grey',fg='white').grid(row=r,column=1,sticky='NWSWSE')
                        en=Entry(manns1,width=30,relief='ridge',bd=2)
                        en.grid(row=r,column=2,sticky='NWSWSE')
                        entries.append(en)
                        r+=1
                    #Report Label
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='Report Of',width=30,bg='black',fg='white').grid(row=14,column=1,sticky='NWSWSE') 
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),width=30,fg='black',bg='gainsboro',textvariable=name).grid(row=14,column=2,sticky='NWSWSE') 


                    #Results TextVariables
                    bmi_calculated=StringVar()
                    bp_calc=StringVar()
                    pulse_calulated=StringVar()
                    cholestrol_calculated=StringVar()
                    wbc_final=StringVar()
                    rbc_final=StringVar()
                    platelets_final=StringVar()
                    uric_acid=StringVar()
                    haemoglobin_calc=StringVar()
             

                    #Final_Labels
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='BMI (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=15,column=1,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='BP (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=16,column=1,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='Pulse Rate (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=17,column=1,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='RBC Count (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=18,column=1,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='WBC Count (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=19,column=1,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='Platelets (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=20,column=1,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='HB (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=21,column=1,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='Uric Acid (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=22,column=1,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='Cholestrol (High/Medium/Low)',width=30,bg='grey',fg='white').grid(row=23,column=1,sticky='NWSWSE')


                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='BMI (High/Medium/Low)',width=30,fg='black',bg='gainsboro',textvariable=bmi_calculated).grid(row=15,column=2,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='BP (High/Normal/Low)',width=30,fg='black',bg='gainsboro',textvariable=bp_calc).grid(row=16,column=2,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='Pulse Rate (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=pulse_calulated).grid(row=17,column=2,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='RBC Count (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=rbc_final).grid(row=18,column=2,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='WBC Count (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=wbc_final).grid(row=19,column=2,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='Platelets (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=platelets_final).grid(row=20,column=2,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='HB (High/Medium/Low)',width=30,fg='black',bg='gainsboro',textvariable=haemoglobin_calc).grid(row=21,column=2,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='Uric Acid (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=uric_acid).grid(row=22,column=2,sticky='NWSWSE')
                    Label(manns2,font=( 'Bradley Hand ITC' ,14, 'bold' ),text='Cholestrol (High/Medium/Low)',width=30,bg='gainsboro',fg='black',textvariable=cholestrol_calculated).grid(row=23,column=2,sticky='NWSWSE')
                        
                    #making the bottom Label
                    Label(mann,bg='black',fg='white',width=30).grid(row=25,column=1,ipadx=5)
                    def logout():
                        calculator.destroy()
                        main1()
                        #calculator.destroy()
                    def get_entries():
                        print(name.get())
                        print(age.get())
                        for entry in entries:
                          print(entry.get())
                        f=open("REPORT.txt","a")
                        f.write("------------------------------------------------------------------------------------------------------------------------------------\n")
                        f.write("******************************************--------D E T A I L S--------*************************************\n")
                        f.write("------------------------------------------------------------------------------------------------------------------------------------\n")
                        f.write("Name-->")
                        f.write(name.get())
                        f.write("\n Age : %d \n" %age.get())
                        if v.get()==1 :
                            f.write("Gender-->Male\n")
                        else:
                            f.write("Gender-->Female\n")
                        f.close()
                        
                    #BMI calculator
                    def calculate_bmi():
                        weight=float(entries[0].get())
                        height=float(entries[1].get())
                        f=open("REPORT.txt","a")
                        f.write("\n------------------------------------------------------------------------------------------------------------------------------------\n")
                        f.write("\nWeight                                     -->          %f" %weight)
                        f.write("\nHeight                                      -->          %f" %height)
                        f.close()
                        bmi=(weight/height)/height
                        if bmi < 15:
                            value='Low'
                        elif bmi >15 and bmi<20:
                            value='Medium'
                        else:
                            value='High'
                        f=open("REPORT.txt","a")
                        f.write("\nBMI(VALUE)                           -->          %f" %bmi)
                        f.write("\nBMI (STATUS)                      -->          ")
                        f.write(value)
                        f.close()
                        bmi_calculated.set(value)
                        

                    
                    def blood_pressure():
                        bpl=int(entries[2].get())
                        bph=int(entries[3].get())
                        f=open("REPORT.txt","a")
                        f.write("\nBP Low                                    -->          %d" %bpl)
                        f.write("\nBP High                                   -->        %d" %bph)
                        if bph>120 and bph <140 and bpl>80 and bpl<90:
                            b_value='Normal'
                        elif(bph>=140 and bpl>=90):
                            b_value='High'
                        else:
                             b_value='Low'
                        f.write("\nBP                                             -->        ")
                        f.write(b_value)
                        f.close()       
                        bp_calc.set(b_value) 

                        
                    
                    #Pulse Monitor
                    def pulse_rate():
                        pulse=int(entries[4].get())
                        f=open("REPORT.txt","a")
                        f.write("\nPulse Rate(VALUE)              -->          %d" %pulse)
                        if pulse <72:
                            p_value='Low'
                        elif pulse >72 and pulse <90:
                            p_value='Medium'
                        elif pulse > 90:
                            p_value='High'
                        f.write("\nPulse Rate(STATUS)          -->")
                        f.write(p_value)
                        pulse_calulated.set(p_value)


                    #Blood Monitor
                    def blood_monitor():
                        rbc=float(entries[5].get())
                        wbc=float(entries[6].get())
                        platelets=float(entries[7].get())
                        haemoglobin=float(entries[8].get())
                        f=open("REPORT.txt","a")
                        f.write("\n------------------------------------------------------------------------------------------------------------------------------------\n")
                        f.write("\nRed Blood Cells                      -->       %f" %rbc)
                        f.write("\nWhite Blood Cells                   -->       %f" %wbc)
                        f.write("\nPlatelets                                    -->        %f" %platelets)
                        f.write("\nHemaglobin                              -->      %f" %haemoglobin)
                        f.close()
                        
                       
                       #calculating Haemoglobin Levels

                        if haemoglobin >=13 and haemoglobin <=16:
                            h_value='Medium'
                        elif haemoglobin >16:
                            h_value='High'
                        elif haemoglobin <13:
                            h_value='Low'
                      # calculating rbc levels 

                        if rbc >= 4.32 and rbc <= 5.72:
                            r_value='Medium'
                        elif rbc < 4.32:
                            r_value='Low'
                        elif rbc>5.72:
                            r_value='High'

                    #calculating wbc values 
                        if wbc >3 and wbc<10:
                            w_value='Medium'
                        elif wbc<3:
                            w_value='Low'
                        elif wbc>10:
                            w_value='High'
                    #calculating platelets levels 

                        if platelets >150 and platelets <450:
                           p_value='Medium'
                        elif platelets<150:
                            p_value='Low'
                        elif platelets>450:
                            p_value='High'
                        f=open("REPORT.txt","a")
                        f.write("\nHemaglobin                              -->      ")
                        f.write(h_value)
                        f.write("\nRed Blood Cells                      -->      ")
                        f.write(r_value)
                        f.write("\nWhite Blood Cells                   -->       ")
                        f.write(w_value)
                        f.write("\nPlatelets                                    -->       ")
                        f.write(p_value)
                        f.write("\n------------------------------------------------------------------------------------------------------------------------------------\n")
                        f.close()
                        #setting Label Values 
                        haemoglobin_calc.set(h_value) 
                        rbc_final.set(r_value)
                        wbc_final.set(w_value)
                        platelets_final.set(p_value)


                    #urine Monitor
                    def urine_monitor():
                        urine=float(entries[9].get())
                        f=open("REPORT.txt","a")                       
                        f.write("\nUric Acid-->%f" %urine)
                        if urine > 4 and urine <8.5:
                            value='Medium'
                        elif urine <4:
                            value='Low'
                        elif urine > 8.5:
                            value='High'
                        f.write("\nUric Acid-->")
                        f.write(value)
                        f.close()
                        uric_acid.set(value)


                    #get Cholestrol
                    def get_cholestrol():
                        cholestrol=float(entries[10].get())
                        f=open("REPORT.txt","a")
                        f.write("\n\nCholestrol--> %f" %cholestrol)
                        f.close()
                        if cholestrol <200:
                            value='Low (Good)'
                        elif cholestrol >200 and cholestrol<239:
                            value='Medium'
                        elif cholestrol>240:
                            value='High'
                        f=open("REPORT.txt","a")
                        f.write("\nCholestrol-->")
                        f.write(value)
                        f.write("\n------------------------------------------------------------------------------------------------------------------------------------\n")
                        f.close()
                        cholestrol_calculated.set(value)

                    def show_results():
                        name.set(name.get())
                        get_entries()
                        calculate_bmi()
                        blood_pressure()
                        pulse_rate()
                        blood_monitor()
                        urine_monitor()
                        get_cholestrol()
                        manns1.pack_forget()
                        manns2.pack()

                        
#*********************************************************************************************************************************************************************************
                 
#*********************************************************************************************************************************************************************************

                        

                    #Button to Show the results of the report 
                    Button(manns1,text="Show Report",relief='ridge',bg='grey',fg='white',bd=2,command=show_results).grid(row=14,column=4,ipadx=4)
                    Button(manns1,text="Logout",relief='ridge',bg='grey',fg='white',bd=2,command=lambda:logout()).grid(row=15,column=4,ipadx=4)
                    Button(manns2,text="Logout",relief='ridge',bg='grey',fg='white',bd=2,command=logout).grid(row=15,column=4,ipadx=4)

                    #Initiating the GUI mainloop Instance (event loop)
                    calculator.mainloop()




            #calling the default constructor to create the GUI
    #FitnessCalculator()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def main1():
    db=sqlite3.connect("Fitnesscalc.db")
    c=db.cursor()
    #============GUI WINDOW==================================================================================================================
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------
    root=Tk()
    root.geometry("1600x800")
    root.title("Fitness Caluculator")
    Tops = Frame(root,width = 1600,height=100,relief=SUNKEN)
    Tops.pack(side=TOP)
    f1 = Frame(root,width = 1600,height=700,relief=SUNKEN)
    f1.pack(side=BOTTOM)

    #========================================================================================================================================
    def createaccount():
        f2.pack()
        f1.pack_forget()
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def logout():
        print("Hey")
        calculator.destroy()
        
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def enter():
        f1.pack()
        f2.pack_forget()


    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def SignUp():
        c.execute("INSERT INTO userdata VALUES(?,?,?,?,?)",(name.get(),name1.get(),mobile.get(),password.get(),dob.get()))
        db.commit()
        #d=c.execute("SELECT * FROM userdata")
        #print(d.fetchall())
        f2.pack_forget()
        f1.pack()
    def logint():
        num=username.get()
        pwd=password1.get()
        with sqlite3.connect ("Fitnesscalc.db") as db:
            cursor=db.cursor()
        find_user=('SELECT * FROM userdata WHERE mobile=? AND password = ?')
        cursor.execute (find_user,[(num),(pwd)])
        results=cursor.fetchall()

        if results:
            m.showinfo("Valid user","Sucessfully LoggedIn")
            root.destroy()
            FitnessCalculator()
        else:
            m.showerror("Error In Logging In","Invalid Username/Password")
    #=======================================================================================================================================================
                                                             #GUI
    #=======================================================================================================================================================
    lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="FITNESS CALUCULATOR",fg="steel blue",bd=10)
    lblinfo.place(x=400,y=10)
    i=ImageTk.PhotoImage(Image.open("S:\Eduction\Sem-3\Python\Programs\Project\Main()\image1122.jpg"))
    Label(f1,image=i,height=700,width=1600).pack(side=BOTTOM)
    username=StringVar()
    password1=StringVar()
    login=Label(f1,font=('aria',30),bg='black',fg='white',text="Mobile No",bd=5,anchor=N)
    login.place(x=1000,y=150)
    txtlogin=Entry(f1,font=('ariel' ,16,'bold') , bd=6,insertwidth=10 ,bg="powder blue" ,justify='left',textvariable=username)
    txtlogin.place(x=1000,y=200)
    passs=Label(f1,font=('aria',30),text="Password",bg="black",fg="white",bd=5,anchor=N)
    passs.place(x=1000,y=250)
    txtpassword=Entry(f1,font=('ariel' ,16,'bold') ,show='*', bd=6,insertwidth=4,bg="powder blue" ,justify='left',textvariable=password1)
    txtpassword.place(x=1000,y=300)
    b1 = Button(f1, text="Login",anchor=W,bd=6,command=lambda:logint())
    b1.place(x=1075,y=350)
    b1 = Button(f1, text="SignUp",anchor=W,bd=6,command=lambda:createaccount())
    b1.place(x=1070,y=400)
    
    #=========================================================================================================================================================
    f2 = Frame(root,width = 1600,height=700,relief=SUNKEN)
    f2.pack(side=BOTTOM)
    j=ImageTk.PhotoImage(Image.open("S:\Eduction\Sem-3\Python\Programs\Project\Main()\image1111.jpg"))
    Label(f2,image=j,height=700,width=1600).pack(side=BOTTOM)
    name=StringVar()
    name1=StringVar()
    mobile=StringVar()
    password=StringVar()
    dob=StringVar()
    la1=Label(f2,font=('ariel' ,20,'bold'),text="First Name",bg='grey').place(x=50,y=0)
    en1=Entry(f2,font=('ariel' ,20,'bold'),bg="powder blue" ,border=1,textvariable=name)
    en1.place(x=50,y=50)
    la2=Label(f2,font=('ariel' ,20,'bold'),bg='grey',text="Last Name").place(x=800,y=0)
    en2=Entry(f2,font=('ariel' ,20,'bold'),bg="powder blue" ,border=1,textvariable=name1)
    en2.place(x=800,y=50)
    la3=Label(f2,font=('ariel' ,20,'bold'),bg='grey',text="Mobile Number  ").place(x=50,y=100)
    en3=Entry(f2,font=('ariel' ,20,'bold'),bg="powder blue" ,border=1,textvariable=mobile)
    en3.place(x=50,y=150)
    la4=Label(f2,font=('ariel' ,20,'bold'),bg='grey',text="Password",).place(x=800,y=100)
    en4=Entry(f2,font=('ariel' ,20,'bold'),bg="powder blue" ,border=1,textvariable=password,show="*")
    en4.place(x=800,y=150)
    la4=Label(f2,font=('ariel' ,20,'bold'),bg='grey',text="Date of birth",).place(x=50,y=200)
    en4=Entry(f2,font=('ariel' ,20,'bold'),bg="powder blue" ,border=1,textvariable=dob)
    en4.place(x=50,y=250)
    button=Button(f2,text="Sign Up",bd=6,command=lambda:SignUp())
    button.place(x=545,y=450)
    b1 = Button(f2, text="Login",bd=6,command=lambda:enter())
    b1.place(x=550,y=500)
    #=========================================================================================================================================================
    #f3=Frame(root,width = 1600,height=700,relief=SUNKEN)
    #f2.pack(side=BOTTOM)
    #=========================================================================================================================================================
    #f1.pack()
    #c.execute("CREATE TABLE userdata(firstname TEXT,lastname TEXT, mobilenumber TEXT primary  key not null,password  TEXT)")
    #c.execute("ALTER TABLE userdata ADD COLUMN dob INT")
    #c.execute("delete from userdata")
    #db.commit()
    #db.close()
    root.mainloop()
main1()
