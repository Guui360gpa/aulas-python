# Exercicios da Aula 02

**Ex1.** Escreva uma função chamada right_align que recebe como parâmetro uma String chamada msg e imprime a String com um número necessário de espaços em branco, para o último caractere de msg aparecer na coluna 70 do display.
Use a função para repetir strings do python (operador  ∗  seguido do número de repetições). Para imprimir o conteúdo com o último caractere na posição 70 você vai precisar saber quantas letras existem em msg, você pode fazer isso através da função len do python, por exemplo len('abc') vai retornar  3 . Depois basta concatenar a repetição com msg e imprimir no display. Se chamarmos right_align('Funções'), deve aparecer algo como a seguir:

**Ex2.** Em Python, uma função pode ser argumento de outra função. Por exemplo, considere do_twice como uma função que recebe como argumento uma função e executa ela duas vezes:

`def do_twice(func):
    func()
    func()`

Esse é um exemplo de chamada de do_twice:

`def print_spam():
    print('Spam')
do_twice(print_spam)`

- 1- Modifique do_twice para receber dois argumentos: uma função e um valor, e chame a função passada por argumento com o valor duas vezes.
- 2- Use a versão de do_twice do exercício anterior para receber a função print_twice e o valor 'Spam'.
- 3- Defina uma nova função chamada do_four que recebe como argumento uma função e um valor e faz a chamada dessa função 4 vezes utilizando o valor. A função do_four deve ter apenas duas linhas.

**Ex3.** Escreva uma função que desenhe o seguinte grid de 2 linhas e 2 colunas (podem ser utilizadas outras funções auxiliares). Para imprimir mais de um valor por linha, basta chamar o print com mais de um parâmetro, ex: print('+', '-'). Por default o print sempre pula para a próxima linha, podemos alterar esse comportamento passando a opção end como um espaço vazio, ex: print('+', '-', end=' ').

**Ex4.** Escreva uma função que imprima um grid similar ao anterior com 4 linhas e 4 colunas (podem ser utilizadas outras funções auxiliares).

**Ex5.** Escreva uma função que imprime um triângulo de 5 linhas usando o caracter +

**Ex6.** Escreva uma função lambda que desenha um retângulo com  n  colunas e 5 linhas usando o caracter +

**Ex7.** Escreva uma função que recebe dois números, digamos  a  e  b  e retorna a soma  c=a+b . A função deve imprimir o valor de  c .
