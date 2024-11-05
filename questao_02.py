#Questão 02:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def filtro(numeros):
    return[num for num in numeros if is_prime(num)]

def main():
    try:
        entrada = input("Entre com os números: ")
        lista_numeros = [int(num) for num in entrada.split()]
        primos = filtro(lista_numeros)
        print(primos)
    except Exception as error:
        print("Ocorreu um erro")
    
if __name__=='__main__':
    main()