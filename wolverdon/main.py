import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("350x200")

form = ttk.Frame(root)
form.pack()

# Cria o título
title_label = ttk.Label(form, text="Formulário", font=("Tahoma", 18, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Cria o campo para o link
link_label = ttk.Label(form, text="Link:")
link_label.grid(row=1, column=0)
link_entry = ttk.Entry(form)
link_entry.grid(row=1, column=1)

# Cria o campo para a imagem
image_label = ttk.Label(form, text="Sinopse do Filme:")
image_label.grid(row=2, column=0)
image_entry = ttk.Entry(form)
image_entry.grid(row=2, column=1)

def submit_form():
    #print("Link:", link_entry.get())
    #print("Imagem:", image_entry.get())
    import abutre
    
    link = link_entry.get()
    desc = image_entry.get()
    
    abutre.main(link,desc)

def clear_form():
    link_entry.delete(0, 'end')
    image_entry.delete(0, 'end')

# Cria o botão de envio
submit_button = ttk.Button(form, text="Enviar", command=submit_form)
submit_button.grid(row=3, column=0, padx=10)

# Cria o botão de limpar
clear_button = ttk.Button(form, text="Limpar", command=clear_form)
clear_button.grid(row=3, column=1, padx=10)

root.mainloop()
