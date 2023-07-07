from tkinter import *
from tkinter import ttk
import re
from tkinter  import messagebox
#from math import sin, cos, tan, factorial, sqrt, fabs, log2, log10
from math import *


root = Tk()
root.title("Tkinter Calc")
root.geometry()
root.option_add("*tearOff", FALSE)
root.resizable(False, False)

#Func for menu
def about():
    messagebox.showinfo("TKinter Calc", "Autor: bolgaro4ka (https://github.com/bolgaro4ka)\nVersion: 1.0a")

def destroy():
    root.destroy()
    
#Menu
program_menu = Menu()
program_menu.add_command(label="Exit", command=destroy)


main_menu = Menu()
main_menu.add_cascade(label="Programm", menu=program_menu)
main_menu.add_cascade(label="About", command=about)

#Func

#-FOR NUMBERS
def imp_1():
    global data
    data.set(data.get()+'1')
    
def imp_2():
    global data
    data.set(data.get()+'2')
    
def imp_3():
    global data
    data.set(data.get()+'3')
    
def imp_4():
    global data
    data.set(data.get()+'4')
    
def imp_5():
    global data
    data.set(data.get()+'5')
    
def imp_6():
    global data
    data.set(data.get()+'6')
    
def imp_7():
    global data
    data.set(data.get()+'7')
    
def imp_8():
    global data
    data.set(data.get()+'8')
    
def imp_9():
    global data
    data.set(data.get()+'9')
    
def imp_0():
    global data
    data.set(data.get()+'0')
    
#-FOR SIMBOLS
def imp_plus():
    global data
    data.set(data.get()+'+')
    
def imp_minus():
    global data
    data.set(data.get()+'-')
    
def imp_division():
    global data
    data.set(data.get()+'/')
    
def imp_multiply():
    global data
    data.set(data.get()+'*')
    
def imp_dot():
    global data
    data.set(data.get()+'.')
    
#-FOR equals and del
def imp_equals(*args):
    global data
    try:
        example=data.get()
        res=eval(data.get())
        data.set(res)
        history_listbox.insert(0, (str(example)+str(' = ')+str(data.get())))
        
    except ZeroDivisionError: 
        data.set("Division by zero")
    except Exception:
        if data.get() == "Error!": data.set('')
        else: data.set("Error!")
    

    
def imp_all_clear():
    global data
    res=data.set("")
    
def imp_not_all_clear():
    global data
    data.set(data.get()[0:-1])
    
#-For sin-cos-tg-(-)
def imp_right_bracket():
    global data
    data.set(data.get()+')')

def imp_left_bracket():
    global data
    data.set(data.get()+'(')
    
def imp_sin():
    global data
    data.set(data.get()+'sin')
    
def imp_cos():
    global data
    data.set(data.get()+'cos')
    
def imp_tan():
    global data
    data.set(data.get()+'tan')
    
#-FOR MATH FUNC

def imp_square():
    global data
    data.set(data.get()+'**2')
    
def imp_square_other():
    global data
    data.set(data.get()+'**')
    
def imp_factorial():
    global data
    data.set(data.get()+'factorial')
    
def imp_mod():
    global data
    data.set(data.get()+'fabs')
    
def imp_per():
    global data
    data.set(data.get()+'%')
    
def imp_log2():
    global data
    data.set(data.get()+'log2')
    
def imp_log10():
    global data
    data.set(data.get()+'log10')
  
def imp_sqrt():
    global data
    data.set(data.get()+'sqrt')
    
def imp_pi():
    global data
    data.set(data.get()+'pi')
    
def imp_e():
    global data
    data.set(data.get()+'e')
    
def imp_ten():
    global data
    data.set(data.get()+'*10**')
    
def imp_log():
    global data
    data.set(data.get()+'log')
    
def imp_hex():
    global data
    data.set(data.get()+'hex')
    
def imp_oct():
    global data
    data.set(data.get()+'oct')
    
def imp_bin():
    global data
    data.set(data.get()+'bin')
    
def imp_int():
    global data
    data.set(data.get()+'int')
    
def imp_ceil():
    global data
    try:
        example=data.get()
        res=eval(example)
        data.set(round(res))
        history_listbox.insert(0, (str(example)+str(' ≈ ')+str(data.get())))
    
    except ZeroDivisionError: 
        data.set("Division by zero")
    except Exception:
        if data.get() == "Error!": data.set('')
        else: data.set("Error!")

#Variable
data=StringVar()
history = []
history1 = Variable(value=history)

#-ENTRY
entry=ttk.Entry(textvariable=data, width=62)
entry.grid(row=3, column=0, columnspan=5)

#-LIST_HISTORY
history_listbox = Listbox(listvariable=history1, height=10, width=62, relief=GROOVE)
 
history_listbox.grid(column=0, row=0, columnspan=5, rowspan=3)


#-BUTTONS


#--NUMBERS
btn1=ttk.Button(text='1', command=imp_1)
btn1.grid(row=4, column=0)

btn2=ttk.Button(text='2', command=imp_2)
btn2.grid(column=1, row=4)

btn3=ttk.Button(text='3', command=imp_3)
btn3.grid(column=2, row=4)

btn4=ttk.Button(text='4', command=imp_4)
btn4.grid(column=0, row=5)

btn5=ttk.Button(text='5', command=imp_5)
btn5.grid(column=1, row=5)

btn6=ttk.Button(text='6', command=imp_6)
btn6.grid(column=2, row=5)

btn7=ttk.Button(text='7', command=imp_7)
btn7.grid(column=0, row=6)

btn8=ttk.Button(text='8', command=imp_8)
btn8.grid(column=1, row=6)

btn9=ttk.Button(text='9', command=imp_9)
btn9.grid(column=2, row=6)

btn0=ttk.Button(text='0', command=imp_0)
btn0.grid(column=1, row=7)


#--SYMBOLS
btnplus=ttk.Button(text='+', command=imp_plus)
btnplus.grid(column=3, row=4)

btn=ttk.Button(text='-', command=imp_minus)
btn.grid(column=3, row=5)

btn=ttk.Button(text='*', command=imp_multiply)
btn.grid(column=3, row=6)

btn=ttk.Button(text='/', command=imp_division)
btn.grid(column=3, row=7)

btnr=ttk.Button(text='=', command=imp_equals)
btnr.grid(column=2, row=7, rowspan=2, ipady=13)

btn=ttk.Button(text='.', command=imp_dot)
btn.grid(column=0, row=7)

btn=ttk.Button(text='AC', command=imp_all_clear)
btn.grid(column=6, row=3)

btn=ttk.Button(text='C', command=imp_not_all_clear)
btn.grid(column=5, row=3)

btn=ttk.Button(text='(', command=imp_left_bracket)
btn.grid(column=4, row=4)

btn=ttk.Button(text=')', command=imp_right_bracket)
btn.grid(column=4, row=5)

#SIN-COS-TG

btn=ttk.Button(text='sin(x)', command=imp_sin)
btn.grid(column=5, row=4)

btn=ttk.Button(text='cos(x)', command=imp_cos)
btn.grid(column=5, row=5)

btn=ttk.Button(text='tan(x)', command=imp_tan)
btn.grid(column=5, row=6)

#OTHER

btn=ttk.Button(text='x^2', command=imp_square)
btn.grid(column=4, row=6)

btn=ttk.Button(text='x^y', command=imp_square_other)
btn.grid(column=0, row=8)

btn=ttk.Button(text='x!', command=imp_factorial)
btn.grid(column=5, row=7)


btn=ttk.Button(text='|x|', command=imp_mod)
btn.grid(column=6, row=4)

btn=ttk.Button(text='√x', command=imp_sqrt)
btn.grid(column=6, row=5)

btn=ttk.Button(text='log2(x)', command=imp_log2)
btn.grid(column=6, row=6)

btn=ttk.Button(text='log10(x)', command=imp_log10)
btn.grid(column=6, row=7)

btn=ttk.Button(text='π', command=imp_pi)
btn.grid(column=4, row=7)

btn=ttk.Button(text='e', command=imp_e)
btn.grid(column=4, row=8)

btn=ttk.Button(text='*10^', command=imp_ten)
btn.grid(column=5, row=8)

btn=ttk.Button(text='ln', command=imp_log)
btn.grid(column=6, row=8)

btn=ttk.Button(text='≈', command=imp_ceil)
btn.grid(column=1, row=8)

btn=ttk.Button(text='%', command=imp_per)
btn.grid(column=3, row=8)
#

btn=ttk.Button(text='bin(x)', command=imp_bin)
btn.grid(column=5, row=0, ipady=28)

btn=ttk.Button(text='oct(x)', command=imp_oct)
btn.grid(column=6, row=0, ipady=28)

btn=ttk.Button(text='hex(x)', command=imp_hex)
btn.grid(column=5, row=1, ipady=28)

btn=ttk.Button(text="int('x', base)", command=imp_int)
btn.grid(column=6, row=1, ipady=28)


#btnr.bind("<KP_Enter>", imp_equals)

root.config(menu=main_menu)
root.mainloop()