


valorDigitado = int(input("Digite seu número: "))
a, b = 0, 1

for i in range(valorDigitado):
   
   a,b = b,a + b
   if(valorDigitado <= a):
      print(a, end=" ")
   else:
      print("NÃO VAI DAAAAR!!!") 