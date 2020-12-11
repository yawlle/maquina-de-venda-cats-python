from os import system, name 
import math as m


def limpaTela(): 
    """
    Auto-explicativo, essa função irada limpa a tela do terminal quando é executada.
    """
    if name == 'nt': 
        system('cls') 
    else: 
        system('clear') 

def maquina(a,b,c,d,e):
    

    """
    Menu da máquina, com preços
    """
    RST     = '\033[00m'
    VIOLET     = '\033[033m'
    print(VIOLET)
    print("+" + "-"*50 + "+")
    print("|" + " "*50 + "|")
    print("|            MÁQUINA DE COMIDA FELINA              |")
    print("|               NYAN ^----^'                       |")
    print("|" + " "*50 + "|")
    print("+" + "-"*50 + "+")
    print("|" + " "*50 + "|")
    if a <= 0:
        print("| 1 - WHISKAS SABOR PEIXE            - Indisponivel|")
    else:
        print("| 1 - WHISKAS SABOR PEIXE                R$ 2,50   |")
    if b <= 0:
        print("| 2 - WHISKAS SABOR CARNE            - Indisponivel|")
    else:
        print("| 2 - WHISKAS SABOR CARNE                R$ 2,10   |")
    if c <= 0:
        print("| 3 -   PETISCO STARFISH             - Indisponivel|")
    else:
        print("| 3 - PETISCO STARFISH                   R$ 5,00   |")
    if d <= 0:
        print("| 4 - BRINQUEDO PURR-CHASE           - Indisponivel|")
    else:
        print("| 4 - BRINQUEDO PURR-CHASE               R$ 10,00  |")
    if e <= 0:
        print("| 5 - ORELHAS NYAN KAWAII            - Indisponivel|")
    else:
        print("| 5 - ORELHAS NYAN KAWAII                R$ 20,00  |")
    if a == 0 and b == 0 and c == 0 and d == 0 and e == 0: #Se não tiver estoque, avisa pro cliente e para o programa imediatamente.
        print("| NÃO HÁ PRODUTOS NA MÁQUINA, VOLTE MAIS TARDE!    |")
        print("Obrigada pela preferência! ^-^")
        x = input("--> Enter para continuar...")
        exit()
    print("|" + " "*50 + "|")
    print("+" + "-"*50 + "+")

  


def escolhadoproduto():
    """
    Verificação do produto digitado pelo usuário.
    """
    produto = 0
    produto = int(input("Escolha seu produto: ")) #Escolha do produto do cliente
    if produto <= 5 and produto > 0:
        return produto
    else: 
        print("Produto inválido ='< Digite os números correspondentes na tela *-* ")
        return escolhadoproduto()

  

def pedidodetroco(troco):
    """
    Essa função tem a finalidade de dividir o troco em forma de notas.
    """
    if troco >= 100:
        print("R$100")
        troco = troco - 100
        pedidodetroco(troco)
    elif troco >= 50:
        print("R$50")
        troco = troco - 50
        pedidodetroco(troco)
    elif troco >= 20:
        print("R$20")
        troco = troco - 20
        pedidodetroco(troco)
    elif troco >= 10:
        print("R$10")
        troco = troco - 10
        pedidodetroco(troco)
    elif troco >= 5:
        print("R$5")
        troco = troco - 5
        pedidodetroco(troco)
    elif troco >= 2:
        print("R$2")
        troco = troco - 2
        pedidodetroco(troco)
    elif troco >= 1:
        print("R$1")
        troco = troco - 1
        pedidodetroco(troco)
    elif troco >= 0.50:
        print("R$0.50")
        troco = troco - 0.50
        pedidodetroco(troco)
    elif troco >= 0.25:
        print("R$0.25")
        troco = troco - 0.25
        pedidodetroco(troco)
    elif troco >= 0.10:
        print("R$0.10")
        troco = troco - 0.10
        pedidodetroco(troco)
    elif troco >= 0.01:
        print("R$0.01")
        troco = troco - 0.01
        pedidodetroco(troco)


  

def insiradinheiro(valorDevido, soma = 0):
    """
    Função que ajuda no inserimento de dinheiro
    """

    dinheirocliente = float(input("Coloque o dinheiro ^-^': "))
    if dinheirocliente <= 0: #Digitar valor negativo dá erro
        print("Valor inválido!")
        return insiradinheiro(valorDevido, soma)
    elif dinheirocliente < valorDevido:
        return insiradinheiro(valorDevido - dinheirocliente, soma + dinheirocliente)
    elif dinheirocliente >= valorDevido:
        return (soma + dinheirocliente)
    

def central(a,b,c,d,e):
    """
    É aqui que eu controlo tudo, e é aqui que eu também coloco quanto de estoque tem nos produtos da máquina.
    Aqui o cliente insere o produto que deseja, e também tem controle de estoque.
    """
    
    limpaTela()
    maquina(a,b,c,d,e) 
    produto = escolhadoproduto()
    if produto == 1 and a > 0:
        preço = 2.50
        prod = 'WHISKAS SABOR PEIXE'
        print(f"Você escolheu {prod}! ^-^ ")
        print(f"Preço: R${preço}")
    elif produto == 1 and a <= 0:
        decisao = input("Esse produto está em falta ='/ Deseja comprar outro? S/N   ")   #Recurso para voltar o programa pro começo caso o produto que a pessoa queira esteja em falta.   
        if decisao == 'S' or decisao == 's':
            central(a,b,c,d,e)
        else: #Botei else em vez de N pois pensei que se o usuário for dumb, ele só precisa saber que S é pra SIM e qualquer outra tecla é NÃO
            print("Obrigada pela preferência! ^-^")
            x = input("--> Enter para continuar...")
            exit()
                
    if produto == 2 and b > 0:
        preço = 2.10
        prod = 'WHISKAS SABOR CARNE'
        print(f"Você escolheu {prod}! ^-^ ")
        print(f"Preço: R${preço}")
    elif produto == 2 and b <= 0:
        decisao = input("Esse produto está em falta ='/ Deseja comprar outro? S/N   ")      
        if decisao == "s" or decisao == "S":
           central(a,b,c,d,e)
        else:
            print("Obrigada pela preferência! ^-^")
            x = input("--> Enter para continuar...")
            exit()  

    if produto == 3 and c > 0:
        preço = 5.00
        prod = 'PETISCO STARFISH'
        print(f"Você escolheu {prod}! ^-^ ")
        print(f"Preço: R${preço}")

    elif produto == 3 and c <= 0:
        decisao = input("Esse produto está em falta ='/ Deseja comprar outro? S/N   ")      
        if decisao == 'S' or decisao == 's':
            central(a,b,c,d,e)
        else:
            print("Obrigada pela preferência! ^-^")
            x = input("--> Enter para continuar...")
            exit()   

    if produto == 4 and d > 0:
        preço = 10.00
        prod = 'BRINQUEDO PURR-CHASE'
        print(f"Você escolheu {prod}! ^-^ ")
        print(f"Preço: R${preço}")
    elif produto == 4 and d <= 0:
        decisao = input("Esse produto está em falta ='/ Deseja comprar outro? S/N   ")      
        if decisao == 'S' or decisao == 's':
            central(a,b,c,d,e)
        else:
            print("Obrigada pela preferência! ^-^")
            x = input("--> Enter para continuar...")
            exit()

    if produto == 5 and e > 0:
        preço = 20.00
        prod = 'ORELHAS NYAN KAWAII'
        print(f"Você escolheu {prod}! ^-^ ")
        print(f"Preço: R${preço}")
    elif produto == 5 and e <= 0:
        decisao = input("Esse produto está em falta ='/ Deseja comprar outro? S/N   ")      
        if decisao == 'S' or decisao == 's':
            central(a,b,c,d,e)
        else:
            print("Obrigada pela preferência! ^-^")
            x = input("--> Enter para continuar...")
            exit() 
    

    soma = insiradinheiro(preço)
    troco = (soma - preço) #Calculando troco
   

    print(f"Valor pago: R$ {soma}")
    print(f"Troco: R${troco:.2f}")
    if troco != 0:
        print("Pegue seu troco:")
    pedidodetroco(troco) #Chamada da função que calcula o troco porém em notas
    decisaofinal = input("Deseja comprar algo novamente? Meow meow? ^-^ S / N  "  )
    if decisaofinal == 's' or decisaofinal == 'S': #Aqui vamos ter um controle do estoque, onde de acordo com o produto escolhido, vai diminuir -1 no estoque na hora de recomeçar o programa.
        if produto == 1:
            central(a-1,b,c,d,e)
        if produto == 2:
            central(a,b-1,c,d,e)
        if produto == 3:
            central(a,b,c-1,d,e)
        if produto == 4:
            central(a,b,c,d-1,e)
        if produto == 5:
            central(a,b,c,d,e-1)           
    else:
        print("Obrigada pela preferência! ^-^ Seus gatinhos agradecem!")
        x = input("--> Enter para continuar...")
        exit()


central(5,5,5,5,5) #Começo do programa, aqui eu coloco o estoque inicial. 
#FOI MUITO DIVERTIDO FAZER ESSE PROGRAMA!!!!!!