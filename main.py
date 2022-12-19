import tkinter as tk
import datetime as dt
from tkinter import ttk
import time

#cria uma animação para fechar o programa com uma animação
def close():
    for i in range(100, -1, -5):
        janela.attributes('-alpha', i / 100)
        janela.update()
        time.sleep(0.01)
    janela.destroy()

def get_data():
    descricao = entry_descricao.get()
    quantidade = entry_quantidade.get()
    data = entry_data.get()
    valor = entry_valor.get()
    fornecedor = entry_fornecedor.get()
    observacao = entry_observacao.get()
    print(descricao, quantidade, data, valor, fornecedor, observacao)
    
#se selecionar a linha e clicar no botão limpar ele apaga as linhas selecionadas
def delete_data():
    x = tree.selection()[0]
    tree.delete(x)

def save_data():
    descricao = entry_descricao.get()
    quantidade = entry_quantidade.get()
    data = entry_data.get()
    valor = entry_valor.get()
    fornecedor = entry_fornecedor.get()
    observacao = entry_observacao.get()
    with open('banco.txt', 'a') as arquivo:
        arquivo.write(f'{descricao};{quantidade};{data};{valor};{fornecedor};{observacao} \n')


def insert_data():
    descricao = entry_descricao.get()
    quantidade = entry_quantidade.get()
    data = entry_data.get()
    valor = entry_valor.get()
    fornecedor = entry_fornecedor.get()
    observacao = entry_observacao.get()
    tree.insert('', 'end', values=(descricao, quantidade, data, valor, fornecedor, observacao))

def limpar():
    entry_descricao.delete(0, 'end')
    entry_quantidade.delete(0, 'end')
    entry_data.delete(0, 'end')
    entry_valor.delete(0, 'end')
    entry_fornecedor.delete(0, 'end')
    entry_observacao.delete(0, 'end')


janela = tk.Tk()
janela.title('Ferramenta Cadastro de Materiais')
janela.geometry('800x600')
janela.configure(background='#d3d3d3')

#definindo o estilo
style = ttk.Style()
style.theme_use('default')
style.configure('Treeview', background='#d3d3d3', foreground='black', rowheight=25, fieldbackground='#d3d3d3')
style.map('Treeview', background=[('selected', 'blue')])
style.configure('Treeview.Heading', font=('Arial', 10, 'bold'))

#criando a treeview
tree = ttk.Treeview(janela, selectmode='browse', height=10)
tree['columns'] = ('Descrição', 'Quantidade', 'Data de Cadastro', 'Valor', 'Fornecedor', 'Observação')
tree.column('#0', width=0, stretch=tk.NO, minwidth=0 )
tree.column('Descrição', anchor=tk.CENTER, width=100)
tree.column('Quantidade', anchor=tk.CENTER, width=100)
tree.column('Data de Cadastro', anchor=tk.CENTER, width=100)
tree.column('Valor', anchor=tk.CENTER, width=100)
tree.column('Fornecedor', anchor=tk.CENTER, width=100)
tree.column('Observação', anchor=tk.CENTER, width=100)


tree.heading('#0', text='', anchor=tk.CENTER)
tree.heading('Descrição', text='Descrição', anchor=tk.CENTER)
tree.heading('Quantidade', text='Quantidade', anchor=tk.CENTER)
tree.heading('Data de Cadastro', text='Data de Cadastro', anchor=tk.CENTER)
tree.heading('Valor', text='Valor', anchor=tk.CENTER)
tree.heading('Fornecedor', text='Fornecedor', anchor=tk.CENTER)
tree.heading('Observação', text='Observação', anchor=tk.CENTER)

tree.grid(column=0, row=0, padx=10, pady=10, sticky='nswe', columnspan=2)

#criando os campos

label_descricao = tk.Label(text="Descrição do Material")
label_descricao.grid(column=0, row=1, padx=10, pady=10, sticky='nswe', columnspan=2)

label_quantidade = tk.Label(text='Quantidade')
label_quantidade.grid(column=0, row=2, padx=10, pady=10, sticky='nswe', columnspan=2)

label_data = tk.Label(text='Data de Cadastro')
label_data.grid(column=0, row=3, padx=10, pady=10, sticky='nswe', columnspan=2)

label_valor = tk.Label(text='Valor')
label_valor.grid(column=0, row=4, padx=10, pady=10, sticky='nswe', columnspan=2)

label_fornecedor = tk.Label(text='Fornecedor')
label_fornecedor.grid(column=0, row=5, padx=10, pady=10, sticky='nswe', columnspan=2)

label_observacao = tk.Label(text='Observação')
label_observacao.grid(column=0, row=6, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_descricao = tk.Entry()
entry_descricao.grid(column=2, row=1, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_quantidade = tk.Entry()
entry_quantidade.grid(column=2, row=2, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_data = tk.Entry()
entry_data.grid(column=2, row=3, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_valor = tk.Entry()
entry_valor.grid(column=2, row=4, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_fornecedor = tk.Entry()
entry_fornecedor.grid(column=2, row=5, padx=10, pady=10, sticky='nswe', columnspan=2)

entry_observacao = tk.Entry()
entry_observacao.grid(column=2, row=6, padx=10, pady=10, sticky='nswe', columnspan=2)

#criando os botões
button_cadastrar = tk.Button(text='Cadastrar', command=insert_data)
button_cadastrar.grid(column=0, row=7, padx=10, pady=10, sticky='nswe', columnspan=2)

button_limpar = tk.Button(text='Limpar', command=limpar)
button_limpar.grid(column=2, row=7, padx=10, pady=10, sticky='nswe', columnspan=2)

button_deletar = tk.Button(text='Deletar', command=delete_data)
button_deletar.grid(column=0, row=8, padx=10, pady=10, sticky='nswe', columnspan=2)

# melhora a interface gráfica
for child in janela.winfo_children():
    child.grid_configure(padx=5, pady=5)

#cria a barra de rolagem para a treeview do lado direito
scrollbar = ttk.Scrollbar(janela, orient='vertical', command=tree.yview)
scrollbar.grid(column=2, row=0, sticky='ns', rowspan=1)
tree.configure(yscrollcommand=scrollbar.set)

#cria animações para os botões se clicar com o mouse no botão ele pisca e depois volta ao normal
button_cadastrar.bind('<Enter>', lambda e: button_cadastrar.configure(relief='sunken'))
button_cadastrar.bind('<Leave>', lambda e: button_cadastrar.configure(relief='raised'))

button_limpar.bind('<Enter>', lambda e: button_limpar.configure(relief='sunken'))
button_limpar.bind('<Leave>', lambda e: button_limpar.configure(relief='raised'))

button_deletar.bind('<Enter>', lambda e: button_deletar.configure(relief='sunken'))
button_deletar.bind('<Leave>', lambda e: button_deletar.configure(relief='raised'))


#cria uma animação para abrir o programa com uma animação
janela.attributes('-alpha', 0)
for i in range(0, 101, 5):
    janela.attributes('-alpha', i / 100)
    janela.update()
    time.sleep(0.01)


janela.protocol('WM_DELETE_WINDOW', close)



janela.mainloop()
