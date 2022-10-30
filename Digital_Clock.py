from tkinter import *
# tkinter is used to make graphics
import datetime
# datetime module is used to work with date and time related tasks
def date_time():
    '''This function is used to change the graphics of the clock with the help of datetime module'''
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%Y')
    day = time.strftime('%a')


    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    lab_hr.after(200,date_time)

# calling the Tk class and storing in a variable
clock = Tk()
clock.title('*************FARHAN DIGITAL CLOCK*************')
clock.geometry('1000x500') #setting the size of the screen
clock.config(bg='green') #setting the background color of the screen


''' The codes are used to make the boxes in the specific dimensions and label them with appropriate text
,font,bg,fg etc'''
lab_hr =Label(clock,text = '00',font=('Time New Roman',40,'bold'),bg='red',fg='white')
lab_hr.place(x=120,y=50,height=110,width=100)
lab_hr_text =Label(clock,text = 'Hours',font=('Time New Roman',20,'bold'),bg='red',fg='white')
lab_hr_text.place(x=120,y=190,height=40,width=100)

lab_min =Label(clock,text = '00',font=('Time New Roman',40,'bold'),bg='red',fg='white')
lab_min.place(x=340,y=50,height=110,width=100)
lab_min_text =Label(clock,text = 'Min',font=('Time New Roman',20,'bold'),bg='red',fg='white')
lab_min_text.place(x=340,y=190,height=40,width=100)

lab_sec =Label(clock,text = '00',font=('Time New Roman',40,'bold'),bg='red',fg='white')
lab_sec.place(x=560,y=50,height=110,width=100)
lab_sec_text =Label(clock,text = 'Sec',font=('Time New Roman',20,'bold'),bg='red',fg='white')
lab_sec_text.place(x=560,y=190,height=40,width=100)

lab_am =Label(clock,text = '00',font=('Time New Roman',40,'bold'),bg='red',fg='white')
lab_am.place(x=780,y=50,height=110,width=100)
lab_am_text =Label(clock,text = 'AM/PM',font=('Time New Roman',20,'bold'),bg='red',fg='white')
lab_am_text.place(x=780,y=190,height=40,width=100)

lab_date =Label(clock,text = '00',font=('Time New Roman',40,'bold'),bg='red',fg='white')
lab_date.place(x=120,y=270,height=110,width=100)
lab_date_text =Label(clock,text = 'Date',font=('Time New Roman',20,'bold'),bg='red',fg='white')
lab_date_text.place(x=120,y=410,height=40,width=100)

lab_mo =Label(clock,text = '00',font=('Time New Roman',40,'bold'),bg='red',fg='white')
lab_mo.place(x=340,y=270,height=110,width=100)
lab_mo_text =Label(clock,text = 'Month',font=('Time New Roman',20,'bold'),bg='red',fg='white')
lab_mo_text.place(x=340,y=410,height=40,width=100)

lab_year =Label(clock,text = '00',font=('Time New Roman',30,'bold'),bg='red',fg='white')
lab_year.place(x=560,y=270,height=110,width=100)
lab_year_text =Label(clock,text = 'Year',font=('Time New Roman',20,'bold'),bg='red',fg='white')
lab_year_text.place(x=560,y=410,height=40,width=100)

lab_day =Label(clock,text = '00',font=('Time New Roman',30,'bold'),bg='red',fg='white')
lab_day.place(x=780,y=270,height=110,width=100)
lab_day_text =Label(clock,text = 'Day',font=('Time New Roman',20,'bold'),bg='red',fg='white')
lab_day_text.place(x=780,y=410,height=40,width=100)

# Calling the function 
date_time()

clock.mainloop()