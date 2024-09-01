import requests
from flask import Flask, request, jsonify, render_template
from hugchat import hugchat
from hugchat.login import Login

app = Flask(__name__)

# Ingresar las credenciales de inicio de sesión en Hugging Face
email = 'squicano8@gmail.com'
password = '(/2teCL#H6#p-CV'

# Función para autenticar con Hugging Face y obtener cookies
def authenticate_huggingface(email, password):
    sign = Login(email, password)
    try:
        cookies = sign.login()
        print("Autenticación exitosa con Hugging Face")
        return cookies
    except Exception as e:
        print(f"Error durante la autenticación: {str(e)}")
        return None

# Obtener las cookies de autenticación
cookies = authenticate_huggingface(email, password)
if cookies is None:
    print("No se pudo autenticar con Hugging Face. Verifica las credenciales.")
    exit(1)

# Crear una instancia de ChatBot con las cookies de autenticación
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

# Ruta principal para la interfaz de usuario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar la conversación con el bot
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_message']

    try:
        # Llamada al método chat del chatbot
        response = chatbot.chat(user_message)
    except Exception as e:
        response = f"Error al intentar consultar el bot: {str(e)}"
    
    return jsonify({'response': response})

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True, port=8080)
