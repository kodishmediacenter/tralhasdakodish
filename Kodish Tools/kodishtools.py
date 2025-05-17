import tkinter as tk
from tkinter import messagebox
import base64
import zlib
import hashlib
from datetime import datetime
import math
import urllib.parse

# Função para corrigir o padding de Base64
def correct_padding(encoded_text):
    padding = len(encoded_text) % 4
    if padding != 0:
        encoded_text += '=' * (4 - padding)
    return encoded_text

# Função para descriptografar Base64
def base64_decode():
    try:
        encoded_text = text_entry.get("1.0", tk.END).strip()
        encoded_text = correct_padding(encoded_text)
        decoded_text = base64.b64decode(encoded_text).decode('utf-8')
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, decoded_text)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao decodificar Base64: {e}")

# Função para criptografar Base64
def base64_encode():
    try:
        raw_text = text_entry.get("1.0", tk.END).strip()
        encoded = base64.b64encode(raw_text.encode('utf-8')).decode('utf-8')
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, encoded)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao codificar Base64: {e}")

# Função para inverter o texto
def invert_text():
    original_text = text_entry.get("1.0", tk.END).strip()
    inverted_text = original_text[::-1]
    text_entry.delete("1.0", tk.END)
    text_entry.insert(tk.END, inverted_text)

# Função para converter hexadecimal em string
def hex_to_string():
    try:
        hex_text = text_entry.get("1.0", tk.END).strip()
        bytes_object = bytes.fromhex(hex_text)
        decoded_string = bytes_object.decode("utf-8")
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, decoded_string)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao converter hexadecimal: {e}")

# Função para remover linhas em branco
def remover_linhas_brancas():
    texto = text_entry.get("1.0", tk.END)
    linhas = [linha for linha in texto.splitlines() if linha.strip() != ""]
    texto_limpo = "\n".join(linhas)
    text_entry.delete("1.0", tk.END)
    text_entry.insert(tk.END, texto_limpo)

# Função para contar dias até a data digitada na caixa de texto (formato dd/mm/aaaa)
def contador_dias():
    try:
        texto = text_entry.get("1.0", tk.END).strip()
        data_alvo = datetime.strptime(texto, "%d/%m/%Y").date()
        hoje = datetime.now().date()
        dias_restantes = (data_alvo - hoje).days
        messagebox.showinfo("Contador de Dias", f"Faltam {dias_restantes} dias para {data_alvo.strftime('%d/%m/%Y')}.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular dias: {e}")

# Funções para gerar hashes

def gerar_md5():
    try:
        texto = text_entry.get("1.0", tk.END).strip()
        hash_result = hashlib.md5(texto.encode('utf-8')).hexdigest()
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, hash_result)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar hash MD5: {e}")

def gerar_sha1():
    try:
        texto = text_entry.get("1.0", tk.END).strip()
        hash_result = hashlib.sha1(texto.encode('utf-8')).hexdigest()
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, hash_result)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar hash SHA-1: {e}")

def gerar_sha256():
    try:
        texto = text_entry.get("1.0", tk.END).strip()
        hash_result = hashlib.sha256(texto.encode('utf-8')).hexdigest()
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, hash_result)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar hash SHA-256: {e}")

# Função do botão Multicódigo
def multicodigo():
    try:
        original_text = text_entry.get("1.0", tk.END).strip()
        reversed_text = original_text[::-1]
        padded = correct_padding(reversed_text)
        base64_decoded = base64.b64decode(padded)
        decompressed = zlib.decompress(base64_decoded)
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, decompressed.decode('utf-8', errors='replace'))
    except Exception as e:
        messagebox.showerror("Erro", f"Erro no processo Multicódigo: {e}")

# Função para calcular expressões matemáticas (com suporte a funções do módulo math)
def calcular():
    try:
        expressao = text_entry.get("1.0", tk.END).strip()
        resultado = eval(expressao, {"__builtins__": None}, math.__dict__)
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, str(resultado))
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular expressão: {e}")

# Função para URL Decode
def url_decode():
    try:
        texto = text_entry.get("1.0", tk.END).strip()
        decoded = urllib.parse.unquote(texto)
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, decoded)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao decodificar URL: {e}")

# Criar a janela principal
root = tk.Tk()
root.title("Kodish Tools 2025")

# Caixa de texto
text_entry = tk.Text(root, height=10, width=50)
text_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Frame para os botões
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, columnspan=2, pady=10)

# Botões alinhados em coluna
base64_button = tk.Button(button_frame, text="Descriptografar Base64", width=30, command=base64_decode)
base64_button.grid(row=0, column=0, padx=5, pady=2)

encode_button = tk.Button(button_frame, text="Criptografar em Base64", width=30, command=base64_encode)
encode_button.grid(row=1, column=0, padx=5, pady=2)

invert_button = tk.Button(button_frame, text="Inverter Texto", width=30, command=invert_text)
invert_button.grid(row=2, column=0, padx=5, pady=2)

hex_button = tk.Button(button_frame, text="Converter Hexadecimal para String", width=30, command=hex_to_string)
hex_button.grid(row=3, column=0, padx=5, pady=2)

remover_button = tk.Button(button_frame, text="Remover Linhas Brancas", width=30, command=remover_linhas_brancas)
remover_button.grid(row=4, column=0, padx=5, pady=2)

contador_button = tk.Button(button_frame, text="Contador de Dias para Data", width=30, command=contador_dias)
contador_button.grid(row=5, column=0, padx=5, pady=2)

md5_button = tk.Button(button_frame, text="Gerar Hash MD5", width=30, command=gerar_md5)
md5_button.grid(row=6, column=0, padx=5, pady=2)

sha1_button = tk.Button(button_frame, text="Gerar Hash SHA-1", width=30, command=gerar_sha1)
sha1_button.grid(row=7, column=0, padx=5, pady=2)

sha256_button = tk.Button(button_frame, text="Gerar Hash SHA-256", width=30, command=gerar_sha256)
sha256_button.grid(row=8, column=0, padx=5, pady=2)

multi_button = tk.Button(button_frame, text="Multicódigo", width=30, command=multicodigo)
multi_button.grid(row=9, column=0, padx=5, pady=2)

calc_button = tk.Button(button_frame, text="Calcular Expressão", width=30, command=calcular)
calc_button.grid(row=10, column=0, padx=5, pady=2)

url_button = tk.Button(button_frame, text="URL Decode", width=30, command=url_decode)
url_button.grid(row=11, column=0, padx=5, pady=2)

# Iniciar interface
tk.mainloop()
