#   Exemplo de Identação
#   Esse programa serve para avaliar se um aluno foi aprovado ou não com base em sua média.

#   Aqui se inicia o programa, onde indentificamos as variaveis e atribuimos a ela um valor
a = int(input(' Nota 1º Bimestre: '))
b = int(input(' Nota 2º Bimestre: '))
c = (a + b) / 2
#   Aqui o programa verifica o resultado da soma das notas e a média, imprimindo o resultado.
if (c) >= 7:
    print('Parabéns! Você foi aprovado!')
else:
    print('Você foi reprovado!')

#   Fim do programa
