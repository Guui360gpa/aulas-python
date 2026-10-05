# Ex11. Escreva um programa que calcule o seguinte polinômio  p=x2+x3+x5 .

print("CALCULO DE POLINÔMIO")
print("Fórmula: p = x² + x³ + x⁵\n")

x = float(input("Digite o valor de x: "))

p = x**2 + x**3 + x**5

print(f"O resultado do polinômio é: {p:.2f}")