def ordem_alfabetica(lista) -> list:
    return sorted(lista, key = lambda pessoa: pessoa[0])

def main():
    try: 
        entrada = input("Entre com os dados divididos por ';': ")
        lista = [(item.split(", ")[0], int(item.split(", ")[1])) for item in entrada.split("; ")]
        print(ordem_alfabetica(lista))
    except Exception as error:
        print("Ocorreu um erro")

if __name__=='__main__':
    main()
