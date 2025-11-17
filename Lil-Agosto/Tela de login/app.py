from flask import Flask, render_template, url_for, session, request, redirect

app = Flask(__name__)
app.secret_key = "agostinho123"  

usuarios = {
    "Valter": {
        "email": "Valtinho@gmail.com",
        "senha": "40028922",
        "status": "Aluno",
        "nota": "Aluno exemplar com médias 10 em todas as matérias",
        "genero": "Masculino",
        "prontuario": "SP3150623",
        "materia": "matemática",
        "prof": "Agostinho"
    },

    "Raphael": {
        "email": "Alunopreguiçoso@gmail.com",
        "senha": "Javascript",
        "status": "Aluno",
        "nota": "Aluno preguicoso com 0 em tudo",
        "genero": "Masculino",
        "prontuario": "SP314982X",
        "materia": "biologia",
        "prof": "Claudete"
    },

    "Cristiano": {
        "email": "cristhebest@gmail.com",
        "senha": "Oguarani256",
        "status": "Professor",
        "nota": "Já é formado",
        "genero": "Masculino",
        "prontuario": "SP3150488",
        "materia": "LOGP",
        "prof": "Ele mesmo"
    }
}


@app.route("/")
def home():
    if "usuario" in session:
        return redirect(url_for("info"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        email = request.form.get("email")
        senha = request.form.get("senha")

        if usuario in usuarios and usuarios[usuario]["senha"] == senha and usuarios[usuario]["email"] == email:
            session["usuario"] = usuario
            return redirect(url_for("info"))
        else:
            return render_template("login.html", erro="Otário! Digitou o nome/senha errada")

    return render_template("login.html")


@app.route("/info")
def info():
    if "usuario" not in session:
        return redirect(url_for("login"))
    
    user = session["usuario"]
    dados = usuarios[user] 

    return render_template("info.html", usuario=user, dados=dados)


@app.route("/logout")
def logout():
    session.pop("usuario")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
