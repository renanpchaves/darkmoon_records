class Albums:
    album = []

    def __init__(self, nome, artista, quant_musicas=0):
        self.nome = nome
        self.artista = artista
        self.quant_musicas = quant_musicas
        Albums.album.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.quant_musicas}'

    @staticmethod
    def listar_albums():
        for i in Albums.album:
            print (f'{i.nome} | {i.artista} | {i.quant_musicas} faixas')

album1 = Albums('The Dark Side of the Moon', 'Pink Floyd', 10)
album2 = Albums('Abbey Road', 'The Beatles', 17)

Albums.listar_albums()