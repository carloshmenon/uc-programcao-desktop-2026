import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

contador_id = 1

class Usuario:
    def __init__(self, id, nome, email, endereco):
        self.id_usuario =  id
        self.nome =  nome
        self.email =  email
        self.endereco =  endereco

def conectar():
    return None

def listar():
    return None #retorna uma lista de usuario

def update(Usuario):

    return None 

def inserir(Usuario):
    return None

def remover(Usuario):
    return None


def novo_usuario():
    global contador_id
    u = Usuario()
    #u.id_usuario = input_id.get()
    u.nome = input_nome.get()
    u.email = input_email.get()
    u.endereco = input_endereco.get()

    if u.nome == "" or u.email == "" or u.endereco == "":
        messagebox.showwarning("Aviso", "Nome, Email e Endereço são obrigatórios")
        return
    try:
        inserir(u)
        tabela.insert("", "end", values=(contador_id, u.nome, u.email, u.endereco))
        contador_id += 1
    except:
        print("ERROR")

    limpar_campos()

def editar_usuario():
    selecionado = tabela.selection()

    if not selecionado:
        messagebox.showwarning("Aviso!","Selecionar um Usuário")
        return
    
    u = Usuario()
    u.id_usuario = input_id.get()
    u.nome = input_nome.get()
    u.email = input_email.get()
    u.endereco = input_endereco.get()

    try:
        update(u)
        tabela.item(selecionado, values=(u.id_usuario, u.nome, u.email, u.endereco))
        limpar_campos()
    except:
        print("ERROR")

def excluir_usuario():
    selecionado = tabela.selection()

    if not selecionado:
        messagebox.showwarning("Aviso!","Selecionar um Usuário")
        return
    tabela.delete(selecionado)
    limpar_campos()

def selecionar_usuario(event):
    selecionado = tabela.selection()

    if selecionado:
        limpar_campos()
        valores = tabela.item(selecionado, "values")

        input_id.insert(0, valores[0])
        input_nome.insert(0, valores[1])
        input_email.insert(0, valores[2])
        input_endereco.insert(0, valores[3])


def limpar_campos():
    input_id.delete(0, tk.END)
    input_nome.delete(0, tk.END)
    input_email.delete(0, tk.END)
    input_endereco.delete(0, tk.END)

janela = tk.Tk()
janela.title("Cadastro de usuario")
janela.geometry("750x450")



#Formulario 
frame_form = tk.Frame(janela)
frame_form.pack(pady=10)

tk.Label(frame_form, text="ID: ").grid(row=0, column=0, padx=5, sticky="e")
input_id = tk.Entry(frame_form, width=20)
input_id.grid(row=0, column=1, padx=5)

tk.Label(frame_form, text="Nome:").grid(row=0, column=2, padx=5, sticky="e")
input_nome = tk.Entry(frame_form, width=40)
input_nome.grid(row=0, column=3, padx=5)

tk.Label(frame_form, text="Email:").grid(row=1, column=0, padx=5, sticky="e")
input_email = tk.Entry(frame_form, width=20)
input_email.grid(row=1, column=1, padx=5)

tk.Label(frame_form, text="Endereço:").grid(row=1, column=2, padx=5, sticky="e")
input_endereco = tk.Entry(frame_form, width=40)
input_endereco.grid(row=1, column=3, padx=5)

#BOTÕES
frame_button = tk.Frame(janela)
frame_button.pack(pady=10)

btn_novo = tk.Button(frame_button, text="Novo", width=10, command=novo_usuario).grid(row=0, column=0, padx=5)
btn_editar = tk.Button(frame_button, text="Editar", width=10, command=editar_usuario).grid(row=0, column=1, padx=5)
btn_excluir = tk.Button(frame_button, text="Excluir", width=10, command=excluir_usuario).grid(row=0, column=2, padx=5)
btn_limpar = tk.Button(frame_button, text="Limpar", width=10, command=limpar_campos).grid(row=0, column=3, padx=5)

#TABELA
colunas = ("ID", "NOME", "EMAIL", "ENDEREÇO")

tabela = ttk.Treeview(janela, columns=colunas, show="headings")

for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=170)

tabela.pack(fill="both", expand=True, padx=20, pady=20)
tabela.bind("<<TreeviewSelect>>", selecionar_usuario)


janela.mainloop()
