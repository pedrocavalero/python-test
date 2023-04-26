def dict_to_string(dicionario):
    lista = [f"{chave}: {valor}" for chave, valor in dicionario.items()]
    resultado = ", ".join(lista)
    return resultado
