# Atividade Lambda + API Gateway - Semana 03

## Documentação da atividade de criação de um lambda com API gateway na AWS (em python) que receba em um endpoint via REST e mensagens com autenticação.

## Aluno: Vinícius Oliveira Fernandes
### Curso: Sistemas de Informação

## Criação da função e conexão com o API Gateway

Para criar a função Lambda e conectá-la ao API Gateway, foi realizado o procedimento de criação de uma nova função Lambda do zero, adicionado o código com os parâmetros padrão e, em seguida, foi feita a configuração da API no API Gateway apontando para a função Lambda recém-criada, especificando os métodos HTTP desejados para interação com a função.

![image_720](https://github.com/furlan2803/lambda-flask-api/assets/99264567/d9556e64-7134-4d7d-b7df-3d706e96c355)

Sendo assim, a partir da definição do código, é esperado que haja um retorno de mensagem com base no que foi pré-definido. Neste caso, no método GET, esperando que seja retornado o corpo da mensagem:

![image_720](https://github.com/furlan2803/lambda-flask-api/assets/99264567/0384bef8-91cd-46be-b6f2-337a2f461a2d)


## Testes Unitários
### Apresentação dos testes unitários:

![image_720](https://github.com/furlan2803/lambda-flask-api/assets/99264567/35a3c18d-b70d-433a-872c-97c12cfa0758)
