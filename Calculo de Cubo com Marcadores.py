#!/usr/bin/python3
# Vamos calcular o volume do cubo.
# Formula básica, 'volume = a*a*a', depois 'área = 6*a*a'

# Atribuindo as variáveis, no caso as de um cubo qualquer.
x = int(input("Altura: "))
y = int(input("largura: "))
z = int(input("Profundidade: "))

# Uma lista simples com os valores atribuídos.
n = ("%s x %s x %s" %(x,y,z))

# Exibindo o resultado do problema.
print ("volume %s = %s" %(n,x*y*z))
print ("Área %s x %s = %s" %(x,y,6*x*y))

# Fim do programa
