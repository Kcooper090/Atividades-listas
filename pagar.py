nome = str(input("Nome do cliente"))
print("bem-vindo", nome)

compra = input("Valor da compra")

forma_pagamento = input("forma de pagamaneto. 1- débito 2-crédito 3-pix")

if forma_pagamento == '1':
    print("Você tem 5 porcento de desconto.")
    valor_de = compra * 5/100
if forma_pagamento == '2':
    print("Você não possui desconto")
    valor_cre = compra

if forma_pagamento == '3':
    print("Você tem 10 porcento de desconto")
    valor_pix = compra * 0,1

    
tipo_cliente = input("Faz parte da categoria VIP? Sim ou Não")

if tipo_cliente =='Sim':
    print("Sou cliente VIP")
else:
    print("Não sou cliente VIP")







