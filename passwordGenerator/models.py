from django.db import models

# Create your models here.
import tkinter as tk
import random, string
window = tk.Tk()
window.title('Passsword Generator')
window.geometry('400x400')
    
password_length=int(input('How long would your password be : '))
##forUppercase
def uppercaseOnly():
 password_char = string.ascii_letters 
 password1=[]
 for x in range(password_length):
  password1.append(random.choice(password_char))
  password=[y.upper() for y in password1]
 password=''.join(password)
 res.config(text = "Your password is : " + password)
 
def uppercaseAndlower():
 password_char = string.ascii_letters 
 password1=[]
 for x in range(password_length):
  password1.append(random.choice(password_char))
 password=''.join(password1)
 res.config(text = "Your password is : " + password)
 
def uppercaseAndnumeric():
 password_char = string.ascii_letters + string.digits 
 password1=[]
 for x in range(password_length):
  password1.append(random.choice(password_char))
  password=[y.upper() for y in password1]
 password=''.join(password)
 res.config(text = "Your password is : " + password)
 
def uppercaseAndunique():
 password_char = string.ascii_letters +  string.punctuation
 password1=[]
 for x in range(password_length):
  password1.append(random.choice(password_char))
  password=[y.upper() for y in password1]
 password=''.join(password)
 res.config(text = "Your password is : " + password)

##For Lowercase
def lowercaseOnly():
 password_char = string.ascii_letters 
 password1=[]
 for x in range(password_length):
  password1.append(random.choice(password_char))
  password=[y.lower() for y in password1]
 password=''.join(password)
 res.config(text = "Your password is : " + password)

def lowercaseAndnumeric():
 password_char = string.ascii_letters + string.digits 
 password1=[]
 for x in range(password_length):
  password1.append(random.choice(password_char))
  password=[y.lower() for y in password1]
 password=''.join(password)
 res.config(text = "Your password is : " + password)
 
def lowercaseAndunique():
 password_char = string.ascii_letters +  string.punctuation
 password1=[]
 for x in range(password_length):
  password1.append(random.choice(password_char))
  password=[y.lower() for y in password1]
 password=''.join(password)
 res.config(text = "Your password is : " + password)
 #for num only
def number():
 password_char = string.digits
 password1=[]
 for x in range(password_length):
  password1.append(random.choice(password_char))
 password=''.join(password1)
 res.config(text = "Your password is : " + password)
 #For unique Only
def unique():
 password_char = string.punctuation
 password1=[]
 for x in range(password_length):
  password1.append(random.choice(password_char))
 password=''.join(password1)
 res.config(text = "Your password is : " + password)
 #for num and unique
def numunique():
 password_char = string.punctuation + string.digits
 password1=[]
 for x in range(password_length):
  password1.append(random.choice(password_char))
 password=''.join(password1)
 res.config(text = "Your password is : " + password)
def all_char():
 password_char = string.ascii_letters + string.digits + string.punctuation
 password1=[]
 for x in range(password_length):
  password1.append(random.choice(password_char))
 password=''.join(password1)
 res.config(text = "Your password is : " + password)


l = tk.Label(window, bg='white', width=900)
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0)&(var3.get() == 0)&(var4.get() == 0):
        l.config(uppercaseOnly())
    elif (var1.get() == 1) & (var2.get() == 1)&(var3.get() == 0)&(var4.get() == 0):
        l.config(uppercaseAndlower())
    elif (var1.get() == 1) & (var2.get() == 0)&(var3.get() == 1)&(var4.get() == 0):
        l.config(text=uppercaseAndnumeric())
    elif (var1.get() == 1) & (var2.get() == 0)&(var3.get() == 0)&(var4.get() == 1):
        l.config(text=uppercaseAndunique())
    elif (var1.get() == 0) & (var2.get() == 1)&(var3.get() == 0)&(var4.get() == 0):
        l.config(lowercaseOnly())
    elif (var1.get() == 1) & (var2.get() == 1)&(var3.get() == 0)&(var4.get() == 0):
        l.config(uppercaseAndlower())
    elif (var1.get() == 0) & (var2.get() == 1)&(var3.get() == 1)&(var4.get() == 0):
        l.config(text=lowercaseAndnumeric())
    elif (var1.get() == 0) & (var2.get() == 1)&(var3.get() == 0)&(var4.get() == 1):
        l.config(text=uppercaseAndunique())
    elif (var1.get() == 0) & (var2.get() == 0)&(var3.get() == 1)&(var4.get() == 0):
        l.config(text=number())
    elif (var1.get() == 0) & (var2.get() == 0)&(var3.get() == 0)&(var4.get() == 1):
        l.config(text=unique())
    elif (var1.get() == 0) & (var2.get() == 0)&(var3.get() == 1)&(var4.get() == 1):
        l.config(text=numunique())
    else:
        l.config(text=all_char())

##for checkbox
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Include Uppercase Character',variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='Include Lowercase Character',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
c3 = tk.Checkbutton(window, text='Include Numeric Character',variable=var3, onvalue=1, offvalue=0, command=print_selection)
c3.pack()
c4 = tk.Checkbutton(window, text='Include Unique Character',variable=var4, onvalue=1, offvalue=0, command=print_selection)
c4.pack()
##answer
res=tk.Label(window)
res.pack()
window.mainloop()
