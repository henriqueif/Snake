P1, C1, P2, C2=input('Digite o valor correspondente:').split()

P1=float(P1)
C1=float(C1)
P2=float(P2)
C2=float(C2)

esquerdo = P1*C1
direito = P2*C2

if esquerdo == direito:
    print('0')

elif esquerdo > direito:
    print('E')

else:
    print('D')