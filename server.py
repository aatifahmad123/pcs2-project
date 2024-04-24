import tkinter as tk
import random
import string

# Password
def generate_password():
    password = ''.join(random.choices(string.digits, k=8))
    return password

# Start button
def create_start_button():
    global start_button
    start_button = tk.Button(root, text='Start', bg='#38b000', fg='#0b090a', font=('Arial', 20, 'bold'),command=start_button_clicked)
    start_button.place(relx=0.5, rely=0.7, anchor='center')

# Function to handle button click event
def button_clicked():
    password = generate_password()
    global label_password
    label_password = tk.Label(root, text=password, bg='#0b090a', fg='#38b000', font=('Arial', 20, 'bold'))
    label_password.place(relx=0.5, rely=0.6, anchor='center')
    create_start_button()

def start_button_clicked():
    label_password.destroy()
    start_button.destroy()
    button.destroy()
    question_text = tk.Text(root, bg='#252422', fg='#ffffff', font=('Arial', 14),height=5,width=25)
    question_text.place(relx=0.5, rely=0.2, anchor='center')
    question_text.focus_set()


    option1 = tk.Text(root, bg='#252422', fg='#ffffff', font=('Arial', 14),height=1,width=25)
    option1.place(relx=0.5, rely=0.4, anchor='center')
    option1.focus_set()

    option2 = tk.Text(root, bg='#252422', fg='#ffffff', font=('Arial', 14),height=1,width=25)
    option2.place(relx=0.5, rely=0.5, anchor='center')
    option2.focus_set()

    option3 = tk.Text(root, bg='#252422', fg='#ffffff', font=('Arial', 14),height=1,width=25)
    option3.place(relx=0.5, rely=0.6, anchor='center')
    option3.focus_set()

    option4 = tk.Text(root, bg='#252422', fg='#ffffff', font=('Arial', 14),height=1,width=25)
    option4.place(relx=0.5, rely=0.7, anchor='center')
    option4.focus_set()

    submit_button = tk.Button(root, text='Submit', bg='#38b000', fg='#0b090a', font=('Arial', 16, 'bold'),command=submit_quiz)
    submit_button.place(relx=0.5, rely=0.85, anchor='center')


def submit_quiz():
    timer = 30
    global timer_label
    timer_label = tk.Label(root, text='', bg='#0b090a',fg='#38b000',font=('Arial', 16))
    timer_label.place(x=332,y=3)
    set_timer(timer)

def set_timer(number):
    if number > 0:
        timer_label.config(text=str(number))
        number -= 1
        root.after(1000, set_timer, number)
    else:
        timer_label.config(text='')


# window
root = tk.Tk()

# title
root.title('Server')

# size
root.geometry('360x640')

# window bg-color
root.configure(bg='#0b090a')

label = tk.Label(root, text='slido', bg='#0b090a', fg='#38b000', font=('Arial', 20, 'bold'))

label.pack(side='top')

button = tk.Button(root, text='Take a quiz', bg='#38b000', fg='#0b090a', font=('Arial', 20, 'bold'),command=button_clicked)

button.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()