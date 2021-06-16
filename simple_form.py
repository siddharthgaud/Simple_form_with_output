from tkinter import *
from tkinter import ttk



root=Tk()
root.geometry("800x800")
root.title("simple form")
root.config(bg="pink")
# sb = Scrollbar(root)  
# sb.pack(side = RIGHT, fill = Y)  
  


# functionality

def display():
    data1=str(var1.get())
    data2=str(var2.get())
    data3=str(var3.get())
    data4=str(var4.get())
    python_value=var5.get()
    java_value=var6.get()
    HTML_value=var7.get()
    CSS_value=var8.get()
    
    msg1="your name is "+data1
    msg2="your age is "+str(data2)
    msg3="your location is "+data3
    msg4="you are "+data4

    if python_value==1:
        o_l5.config(text="you selected the option python")
    else:
        o_l5.config(text="python option not selected")   

    if java_value==1:
        o_l6.config(text="you selected the option java")
    else:
        o_l6.config(text="java option not selected")    

    if HTML_value==1:
        o_l7.config(text="you selected the option HTML")
    else:
        o_l7.config(text="HTML option not selected")    

    if CSS_value==1:
        o_l8.config(text="you selected the option CSS")
    else:
        o_l8.config(text="CSS option not selected") 

    cb_value=str(cb.get())
    msg="you selected the option "+cb_value


    o_l1.config(text=msg1)
    o_l2.config(text=msg2)
    o_l3.config(text=msg3)
    o_l4.config(text=msg4)
    o_l9.config(text=msg)
    

l1=Label(root,text="simple form",font=("arial",20,"bold",UNDERLINE),bg="cyan",fg="blue")
l1.pack()

# label


l2=Label(root,text="Name",font=("arial",15),bg="cyan",fg="red",)
l2.place(x=20,y=60)


l2=Label(root,text="Age",font=("arial",15),bg="cyan",fg="red")
l2.place(x=20,y=100)


l2=Label(root,text="Location",font=("arial",15),bg="cyan",fg="red")
l2.place(x=20,y=140)


l2=Label(root,text="Gender",font=("arial",15),bg="cyan",fg="red",)
l2.place(x=20,y=180)

l2=Label(root,text="Select Language",font=("arial",15),bg="cyan",fg="red")
l2.place(x=20,y=260)

l2=Label(root,text="select Branch",font=("arial",15),bg="cyan",fg="red")
l2.place(x=20,y=390)

branch=["select Branch","EXTC","Mechanical","Computer Science","Information Technology"]


cb=ttk.Combobox(root,values=branch,font=(0.5))
cb.place(x=200,y=400)
cb.current(0)

# entry


var1=StringVar()
e1=Entry(root,font=("arial",12),textvariable=var1)
e1.place(x=130,y=60)

var2=StringVar()
e1=Entry(root,font=("arial",12),textvariable=var2)
e1.place(x=130,y=100)

var3=StringVar()
e1=Entry(root,font=("arial",12),textvariable=var3)
e1.place(x=130,y=140)

# radiobutton

var4=StringVar()

r1=Radiobutton(root,text="Male", variable=var4, value="Male")
r1.place(x=130,y=180)

r1=Radiobutton(root,text="Female", variable=var4, value="Female")
r1.place(x=130,y=210)

# checkbox

var5=IntVar()
c1=Checkbutton(root,text="python",variable=var5)
c1.place(x=200,y=260)

var6=IntVar()
c2=Checkbutton(root,text="java",variable=var6)
c2.place(x=200,y=290)


var7=IntVar()
c3=Checkbutton(root,text="HTML",variable=var7)
c3.place(x=200,y=320)


var8=IntVar()
c4=Checkbutton(root,text="CSS",variable=var8)
c4.place(x=200,y=350)



# button 

var=StringVar()
b1=Button(root,text="show",font=("arial",15),bg="cyan",fg="blue",command=display)
b1.place(x=200,y=520)

# output

o_l1=Label(root,font=("arial",15),bg="pink",fg="red")
o_l1.place(x=350,y=60)

o_l2=Label(root,font=("arial",15),bg="pink",fg="red")
o_l2.place(x=350,y=90)

o_l3=Label(root,font=("arial",15),bg="pink",fg="red")
o_l3.place(x=350,y=120)

o_l4=Label(root,font=("arial",15),bg="pink",fg="red")
o_l4.place(x=350,y=150)

o_l5=Label(root,font=("arial",15),bg="pink",fg="red")
o_l5.place(x=350,y=180)

o_l6=Label(root,font=("arial",15),bg="pink",fg="red")
o_l6.place(x=350,y=210)

o_l7=Label(root,font=("arial",15),bg="pink",fg="red")
o_l7.place(x=350,y=240)

o_l8=Label(root,font=("arial",15),bg="pink",fg="red")
o_l8.place(x=350,y=270)

o_l9=Label(root,font=("arial",15),bg="pink",fg="red")
o_l9.place(x=350,y=310)

root.mainloop()