pesquisadores = []
def inserir_pesquisador(pesquisador):pesquisadores.append(pesquisador)
def obter_pesquisadores(): return pesquisadores


def selecionar_pesquisadores(nobel=None, min_ano_nascimento=None, prefixo_nome=None):
    pesquisadores_selecionados = []
    filtros = '\nFiltros -- '
    if nobel is not None:
        filtros += f'  Prêmio Nobel: {nobel}'
    if min_ano_nascimento is not None:
        filtros += f' - Ano de Nascimento Mínimo: {min_ano_nascimento}'
    if prefixo_nome is not None:
        filtros += f' - Prefixo Nome: {prefixo_nome} '
    for pesquisador in pesquisadores:
        if nobel is not None and pesquisador.premio_nobel != nobel:
            continue
        if min_ano_nascimento is not None and pesquisador.ano_nascimento < min_ano_nascimento:
            continue
        if prefixo_nome is not None and not pesquisador.nome.startswith(prefixo_nome):
            continue
        pesquisadores_selecionados.append(pesquisador)
    return pesquisadores_selecionados, filtros


class Pesquisador:

    def __init__(self, nome, ano_nascimento, instituicao, pais, premio_nobel=False):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.premio_nobel = premio_nobel
        self.instituicao = instituicao
        self.pais = pais

    def __str__(self):
        premio_nobel_str = "Prêmio Nobel" if self.premio_nobel is True else "-"
        frase = '| {:^17}|{:^6}|{:^45}| {:^16} |{:^14}|'
        return frase.format(self.nome, self.ano_nascimento, self.instituicao, self.pais, premio_nobel_str)
