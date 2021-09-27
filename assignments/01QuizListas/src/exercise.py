def main():
    #escribe tu código abajo de esta línea
    lista1 = []
    lista2 = []
    lista3 = []

    num = int(input())

    if num <= 0:
        print("Error")
    else:
        for i in range(num):
            lista1.append(int(input()))
        
        for i in range(num):
            lista2.append(int(input()))

        for i in range(num):
            lista3.append(lista1[i] + lista2[i])
        
        print(lista3)



if __name__=='__main__':
    main()