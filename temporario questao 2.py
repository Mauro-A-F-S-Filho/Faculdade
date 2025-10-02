while True:
 sabores = input('Escolha o sabor desejado utilizando as siglas (tr/pr/es) conforme MENU: ')
 if sabores != 'tr' and sabores != 'pr' and sabores != 'es':
     print('sabor invalido, tente novamente')
     continue

 bola = input('Escolha o Nº de bolas  desejado (1/2/3): ')
 if bola != '1' and bola != '2' and bola != '3':
     print('Nº de bolas de sorvete invalido, tente novamente')
     continue

 valor = 0
 if sabores == 'tr' and bola == '1':
         valor1 = valor + 6
         print(' você pediu UMA bola de sorvete sabor TRADICIONAL valor a ser pago: R$ {:.2f} ' . format (valor1))
 elif sabores == 'tr' and bola == '2':
         valor2 = valor + 10
         print(' você pediu DUAS bolas de sorvete sabor TRADICIONAL valor a ser pago: R$ {:.2f} '.format(valor2))
 elif sabores == 'tr' and bola == '3':
         valor3 = valor + 18
         print(' você pediu TRÊS bolas de sorvete sabor TRADICIONAL valor a ser pago: R$ {:.2f} '.format(valor3))
 elif sabores == 'pr' and bola == '1':
         valor4 = valor + 7
         print(' você pediu UMA bola de sorvete sabor PREMIUM valor a ser pago: R$ {:.2f} '.format(valor4))
 elif sabores == 'pr' and bola == '2':
         valor5 = valor + 12
         print(' você pediu DUAS bolas de sorvete sabor PREMIUM valor a ser pago: R$ {:.2f} '.format(valor5))
 elif sabores == 'pr' and bola == '3':
         valor6 = valor + 21
         print(' você pediu TRÊS bolas de sorvete sabor PREMIUM valor a ser pago: R$ {:.2f} '.format(valor6))
 elif sabores == 'es' and bola == '1':
         valor7 = valor + 8
         print(' você pediu UMA bola de sorvete sabor ESPECIAL valor a ser pago: R$ {:.2f} '.format(valor7))
 elif sabores == 'es' and bola == '2':
         valor8 = valor + 14
         print(' você pediu DUAS bolas de sorvete sabor ESPECIAL valor a ser pago: R$ {:.2f} '.format(valor8))
 elif sabores == 'es' and bola == '3':
         valor9 = valor + 24
         print(' você pediu TRÊS bolas de sorvete sabor ESPECIAL valor a ser pago: R$ {:.2f} '.format(valor9))
 else:
         print('Código do sabor invalido, digite um codigo valido!')
         continue
 resposta = input('Deseja mais um sorvete? (s/n): ')
 if resposta == 's':
   continue
 else:
        print('O valor total:R$ {:.2f}' . format (valor1 + valor9))
        print('Obrigado, e volte sempre !!!')
 break