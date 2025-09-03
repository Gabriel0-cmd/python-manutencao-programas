#Exercícios de Manutenção de Código – Python

Esse repositório tem 12 programinhas em Python cheios de erros de propósito.  
O objetivo é você rodar, achar os erros e consertar, pra que cada programa funcione certinho.

---

#O que é pra fazer
- Rodar cada programa
- Descobrir o que tá errado
- Corrigir pra funcionar como esperado
- Anotar rapidinho o que mudou

---

#Programas e o que foi corrigido

#Programa 1 – Calculadora de Média
O que tava errado: Somava strings em vez de números, e não lidava direito com média = 7.  
Como consertei: Transformei as entradas em `float` e ajustei a condição `if ... else`.

#Programa 2 – Contador de Números Pares
O que tava errado: Loop `while` e `if` errados, só mostrava alguns números.  
Como consertei: Usei `for` indo de 2 até N de 2 em 2, mostrando todos os pares.

#Programa 3 – Caixa Eletrônico
O que tava errado: Calculava notas na ordem errada e dava notas a mais.  
Como consertei: Comecei pelas maiores (100, 50, 20) e tirei notas desnecessárias.

#Programa 4 – Tabuada
O que tava errado: Loop só até 9 e sem formatar o resultado.  
Como consertei: Ajustei pra 1–10 e usei `f-string` pra mostrar `n x i = resultado`.

#Programa 5 – Jogo de Adivinhação
O que tava errado: Número fixo e só uma tentativa.  
Como consertei: Usei `random.randint(1, 20)` e loop até acertar, avisando se é maior ou menor.

#Programa 6 – Busca em Lista
O que tava errado: Continuava procurando mesmo depois de achar.  
Como consertei: Adicionei `break` e tratei o caso de “não encontrado”.

#Programa 7 – Impressão de Ímpares
O que tava errado: `continue` travava o loop porque `i` não aumentava.  
Como consertei: Incremento de `i` antes do `continue`.

#Programa 8 – Validação de Senha
O que tava errado: `break` fora do `if`, encerrava o loop na primeira tentativa.  
Como consertei: Coloquei o `break` dentro do `if` e mostrei mensagem de senha errada.

#Programa 9 – Contagem de Vogais
O que tava errado: Não contava letras maiúsculas.  
Como consertei: Transformei a palavra em minúscula antes de contar as vogais.

#Programa 10 – Acumulador de Valores
O que tava errado: Sobrescrevia a soma em vez de acumular.  
Como consertei: Usei `soma += valor` até o usuário digitar 0.

#Programa 11 – Função Soma
O que tava errado: Função só atribuía `total = x` e não era chamada direito.  
Como consertei: Troquei pra `total += x` e chamei a função com a lista de números.

#Programa 12 – Menu com elif
O que tava errado: Três `if` separados, `else` só no último.  
Como consertei: Usei `if ... elif ... else` pra todas as opções funcionarem.

---

#Como rodar
No terminal, é só:

```bash
python prog1.py
python prog2.py
...
python prog12.py