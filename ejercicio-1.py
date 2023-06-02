"""
1. Crear función para eliminar espacios de un string
2. Crear función que devuelva un diccionario con el conteo total por letra
3. Crear función que ordene el diccionario por letras y retorne una lista de tuplas. Ejemplo: [("a",2),("b",3)]
4. Crear funcion que retorne el una lista de tuplas que contengan el mayor valor de conteo
5. Crear una funcion que imprima un mensaje en consola indicando las letras con mayor conteo

Nota La funcion N°5 tiene que implementar las funciones anteriores a ella.
"""
def eliminar_espacios(s: str):
    return s.replace(" ", "")


def contar_caracteres(s: str):
    newStr = eliminar_espacios(s)
    count_caracter = {}
    for l in set(newStr):
        count_caracter[l] = newStr.count(l)
    return count_caracter


def order_diccionary(diccionary: dict):
    list_order = [(x, y) for x, y in diccionary.items()]
    list_order.sort()
    return list_order


def order_tuple(tupla: tuple):
    lista = [(x, y) for x, y in tupla]
    lista.sort(key=lambda a: a[1], reverse=True)
    cantidad = [x[1] for x in lista].count(lista[0][1])
    return lista[:cantidad]


def print_mesaje(string: str):
    dictionary_caracter = contar_caracteres(string)
    new_dictionary = order_diccionary(dictionary_caracter)
    new_list = order_tuple(new_dictionary)
    print(f"Los caracteres que más se repiten con {new_list[0][1]} repeticiones son: ")
    for tupla in new_list:
        print(tupla[0].upper())


print_mesaje("ddddaaaccccbb")
