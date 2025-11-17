from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "abc123"

a = [
    "Qual é a capital do Brasil?|A) Brasília|B) Rio de Janeiro|C) São Paulo|D) Belo Horizonte|A",
    "Quem escreveu 'Dom Casmurro'?|A) Machado de Assis|B) José de Alencar|C) Clarice Lispector|D) Graciliano Ramos|A",
    "Qual é o resultado de 8 x 7?|A) 56|B) 49|C) 64|D) 63|A",
    "Em que estado está o Pantanal?|A) Mato Grosso do Sul|B) Goiás|C) Tocantins|D) Pará|A",
    "Qual é a principal estrela do nosso sistema solar?|A) Sol|B) Vênus|C) Marte|D) Saturno|A"
]

b = [
    "Qual é a fórmula da água?|A) CO₂|B) H₂O|C) O₂|D) CH₄|B",
    "Quem pintou 'A Última Ceia'?|A) Van Gogh|B) Leonardo da Vinci|C) Picasso|D) Michelangelo|B",
    "Qual é o símbolo químico do ferro?|A) Fe²|B) Fe|C) Ir|D) F|B",
    "Quem foi o primeiro presidente do Brasil?|A) Getúlio Vargas|B) Deodoro da Fonseca|C) Juscelino Kubitschek|D) Floriano Peixoto|B",
    "Quantos continentes existem?|A) 5|B) 7|C) 6|D) 8|B"
]

c = [
    "Qual planeta é conhecido como o planeta vermelho?|A) Júpiter|B) Mercúrio|C) Marte|D) Netuno|C",
    "Qual é a função principal do coração?|A) Controlar hormônios|B) Produzir sangue|C) Bombear o sangue|D) Filtrar toxinas|C",
    "Qual é o plural de 'pão'?|A) Pãos|B) Pãoses|C) Pães|D) Pãozes|C",
    "Quanto é 5²?|A) 10|B) 15|C) 25|D) 20|C",
    "Quem descobriu o Brasil?|A) Cristóvão Colombo|B) Pedro Álvares de Lima|C) Pedro Álvares Cabral|D) Vasco da Gama|C"
]

d = [
    "Qual é o maior animal terrestre?|A) Leão|B) Hipopótamo|C) Girafa|D) Elefante|D",
    "Qual é a unidade de medida da corrente elétrica?|A) Ohm|B) Volt|C) Watt|D) Ampère|D",
    "Qual dessas linguagens é usada para criar sites?|A) Python|B) Java|C) C++|D) HTML|D",
    "Qual desses planetas é o mais distante do Sol?|A) Terra|B) Marte|C) Urano|D) Netuno|D",
    "Qual é a cor resultante da mistura de azul e amarelo?|A) Roxo|B) Laranja|C) Vermelho|D) Verde|D"
]

grupos = [a, b, c, d]

@app.route("/")
def home():
    return """
    <h1>Escolha um jogo</h1>
    <a href='/numero'>Número Aleatório</a><br>
    <a href='/forca'>Jogo da Forca</a><br>
    <a href='/campo'>Campo de Tiro</a><br>
    <a href='/quiz'>Quiz de Perguntas</a><br>
    <a href='/hanoi'>Torre de Hanoi</a><br>
    """

@app.route("/numero", methods=["GET", "POST"])
def numero():
    if "aleatorio" not in session:
        session["aleatorio"] = random.randint(1, 100)

    msg = ""

    if request.method == "POST":
        try:
            nu = int(request.form["nu"])
            na = session["aleatorio"]

            if nu == na:
                msg = "Acertou!"
                session.pop("aleatorio")

            elif nu < na:
                msg = "Número maior (perto)" if na - nu < 10 else "Número maior (longe)"

            else:
                msg = "Número menor (perto)" if nu - na < 10 else "Número menor (longe)"

        except:
            msg = "Digite um número válido."

    return render_template("numero.html", msg=msg)

@app.route("/forca", methods=["GET", "POST"])
def forca():
    palavras = ["gumball", "jake", "mordecai", "rick", "clarencio", "finn", "rigby", "steven", "darwin", "morty"]

    if "palavra" not in session:
        session["palavra"] = random.choice(palavras)
        session["certas"] = ["_" for _ in session["palavra"]]
        session["chances"] = 0

    palavra = session["palavra"]
    certas = session["certas"]
    chances = session["chances"]
    mensagem = ""

    if request.method == "POST":
        letra = request.form["letra"].lower()
        achou = False

        for i in range(len(palavra)):
            if palavra[i] == letra:
                certas[i] = letra
                achou = True

        session["certas"] = certas

        if achou:
            mensagem = "Existe essa letra"
        else:
            mensagem = "Não tem essa letra"
            session["chances"] += 1
            chances += 1

        if "".join(certas) == palavra:
            mensagem = f"Parabéns! A palavra era {palavra}"
            session.clear()

        elif chances >= 5:
            mensagem = f"Você perdeu! A palavra era {palavra}"
            session.clear()

    return render_template("forca.html", certas=certas, chances=chances, mensagem=mensagem)


def criar_campo():
    campo = [["O"] * 10 for _ in range(10)]
    campo[2][3] = "x"
    return campo


@app.route("/campo", methods=["GET", "POST"])
def campo():
    if "campo" not in session:
        session["campo"] = criar_campo()
        session["vidas"] = 10
        session["tentativa"] = 0
        session["msg"] = ""

    campo_sess = session["campo"]
    vidas = session["vidas"]
    tentativa = session["tentativa"]
    msg = session["msg"]

    if request.method == "POST":
        linha = int(request.form["linha"])
        coluna = int(request.form["coluna"])

        if linha not in range(10) or coluna not in range(10):
            msg = "Mire dentro do campo!"

        else:
            if campo_sess[linha][coluna] == "x":
                msg = "Acertou!"
                campo_sess[linha][coluna] = "X"
                vidas = 0
            else:
                msg = "Errou!"
                campo_sess[linha][coluna] = "*"
                vidas -= 1

        tentativa += 1

        session["campo"] = campo_sess
        session["vidas"] = vidas
        session["tentativa"] = tentativa
        session["msg"] = msg

        if vidas <= 0:
            msg += " | Fim de jogo!"
            session.clear()

    return render_template("campo.html", campo=campo_sess, vidas=vidas, tentativa=tentativa, msg=msg)


@app.route("/quiz")
def quiz_index():
    session["acertos"] = 0
    session["erros"] = 0
    session["contador"] = 0
    return redirect("/quiz/pergunta")


@app.route("/quiz/pergunta")
def quiz_pergunta():
    session["contador"] += 1

    grupo = random.choice(grupos)
    pergunta = random.choice(grupo)
    session["pergunta_atual"] = pergunta

    partes = pergunta.split("|")

    return render_template("quiz.html", pergunta=partes[0], A=partes[1], B=partes[2], C=partes[3], D=partes[4])


@app.route("/quiz/responder", methods=["POST"])
def quiz_responder():
    escolha = request.form.get("escolha")
    atual = session.get("pergunta_atual", "")
    certa = atual.split("|")[5]

    if escolha == certa:
        session["acertos"] += 1
    else:
        session["erros"] += 1

    if escolha == "Z":
        return redirect("/quiz/resultado")

    return redirect("/quiz/pergunta")


@app.route("/quiz/resultado")
def quiz_resultado():
    acertos = session.get("acertos", 0)
    erros = session.get("erros", 0)
    total = session.get("contador", 1) - 1
    porc = (acertos / total) * 100 if total > 0 else 0

    session.clear()

    return render_template("quizresultado.html", acertos=acertos, erros=erros, porc=porc)


@app.route("/hanoi", methods=["GET", "POST"])
def hanoi():
    if "hanoi" not in session:
        session["hanoi"] = {"A": [3, 2, 1], "B": [], "C": []}
        session["movimentos"] = 0

    torres = session["hanoi"]
    msg = ""

    if request.method == "POST":
        origem = request.form["origem"]
        destino = request.form["destino"]

        if not torres[origem]:
            msg = "Não há discos na torre."

        else:
            disco = torres[origem][-1]

            if torres[destino] and torres[destino][-1] < disco:
                msg = "Movimento inválido!"
            else:
                torres[origem].pop()
                torres[destino].append(disco)
                session["movimentos"] += 1

        if torres["C"] == [3, 2, 1]:
            msg = f"Você venceu! Movimentos: {session['movimentos']}"
            session.clear()

    session["hanoi"] = torres

    return render_template("hanoi.html", torres=torres, msg=msg)


if __name__ == "__main__":
    app.run(debug=True)