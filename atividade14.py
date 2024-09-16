# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado
n1 = float(input())
n2 = float(input())
n3 = float(input())
resultado = (n1+n2+n3) / 3
if resultado>=7:
    print('Aprovado')
elif resultado>=5:
    print("recuperação")
else:
    print('reprovado')