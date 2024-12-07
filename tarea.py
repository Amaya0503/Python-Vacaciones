print ("")
print ("---------Bienvenido a la calculadora---------")

print ("")
print ("Digita el primer numero")
n1 = int(input())
print ("Digita el segundo numero")
n2 = int(input())
print ("")

print ("Que operación deseas realizar?")
print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicacion")
print ("4. Division")
print ("5. Salir")
op = int(input())

if op == 1:
    print("El resultado de la suma de " + str(n1) + " + " + str(n2) + " es: " + str(n1 + n2))
elif op == 2:
    print("El resultado de la resta de " + str(n1) + " - " + str(n2) + " es: " + str(n1 - n2))
elif op == 3:
    print("El resultado de la multiplicacion de " + str(n1) + " * " + str(n2) + " es: " + str(n1 * n2))
elif op == 4:
    if n2 == 0:
        print("No se puede dividir entre cero")
    else:
        print("El resultado de la division de " + str(n1) + " / " + str(n2) + " es: " + str(n1 / n2))
elif op == 5:
    print("")
    print ("---------Gracias por usar mi calculadora---------")
else:
    print("Operacion no valida")

    