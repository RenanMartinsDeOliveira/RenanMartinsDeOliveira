#programa básico para apartir da altura e largura de uma parede calcular sua aréa e quantia de tinta nescessaria para pinta-la.

n1 = float(input('digite a largura da parede em metros:'))
n2 = float(input('digite a altura da parede em metros:'))

print('Sua parede tem {} metros quadrados e você precisa de {} litros de tinta.'.format(n1*n2,(n1*n2)/2))
