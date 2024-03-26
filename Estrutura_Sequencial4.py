# Faça um Programa que peça as 4 notas bimestrais e mostre a média.


#Perguntei cada uma das notas e coloquei "float" por que podem não ser números inteiros como, EX: 9.7
nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("Digite sua nota 2: "))
nota3 = float(input("Digite sua nota 3: "))
nota4 = float(input("Digite sua nota 4: "))


#Fiz as contas, Somei todas as notas e depois dividi pelo numero de notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# E imprimi com um pouco mais de efeito usando a f-string - (f''' Espaço ''')
print(f'''
======================================
      Sua média de nota é: {media}
======================================
''')