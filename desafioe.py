##### ESCREVER A FUNCAO ABAIXO
def calcula_media(M1,M2,M3):
  ###### escrever abaixo
    media = (M1+M2+M3)/3

if(media > 0.0 and media  <=4.0):
      print(f'Sua média final é ', media , 'Aluno REPROVADO')
    else:
    if(media >= 4.1 and media <= 6.0):
            print(f'Sua méida final é', media, 'Aluno pegou EXAME')
    exame = float(input('Digite a nota do EXAME : '))
    if(exame >= 6.0):
           print(f'Aluno APROVADO')
    else:
           print('REPROVADO')
else:
    print('Aluno Aprovado')