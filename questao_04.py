#Questão 04
def segundo_maior(lista) -> int:
    ordem = sorted(lista)
    for num in ordem:
        if num > ordem[0]:
            return num
        
def main():
    try:
        entrada = input("Entre com a lista de numeros: ")
        lista = [int(num) for num in entrada.split()]
        print(segundo_maior(lista))
    except Exception as error:
        print("Ocorreu um erro")

if __name__=='__main__':
    main()