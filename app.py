import requests
from flask import Flask, request, jsonify
from hugchat import hugchat
from hugchat.login import Login

app = Flask(__name__)

# Ingresar las credenciales de inicio de sesión en huggingface
email = 'squicano8@gmail.com'
password = '(/2teCL#H6#p-CV'

# Crear una instancia de la clase Login con las credenciales
sign = Login(email, password)

# Iniciar sesión y obtener las cookies
cookies = sign.login()

# Crear una instancia de ChatBot con las cookies de autenticación
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']
    print(f"Mensaje del usuario: {user_message}")
    
    try:
        # Llamada al método chat del chatbot
        response = chatbot.chat(user_message)
        
        # Si response es un objeto, extraer solo el texto
        if isinstance(response, dict) or isinstance(response, list):
            response = str(response)
        
        print(f"Respuesta del bot: {response}")
    except Exception as e:
        response = f"Error al intentar consultar el bot: {str(e)}"
        print(f"Error: {response}")
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
