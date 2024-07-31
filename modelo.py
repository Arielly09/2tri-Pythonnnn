class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
         return self._nome

    @nome.setter
    def nome (self,novo__nome):
        self._nome = novo__nome.title()

    @property
    def likes(self):
         return self._likes

    def dar_likes(self): 
        self._likes += 1

    def __str__(self):
        return f'{self.nome}- {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao
        self._likes = 0
        
class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome,ano)
        self.temporada = temporada 
        self._likes = 0
        
class Playlist(list):
    def __init__(self,nome,programas):
        self.nome = nome 
        super().__init__(programas)


vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
atlanta = Serie('Atlanta', 218, 2)
tmep = Filme('Todo mundo em  pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

filmes__e__series = [vingadores,atlanta]
playlist_fim_de_semana = Playlist('fim e semana',filmes__e__series)

print (f'Tamanho da Playlist: {len(playlist_fim_de_semana)}')

for programa in filmes__e__series:
    print (programa)

print(f'Está ou não? {demolidor in playlist_fim_de_semana}')