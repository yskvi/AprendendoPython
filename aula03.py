#a = int(input('digite sua idade:'))
 
#if a < 16:
#  print('você não pode votar')
#elif a < 18:
# print('você pode escolher se quer votar ou não')
#elif a > 65:
#  print('você não precisa votar ')
#else:
#  print('você é obrigado a votar!!')
 
# a = int(input('Digite um numero para o contador:'))
 
 
# while a != 0:
#   print(f'Valor digitado é :{a}')
#   a = int(input('Digite um numero para o contador:'))
 
 
# for contador in range(10):
#     print(f'{contador}')
 
# a = int(input('Digite um numero para fazer a tabuada dele:'))
 
# for contador in range(1,11):
#  print(f'{a} x {contador} = {a * contador}')
 
a = int(input('Digite um numero para fazer a tabuada dele:'))
while a > 0:
  for contador in range(1,11):
   print(f'{a} x {contador} = {a * contador}')  
  a = int(input('Digite um numero para fazer a tabuada dele:'))