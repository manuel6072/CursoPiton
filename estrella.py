def imprimir(altura):
    for i in range(altura):
        print(' '*(altura+i)+ '*'+(' '*(altura-i-1)+('*'*(altura-i+1))))








imprimir(int(input("ingresa su tamaño:")))