#Ex3. Suponha que em uma gráfica, a capa de um livro custe
# R$24,95  reais, porém, a gráfica está dando  40%  de desconto por capa.
# A primeira cópia do conteúdo do livro custa
# R$3,00  reais e as demais custam  R$0,75  centavos cada.
# Qual o custo total de  60  cópias do livro (incluindo as capas)? (utilize variáveis)

CAPA_LIVRO = 24.95
DESCONTO_CAPA = 0.4
total = 0

for i in range(60):
    capa_desconto = CAPA_LIVRO - (CAPA_LIVRO * DESCONTO_CAPA)
    if i == 0:
        preco_livro = capa_desconto + 3
        total += preco_livro
    else:
        preco_livro = capa_desconto + 0.75
        total += preco_livro

print(f"Total: {total:.2f}")