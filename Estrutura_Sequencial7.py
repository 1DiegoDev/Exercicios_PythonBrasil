# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.


#A area de um quadrado é feita pela multiplicação da base e da lateral que tem o mesmo tamanho e valor
lateralDoQuadrado = int(input("Coloque o valor da lateral: "))
# ** = é a operação matemática que representa a multiplicação de fatores iguais
area = lateralDoQuadrado ** 2

dobroArea = area * 2

print(f"O dobro da área do quadrado é {dobroArea}")