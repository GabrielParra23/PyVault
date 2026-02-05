from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import os
import sys
# d = open('dia 29/data.txt', 'a') # criando o arquivo de texto

if getattr(sys, 'frozen', False):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(__file__)

date_file_patch = os.path.join(base_path, 'data.json')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_numbers = randint(2, 4)
    nr_symbols = randint(2, 4)

    password_letters =[choice(letters) for _ in range(nr_letters)] # loop para pegar letras aleatórias da lista
    password_numbers =[choice(numbers) for _ in range(nr_numbers)]
    password_symbols =[choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = ''.join(password_list)
    tb_password.delete(0, END)
    tb_password.insert(0, password) 

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = tb_website.get()
    user = tb_user.get()
    password = tb_password.get()
    new_data = {
        website: {
            'Email': user,
            'Password': password,
        }
    }

    if website == '' or password == '' or user == '':
        messagebox.showerror(title='Error', message='Fill in all the information to proceed') 
    else:
        result = messagebox.askokcancel(title=website, message=f'This information can be saved? \n Email/Username: {user}\n Senha: {password}')
        if result:
            try:
                with open(date_file_patch, 'r') as d: # abrindo o arquivo para ler
                    date = json.load(d) # Carrega o JSON
            except FileNotFoundError:
                with open(date_file_patch, 'w') as d: # abrindo o arquivo para edita-lo
                    json.dump(new_data, d, indent=4)     
            else:
                print(date)
                print(new_data)
                date.update(new_data) # Atualiza o JSON
                print(date)
                with open(date_file_patch, 'w') as d: 
                    json.dump(date, d, indent=4) # dump para escrever no JSON 
            finally:       
                tb_website.delete(0, END)
                tb_password.delete(0, END)
                tb_user.delete(0, END)

# ---------------------------- GET DATE ------------------------------- #

def get_date():
    try:
        website = tb_website.get()
        with open(date_file_patch, 'r') as d:
            date = json.load(d)
        account = date[website]
        result = messagebox.askokcancel(title=website, message=f'This information is the correct? \n Email/Username: {account['Email']}\n Senha: {account['Password']}')
        if result:
            tb_user.delete(0, END)
            tb_user.insert(0, account['Email']) 
            tb_password.insert(0, account['Password']) 
    except:
        messagebox.showerror(title='Error', message="This information don't exist") 

# ---------------------------- GET IMG ------------------------------- #
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(base_path, relative_path)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk() # criando a tela
window.title('Gerente de Senhas') # Titulo
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0) # criando o fundo da imagem
logo_img = PhotoImage(file=resource_path('logo.png')) # pegando uma imagem
canvas.create_image(100,100, image=logo_img) 
canvas.grid(row=0,column=1) # colocando a imagem na tela


# ------------- TEXTOS ------------- #
tx_webSite = Label(text='Website:')
tx_webSite.grid(row=1, column=0 )

tx_user = Label( text='Email/Username:')
tx_user.grid(row=2, column=0)

tx_password = Label( text='Password:')
tx_password.grid(row=3, column=0)
# ------------- CAIXAS DE TEXTO ------------- #
tb_website = Entry(width=35)
tb_website.grid(row=1, column=1, sticky="EW") # O sticky força para esticar até as bordas da grade
tb_website.focus() # já inicia com o cursor aqui

tb_user = Entry(width=35)
tb_user.grid(row=2, column=1, columnspan=2, sticky="EW")

tb_password = Entry(width=21)
tb_password.grid(row=3, column=1, sticky="EW")

# ------------- BOTÕES ------------- #

btn_gen_password = Button(text='Search', command=get_date)
btn_gen_password.grid(row=1, column=2, sticky="EW")

btn_get_date = Button(text='Generate Password', command=gen_password)
btn_get_date.grid(row=3, column=2, sticky="EW")

btn_add = Button(text='Add', width=36, command=save)
btn_add.grid(row=4, column=1, columnspan=2, sticky="EW")



window.mainloop() # executando a tela