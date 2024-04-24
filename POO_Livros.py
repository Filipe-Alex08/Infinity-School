"""
Imagine que você está desenvolvendo um sistema para gerenciar uma biblioteca. 
Nessa biblioteca, existem diferentes tipos de livros, como romances, biografias, livros infantis, etc. 
Todos esses livros possuem algumas características em comum, como o título, o autor e a editora, mas também possuem características específicas,
como o número de páginas, a faixa etária recomendada, etc.
"""

class Livro:
    def __init__(self, titulo, autor, editora, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.num_paginas = num_paginas

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Editora: {self.editora}")
        print(f"Número de Páginas: {self.num_paginas}")

class Romance(Livro):
    def __init__(self, titulo, autor, editora, num_paginas, faixa_etaria):
        super().__init__(titulo, autor, editora, num_paginas)
        self.faixa_etaria = faixa_etaria

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Faixa Etária Recomendada: {self.faixa_etaria}")

class Biografia(Livro):
    def __init__(self, titulo, autor, editora, num_paginas, personagem_principal):
        super().__init__(titulo, autor, editora, num_paginas)
        self.personagem_principal = personagem_principal

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Personagem Principal: {self.personagem_principal}")

livro_romance = Romance("Romeu e Julieta", "William Shakespeare", "Editora A", 200, "12+")
livro_biografia = Biografia("Steve Jobs: A Biografia", "Walter Isaacson", "Editora B", 600, "Steve Jobs")

print("Detalhes do Romance:")
livro_romance.exibir_detalhes()

print("\nDetalhes da Biografia:")
livro_biografia.exibir_detalhes()