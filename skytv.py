import tkinter as tk

# Função para ser executada quando o botão "OK" for clicado
def on_ok_click():
    for i in range(10):
        print(f"<item>\n<title>Canal {i+1}</title>\n<link>{input_entries[i].get()}</link>\n<thumbnail>https://assineskyagora.com.br/wp-content/uploads/2020/05/logo-sky-play2.png</thumbnail>\n<fanart></fanart>\n<info></info>\n</item>\n\n")





        

# Cria a janela principal
janela = tk.Tk()
janela.title("Cine Sky")
janela.geometry("640x480")

# Cria uma lista para armazenar as entradas de texto
input_entries = []

# Cria 10 rótulos e campos de entrada
for i in range(10):
    label = tk.Label(janela, text=f"Canal {i+1}:")
    label.pack()

    entry = tk.Entry(janela, width=60)  # Aumente o valor de width para tornar o campo de entrada mais largo
    entry.pack()

    input_entries.append(entry)

# Cria o botão "OK" e associa a função on_ok_click a ele
ok_button = tk.Button(janela, text="OK", command=on_ok_click)
ok_button.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()
