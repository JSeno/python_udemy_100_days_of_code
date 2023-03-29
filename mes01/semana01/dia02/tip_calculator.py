"""
Day 02 Project: Tip Calculator

"""

bill = float(input("Qual o valor da conta? Insira o valor: "))
share = float(input("Vai dividir em quantas pessoas? Insira a quantidade: "))
tip_percentage = int(input("Quanto você quer dar de gorjeta? 10, 15, ou 20 porcento? "))
tip = bill * (tip_percentage / 100)
total = (bill + tip) / share

print(f"Cada pessoa deve pagar R${total:.2f}")