from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session,url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

#Agregar hora local
from datetime import datetime
from pytz import timezone

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQL("sqlite:///florence.db")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        rows=db.execute("select * from pacientes")

        return redirect("/",rows=rows)
    else:
        rows=db.execute("select * from pacientes")
        return render_template("dashboard.html",rows=rows)


@app.route("/kiosco", methods=["GET", "POST"])
def kiosco():
    if request.method == "POST":

        return redirect("/")
    else:
        #rows= db.execute("select * from users where id=:id",id=session["user_id"])
        return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Escribe un nombre de usuario valido", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Escribe una contraseña valida", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE user = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["pass"], request.form.get("password")):
            return apology("Usuario o contraseña invalida", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = request.form.get("username")
        ps = request.form.get("password")
        psa =request.form.get("Cpassword")
       

        userE = db.execute("SELECT user FROM users WHERE user = :username",username=user)


        if not user:
            return apology("El campo usuario esta vacio",400 )
        elif not ps:
            return apology("El campo password esta vacio",400 )
        elif not psa:
            return apology("El campo password Again esta vacio",400 )
        elif ps != psa:
            return apology("Las contraseñas no coinciden",400 )
        elif not userE :
            rows = db.execute("INSERT INTO users (id,user,pass,cedula,nombres,apellidos,telefono,direccion) values (NULL,:username,:hashh,:cedula,:nombres,:apellidos,:telefono,:direccion) ",username = user,\
            cedula=request.form.get("cedula"),\
                 nombres=request.form.get("nombres"),\
            apellidos=request.form.get("apellidos"),\
            telefono=request.form.get("telefono"),  \
            direccion=request.form.get("direccion"),\
             hashh=generate_password_hash(ps) )
        else:
            return apology("El usuario ya existe",400 )

        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/rpacientes", methods=["GET", "POST"])
@login_required
def rpacientes():
    if request.method == "POST":
        rows=db.execute("insert into pacientes (cedula,nombres,apellidos,correo,telefono,direccion,sexo) \
            values (:cedula,:nombres,:apellidos,:correo,:telefono,:direccion,:sexo)",\
            cedula=request.form.get("cedula"),\
            nombres=request.form.get("nombres"),\
            apellidos=request.form.get("apellidos"),\
            correo=request.form.get("correo") ,  \
            telefono=request.form.get("telefono"),  \
            direccion=request.form.get("direccion"),\
            sexo=request.form.get("sexo")   )

        rclientes=rows
        return render_template("rpacientes.html")

    else:
        return render_template("rpacientes.html")

@app.route('/eliminarPaciente/<int:id>')
@login_required
def eliminarPaciente(id):
    db.execute("DELETE FROM pacientes where id=:idInv",idInv=id)
    return redirect(url_for('index'))

@app.route('/mpacientes/<int:id>', methods=["GET","POST"])
@login_required
def mpacientes(id):
    if request.method == 'POST':
        db.execute('UPDATE pacientes set cedula=:cedula, nombres = :nombres, apellidos = :apellidos, correo=:correo,telefono=:telefono,sexo=:sexo, \
            direccion = :direccion WHERE id = :idInv', \
                cedula=request.form.get("cedula"),\
                 nombres=request.form.get("nombres"),\
            apellidos=request.form.get("apellidos"),\
            correo=request.form.get("correo") ,  \
            telefono=request.form.get("telefono"),  \
            direccion=request.form.get("direccion"),\
            sexo=request.form.get("sexo")
            , idInv = id)
        return redirect(url_for('index'))
    else:
        rows = db.execute('select * from pacientes where id = :idInv', idInv = id)
        return render_template('mpacientes.html', rows=rows)




if __name__ == '__main__':
    app.run(debug=True)
