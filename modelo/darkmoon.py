from modelo.rating import Rating
from modelo.database import Session, AlbumDB, RatingDB

class Albums:
    album = []

    def __init__(self, nome, artista, quant_musicas=0):
        self._nome = nome.title()
        self._artista = artista.upper()
        self._quant_musicas = quant_musicas
        self._ativo = False
        self._avaliacao = []
        self._id = None #id na DB
        Albums.album.append(self)

    def __str__(self):
        return f'{self._nome} | {self._artista} | {self._quant_musicas} | {self._ativo}'

    @classmethod
    def listar_albums(cls):
        print (f'{'Nome do Album'.ljust(28)} | {'Artista'.ljust(25)} | {'Número de faixas'.ljust(25)} | {'Avaliação'.ljust(26)} | Estoque')
        for i in Albums.album:
            print (f'{i._nome.ljust(28)} | {i._artista.ljust(25)} | {str(i._quant_musicas).ljust(25)} | {str(i.media_avaliacoes).ljust(25)} | {i.ativo}')

    @property
    def ativo(self):
        return '✅ - em estoque' if self._ativo else '❌ - fora de estoque'

    def estoque_alt(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
            if 0 <= nota <= 5:
                avaliacao = Rating(cliente, nota)
                self._avaliacao.append(avaliacao)
                return True
            return False

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '⭐ ---'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return f'⭐ {media}'
    
    def salvar_db(self):
        '''
        salva o album no banco
        '''
        session = Session()
        try:
            #objeto:
            album_db = AlbumDB(
                nome=self._nome,
                artista=self._artista,
                quant_musicas=self._quant_musicas,
                ativo=self._ativo
            )
            #avaliaçoes:
            for avaliacao in self._avaliacao:
                rating_db = RatingDB(
                    cliente=avaliacao._cliente,
                    nota=avaliacao._nota
                )
                album_db.avaliacoes.append(rating_db)

            #Salvando aqui:
            session.add(album_db)
            session.commit()

            self._id = album_db.id
            print (f'✅ Salvo na base de dados com o ID: {self._id}')
        
        except Exception as e:
            session.rollback()
            print (f'❌ Erro ao salvar: {e}')
        finally:
            session.close()

    @classmethod
    def carregar_db(cls):
        '''
        carrega todos os albuns do banco
        '''
        session = Session()
        try:
            albums_db = session.query(AlbumDB).all()

            #limpa a lista atual
            cls.album.clear()

            #recriar os objetos:
            for album_db in albums_db:
                album = cls(
                    album_db.nome,
                    album_db.artista,
                    album_db.quant_musicas
                )
                album._ativo = album_db.ativo
                album._id = album_db.id

                #carrega as avaliaçoes pra listar:
                for rating_db in album_db.avaliacoes:
                    rating = Rating(rating_db.cliente, rating_db.nota)
                    album._avaliacao.append(rating)

            print(f'✅ {len(cls.album)} álbuns carregados do banco!')

        except Exception as e:
            print(f'❌ Erro ao carregar: {e}')
        finally:
            session.close()

