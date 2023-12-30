import tkinter as tk

def on_numeric_key_press(value):
    entry.focus_set()
    current_value = entry.get()
    new_value = current_value + str(value)
    entry.delete(0, tk.END)
    entry.insert(0, new_value)

def perform_calculation():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def calculate_percentage():
    try:
        expression = entry.get()
        result = eval(expression) / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)

def delete_last():
    current_value = entry.get()[:-1]
    entry.delete(0, tk.END)
    entry.insert(0, current_value)

def bind_enter_key(event):
    perform_calculation()   

root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg='black')
root.bind('<Return>', bind_enter_key)

entry = tk.Entry(root, width=20, font=("Arial", 25), bg='black', fg='white', bd=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

keys = [
    'C','Del','%','/', 
    '7', '8', '9','*',
    '4', '5', '6','-',
    '1', '2', '3','+',
    '0', '.', '='
]

row_val = 1
col_val = 0

for key in keys:
    if key in ['/', '*', '-', '+', '=']:
        if key == '=':
            tk.Button(root, text=key, width=5, font=("Arial", 16), bg='orange',
                      command=lambda val=key: perform_calculation() if val == '=' else entry.insert(tk.END, val)).grid(row=row_val, column=col_val, padx=5, pady=5)
        else:
            tk.Button(root, text=key, width=5, font=("Arial", 16), bg='gray', fg='white',
                      command=lambda val=key: perform_calculation() if val == '=' else entry.insert(tk.END, val)).grid(row=row_val, column=col_val, padx=5, pady=5)
    elif key == 'C':
        tk.Button(root, text=key, width=5, font=("Arial", 16), bg='red', fg='white', command=clear_entry).grid(row=row_val, column=col_val, padx=5, pady=5)
    elif key == 'Del':
        tk.Button(root, text=key, width=5, font=("Arial", 16), bg='red', fg='white', command=delete_last).grid(row=row_val, column=col_val, padx=5, pady=5)
    elif key == '%':
        tk.Button(root, text=key, width=5, font=("Arial", 16), bg='blue', fg='white', command=calculate_percentage).grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        tk.Button(root, text=key, width=5, font=("Arial", 16), bg='lightblue', fg='black',
                  command=lambda val=key: on_numeric_key_press(val)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if key == '0':
        col_val -= 1
        tk.Button(root, text=key, width=14, font=("Arial", 16), bg='lightblue', fg='black',
                  command=lambda val=key: on_numeric_key_press(val)).grid(row=row_val, column=col_val, columnspan=2, padx=5, pady=5)
        col_val += 2
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
