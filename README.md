# validador-doadores-python
# Sistema de Cadastro de Doadores de Sangue 🩸

## Sobre o Projeto
Este é um sistema desenvolvido em Python para automatizar e validar o registo de voluntários para a doação de sangue. O programa recolhe os dados dos utilizadores, verifica se cumprem os requisitos mínimos de saúde (idade e peso) e armazena as informações validadas de forma persistente num ficheiro de texto local. 

Este projeto foi construído para consolidar fundamentos essenciais de programação, tais como manipulação de ficheiros locais, estruturas de controlo de fluxo, tratamento de exceções e validação rigorosa de inputs — competências fundamentais para o desenvolvimento de scripts fiáveis aplicados a infraestruturas de TI e segurança da informação.

## Funcionalidades
- **Validação de Requisitos:** O sistema bloqueia o registo de candidatos que tenham menos de 50 kg ou menos de 16 anos, informando o motivo exato da recusa.
- **Tratamento de Erros:** Prevenção de quebras no sistema caso o utilizador insira letras em campos numéricos (idade, altura, peso).
- **Loop Contínuo:** Permite registar múltiplos doadores numa única execução do programa.
- **Armazenamento Persistente:** Os registos aprovados são guardados e formatados automaticamente no ficheiro `informacoes_salvas.txt` utilizando o modo de adição (append), sem sobrescrever dados anteriores.

## Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Bibliotecas:** Apenas funções nativas do Python (Built-in functions).

## Como Executar

1. Certifica-te de que tens o Python instalado no teu computador.
2. Faz o download do ficheiro principal do código (`main.py`).
3. Abre o ficheiro no teu editor de código (como o VS Code) e clica no botão de "Run" (Executar), ou roda diretamente no terminal com o comando:
   ```bash
   python main.py
