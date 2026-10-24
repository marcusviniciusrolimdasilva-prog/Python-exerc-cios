#Treinando Python - conversor de rais para dolar e euros.
real = float (input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.00
euros = real / 5.94
print ('Com R${:.2f}, você pode comprar US${:.2f}, agora com euros é €{:.2f}'.format(real, dolar, euros))
