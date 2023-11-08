# Atividade Lambda + API Gateway - Semana 03

## Documentação da atividade de criação de um lambda com API gateway na AWS (em python) que receba em um endpoint via REST e mensagens com autenticação.
### Aluno: Vinícius Oliveira Fernandes
### Curso: Sistemas de Informação

## Criação da função e conexão com o API Gateway

Para criar a função Lambda e conectá-la ao API Gateway, foi realizado o procedimento de criação de uma nova função Lambda do zero, adicionado o código com os parâmetros padrão e, em seguida, foi feita a configuração da API no API Gateway apontando para a função Lambda recém-criada, especificando os métodos HTTP desejados para interação com a função.

![image_720](https://github.com/furlan2803/lambda-flask-api/assets/99264567/d9556e64-7134-4d7d-b7df-3d706e96c355)

## Autenticação

Na função lambda, também foi utilizado um método de autenticação das credenciais de um usuário (neste caso quem fará o acesso). Com definição do nome de usuário e a senha diretamente no código. 

A função recebe os parâmetros username e password da consulta em uma URL. Se ambos os parâmetros estiverem presentes e corresponderem às credenciais definidas, a autenticação é bem-sucedida (código de status 200). 

Caso contrário, a função retorna uma resposta de não autorizado (código de status 401). 

**É importante salientar que a URL de acesso à função Lambda deve incluir os parâmetros de consulta username e password para autenticar o usuário.**

**URL de acessso:** https://5rbnkz89vf.execute-api.us-east-1.amazonaws.com/teste_post/exercicio_ponderada_vini/?username=caca_rato&password=remo_cr7 

Sendo assim, a partir da definição do código, é esperado que haja um retorno de mensagem com base no que foi pré-definido. Neste caso, no método GET, esperando que seja retornado o corpo da mensagem:

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/05525171-ad55-49e2-9994-0bad5487be15)


## Testes Unitários
### Apresentação dos testes unitários:

![image_720](https://github.com/furlan2803/lambda-flask-api/assets/99264567/35a3c18d-b70d-433a-872c-97c12cfa0758)
