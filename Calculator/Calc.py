from tkinter import *
import parser,math
from builtins import Exception

cal = Tk(bg="Black")
cal.title("MyCalculator")
display = Entry(cal)
display.grid(row=0,columnspan = 6,sticky=W+E)

i=0
def get_variable(num):
    global i
    display.insert(i,num)
    i+=1

def fact(num):
    global i
    clear_all()
    b = math.factorial(int(num))
    display.insert(0,b)
    i = 0
    i += len(str(b))
def clear_all():
    display.delete(0, END)

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0,"Error")

def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")


#adding numeric buttons
Button(cal,text="1",command = lambda: get_variable(1)).grid(row=1,column=0)
Button(cal,text="2",command = lambda: get_variable(2)).grid(row=1,column=1)
Button(cal,text="3",command = lambda: get_variable(3)).grid(row=1,column=2)
Button(cal,text="4",command = lambda: get_variable(4)).grid(row=2,column=0)
Button(cal,text="5",command = lambda: get_variable(5)).grid(row=2,column=1)
Button(cal,text="6",command = lambda: get_variable(6)).grid(row=2,column=2)
Button(cal,text="7",command = lambda: get_variable(7)).grid(row=3,column=0)
Button(cal,text="8",command = lambda: get_variable(8)).grid(row=3,column=1)
Button(cal,text="9",command = lambda: get_variable(9)).grid(row=3,column=2)
Button(cal,text="0",command = lambda: get_variable(0)).grid(row=4,column=1)

#adding operations
Button(cal,text="=",command = lambda: calculate()).grid(row=4,column=0)
Button(cal,text="AC",command = lambda: clear_all()).grid(row=4,column=2)

Button(cal,text="+",command = lambda: get_operation("+")).grid(row=1,column=3)
Button(cal,text="-",command = lambda: get_operation("-")).grid(row=2,column=3)
Button(cal,text="*",command = lambda: get_operation("*")).grid(row=3,column=3)
Button(cal,text="/",command = lambda: get_operation("/")).grid(row=4,column=3)
Button(cal,text="%",command = lambda: get_operation("%")).grid(row=1,column=4)
Button(cal,text="(",command = lambda: get_operation("(")).grid(row=2,column=4)
Button(cal,text="pi",command = lambda: get_operation("*3.14")).grid(row=3,column=4)
Button(cal,text="^2",command = lambda: get_operation("**2")).grid(row=4,column=4)
Button(cal,text="<-",command = lambda: undo()).grid(row=1,column=5)
Button(cal,text=")").grid(row=2,column=5)
Button(cal,text="exp",command = lambda: get_operation("**")).grid(row=3,column=5)
Button(cal,text="X!",command = lambda: fact(display.get())).grid(row=4,column=5)
cal.mainloop()
