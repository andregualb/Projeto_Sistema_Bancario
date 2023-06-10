MENU = '''
[D] Depósito
[S] Saque
[E] Extrato
[Q] Sair
'''
pular_linha = '\n'
crt = "=" * 35
D = (f"{' Depósito ':=^35}")
S = (f"{' Saque ':=^35}")
E = (f"{' Extrato ':=^35}")
Q = (f"{' Sair ':=^35}")
saldo = 0
extrato_saque = 0
extrato_deposito = 0
limite_saque = 500
saque_diarios = 3


while True:

    print(f'{" Menu ":=^35}{MENU}{crt}')
    print(pular_linha)

    opcao = str(input("Escolha um opção: ")).upper()
    print(pular_linha)

    if opcao == "D":
        print(D)
        print(pular_linha)

        deposito = int(input("Digite o valor do depósito:R$ "))
        print(pular_linha)

        if deposito <= 0:
            print(' Valor inválido ')
            print(pular_linha)
            continue

        else:
            extrato_deposito = extrato_deposito + deposito
            saldo = deposito + saldo

    elif opcao == "S":
        print(S)
        print(pular_linha)
        print(f'Saldo: {saldo:.2f}')
        print(pular_linha)

        saque = int(input("Digite o valor do Saque: R$"))

        if saque <= 0 or saque > limite_saque:
            print(pular_linha)
            print('Valor inválido!\n'
                  'Valor minimo para saque: R$ 10.00\n'
                  f'Valor maximo para saque: {limite_saque:.2f}'
                  )
            print(pular_linha)

        elif saque > saldo or saldo == 0:
            print(pular_linha)
            print('Saldo Insuficiente!')
            print(pular_linha)

        elif saque_diarios <= 0:
            print(pular_linha)
            print('Voçê excedeu o limite diário de saques')
            print(pular_linha)

        else:
            extrato_saque = extrato_saque + saque
            saldo = saldo - saque
            saque_diarios -= 1

    elif opcao == "E":
        print(E)
        print(pular_linha)
        print(f"Total de Depósito: R${extrato_deposito:.2f}\n\n"
              f"Total de Saque: R${extrato_saque:.2f}\n\n"
              f"Saldo em Conta: R${saldo:.2f}"
              )
        print(pular_linha)

    elif opcao == "Q":
        print(Q)
        print(pular_linha)
        print(f'{" Obrigado,Volte Sempre! ":=^35}')
        print(pular_linha)
        break
