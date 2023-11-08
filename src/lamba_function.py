import json

USUARIO_ESPERADO = 'caca_rato'
SENHA_ESPERADA = 'remo_cr7'

def lambda_handler(event, context):
    # TODO implement
    
    username = event.get('queryStringParameters', {}).get('username')
    password = event.get('queryStringParameters', {}).get('password')

    if username and password:
        if username == USUARIO_ESPERADO and password == SENHA_ESPERADA:
    
            return {
                'statusCode': 200,
                'body': json.dumps(event) 
            }
        
        
        
        
