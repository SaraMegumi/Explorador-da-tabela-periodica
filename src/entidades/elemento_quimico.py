elementos_quimicos = []
def inserir_elemento_quimico(elemento_quimico): elementos_quimicos.append(elemento_quimico)
def obter_elementos_quimicos(): return elementos_quimicos
def get_elementos_quimicos(): return elementos_quimicos




def selecionar_elementos_quimicos(max_massa_atomica=None, prefixo_elemento=None, min_numero_atomico=None ):
    elementos_selecionados = []
    filtros = '\nFiltros -- '
    if max_massa_atomica is not None:
        filtros += f' Massa Atômica Máxima: {max_massa_atomica}'
    if prefixo_elemento is not None:
        filtros += f' - Prefixo Elemento: {prefixo_elemento} '
    if min_numero_atomico is not None:
        filtros += f' - Número Atômico Mínimo: {min_numero_atomico} '
    for elemento in elementos_quimicos:
        if max_massa_atomica is not None and elemento.massa_atomica > max_massa_atomica:
            continue
        if prefixo_elemento is not None and not elemento.nome.startswith(prefixo_elemento):
            continue
        if min_numero_atomico is not None and elemento.numero_atomico < min_numero_atomico:
            continue
        elementos_selecionados.append(elemento)
    return elementos_selecionados, filtros




class ElementoQuimico:
    def __init__(self, nome, simbolo, numero_atomico, massa_atomica):
        self.nome = nome
        self.simbolo = simbolo
        self.numero_atomico = numero_atomico
        self.massa_atomica = massa_atomica

    def __str__(self):
        frase ='| {:^15} | {:^4} | {:^4} | {:^8} |'
        return frase.format(self.nome, self.simbolo, self.numero_atomico, self.massa_atomica)
