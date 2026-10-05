# Ex6. Escreva um programa inverso ao anterior, ou seja converte dolar, euro, Som uzbeque e Iene Japônes para real.
# De acordo com o exercício acima, considere que:
# Um dolar equivale a  10.27  real.
# Pensem nos demais olhando o exercício anterior...

valor = float(input("Digite um valor: "))
opcao = -1

while opcao != 0:
    print("\n------------------------")
    print("---MENU DE CONVERSÕES---")
    print("------------------------")
    print(""" 
    Qual é a unidade monetária:
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
        print(f"\n R$ {(valor / 0.27):.2f}")
    elif opcao == 2:
        print(f"\n R$ {(valor / 0.23):.2f}")
    elif opcao == 3:
        print(f"\n R$ {(valor / 2241.99):.2f}")
    elif opcao == 4:
        print(f"\n R$ {(valor / 29.49):.2f}")
    else:
        print("\nOpção inválida")
