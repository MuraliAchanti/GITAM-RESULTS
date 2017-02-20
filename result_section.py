import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
from tkinter import *
import tkinter
import numpy as np
import matplotlib.pyplot as plt


arsenal_1=0
arsenal_2=0
arsenal_3=0
arsenal_4=0
arsenal_5=0
#definitions
def ok_click():
    global sec
    sec = e1.get()
    global sem 
    sem = e2.get()
    root.destroy()

def ok_click2():
    
    def ok_click1():
        def ok_click3():
            root2.destroy()
            if section[0] == 'A':
                global objects
                objects = ['O','A+','A','B+','B','C','P','F','Ab']
                if arsenal_1 == 1:
                    result = [sub1['O'],sub1['A+'],sub1['A'],sub1['B+'],sub1['B'],sub1['C'],sub1['P'],sub1['F'],sub1['Ab']]
                    y_pos = np.arange(len(objects))
                    plt.bar(y_pos,result,align = 'center',alpha = 0.5)
                    plt.xticks(y_pos,objects)
                    plt.title("ELECTIVE: Complex Variables and Transforms")
                    plt.xlabel("Grades")
                    plt.ylabel("No of students")
                    plt.show()
                    plt.close()
                if arsenal_2 == 1:
                    result = [sub2['O'],sub2['A+'],sub2['A'],sub2['B+'],sub2['B'],sub2['C'],sub2['P'],sub2['F'],sub2['Ab']]
                    y_pos = np.arange(len(objects))
                    plt.bar(y_pos,result,align = 'center',alpha = 0.5)
                    plt.xticks(y_pos,objects)
                    plt.title("Signals and Systems")
                    plt.xlabel("Grades")
                    plt.ylabel("No of students")
                    plt.show()
                    plt.close()
                if arsenal_3 == 1:
                    result = [sub3['O'],sub3['A+'],sub3['A'],sub3['B+'],sub3['B'],sub3['C'],sub3['P'],sub3['F'],sub3['Ab']]
                    y_pos = np.arange(len(objects))
                    plt.bar(y_pos,result,align = 'center',alpha = 0.5)
                    plt.xticks(y_pos,objects)
                    plt.title("Electronic Devices and Circuits")
                    plt.xlabel("Grades")
                    plt.ylabel("No of students")
                    plt.show()
                    plt.close()
                if arsenal_4 == 1:
                    result = [sub4['O'],sub4['A+'],sub4['A'],sub4['B+'],sub4['B'],sub4['C'],sub4['P'],sub4['F'],sub4['Ab']]
                    y_pos = np.arange(len(objects))
                    plt.bar(y_pos,result,align = 'center',alpha = 0.5)
                    plt.xticks(y_pos,objects)
                    plt.title("Digital Logic Design")
                    plt.xlabel("Grades")
                    plt.ylabel("No of students")
                    plt.show()
                    plt.close()
                if arsenal_5 == 1:
                    result = [sub5['O'],sub5['A+'],sub5['A'],sub5['B+'],sub5['B'],sub5['C'],sub5['P'],sub5['F'],sub5['Ab']]
                    y_pos = np.arange(len(objects))
                    plt.bar(y_pos,result,align = 'center',alpha = 0.5)
                    plt.xticks(y_pos,objects)
                    plt.title("Electromagnetic Waves")
                    plt.xlabel("Grades")
                    plt.ylabel("No of students")
                    plt.show()
                    plt.close()
            else :
                objects = ['O','A+','A','B+','B','C','P','F','Ab']
                if arsenal_1 == 1:
                    result = [sub1['O'],sub1['A+'],sub1['A'],sub1['B+'],sub1['B'],sub1['C'],sub1['P'],sub1['F'],sub1['Ab']]
                    y_pos = np.arange(len(objects))
                    plt.bar(y_pos,result,align = 'center',alpha = 0.5)
                    plt.xticks(y_pos,objects)
                    plt.title("ELECTIVE: Probability and Statistics")
                    plt.xlabel("Grades")
                    plt.ylabel("No of students")
                    plt.show()
                    plt.close()
                if arsenal_2 == 1:
                    result = [sub2['O'],sub2['A+'],sub2['A'],sub2['B+'],sub2['B'],sub2['C'],sub2['P'],sub2['F'],sub2['Ab']]
                    y_pos = np.arange(len(objects))
                    plt.bar(y_pos,result,align = 'center',alpha = 0.5)
                    plt.xticks(y_pos,objects)
                    plt.title("Object Oriented Programming with C++")
                    plt.xlabel("Grades")
                    plt.ylabel("No of students")
                    plt.show()
                    plt.close() 
                if arsenal_3 == 1:
                    result = [sub3['O'],sub3['A+'],sub3['A'],sub3['B+'],sub3['B'],sub3['C'],sub3['P'],sub3['F'],sub3['Ab']]
                    y_pos = np.arange(len(objects))
                    plt.bar(y_pos,result,align = 'center',alpha = 0.5)
                    plt.xticks(y_pos,objects)
                    plt.title("Computer Organization and Architecture")
                    plt.xlabel("Grades")
                    plt.ylabel("No of students")
                    plt.show()
                    plt.close() 
                if arsenal_4 == 1:
                    result = [sub4['O'],sub4['A+'],sub4['A'],sub4['B+'],sub4['B'],sub4['C'],sub4['P'],sub4['F'],sub4['Ab']]
                    y_pos = np.arange(len(objects))
                    plt.bar(y_pos,result,align = 'center',alpha = 0.5)
                    plt.xticks(y_pos,objects)
                    plt.title("Data Communications")
                    plt.xlabel("Grades")
                    plt.ylabel("No of students")
                    plt.show()
                    plt.close() 
                if arsenal_5 == 1:
                    result = [sub5['O'],sub5['A+'],sub5['A'],sub5['B+'],sub5['B'],sub5['C'],sub5['P'],sub5['F'],sub5['Ab']]
                    y_pos = np.arange(len(objects))
                    plt.bar(y_pos,result,align = 'center',alpha = 0.5)
                    plt.xticks(y_pos,objects)
                    plt.title("Programming Language Pragmatics")
                    plt.xlabel("Grades")
                    plt.ylabel("No of students")
                    plt.show()
                    plt.close()
        main.destroy()
        root2 = Tk()
        root2.geometry("280x100+20+20")
        root2.title("Pass Percentage")
        l5 = Label(root2,text = "Pass Percentage is :")
        l5.grid(row = 0,column = 0,padx = 2,pady = 2)
        l6 = Label(root2,text = pass_o_per)
        l6.grid(row = 0,column = 1)
        l7 = Label(root2,text = "Fail Percentage is :")
        l7.grid(row = 1,column = 0,padx = 2,pady = 2)
        l8 = Label(root2,text = fail_o_per)
        l8.grid(row = 1,column = 1)
        b5 = Button(root2,text = "OK",command = ok_click3)
        b5.grid(row = 2,column = 2,padx =2,pady =2,ipady=2,ipadx=5)
        
    main = Tk()
    main.geometry("400x330+10+10")
    main.title("Gitam Statistics")
    l = Label(main,text = "Grade-wise Statistics")
    l.grid(row = 0,column =0,ipadx = 2,ipady = 2,padx=5,sticky = W)
    lb = Listbox(main,height = 14,width = 60)
    lb.grid(row = 1,column = 0,padx=10,pady=5)
    b = Button(main,text = "OK",command = ok_click1)
    b.grid(row=2,column = 0,ipadx=5,ipady=2,pady = 7,sticky = E)
    sb = Scrollbar(main,orient = VERTICAL)
    sb.grid(row = 1,column = 0,sticky = N + S + E)
    lb.configure(yscrollcommand=sb.set)
    sb.config(command=lb.yview)
    if section[0] == 'A':
        if M.a.get() == 1:
            arsenal_1=1
            lb.insert(END,"ELECTIVE: Complex Variables and Transforms")
            lb.insert(END,"O  :",sub1['O'])
            lb.insert(END,"A+ :",sub1['A+'])
            lb.insert(END,"A  :",sub1['A'])
            lb.insert(END,"B+ :",sub1['B+'])
            lb.insert(END,"B  :",sub1['B'])
            lb.insert(END,"C  :",sub1['C'])
            lb.insert(END,"P  :",sub1['P'])
            lb.insert(END,"F  :",sub1['F'])
            lb.insert(END,"Ab :",sub1['Ab'])
        if M.b.get() == 1:
            arsenal_2=1
            lb.insert(END,"Signals and Systems")
            lb.insert(END,"O  :",sub2['O'])
            lb.insert(END,"A+ :",sub2['A+'])
            lb.insert(END,"A  :",sub2['A'])
            lb.insert(END,"B+ :",sub2['B+'])
            lb.insert(END,"B  :",sub2['B'])
            lb.insert(END,"C  :",sub2['C'])
            lb.insert(END,"P  :",sub2['P'])
            lb.insert(END,"F  :",sub2['F'])
            lb.insert(END,"Ab :",sub2['Ab'])
        if M.c.get() == 1:
            arsenal_3=1
            lb.insert("Electronic Devices and Circuits")
            lb.insert(END,"O  :",sub3['O'])
            lb.insert(END,"A+ :",sub3['A+'])
            lb.insert(END,"A  :",sub3['A'])
            lb.insert(END,"B+ :",sub3['B+'])
            lb.insert(END,"B  :",sub3['B'])
            lb.insert(END,"C  :",sub3['C'])
            lb.insert(END,"P  :",sub3['P'])
            lb.insert(END,"F  :",sub3['F'])
            lb.insert(END,"Ab :",sub3['Ab'])
        if M.d.get() == 1:
            arsenal_4=1
            lb.insert(END,"Digital Logic Design")
            lb.insert(END,"O  :",sub4['O'])
            lb.insert(END,"A+ :",sub4['A+'])
            lb.insert(END,"A  :",sub4['A'])
            lb.insert(END,"B+ :",sub4['B+'])
            lb.insert(END,"B  :",sub4['B'])
            lb.insert(END,"C  :",sub4['C'])
            lb.insert(END,"P  :",sub4['P'])
            lb.insert(END,"F  :",sub4['F'])
            lb.insert(END,"Ab :",sub4['Ab'])
        if M.e.get() == 1:
            arsenal_5=1
            lb.insert(END,"Electromagnetic Waves")
            lb.insert(END,"O  :",sub5['O'])
            lb.insert(END,"A+ :",sub5['A+'])
            lb.insert(END,"A  :",sub5['A'])
            lb.insert(END,"B+ :",sub5['B+'])
            lb.insert(END,"B  :",sub5['B'])
            lb.insert(END,"C  :",sub5['C'])
            lb.insert(END,"P  :",sub5['P'])
            lb.insert(END,"F  :",sub5['F'])
            lb.insert(END,"Ab :",sub5['Ab'])
    else :
        if M.a.get() == 1:
            arsenal_1=1
            lb.insert(END,"ELECTIVE: Probability and Statistics")
            lb.insert(END,"O  :",sub1['O'])
            lb.insert(END,"A+ :",sub1['A+'])
            lb.insert(END,"A  :",sub1['A'])
            lb.insert(END,"B+ :",sub1['B+'])
            lb.insert(END,"B  :",sub1['B'])
            lb.insert(END,"C  :",sub1['C'])
            lb.insert(END,"P  :",sub1['P'])
            lb.insert(END,"F  :",sub1['F'])
            lb.insert(END,"Ab :",sub1['Ab'])
        if M.b.get() == 1:
            arsenal_2=1
            lb.insert(END,"Object Oriented Programming with C++")
            lb.insert(END,"O  :",sub2['O'])
            lb.insert(END,"A+ :",sub2['A+'])
            lb.insert(END,"A  :",sub2['A'])
            lb.insert(END,"B+ :",sub2['B+'])
            lb.insert(END,"B  :",sub2['B'])
            lb.insert(END,"C  :",sub2['C'])
            lb.insert(END,"P  :",sub2['P'])
            lb.insert(END,"F  :",sub2['F'])
            lb.insert(END,"Ab :",sub2['Ab'])
        if M.c.get() == 1:
            arsenal_3=1
            lb.insert(END,"Computer Organization and Architecture")
            lb.insert(END,"O  :",sub3['O'])
            lb.insert(END,"A+ :",sub3['A+'])
            lb.insert(END,"A  :",sub3['A'])
            lb.insert(END,"B+ :",sub3['B+'])
            lb.insert(END,"B  :",sub3['B'])
            lb.insert(END,"C  :",sub3['C'])
            lb.insert(END,"P  :",sub3['P'])
            lb.insert(END,"F  :",sub3['F'])
            lb.insert(END,"Ab :",sub3['Ab'])
        if M.d.get() == 1:
            arsenal_4=1
            lb.insert(END,"Data Communications")
            lb.insert(END,"O  :",sub4['O'])
            lb.insert(END,"A+ :",sub4['A+'])
            lb.insert(END,"A  :",sub4['A'])
            lb.insert(END,"B+ :",sub4['B+'])
            lb.insert(END,"B  :",sub4['B'])
            lb.insert(END,"C  :",sub4['C'])
            lb.insert(END,"P  :",sub4['P'])
            lb.insert(END,"F  :",sub4['F'])
            lb.insert(END,"Ab :",sub4['Ab'])
        if M.e.get() == 1:
            arsenal_5=1
            lb.insert(END,"Programming Language Pragmatics")
            lb.insert(END,"O  :",sub5['O'])
            lb.insert(END,"A+ :",sub5['A+'])
            lb.insert(END,"A  :",sub5['A'])
            lb.insert(END,"B+ :",sub5['B+'])
            lb.insert(END,"B  :",sub5['B'])
            lb.insert(END,"C  :",sub5['C'])
            lb.insert(END,"P  :",sub5['P'])
            lb.insert(END,"F  :",sub5['F'])
            lb.insert(END,"Ab :",sub5['Ab']) 
        root1.destroy()
        
#definitions
class create(Frame):
    def __init__(self,root1):
        self.root1=root1
        self.a = IntVar()
        self.b = IntVar()
        self.c = IntVar()
        self.d = IntVar()
        self.e = IntVar()
        """self.a = IntVar()"""
        if section[0] == 'A':
            self.c1=Checkbutton(self.root1,text = "ELECTIVE: Complex Variables and Transforms",variable=self.a,onvalue=1, offvalue=0)
            self.c1.grid(row=1,column=0,pady=2,sticky=W)
            self.c2=Checkbutton(self.root1,text = "Signals and Systems",variable=self.b,onvalue=1, offvalue=0)
            self.c2.grid(row=2,column=0,pady=2,sticky=W)
            self.c3=Checkbutton(self.root1,text = "Electronic Devices and Circuits",variable=self.c,onvalue=1, offvalue=0)
            self.c3.grid(row=3,column=0,pady=2,sticky=W)
            self.c4=Checkbutton(self.root1,text = "Digital Logic Design",variable=self.d,onvalue=1, offvalue=0)
            self.c4.grid(row=4,column=0,pady=2,sticky=W)
            self.c5=Checkbutton(self.root1,text = "Electromagnetic Waves",variable=self.e,onvalue=1, offvalue=0)
            self.c5.grid(row=5,column=0,pady=4,sticky=W)
            """self.c6=Checkbutton(self.root1,text = "16", onvalue=1, offvalue=0)
            self.c6.grid(row=6,column=0,pady=2,sticky=W)"""
            self.b1=Button(self.root1,text = "OK",command = ok_click2)
            self.b1.grid(row=8,column=1,ipadx=5,ipady=3)    
        else:
            self.c1=Checkbutton(self.root1,text = "ELECTIVE: Probability and Statistics",variable=self.a,onvalue=1, offvalue=0)
            self.c1.grid(row=1,column=0,pady=2,sticky=W)
            self.c2=Checkbutton(self.root1,text = "Object Oriented Programming with C++",variable=self.b,onvalue=1, offvalue=0)
            self.c2.grid(row=2,column=0,pady=2,sticky=W)
            self.c3=Checkbutton(self.root1,text = "Computer Organization and Architecture",variable=self.c,onvalue=1, offvalue=0)
            self.c3.grid(row=3,column=0,pady=2,sticky=W)
            self.c4=Checkbutton(self.root1,text = "Data Communications",variable=self.d,onvalue=1, offvalue=0)
            self.c4.grid(row=4,column=0,pady=2,sticky=W)
            self.c5=Checkbutton(self.root1,text = "Programming Language Pragmatics",variable=self.e,onvalue=1, offvalue=0)
            self.c5.grid(row=5,column=0,pady=2,sticky=W)
            """self.c6=Checkbutton(self.root1,text = "16", onvalue=1, offvalue=0)
            self.c6.grid(row=6,column=0,pady=2,sticky=W)"""
            self.b1=Button(self.root1,text = "OK",command = ok_click2)
            self.b1.grid(row=8,column=1,ipadx=5,ipady=3)



#GUI FOR THE APP
root = Tk()
root.title("Result")
root.geometry("220x150+5+5")
l = Label(root,text = "Please Enter The Section").grid(row=0,column=0,columnspan=2,sticky=W)
l1 = Label(root,text = "Section :").grid(row=1,column=0,padx=2,pady=10,sticky=W)
l2 = Label(root,text = "Semester :").grid(row=2,column=0,padx=2,pady=10,sticky=W)
e1 = Entry(root,width=15)
e1.grid(row=1,column=1,ipady=2)
e2 = Entry(root,width=15)
e2.grid(row=2,column=1,ipady=2)
b = Button(root,text="OK",command = lambda:ok_click())
b.grid(row=3,column=3,ipadx=8,ipady=1)
root.mainloop()
#GUI FOR THE APP

#Browser initializing and etc
driver = webdriver.Chrome()
driver.get('https://doeresults.gitam.edu/onlineresults/pages/Newgrdcrdinput1.aspx')
select = Select(driver.find_element_by_id('cbosem'))
select.select_by_visible_text(sem)
text_field=driver.find_element_by_id('txtreg').clear()
text_field=driver.find_element_by_id('txtreg')


section = list(sec)
m=int(section[1])
#end=int(input("Enter the number of students"))
if section[0] == 'A':
    myid = 1210415000 + (m*100)
elif section[0] == 'B':
    myid = 1210315000 + (m*100)
#n = myid + end Number of students limit
#Browser initializing and etc


#variables for subject statistics
pass_o=0.0
fail_o=0.0
if section[0] == 'A':
    sub_names = ["ELECTIVE: Complex Variables and Transforms","Signals and Systems","Electronic Devices and Circuits","Digital Logic Design","Electromagnetic Waves"]
else :
    sub_names = ["ELECTIVE: Probability and Statistics","Object Oriented Programming with C++","Computer Organization and Architecture","Data Communications","Programming Language Pragmatics"]
sub1 = {}
sub1['O']=0
sub1['A+']=0
sub1['A']=0
sub1['B+']=0
sub1['B']=0
sub1['C']=0
sub1['P']=0
sub1['F']=0
sub1['Ab']=0
sub2 = {}
sub2['O']=0
sub2['A+']=0
sub2['A']=0
sub2['B+']=0
sub2['B']=0
sub2['C']=0
sub2['P']=0
sub2['F']=0
sub2['Ab']=0
sub3 = {}
sub3['O']=0
sub3['A+']=0
sub3['A']=0
sub3['B+']=0
sub3['B']=0
sub3['C']=0
sub3['P']=0
sub3['F']=0
sub3['Ab']=0
sub4 = {}
sub4['O']=0
sub4['A+']=0
sub4['A']=0
sub4['B+']=0
sub4['B']=0
sub4['C']=0
sub4['P']=0
sub4['F']=0
sub4['Ab']=0
sub5 = {}
sub5['O']=0
sub5['A+']=0
sub5['A']=0
sub5['B+']=0
sub5['B']=0
sub5['C']=0
sub5['P']=0
sub5['F']=0
sub5['Ab']=0
sub6 = {}
sub6['O']=0
sub6['A+']=0
sub6['A']=0
sub6['B+']=0
sub6['B']=0
sub6['C']=0
sub6['P']=0
sub6['F']=0
sub6['Ab']=0
#variables for subject statistics


#definitions
def for_sub1():
    if marks[1] == 'O':
        sub1['O'] +=1
    elif marks[0] == 'A' and marks[1] == '+':
        sub1['A+'] += 1
    elif marks[1] == 'A':
        sub1['A'] += 1
    elif marks[0] == 'B' and marks[1] == '+':
        sub1['B+'] += 1
    elif marks[1] == 'B':
        sub1['B'] += 1
    elif marks[1] == 'C':
        sub1['C'] += 1
    elif marks[1] == 'P':
        sub1['P'] += 1    
    elif marks[1] == 'F':
        sub1['F'] += 1
    else:
        sub1['Ab'] +=1
def for_sub2():
    if marks[3] == 'O':
        sub2['O'] +=1
    elif marks[2] == 'A' and marks[3] == '+':
        sub2['A+'] += 1
    elif marks[3] == 'A':
        sub2['A'] += 1
    elif marks[2] == 'B' and marks[3] == '+':
        sub2['B+'] += 1
    elif marks[3] == 'B':
        sub2['B'] += 1
    elif marks[3] == 'C':
        sub2['C'] += 1
    elif marks[3] == 'P':
        sub2['P'] += 1    
    elif marks[3] == 'F':
        sub2['F'] += 1
    else:
        sub2['Ab'] += 1
def for_sub3():
    if marks[5] == 'O':
        sub3['O'] +=1
    elif marks[4] == 'A' and marks[5] == '+':
        sub3['A+'] += 1
    elif marks[5] == 'A':
        sub3['A'] += 1
    elif marks[4] == 'B' and marks[5] == '+':
        sub3['B+'] += 1
    elif marks[5] == 'B':
        sub3['B'] += 1
    elif marks[5] == 'C':
        sub3['C'] += 1
    elif marks[5] == 'P':
        sub3['P'] += 1    
    elif marks[5] == 'F':
        sub3['F'] += 1
    else:
        sub3['Ab'] +=1
def for_sub4():
    if marks[7] == 'O':
        sub4['O'] +=1
    elif marks[6] == 'A' and marks[7] == '+':
        sub4['A+'] += 1
    elif marks[7] == 'A':
        sub4['A'] += 1
    elif marks[6] == 'B' and marks[7] == '+':
        sub4['B+'] += 1
    elif marks[7] == 'B':
        sub4['B'] += 1
    elif marks[7] == 'C':
        sub4['C'] += 1
    elif marks[7] == 'P':
        sub4['P'] += 1    
    elif marks[7] == 'F':
        sub4['F'] += 1
    else:
        sub4['Ab'] +=1
def for_sub5():
    if marks[9] == 'O':
        sub5['O'] +=1
    elif marks[8] == 'A' and marks[9] == '+':
        sub5['A+'] += 1
    elif marks[9] == 'A':
        sub5['A'] += 1
    elif marks[8] == 'B' and marks[9] == '+':
        sub5['B+'] += 1
    elif marks[9] == 'B':
        sub5['B'] += 1
    elif marks[9] == 'C':
        sub5['C'] += 1
    elif marks[9] == 'P':
        sub5['P'] += 1
    elif marks[9] == 'F':
        sub5['F'] += 1
    else:
        sub5['Ab'] +=1
def for_sub6():
    if marks[11] == 'O':
        sub6['O'] +=1
    elif marks[10] == 'A' and marks[11] == '+':
        sub6['A+'] += 1
    elif marks[11] == 'A':
        sub6['A'] += 1
    elif marks[10] == 'B' and marks[11] == '+':
        sub6['B+'] += 1
    elif marks[11] == 'B':
        sub6['B'] += 1
    elif marks[11] == 'C':
        sub6['C'] += 1
    elif marks[11] == 'P':
        sub6['P'] += 1    
    elif marks[11] == 'F':
        sub6['F'] += 1
    else:
        sub6['Ab'] +=1
#definitions
z=5
end = -1
test = 0
while 1 :
    marks = []
    i=0
    grades = open(r'C:\Users\CHINNU\Desktop\mini projects\Result_of _section\grades.txt','r+')
    myid = myid + 1
    end += 1
    text_field=driver.find_element_by_id('txtreg').clear()
    text_field=driver.find_element_by_id('txtreg')
    text_field.send_keys(myid)
    text_field.submit()
    driver.find_element_by_name('Button1').click()
    try :
        elem = driver.find_element_by_id("lblgpa").text
        name = driver.find_element_by_id("lblname").text
        if name != 'lblname':
            table= driver.find_element_by_class_name('table-responsive').text
            grades.write(table)
            grades.seek(39,0)
            """if section[0] == 'B':
                z=5
            else :
                z=6  """
            while i < z:
                m = grades.readline()
                m = list(m)
                marks.append(m[-3])
                marks.append(m[-2])
                i += 1
            #print(marks)
            for_sub1()
            for_sub2()
            for_sub3()
            for_sub4()
            for_sub5()
            """ #for ECE
            if section[0] == 'A':
                for_sub6()
            else:
                pass
            #for ECE """
            """print(name,myid,":",elem)
            print(table)"""
            #overall pass percentage
            if(elem == '0'):
                fail_o +=1
            else:
                pass_o +=1    
            driver.back()
            #overall pass percentage
        elif name == 'lblname':
            if end > 60:
                print("Number of students are :",end)
                break
            else :
                driver.back()
                text_field=driver.find_element_by_id('txtreg')
                text_field.send_keys(myid)
                text_field.submit()
        else:
            raise StudentEnd
    except StudentEnd:
         driver.switch_to_alert().accept()
         driver.get('https://doeresults.gitam.edu/onlineresults/pages/Newgrdcrdinput1.aspx')
         print(name,"Has left the College")
         select = Select(driver.find_element_by_id('cbosem'))
         select.select_by_visible_text('3')
    grades.close()
    grades = open(r'C:\Users\CHINNU\Desktop\mini projects\Result_of _section\grades.txt','w')
    grades.close()
fail_o_per= float((fail_o / end)*100)
pass_o_per= float((pass_o / end)*100)


#CHECKBOX



#LISTBOX    



#result

root1 = Tk()
root1.title("Gitam Statistics")
root1.geometry("320x210+10+10")
M = create(root1)
driver.close()
 
            
