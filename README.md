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

Credenciais para autenticação (já configuradas na URL):

- USUARIO_ESPERADO = 'caca_rato'
- SENHA_ESPERADA = 'remo_cr7'

**URL de acessso:** https://5rbnkz89vf.execute-api.us-east-1.amazonaws.com/teste_post/exercicio_ponderada_vini/?username=caca_rato&password=remo_cr7 

Sendo assim, a partir da definição do código, é esperado que haja um retorno de mensagem com base no que foi pré-definido. Neste caso, no método GET, esperando que seja retornado o corpo da mensagem:

![image](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/05525171-ad55-49e2-9994-0bad5487be15)


## Criando métodos no API Gateway

No contexto da função Lambda que foi criada, o API Gateway atua para direcionar os métodos REST para um endpoint específico, que, por sua vez, está vinculado à função. Sendo assim, quando uma solicitação é feita para o endpoint, o API Gateway recebe a solicitação e a encaminha para a função Lambda correspondente.

Neste caso especificamente, o evento recebido contém informações sobre a solicitação, incluindo os parâmetros da consulta, corpo da solicitação, cabeçalhos e outros detalhes.

Assim, o API Gateway atua como um intermediário entre a solicitação e a função Lambda, garantindo que as solicitações sejam roteadas corretamente para a função e que as respostas sejam enviadas de volta ao "remetente final". 

Gatilho, exemplificado no método POST:

![image_720](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/227909a1-8cd3-4b80-958f-b683461f632c)


Como padrão e formatado no código, as credenciais do usuário são enviadas no corpo de qualquer solicitação. Quando a função Lambda recebe a solicitação POST, ela extrai o nome de usuário e a senha do corpo JSON. Em seguida, verifica se as credenciais fornecidas correspondem às credenciais esperadas. Se forem válidas, a função responde com um código de status 200 indicando uma autenticação bem-sucedida e retorna o corpo da solicitação JSON como resposta.

No contexto da atividade (e pelo o que "setado"), a resposta JSON contém os mesmos dados que foram enviados na solicitação. Ou seja, o JSON retornado é um espelho do JSON recebido, demonstrando que a função Lambda recebeu corretamente os parâmetros da solicitação.

Como exemplo de outro tipo de utilização do método POST, passando uma parâmetro adicional no corpo, no Postman:

![image_720](https://github.com/2023M8T4Inteli/grupo5/assets/99264567/ecc627dd-d71f-415e-95b6-e2aa989b69b7)


## Testes Unitários - Testes Padrão da AWS
### Apresentação dos testes unitários:

Para complementação e validação do código, foi feita a utilização de um teste padrão definido na AWS Lambda, no qual consiste em uma validação na solicitação dos eventos.

A validação foi feita com sucesso!

![image_720](https://github.com/furlan2803/lambda-flask-api/assets/99264567/35a3c18d-b70d-433a-872c-97c12cfa0758)


## Fontes e Recursos da AWS para Configuração

*Configurar as opções da função do Lambda - AWS Lambda. (n.d.).* https://docs.aws.amazon.com/pt_br/lambda/latest/dg/configuration-function-common.html 

*Configurar métodos da API REST no API Gateway - Amazon API Gateway. (n.d.).* https://docs.aws.amazon.com/pt_br/apigateway/latest/developerguide/how-to-method-settings.html

*Conceitos básicos do API Gateway - Amazon API Gateway. (n.d.).* https://docs.aws.amazon.com/pt_br/apigateway/latest/developerguide/getting-started.html
