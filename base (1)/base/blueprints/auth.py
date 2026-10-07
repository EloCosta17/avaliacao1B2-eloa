from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database
auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form.get["nome"]
        email = request.form.get["email"]
        senha = request.form.get["senha"]

        conexao = conectar()
        registrar = criar_usuario()

        senha_hash = generate_password_hash(senha)

        conexao.commit()
        conexao.close()

        return redirect(url_for("auth.login"))
    
    return render_template("registro.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"] 

        conexao = conectar()
        registrar = criar_usuario()

        for user[nome] in database.usuarios:
            if user["nome"] == nome and check_password_hash(senha):
                session["usuario"] = nome
                return redirect(url_for("index"))
        conexao.commit()
        conexao.close()
        return redirect(url_for("auth.login"))

        conexao = conectar()

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("usuario",None)
    flash("Implemente o logout com session.")
    return redirect(url_for("index"))
