def mostrar_objetos(cabecalho, lista, filtros=None) -> None:
    if filtros is not None: print(filtros, end='')
    print(cabecalho)
    for indice, objeto in enumerate(lista):
        mostrar_objeto(indice, str(objeto))

def mostrar_objeto(indice, objeto) -> None:
    separador = '-'
    ordem = indice + 1
    frase = f'{ordem:2d} {separador} {objeto}'
    print(frase)



