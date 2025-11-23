import expression_handler
import complex_operations # Importação de dependência

print("\n\tCalculadora de Numeros Complexos (Trabalho A3)\t")
print("Regra: Digite a conta ou escreva 'sair' para fechar o programa")

# Teste de Igualdade (Regra 3)
print("\n--- Teste de Igualdade ---")
print("Teste: 2*(1+i) == 2+2i -> ", expression_handler.checar_igualdade("2*(1+i)", "2+2i"))
print("Teste: 5 == 5i -> ", expression_handler.checar_igualdade("5", "5i"))
print("--------------------------")

# Loop principal da interface (Regra 10)
while True:
    eq = input("\nDigite a expressao aqui: ")
    
    if eq.lower() == "sair":
        print("Saindo do programa...")
        break
    
    print("Voce digitou:", eq)
    print("Processando...")
    
    # Resolve a expressão, que exibe a AST (Regra 6) e pede variáveis (Regra 7)
    resultado = expression_handler.resolver_expressao(eq)
    
    print("\n\tResultado:", resultado)
    print("-" * 30)