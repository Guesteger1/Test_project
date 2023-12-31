import tkinter as tk

def add_digit(digit):
    value=calc.get()
    if value[0]=='0'and len(value)==1:
        value=value[1:]
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)

def add_operation(operation):
    value=calc.get()
    if value[-1] in '-+/*':
        value=value[:-1]
    elif '+'in value or '-'in value or '/'in value or '*'in value:
          Calculate()
          value=calc.get()
    calc.delete(0,tk.END)
    calc.insert(0,value+operation)

def Calculate():
    value=calc.get()
    if value[-1] in '+-*/':
        value=value+value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,eval(value))

def clear():
    calc.delete(0,tk.END)
    calc.insert(0,0)

def make_digit_button(digit):
    return tk.Button(window,text=digit,bd=5,font=('Arial',15),command=lambda:add_digit(digit))

def make_operation_button(operation):
    return tk.Button(window,text=operation, bd=5, font=('Arial',15), 
                     command=lambda:add_operation(operation),
                     fg='red'
                     )

def make_calc_button(operation):
    return tk.Button(window,text=operation, bd=5, font=('Arial',15), 
                     command=Calculate,
                     fg='green'
                     )

def make_clear_button(operation):
    return tk.Button(window,text=operation, bd=5, font=('Arial',15), 
                     command=clear,
                     )


window=tk.Tk()
window.geometry(f"250x280+300+200")
window['bg']='#33ffe6'
window.title('Калькулятор')

calc=tk.Entry(window,justify=tk.RIGHT,font=('Arial',15),bd=5,width=15)
calc.insert(0,'0')
calc.grid(row=0,column=0,columnspan=4,padx=5,sticky='we')

make_digit_button('1').grid(row=1,column=0,stick='wens',padx=3,pady=3)
make_digit_button('2').grid(row=1,column=1,stick='wens',padx=3,pady=3)
make_digit_button('3').grid(row=1,column=2,stick='wens',padx=3,pady=3)
make_digit_button('4').grid(row=2,column=0,stick='wens',padx=3,pady=3)
make_digit_button('5').grid(row=2,column=1,stick='wens',padx=3,pady=3)
make_digit_button('6').grid(row=2,column=2,stick='wens',padx=3,pady=3)
make_digit_button('7').grid(row=3,column=0,stick='wens',padx=3,pady=3)
make_digit_button('8').grid(row=3,column=1,stick='wens',padx=3,pady=3)
make_digit_button('9').grid(row=3,column=2,stick='wens',padx=3,pady=3)
make_digit_button('0').grid(row=4,column=0,stick='wens',padx=3,pady=3)

make_operation_button('+').grid(row=1,column=3,stick='wens',padx=3,pady=3)
make_operation_button('-').grid(row=2,column=3,stick='wens',padx=3,pady=3)
make_operation_button('*').grid(row=3,column=3,stick='wens',padx=3,pady=3)
make_operation_button('/').grid(row=4,column=3,stick='wens',padx=3,pady=3)

make_calc_button('=').grid(row=4,column=2,stick='wens',padx=3,pady=3)
make_clear_button('C').grid(row=4,column=1,stick='wens',padx=3,pady=3)


window.grid_columnconfigure(0,minsize=60)
window.grid_columnconfigure(1,minsize=60)
window.grid_columnconfigure(2,minsize=60)
window.grid_columnconfigure(3,minsize=60)

window.grid_rowconfigure(1,minsize=60)
window.grid_rowconfigure(2,minsize=60)
window.grid_rowconfigure(3,minsize=60)
window.grid_rowconfigure(4,minsize=60)





window.mainloop()