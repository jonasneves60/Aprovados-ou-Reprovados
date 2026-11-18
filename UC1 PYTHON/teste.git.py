aprovados = reprovados =0
for a in range (0,10):
    ra=input('Seu RA?')
    notas_soma=0
    for n in range(0,4):
        notas=float(input('Digite a nota :'))
        notas_soma+=notas
    média = notas_soma/4
if média >= 6:
    print(f'Sua média foi {média} Você foi aprovado !')
    aprovados+=1
else:
    print(f'Você não alcançou sua média necessária {média}')
    reprovados+=1
print(f'No total foram aprovados {aprovados} alunos')
print(f'No total foram reprovados {reprovados} alunos')
