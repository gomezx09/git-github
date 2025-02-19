# 💰 Simulador de Empréstimo 💰
print("=" * 50)
print("   📢 Bem-vindo ao Simulador de Empréstimo! 📢")
print("=" * 50)

# 🔹 Entrada de dados do usuário
salario = float(input("Informe seu salário (R$): "))
emprestimo = float(input("Digite o valor do empréstimo desejado (R$): "))
anos = int(input("Em quantos anos deseja pagar? "))

# 🔹 Cálculos do financiamento
parcelas = anos * 12
parcela_mensal = emprestimo / parcelas
limite_parcela = salario * 0.30  # 30% do salário
juros = parcela_mensal * 0.05  # 5% de juros ao ano
valor_final = parcela_mensal + juros

# 🔹 Exibição dos resultados
print("\n📊 Analisando sua solicitação...\n")
print(f"💰 Valor do empréstimo: R$ {emprestimo:,.2f}")
print(f"📆 Tempo de financiamento: {anos} anos ({parcelas} meses)")
print(f"📉 Valor da parcela: R$ {parcela_mensal:,.2f} + juros de R$ {juros:,.2f} ao ano")

# 🔹 Condição de aprovação
if parcela_mensal <= limite_parcela:
    print("\n✅ Seu empréstimo foi \033[32mAPROVADO!\033[m")
    print("Parabéns! Seu sonho está mais próximo de se realizar. 🎉")
else:
    print("\n❌ Seu empréstimo foi \033[31mNEGADO!\033[m")
    print(f"O valor máximo da parcela permitido é de R$ {limite_parcela:,.2f}")

print("\n📌 Obrigado por usar nosso simulador! 😊")

