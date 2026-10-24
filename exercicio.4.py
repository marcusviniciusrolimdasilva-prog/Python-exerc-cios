#Programa para que os pintores saibam quantos litros devem usar para pintar a parede
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print ('A largura é {}m, sua altura é {}m, sua área é {}m²'.format(largura, altura, area))
print ('Portanto para pintar essa parede é necessário {}L de tinta'.format(tinta))
