import requests
from flask import Flask, request, render_template, jsonify
from hugchat import hugchat
from hugchat.login import Login

app = Flask(__name__)

# Ingresar las credenciales de inicio de sesión en Hugging Face
email = 'squicano8@gmail.com'
password = '(/2teCL#H6#p-CV'

# Crear una instancia de la clase Login con las credenciales
sign = Login(email, password)

# Iniciar sesión y obtener las cookies
cookies = sign.login()

# Crear una instancia de ChatBot con las cookies de autenticación
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.form["user_input"]

    # Cambiar a la conversación actual
    conversation_id = chatbot.new_conversation()
    chatbot.change_conversation(conversation_id)

    # Obtener la respuesta del chatbot
    response = chatbot.query(user_message)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
