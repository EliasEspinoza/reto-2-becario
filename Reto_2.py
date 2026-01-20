#Funcion para sumar 2 numeros enteros
def sumarNumeros(a, b):
    if not(isinstance(a, int) and isinstance(b,int)): #Verificamos que los valores sean enteros
        return "Ambos parametros deben ser numeros enteros." #Retornar mensaje de error

    # Verificamos que no sean valores booleanos porque estos son tamos como 0 o 1
    if (isinstance(a, bool) or isinstance(b, bool)):
        return "Ambos parametros deben ser numeros enteros." #Retornar mensaje de error

    #Si se llega aqui ambos numeros son enteros
    return f"El resultado de la suma es: {a+b} SW"



parametros = [(5, 3), (-10, 4), (0, 0), (123, 877), (5.5, 3), ("10", 2), (8, None), (True, 1), ([], {})]

for p in parametros:
    a, b = p
    print(sumarNumeros(a, b))
