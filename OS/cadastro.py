from tkinter import Tk, Label, Entry, Button, Text
import win32print
import win32api

def cadastrar():
    nome = nome_entry.get()
    endereco = endereco_entry.get()
    cep = cep_entry.get()
    telefone = telefone_entry.get()
    celular = celular_entry.get()
    cpf_cnpj = cpf_cnpj_entry.get()
    conta_pix = conta_pix_entry.get()
    problema = problema_text.get("1.0", "end")[:-1]  # Remove a quebra de linha final
    solucao = solucao_text.get("1.0", "end")[:-1]  # Remove a quebra de linha final

    # Criando uma string com os dados do cadastro
    dados = f"Nome: {nome}\nEndereço: {endereco}\nCEP: {cep}\nTelefone: {telefone}\nCelular: {celular}\nCPF/CNPJ: {cpf_cnpj}\nConta Pix para Estorno: {conta_pix}\n\nProblema:\n{problema}\n\nSolução:\n{solucao}\n"

    # Salvando os dados em um arquivo de texto
    with open("cadastros.txt", "a") as arquivo:
        arquivo.write(dados)

    messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")

def imprimir_cadastro():
    nome = nome_entry.get()
    endereco = endereco_entry.get()
    cep = cep_entry.get()
    telefone = telefone_entry.get()
    celular = celular_entry.get()
    cpf_cnpj = cpf_cnpj_entry.get()
    conta_pix = conta_pix_entry.get()
    problema = problema_text.get("1.0", "end")[:-1]  # Remove a quebra de linha final
    solucao = solucao_text.get("1.0", "end")[:-1]  # Remove a quebra de linha final

    # Criando uma string com os dados do cadastro
    dados = f"Nome: {nome}\nEndereço: {endereco}\nCEP: {cep}\nTelefone: {telefone}\nCelular: {celular}\nCPF/CNPJ: {cpf_cnpj}\nConta Pix para Estorno: {conta_pix}\n\nProblema:\n{problema}\n\nSolução:\n{solucao}\n"

    # Imprimir os dados
    try:
        printer_name = win32print.GetDefaultPrinter()
        hPrinter = win32print.OpenPrinter(printer_name)
        win32print.StartDocPrinter(hPrinter, 1, ("Cadastros", None, "RAW"))
        win32print.WritePrinter(hPrinter, dados.encode())
        win32print.EndDocPrinter(hPrinter)
        win32print.ClosePrinter(hPrinter)
        messagebox.showinfo("Impressão", "Cadastro impresso com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro de Impressão", str(e))

# Criação da janela principal
janela = Tk()
janela.title("Formulário de Cadastro")
janela.geometry("500x500")

# Labels
Label(janela, text="Nome:", width=15, anchor="e").grid(row=0, column=0, pady=5)
Label(janela, text="Endereço:", width=15, anchor="e").grid(row=1, column=0, pady=5)
Label(janela, text="CEP:", width=15, anchor="e").grid(row=2, column=0, pady=5)
Label(janela, text="Telefone:", width=15, anchor="e").grid(row=3, column=0, pady=5)
Label(janela, text="Celular:", width=15, anchor="e").grid(row=4, column=0, pady=5)
Label(janela, text="CPF/CNPJ:", width=15, anchor="e").grid(row=5, column=0, pady=5)
Label(janela, text="Conta Pix para Estorno:", width=20, anchor="e").grid(row=6, column=0, pady=5)
Label(janela, text="Problema:", width=15, anchor="e").grid(row=8, column=0, pady=5)
Label(janela, text="Solução:", width=15, anchor="e").grid(row=10, column=0, pady=5)

# Entradas de texto
nome_entry = Entry(janela, width=30)
nome_entry.grid(row=0, column=1, pady=5)
endereco_entry = Entry(janela, width=30)
endereco_entry.grid(row=1, column=1, pady=5)
cep_entry = Entry(janela, width=30)
cep_entry.grid(row=2, column=1, pady=5)
telefone_entry = Entry(janela, width=30)
telefone_entry.grid(row=3, column=1, pady=5)
celular_entry = Entry(janela, width=30)
celular_entry.grid(row=4, column=1, pady=5)
cpf_cnpj_entry = Entry(janela, width=30)
cpf_cnpj_entry.grid(row=5, column=1, pady=5)
conta_pix_entry = Entry(janela, width=30)
conta_pix_entry.grid(row=6, column=1, pady=5, padx=5)

# Áreas de texto para Problema e Solução
problema_text = Text(janela, height=4, width=30)
problema_text.grid(row=8, column=1, pady=5)
solucao_text = Text(janela, height=4, width=30)
solucao_text.grid(row=10, column=1, pady=5)

# Botões de cadastro e impressão
cadastrar_button = Button(janela, text="Cadastrar", command=cadastrar)
cadastrar_button.grid(row=11, column=0, columnspan=2, pady=10)

imprimir_button = Button(janela, text="Imprimir", command=imprimir_cadastro)
imprimir_button.grid(row=12, column=0, columnspan=2, pady=10)

# Iniciar a execução da janela
janela.mainloop()
