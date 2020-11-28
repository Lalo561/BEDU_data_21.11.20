# Script que calcula la tabla de multiplicar de un número
#Solicitar numero al usuario por consola
numero = input('¿Qué numero quieres multiplicar?\t')

#Solcita el número hasta el cual se desea realizar la multiplicación
limite = input('¿Hasta que número deseas multiplicar?\t')

#El dato ingresado por el usuario es una cadena "<str>"
#Se debe convertir a numero "<int>" para poder multiplicar
numero = int(numero)
limite = int(numero)

#for n in range(10):
#    resultado = numero * (n + 1)
#    print(resultado)

for num in range(limite):
    r = numero * (num + 1)
    print(f'{numero} * {num+1} = {r}')