import tkinter as tk
from tkinter import END, Label, Button, Entry
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
from tkinter import filedialog
from tkinter import scrolledtext
import math
import os
from analizadorlexico import *


principal = None


principal = tk.Tk()
principal.title("Menú Principal")
principal.geometry("600x500")
principal.config(bg="#D4E6FF")
principal.resizable(0,0)

#label
tit1 = Label(principal, text="Menú de Archivo", font="Arial 12 bold", fg="black", bg="#D4E6FF")
tit1.place(x=20,y=40)


text_area = scrolledtext.ScrolledText(principal, wrap = tk.WORD, width = 60, height = 15, font = ("Arial",12))
text_area.grid(column = 0, pady = 160, padx = 20)
text_area.focus()

menu = Menu(principal)
principal.config(menu=menu)

def abrirarchivo():
    ruta=filedialog.askopenfilename(title="Cargar Archivo", filetypes=(("Text files", "*.lfp"), ("all files", "*.*")))
    if ruta != "":
        archivo = open(ruta, "r")
        contenido = archivo.read()
        text_area.insert(tk.INSERT, contenido)

def analizar():
    global text_area
    scanner = analizadorlexico()
    scanner.analizar(text_area.get(1.0, END))
    for t in scanner.listatokens:
        t.mostrartoken()
    for e in scanner.listaerrores:
        e.mostrarerror()

def repoerrores():
    pass

def guardarcomo():
    nombrearch=filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("lfp files","*.lfp"),("todos los archivos","*.*")))
    if nombrearch!='':
        archi1=open(nombrearch+".lfp", "w", encoding="utf-8")
        archi1.write(text_area.get("1.0", tk.END))
        archi1.close()

def salir():
    principal.destroy()

def manualdeusuario():
    os.startfile("Documentacion\Manual de Usuario.pdf")

def temasdeayuda():
    os.startfile("Documentacion\Temas de ayuda.pdf")

def manualtecnico():
    os.startfile("Documentacion\Manual Técnico.pdf")


fileMenu = Menu(menu)
fileMenu.add_command(label="Abrir", command=abrirarchivo)
fileMenu.add_command(label="Guardar", command=guardarcomo)
fileMenu.add_command(label="Guardar Como", command = guardarcomo)
fileMenu.add_command(label="Errores", command=repoerrores)
menu.add_cascade(label="Archivo", menu=fileMenu)

editMenu = Menu(menu)
editMenu.add_command(label="Manual de Usuario", command= manualdeusuario)
editMenu.add_command(label="Manual Técnico", command=manualtecnico)
editMenu.add_command(label="Temas de Ayuda", command=temasdeayuda)
menu.add_cascade(label="Ayuda", menu=editMenu)

#botones
bot1 = Button(principal, text="Analizar", font="Arial 12", bg="#FFD8D4", command=analizar)
bot1.place(x=50, y= 100)
bot2 = Button(principal, text="Salir", font="Arial 12", bg="#FFD8D4", command=salir)
bot2.place(x=150, y= 100)

principal.mainloop()
