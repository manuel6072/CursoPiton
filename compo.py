def copo_nieve_complejo(tamano=7)
    for i in range(tamano):
        for j in range (tamano):
            if i == tamano//2 or j == tamano//2 or i == j or i + j == tamano -1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
        
copo_nieve_complejo(9)