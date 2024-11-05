#Questão 03
def diferentes(lista_a, lista_b):
   return list(set(lista_a).symmetric_difference(set(lista_b)))

def main():
    try:
        a = input("Entre com a primeira lista: ")
        b = input("Entre com a segunda lista: ")
        lista_a = [int(num) for num in a.split()]
        lista_b = [int(num) for num in b.split()]
        print(diferentes(lista_a,lista_b))
    except Exception as error:
        print("Ocorreu um erro")

if __name__=='__main__':
    main()