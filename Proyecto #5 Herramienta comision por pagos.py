'''Este programa cobra $25.00 pesos de comision por hacer pagos.
El saldo inicial es de $200.00
Pregunta el monto a pagar, y revisa si el pago se puede o no realizar
El saldo se actualiza cada vez, y el programa se repite
mientras el monto a retirar no sea cero
'''

saldo=200
cantidad=1
while cantidad>0:
    monto=input("Dame la cantidad a pagar: $")
    cantidad=float(monto)
    if cantidad+25<=saldo and cantidad>0:
        print("Transaccion autorizada")
        saldo=saldo - cantidad-25
    else:
        print("Saldo insuficiente")
    print("Tu nuevo saldo es de $",saldo)
print("Gracias por usar nuestro servicio")