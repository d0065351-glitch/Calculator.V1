import tkinter as tk

root= tk.Tk()
root.title("My Calculator")
root.geometry("300x500")


entry = tk.Entry(root, width=20,font=("Arial",18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

def click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0,current+str(number))

def clear(): 
    entry.delete(0, tk.END)   

def add():
    global first_number
    global operation

    first_number = int(entry.get())      
    operation = "add"
    entry.delete(0, tk.END)

def sub():
    global first_number
    global operation

    first_number = int(entry.get())      
    operation = "sub"
    entry.delete(0, tk.END)

def mul():
    global first_number
    global operation

    first_number = int(entry.get())      
    operation = "mul"
    entry.delete(0, tk.END)                                     

def div():
    global first_number
    global operation

    first_number = int(entry.get())      
    operation = "div"
    entry.delete(0, tk.END)

def equal(): 
    second_number = int(entry.get())
    entry.delete(0, tk.END)

    if operation == "add":
        entry.insert(0, first_number + second_number) 
    elif operation == "sub":
        entry.insert(0, first_number - second_number) 
    elif operation == "mul": 
        entry.insert(0, first_number * second_number)
    elif operation == "div":
        entry.insert(0, first_number / second_number)

bottons = []
for i in range(1,10):
    btn = tk.Button(root, text=str(i), padx=20, pady=20, command=lambda x=i: click(x))
    bottons.append(btn)

#btn1 = tk.Button(root, text="1", padx=20, pady=20, command=lambda: click(1))
#btn2 = tk.Button(root, text="2", padx=20, pady=20, command=lambda: click(2))
#btn3 = tk.Button(root, text="3", padx=20, pady=20, command=lambda: click(3))

#btn4 = tk.Button(root, text="4", padx=20, pady=20, command=lambda: click(4))
#btn5 = tk.Button(root, text="5", padx=20, pady=20, command=lambda: click(5))
#btn6 = tk.Button(root, text="6", padx=20, pady=20, command=lambda: click(6))

#btn7 = tk.Button(root, text="7", padx=20, pady=20, command=lambda: click(7))
#btn8 = tk.Button(root, text="8", padx=20, pady=20, command=lambda: click(8))
#btn9 = tk.Button(root, text="9", padx=20, pady=20, command=lambda: click(9))

btn0 = tk.Button(root, text="0", padx=20, pady=20, command=lambda: click(0))
btn_dot=tk.Button(root, text=".", padx=20, pady=20, command=lambda: click("."))

for i in range(3):
    bottons[i].grid(row=3, column=i)
    bottons[i+3].grid(row=2, column=i)
    bottons[i+6].grid(row=1, column=i)
    

#btn7.grid(row=1, column=0)
#btn8.grid(row=1, column=1)
#btn9.grid(row=1, column=2)

#btn4.grid(row=2, column=0)
#btn5.grid(row=2, column=1)
#btn6.grid(row=2, column=2)

#btn1.grid(row=3, column=0)
#btn2.grid(row=3, column=1)
#btn3.grid(row=3, column=2)

btn0.grid(row=4, column=0)

for j in range(4):
    met=[add,sub,mul,div]
    sign=["+","-","*","/"]
    btn=tk.Button(root, text=sign[j], padx=20, pady=20, command=met[j])
    btn.grid(row=4-j, column=3)

#btn_add = tk.Button(root, text="+", padx=20, pady=20, command=add)
#btn_sub = tk.Button(root, text="-", padx=20, pady=20, command=sub)
#btn_mul = tk.Button(root, text="*", padx=20, pady=20, command=mul)
#btn_div = tk.Button(root, text="/", padx=20, pady=20, command=div)
btn_equal = tk.Button(root, text="=", padx=20, pady=20, command=equal)
btn_clear = tk.Button(root, text="C", padx=20, pady=20, command=clear)

#btn_add.grid(row=4, column=3)
#btn_sub.grid(row=3, column=3)
#btn_mul.grid(row=2, column=3)
#btn_div.grid(row=1, column=3)
btn_equal.grid(row=4, column=2)
btn_clear.grid(row=4, column=1)

root.mainloop() 