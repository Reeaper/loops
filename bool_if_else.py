saldo_positivo = False

for enviar in range(3):
    if saldo_positivo:
        print("Compra no valor de R$12,50 aprovada")
        print("Entrega confirmada")
        print("Detalhes enviados para o seu e-mail.")
        break
    else:
        print('Falha na compra')
        break