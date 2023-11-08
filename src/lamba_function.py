import json

USUARIO_ESPERADO = 'caca_rato'
SENHA_ESPERADA = 'remo_cr7'

def lambda_handler(event, context):
    # TODO implement
    
    username = event.get('queryStringParameters', {}).get('username')
    password = event.get('queryStringParameters', {}).get('password')

    # Check if both username and password are provided
    if username and password:
        # Check if the provided username and password are valid
        if username == USUARIO_ESPERADO and password == SENHA_ESPERADA:
            # Authentication successful, allow access to the POST route
            # TODO: Implemente sua lógica para a rota POST aqui
    
            return {
                'statusCode': 200,
                'body': json.dumps(event) 
            }
        
        
        
        
