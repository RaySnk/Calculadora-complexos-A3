import expression_handler
import complex_operations

print("\n\tCalculadora de Numeros Complexos (Trabalho A3)\t")
print("Regra: Digite a conta ou escreva 'sair' para fechar o programa")

print("\n--- Teste de Igualdade ---")
print("Teste: 2*(1+i) == 2+2i -> ", expression_handler.checar_igualdade("2*(1+i)", "2+2i"))
print("Teste: 5 == 5i -> ", expression_handler.checar_igualdade("5", "5i"))
print("--------------------------")

while True:
    eq = input("\nDigite a expressao aqui: ")
    if eq.lower() == "sair":
        print("Saindo do programa...")
        break
    print("Voce digitou:", eq)
    print("Processando...")
    resultado = expression_handler.resolver_expressao(eq)
    print("\n\tResultado:", resultado)
    print("-" * 30)
