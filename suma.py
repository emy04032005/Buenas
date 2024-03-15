from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello, World!</h1>" 

#Nombre y edad
@app.route('/user/<name>')   
@app.route('/user/<name>/<int:edad>')   
def user(name = None, edad = None): 
    if edad == None:
        return f"<h1>Bienvenido user {name}</h1>" 
    else:
        return f"<h1>Bienvenido user {name} tienes {edad} años</h1>" 
    
# Calculadora

@app.route('/calculadora/<operation>/<int:num1>/<int:num2>/<int:num3>/<int:num4>')
def calculadora(num1,num2,num3,num4,operation):
    if operation == "suma":
        return f" {num1 + num2 + num3 + num4}"
    elif operation == "resta":
        return f" {num1 - num2 - num3 - num4}"
    elif operation == "multiplicacion":
        return f" {num1 * num2  * num3 * num4}"
    elif operation == "divicion":
        return f" {num1 / num2 / num3 / num4}"
    elif operation == "elevado":
        return f" {num1 ** num2 **num3 ** num4}"
    
        

#Login 

@app.route('/login')
def login():
    return "<h1>Iniciar sesion</h1>" 


if (__name__) == '_main_':
    app.run( debug=True)