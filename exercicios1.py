#Transformação de metros para outras medidas:
medida = float(input("Uma medida em metros: "))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print (f'A medida {medida}m corresponde a {km} km, a {hm}  hm, a {dam} dam, a {dm} dm, a {cm} cm, {mm} mm')
