from util.gerais import mostrar_objetos
from entidades.pesquisador import (inserir_pesquisador, obter_pesquisadores, selecionar_pesquisadores, Pesquisador)
from entidades.elemento_quimico import (inserir_elemento_quimico, obter_elementos_quimicos, selecionar_elementos_quimicos,
                                        ElementoQuimico)
def cadastrar_elementos_quimicos():
    inserir_elemento_quimico(ElementoQuimico(nome='Hidrogênio', simbolo='H', numero_atomico=1, massa_atomica=1.01))
    inserir_elemento_quimico(ElementoQuimico('Hélio', 'He', 2, 4.0))
    inserir_elemento_quimico(ElementoQuimico('Lítio', 'Li', 3, 6.94))
    inserir_elemento_quimico(ElementoQuimico('Berílio', 'Be', 4, 9.01))
    inserir_elemento_quimico(ElementoQuimico('Boro', 'B', 5, 10.8))
    inserir_elemento_quimico(ElementoQuimico('Carbono', 'C', 6, 12.0))
    inserir_elemento_quimico(ElementoQuimico('Nitrogênio', 'N', 7, 14.0))
    inserir_elemento_quimico(ElementoQuimico('Oxigênio', 'O', 8, 16.0))
    inserir_elemento_quimico(ElementoQuimico('Flúor', 'F', 9, 19.0))
    inserir_elemento_quimico(ElementoQuimico('Neônio', 'Ne', 10, 20.2))

def cadastrar_pesquisador():
    inserir_pesquisador(Pesquisador(nome='Marie Curie', ano_nascimento=1867, instituicao='Universidade de Paris',
                                    pais='França', premio_nobel=True))
    inserir_pesquisador(Pesquisador('Dmitri Mendeleev', 1834, 'Universidade de São Petersburgo',
                                    'Rússia',False))
    inserir_pesquisador(Pesquisador('Glenn T. Seaborg', 1912, 'Universidade da Califórnia, Berkeley',
                                    'Estados Unidos', True))
    inserir_pesquisador(Pesquisador('Linus Pauling', 1901, 'California Institute of Technology',
                                    'Estados Unidos', True))
    inserir_pesquisador(Pesquisador('Henry Moseley', 1887, 'Universidade de Oxford',
                                    'Reino Unido', False))


if __name__ == '__main__':

    cadastrar_elementos_quimicos()
    cabecalho = 'Elementos Químicos: Nome -- Símbolo -- Número Atômico -- Massa Atômica'
    mostrar_objetos(cabecalho='\n' + cabecalho, lista=obter_elementos_quimicos())
    elementos_selecionados, filtros = selecionar_elementos_quimicos()
    mostrar_objetos(cabecalho='\n' + cabecalho, lista=elementos_selecionados, filtros=filtros)

    elementos_selecionados, filtros = selecionar_elementos_quimicos(max_massa_atomica=8.10)
    mostrar_objetos(cabecalho='\n' + cabecalho, lista=elementos_selecionados, filtros=filtros)

    elementos_selecionados, filtros = selecionar_elementos_quimicos(8.10, prefixo_elemento='H',)
    mostrar_objetos(cabecalho='\n' + cabecalho, lista=elementos_selecionados, filtros=filtros)

    elementos_selecionados, filtros = selecionar_elementos_quimicos(8.10, 'H',
                                                                    min_numero_atomico=2)
    mostrar_objetos(cabecalho='\n' + cabecalho, lista=elementos_selecionados, filtros=filtros)

    cadastrar_pesquisador()
    cabecalho = 'Pesquisadores: Nome -- Ano de Nascimento -- Instituição -- País -- Prêmio Nobel'
    mostrar_objetos(cabecalho='\n' + cabecalho, lista=obter_pesquisadores())
    pesquisadores_selecionados, filtros = selecionar_pesquisadores()
    mostrar_objetos(cabecalho='\n' + cabecalho, lista=pesquisadores_selecionados, filtros=filtros)

    pesquisadores_selecionados, filtros = selecionar_pesquisadores(nobel=True)
    mostrar_objetos(cabecalho='\n' + cabecalho, lista=pesquisadores_selecionados, filtros=filtros)

    pesquisadores_selecionados, filtros = selecionar_pesquisadores(True, min_ano_nascimento=1900)
    mostrar_objetos(cabecalho='\n' + cabecalho, lista=pesquisadores_selecionados, filtros=filtros)

    pesquisadores_selecionados, filtros = selecionar_pesquisadores(True, 1900, prefixo_nome='L')
    mostrar_objetos(cabecalho='\n' + cabecalho, lista=pesquisadores_selecionados, filtros=filtros)
