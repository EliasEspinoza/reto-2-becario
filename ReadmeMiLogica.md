swcoding-challenges
Challenges

# Reto de Programación 2

Graciar por la oportunidad
Código realizado en python. Funcion implementada que recibe 2 numeros enteros
Si estos no son datos enteros retorna el siguiente mensaje:
"Ambos parametros deben ser numeros enteros."
Si ambos datos son enteros el mensaje sera el siguiente:
"El resultado de la suma es: Resultado SW"

Primero se revisa con una validacion que ambos parametros sean enteros, luego que alguno
de estos no sea un valor booleano, (los valores booleanos retornan verdadero en la función,
isinstance(True, int)), si se pasan ambas verificaciones se hace la suma y
se retorna el mensaje de exito, en caso de que en las validaciones se encuentre un datos
que no sea un entero o un booleano, se retorna el mensaje de error.

Se declaro una lista de tuplas con valores de prueba, tanto correctos como incorrectos para que al ejecutar
el script se pueda revisar su correcto funcionamiento.