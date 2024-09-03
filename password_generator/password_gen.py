import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import string
from PIL import Image

def generate_password():
    if not check_switch():
        length = int(length_var.get())
        include_uppercase = uppercase_var.get()
        include_lowercase = lowercase_var.get()
        include_numbers = numbers_var.get()
        include_symbols = symbols_var.get()
        
        characters = ''
        if include_uppercase:
             characters += string.ascii_uppercase
        if include_lowercase:
             characters += string.ascii_lowercase
        if include_numbers:
             characters += string.digits
        if include_symbols:
             characters += string.punctuation
         
        if characters:
             password = ''.join(random.choice(characters) for _ in range(length))
             password_var.set(password)
             strength_label_2.configure(text=f"{calculate_strength(password)}")

def check_switch():
    if not uppercase_var.get() and not lowercase_var.get() and not numbers_var.get() and not symbols_var.get():
        messagebox.showerror("Invalid option","Please Choose Any Option")

def calculate_strength(password):
    length = len(password)
    if length >= 12:
        strength_icon.configure(fg_color="#0f0")
        return "STRONG"
    elif 8 <= length < 12:
        strength_icon.configure(fg_color="#ff0")
        return "MEDIUM"
    else:
        strength_icon.configure(fg_color="#f00")
        return "WEAK"

def update_lab(length):
    length_lab_2.configure(text=int(length))

def cpy_clipboard():
   pyperclip.copy(password_var.get())

app = ctk.CTk()
app.title("Password Generator")
app.configure(fg_color="#0E0D13")
app.resizable(False,False)
app.geometry("400x500")

title_lab=ctk.CTkLabel(app,text="PASSWORD GENERATOR",text_color="#e6e5ea",font=('Liberation Mono', 18,'bold'))
title_lab.place(x=105,y=20)

# Password Display
display_frame=ctk.CTkFrame(app,width=300,height=40,fg_color="#24232B",corner_radius=0)
display_frame.place(x=50,y=60)
password_var = ctk.StringVar()
password_lab = ctk.CTkLabel(display_frame,fg_color="#24232B",textvariable=password_var, font=('Liberation Mono', 18,'bold'),height=40, width=200,anchor='w',text_color="#e6e5ea")
password_lab.place(x=20,y=0)

cpy_img=ctk.CTkImage(light_image=Image.open('password_generator/copy.png'),size=(25,25))
copy=ctk.CTkButton(display_frame,height=40,fg_color="#24232B",width=40,command=cpy_clipboard,text='',image=cpy_img,hover_color="#0E0D13",corner_radius=0)
copy.place(x=260,y=0)

#Input Frame

input_frame=ctk.CTkFrame(app,width=300,height=300,fg_color="#24232B",corner_radius=0)
input_frame.place(x=50,y=120)

# Character Length Slider
length_lab=ctk.CTkLabel(input_frame, text="Character Length", font=('Liberation Mono', 12,'bold'),text_color="#e6e5ea")
length_lab.place(x=25,y=10)
length_var = ctk.IntVar(value=10)

length_slider = ctk.CTkSlider(input_frame, from_=4, to=20, variable=length_var,width=260,fg_color="#0E0D13",progress_color="#6edb7b",button_color="#e6e5ea",button_hover_color="#cccbd0",command=update_lab)
length_slider.place(x=20,y=40)

length_lab_2=ctk.CTkLabel(input_frame,fg_color="#24232B",width=25,height=25,text=f"{int(length_slider.get())}",font=('Liberation Mono', 16,'bold'),text_color="#6edb7b")
length_lab_2.place(x=255,y=10)


# Checkbuttons for character types
uppercase_var = ctk.BooleanVar(value=True)
lowercase_var = ctk.BooleanVar(value=True)
numbers_var = ctk.BooleanVar(value=True)
symbols_var = ctk.BooleanVar(value=False)

upper=ctk.CTkSwitch(input_frame, text="Include Uppercase Letters", variable=uppercase_var, font=('Liberation Mono', 12,'bold'),text_color="#e6e5ea",fg_color="#0E0D13",progress_color="#6edb7b",button_color="#e6e5ea",button_hover_color="#cccbd0")
upper.place(x=20,y=60)
lower=ctk.CTkSwitch(input_frame, text="Include Lowercase Letters", variable=lowercase_var, font=('Liberation Mono', 12,'bold'),text_color="#e6e5ea",fg_color="#0E0D13",progress_color="#6edb7b",button_color="#e6e5ea",button_hover_color="#cccbd0")
lower.place(x=20,y=90)
number=ctk.CTkSwitch(input_frame, text="Include Numbers", variable=numbers_var, font=('Liberation Mono', 12,'bold'),text_color="#e6e5ea",fg_color="#0E0D13",progress_color="#6edb7b",button_color="#e6e5ea",button_hover_color="#cccbd0")
number.place(x=20,y=120)
symbol=ctk.CTkSwitch(input_frame, text="Include Symbols", variable=symbols_var, font=('Liberation Mono', 12,'bold'),text_color="#e6e5ea",fg_color="#0E0D13",progress_color="#6edb7b",button_color="#e6e5ea",button_hover_color="#cccbd0")
symbol.place(x=20,y=150)

# Password Strength

strength_frame=ctk.CTkFrame(input_frame,width=260,height=40,fg_color='#0E0D13',corner_radius=0)
strength_frame.place(x=20,y=180)
strength_label = ctk.CTkLabel(strength_frame, text="Strength:", font=('Liberation Mono', 12,'bold'),text_color="#fff",fg_color="#0E0D13",height=40)
strength_label.place(x=10,y=0)

strength_label_2 = ctk.CTkLabel(strength_frame, text="MEDIUM", font=('Liberation Mono', 12,'bold'),text_color="#fff",fg_color="#0E0D13",height=40,width=100,compound='left')
strength_label_2.place(x=150,y=0)

strength_icon=ctk.CTkLabel(strength_label_2,width=20,height=20,corner_radius=20,fg_color="#ff0",text="")
strength_icon.place(x=80,y=10)

# Generate Button
generate_button = ctk.CTkButton(input_frame, text="GENERATE >", command=generate_password, font=('Liberation Mono', 15,'bold'), fg_color='#6edb7b',width=260,height=40,text_color="#0E0D13",corner_radius=0,hover=0)
generate_button.place(x=20,y=240)

app.mainloop()

