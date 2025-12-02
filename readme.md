# CALCULADORA CIENTÍFICA DE NÚMEROS COMPLEXOS (TRABALHO A3)

## 📌 Sobre o Projeto

Este projeto consiste em uma calculadora científica desenvolvida em **Python 3.x** capaz de processar números complexos. A aplicação roda via linha de comando e se destaca por não apenas calcular operações simples, mas interpretar expressões matemáticas completas.

Para isso, o sistema utiliza uma **Árvore Sintática Abstrata (AST)**. Isso significa que ele lê a expressão, entende a precedência dos operadores (ex: multiplicação antes de soma) e exibe a estrutura de execução em notação LISP antes de mostrar o resultado final.

## 👥 Desenvolvedores

Abaixo, a identificação dos membros da equipe e a divisão das responsabilidades no desenvolvimento do código.

| Membro | RA | Módulo Principal de Responsabilidade |
| :--- | :--- | :--- |
| **Duilio do Nascimento Brandao** | 12724216242 | **Backend Matemático:** Operações com Complexos (`complex_operations.py`) |
| **Alisson Nonato de Lima Conceição** | 12724216237 | **Interpretador:** Expressões e Variáveis (`expression_handler.py`) |
| **Edinaldo Andrade da Silva** | 12724146825 | **Frontend/Integração:** Interface e Árvore (`main.py`) |
| **Raimundo Neto** | 12724119913 | **Documentação:** Relatório Técnico e Organização do GitHub |

---

## 🛠️ Relatório Técnico (Detalhamento da Implementação)

O sistema foi arquitetado em três módulos principais para garantir a organização e a escalabilidade do código.

### 1. Módulo de Operações (`src/complex_operations.py`)
Este arquivo é o "motor" matemático do projeto. Ele isola a lógica de cálculo da lógica de texto.
* **Operações:** Implementa as funções básicas (soma, subtração, multiplicação, divisão, potência) e avançadas (raiz e conjugado) utilizando a biblioteca nativa do Python.
* **Formatação Visual:** Inclui uma função dedicada a formatar a saída para o padrão matemático `a + bi`, substituindo o `j` (padrão do Python) por `i` e ocultando partes nulas para uma visualização mais limpa.
* **Tratamento de Erros:** Previne falhas críticas, como a divisão por zero, lançando exceções controladas.

### 2. Módulo do Interpretador (`src/expression_handler.py`)
É o núcleo inteligente do sistema. Ele é responsável por ler o texto digitado pelo usuário e transformá-lo em instruções que o computador entende.
* **Tokenização e Parsing:** O código quebra a string de entrada e constrói a Árvore Sintática (AST), garantindo que a ordem das operações matemáticas seja respeitada (precedência).
* **Notação LISP:** Conforme os requisitos, o sistema converte a árvore interna para uma representação visual em LISP (ex: `(+ 2 3)`), que é exibida no terminal.
* **Variáveis:** O interpretador identifica quando o usuário digita letras (variáveis), pausa a execução e solicita os valores correspondentes em tempo de execução.

### 3. Interface Principal (`src/main.py`)
É o ponto de entrada da aplicação.
* **Verificação Automática:** Ao iniciar, o script executa testes automáticos de igualdade para validar a lógica de comparação do sistema.
* **Loop de Execução:** Mantém a aplicação rodando em um loop contínuo, recebendo as expressões do usuário e enviando para o interpretador processar, até que o comando de saída seja acionado.

---

## 🚀 Como Executar

1.  **Baixe o Projeto:** Faça o clone deste repositório ou o download do arquivo ZIP.
2.  **Abra o Terminal:** Navegue até a pasta raiz do projeto.
3.  **Execute o Comando:**
    ```bash
    python src/main.py
    ```
O programa iniciará automaticamente, exibirá os testes de verificação e ficará aguardando a entrada da sua expressão.
