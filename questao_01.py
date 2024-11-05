#Questão 01:
def numeros_impares(n)-> list:
    impares = []
    for num in n:
        if num %2 != 0:
            impares.append(num)
    return impares

def main():
    try:
        entrada = input("Entre com os numeros: ")
        n = [int(i) for i in entrada.split()]
        print(numeros_impares(n))
    except Exception as error:
        print("Ocorreu um erro")

if __name__=='__main__':
    main()