
nome = input('Digite o nome no Canal: ')
link = input('Digite o Link no Canal: ')
link2 = link.replace('/','\/')
img  = input('Digite o Link da Imagem: ')
img2 = img.replace('/','\/')
print("[\""+nome+"\",")
print("\""+link2+"\",")
print("\""+img2+"\"]")
