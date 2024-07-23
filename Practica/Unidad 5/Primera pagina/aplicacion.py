from flask import Flask, request, render_template
from datetime import datetime

app=Flask(__name__)

@app.route("/")
def raiz():
    return render_template("inicio_sesion.html")

@app.route("/bienvenida", methods=["POST", "GET"])
def bienvenida():
    if request.method=="POST":
        if request.form["nombre"] and request.form["email"] and request.form["password"]:
            datos=request.form
            return render_template("bienvenida.html", datosUsuario=datos, hora=datetime.now().hour)
        else: 
            return render_template("inicio_sesion.html")
if __name__ == '__main__':
    app.run(debug=True)