class Livro:
    def __init__(self,titulo:str,autor:str,num_paginas:int):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        
    def detalhes(self):
        print(f"Titulo: {self.titulo}\nAutor: {self.autor}\nNumero de paginas: {self.num_paginas}\n")
    

lista = [
    {"title": "O guarani", "autor": "jose de alencar", "NumPag": "250"},
    {"title": "Iracema", "autor": "José de Alencar", "NumPag": "210"},
    {"title": "Dom Casmurro", "autor": "Machado de Assis", "NumPag": "256"}

]

for i in lista:
    det = Livro(i["title"],i["autor"],i["NumPag"])
    det.detalhes()