from entidades.elemento_quimico import ElementoQuimico

grupos = {}
def get_grupos(): return grupos
def obter_grupos(): return grupos
def inserir_grupo(grupo): grupos.append(grupo)


def inserir_grupo(grupo):
    nome_grupo = grupo.nome
    if nome_grupo not in grupo.keys():
        grupos[nome_grupo] = grupo
        return True
    else:
        print('grupo'+nome_grupo + 'Já tem cadastro')
        return False


class Grupo:
    def __init__(self, nome):
        self.nome = nome
        self.elementos_quimicos = {}

    def __str__(self):
        formato = '{} {:<20} {}'
        grupo_formatada = formato.format('|', self.nome, '|')
        return grupo_formatada


    def inserir_elemento_quimico(self, elemento_quimico):
        nome_elemento_quimico = elemento_quimico.nome
        if nome_elemento_quimico not in self.elementos_quimicos.keys():
            self.elementos_quimicos[nome_elemento_quimico] = elemento_quimico
        else:
            print('Elemento Químico ' + nome_elemento_quimico + ' já tem cadastro no Grupo')



