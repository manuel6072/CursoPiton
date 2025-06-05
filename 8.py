print ("BINVENIDO A LA CALCULADORA AUTOMATICA")
nombre=input("antes que nada queremos saber mas de ti, ¿Cual es tu nombre?")
edad=int(input("Cual es tu edad"))

if edad >= 18:
   
    ope=int(input("Que operacion deseas hacer:\n 1.SUMA \n 2.RESTA \n 3.MULTIPLICACION \n 4.DIVISION \n "))
    numero1=int(input("Dame el primer numero:"))
    numero2=int(input("Dame el segundo numero:"))

    print("estos son los numeros que me diste")
    primes = [numero1,numero2]
    for prime in primes:
        print(prime)

    if ope == 1:
        print(f"Resultado de la suma: ",numero1+numero2)
    elif ope == 2:
        print(f"Resultado de la resta: ",numero1-numero2)
    elif ope == 3:
        print("Resultado de la multiplicacion: ",numero1*numero2)
    elif ope == 4:
        print("Resultado de la division: ", numero1/numero2)

    else:
        print("no puedes pasar chamaco")


else:
    print("no puedes pasar {}".format(nombre))


