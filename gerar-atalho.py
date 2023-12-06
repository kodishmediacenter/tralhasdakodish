import tkinter as tk
from tkinter import filedialog

def gerar_desktop():
    nome_aplicativo = entry_nome.get()
    caminho_aplicativo = entry_caminho.get()
    icone_aplicativo = entry_icone.get()

    if nome_aplicativo and caminho_aplicativo:
        # Criar o conteúdo do arquivo .desktop
        conteudo_desktop = f"[Desktop Entry]\nName={nome_aplicativo}\nExec={caminho_aplicativo}\nIcon={icone_aplicativo}\nType=Application\n"

        # Salvar o arquivo .desktop
        file_path = filedialog.asksaveasfilename(defaultextension=".desktop", filetypes=[("Arquivos .desktop", "*.desktop")])
        with open(file_path, 'w') as file:
            file.write(conteudo_desktop)

        status_label.config(text=f"Arquivo {file_path} gerado com sucesso!")

def selecionar_icone():
    icone_path = filedialog.askopenfilename(filetypes=[("Arquivos de Ícone", "*.png;*.ico;*.xpm")])
    entry_icone.delete(0, tk.END)
    entry_icone.insert(0, icone_path)

# Criar a janela principal
janela = tk.Tk()
janela.title("Gerador de Arquivo .desktop")

# Criar rótulos e campos de entrada
label_nome = tk.Label(janela, text="Nome do Aplicativo:")
label_nome.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_caminho = tk.Label(janela, text="Caminho do Aplicativo:")
label_caminho.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_caminho = tk.Entry(janela)
entry_caminho.grid(row=1, column=1, padx=10, pady=10)

label_icone = tk.Label(janela, text="Ícone do Aplicativo:")
label_icone.grid(row=2, column=0, padx=10, pady=10, sticky="w")

entry_icone = tk.Entry(janela)
entry_icone.grid(row=2, column=1, padx=10, pady=10)

botao_selecionar_icone = tk.Button(janela, text="Selecionar Ícone", command=selecionar_icone)
botao_selecionar_icone.grid(row=2, column=2, padx=10, pady=10)

# Botão para gerar o arquivo .desktop
botao_gerar = tk.Button(janela, text="Gerar .desktop", command=gerar_desktop)
botao_gerar.grid(row=3, column=0, columnspan=2, pady=10)

# Rótulo para exibir o status
status_label = tk.Label(janela, text="", fg="green")
status_label.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar o loop principal
janela.mainloop()
