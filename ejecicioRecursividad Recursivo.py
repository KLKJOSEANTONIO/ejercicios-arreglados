def leerLista(lista):
    if len(lista)==1:
        return lista[0]
    num = lista[0]
    if type(num)==list:
        for j in num:
            if len(num)==1:
                return j+leerLista(lista[1:])
            return j+leerLista(num[1:])+leerLista(lista[1:])
    if type(num)==int:
        return num+leerLista(lista[1:])
lista_numeros = [2, 3, [ 1, 2 ], 3, 5, [2, 3, 6, 10, 7], 3]
print(leerLista(lista_numeros))