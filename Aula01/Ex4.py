# Ex4. Como podemos alterar o código acima, para calcular o custo de  n  cópias do livro?

CAPA_LIVRO = 24.95
DESCONTO_CAPA = 0.4
total = 0

quantidade_copias = int(input("Quantidade de cópias: "))

for i in range(quantidade_copias):
    capa_desconto = CAPA_LIVRO - (CAPA_LIVRO * DESCONTO_CAPA)
    if i == 0:
        preco_livro = capa_desconto + 3
        total += preco_livro
    else:
        preco_livro = capa_desconto + 0.75
        total += preco_livro

print(f"Total {total:.2f}")