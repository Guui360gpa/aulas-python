# Ex5. Escreva um código que converte um valor em reais para as moedas dolar, euro, Som uzbeque e Iene Japônes.
#Considere que:
#Um real equivale a  0.27  dolar
#Um real equivale a  0.23  euro
#Um real equivale a  2241.99  Som uzbeque
#Um real euqivale a  29.49  Iene Japônes

valor = float(input("Digite um valor: "))
opcao = -1

while opcao != 0:
    print("\n------------------------")
    print("---MENU DE CONVERSÕES---")
    print("------------------------")
    print(""" 
    [0] sair
    [1] dolar
    [2] euro
    [3] uzbeque
    [4] iene
    """)
    opcao = int(input("Digite uma opção: "))

    if opcao == 0:
        break
    elif opcao == 1:
        print(f"\n{(valor * 0.27):.2f} USD")
    elif opcao == 2:
        print(f"\n{(valor * 0.23):.2f} EUR")
    elif opcao == 3:
        print(f"\n{(valor * 2241.99):.2f} UZS")
    elif opcao == 4:
        print(f"\n{(valor * 29.49):.2f} JPY")
    else:
        print("\nOpção inválida")
