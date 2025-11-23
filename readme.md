# CALCULADORA CIENTÍFICA DE NÚMEROS COMPLEXOS (A3)

## 📌 Introdução e Requisitos

Este projeto implementa uma calculadora científica completa para números complexos em **Python 3.x** (Regra 9). A interface é em linha de comando (Regra 10) e o sistema utiliza uma **Árvore Sintática Abstrata (AST) em notação LISP** para avaliar expressões (Regra 6).

O código-fonte completo está disponível neste repositório:
**Link do GITHUB:** `https://github.com/RaySnk/Calculadora-complexos-A3/`

## 👥 Membros da Equipe e Responsabilidades

A entrega é feita através deste repositório, constando as informações de identificação (Regra 11).

| Membro | RA | Módulo Principal de Responsabilidade |
| :--- | :--- | :--- |
| **[Duilio do nascimento brandao ]** | [12724216242] | **Função 1:** Operações com Complexos (`complex_operations.py`) |
| **[Alisson nonato de lima conceição]** | [12724216237] | **Função 2:** Expressões e Variáveis (`expression_handler.py`) |
| **[Edinaldo andrade da silva]** | [12724146825] | **Função 3:** Interface e Árvore (`main.py`) |
| **[Raimundo Neto]** | [12724119913] | Documentação e GitHub (Relatório e Organização Final) |

---

## 🛠️ Detalhamento da Implementação do Código (Relatório Técnico)

### 1. Módulo de Operações Aritméticas (`src/complex_operations.py`)

Este módulo atende integralmente à **Regra 1** (Aritmética) e à **Regra 0** (Representação).

* **Aritmética Base:** As funções (`soma`, `subtracao`, `multiplicacao`, etc.) são *wrappers* que utilizam o tipo `complex` nativo do Python, garantindo a manipulação precisa das partes real e imaginária.
* **Formatação (`formatar`):** Esta função customizada garante que a saída esteja sempre no formato **`(a + bi)`** ou **`(a - bi)`** (Regra 0), omitindo termos nulos e simplificando a representação.
* **Detecção de Erro:** A função `divisao` inclui uma verificação de `z2 == 0` para levantar a exceção `ZeroDivisionError` (Regra 5).

### 2. Módulo de Expressões e Variáveis (`src/expression_handler.py`)

Este é o núcleo da lógica, responsável pela AST, variáveis e execução (Regras 2, 4, 6 e 7).

#### A. Parsing e AST (Regras 2 e 6)

* **Processamento da Expressão:** O módulo utiliza o *parsing* para construir a AST respeitando a precedência dos operadores (Regra 2).
* **Notação LISP:** A AST é internamente uma lista aninhada. A função **`format_lisp_output`** converte essa estrutura para a notação **(operador argumento1 argumento2...)** exigida, que é exibida no console antes do cálculo (Regra 6 e 10).

#### B. Execução e Variáveis (Regras 4 e 7)

* **Execução Recursiva:** A função **`executar_arvore`** executa a AST de forma recursiva (pós-ordem), garantindo que os cálculos ocorram na ordem correta, chamando as funções de `complex_operations.py` (Regra 4).
* **Variáveis:** O sistema identifica variáveis e, através da função `resolver_expressao`, solicita o valor ao usuário em tempo de execução, tratando-o como um complexo válido (Regra 7).

#### C. Teste de Igualdade (Regra 3)

* A função **`checar_igualdade`** avalia as duas expressões separadamente através da AST. Os resultados são comparados numericamente com uma pequena margem de tolerância para garantir a veracidade da igualdade (Regra 3).

### 3. Módulo de Interface e Execução (`src/main.py`)

* **Ponto de Entrada:** É o *script* principal que inicia o programa.
* **Interface:** Implementa o loop de linha de comando para entrada de expressões (Regra 10).
* **Integração:** Inicia os testes de igualdade (Regra 3) e chama a função principal de resolução para processar a entrada do usuário.

---

## 🚀 Instruções Finais de Execução

1.  **Baixar o Repositório:** Obtenha os arquivos (clonando ou baixando o ZIP).
2.  **Execute o Arquivo Principal:** No terminal, navegue até a pasta raiz do projeto e execute:
    ```bash
    python src/main.py
    ```
A aplicação iniciará, executará os testes e aguardará a entrada de expressões.
