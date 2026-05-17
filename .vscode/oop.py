class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 100
    canal:int = 1
    volume_min:int = 0
    volume_max:int = 100
    volume:int = 0

    def __init__(self, canal=1, volume=2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def mostrar_tv(self):
        conteudo = ''
if self.ligado==False:
            conteudo = 'TV desligada'
        else:
      conteudo = 'CANAL E VOLUME ATUAL '
      