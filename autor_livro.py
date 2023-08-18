class Autor:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

autor1 = Autor("Leonardo Moleiro", "18/02/2003")

livro1 = Livro("Aulinha de Python", autor1)

print(f"Autor: {livro1.autor.nome}")
print(f"Título: {livro1.titulo}")
print(f"Data de Nascimento do Autor: {livro1.autor.data_nascimento}")