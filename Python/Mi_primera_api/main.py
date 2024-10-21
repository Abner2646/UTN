from flask import Flask, jsonify, request #Importa librerías

app = Flask(__name__) #Define a "app" como una instancia de Flask

@app.route('/') #Decorador que indica que "app" se llama con un "/"
def root(): #Lo que hace la api
    return "root"

@app.route("/users/<user_id>")
def get_user(user_id):
    user = {"id":user_id, "name": "Abner", "telefono": "999-666-333"}
    #/users/2654?query=query_test
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200

if __name__ == "__main__": #Inicia la api
    app.run(debug=True)