from flask import Flask, render_template, request, redirect, jsonify
from database import get_connection

app = Flask(__name__)


# ==================================================
# HTML - LISTAR ARTISTAS Y CANCIONES
# ==================================================

@app.route("/")
def index():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            a.id_artista,
            a.nombre,
            a.pais,
            a.genero,
            c.id_cancion,
            c.titulo,
            c.duracion,
            c.anio

        FROM artistas a

        LEFT JOIN canciones c
        ON a.id_artista = c.id_artista

        ORDER BY a.id_artista
    """)


    artistas = cursor.fetchall()


    cursor.close()
    conn.close()


    return render_template(
        "index.html",
        artistas=artistas
    )



# ==================================================
# HTML - GUARDAR ARTISTA + CANCION
# ==================================================

@app.route("/guardar", methods=["POST"])
def guardar():

    nombre = request.form["nombre"]
    pais = request.form["pais"]
    genero = request.form["genero"]

    titulo = request.form["titulo"]
    duracion = request.form["duracion"]
    anio = request.form["anio"]


    conn = get_connection()
    cursor = conn.cursor()


    # Guardar artista

    cursor.execute("""
        INSERT INTO artistas
        (nombre,pais,genero)

        VALUES(%s,%s,%s)

        RETURNING id_artista

    """,
    (
        nombre,
        pais,
        genero
    ))


    id_artista = cursor.fetchone()[0]


    # Guardar canción

    cursor.execute("""
        INSERT INTO canciones
        (titulo,duracion,anio,id_artista)

        VALUES(%s,%s,%s,%s)

    """,
    (
        titulo,
        duracion,
        anio,
        id_artista
    ))


    conn.commit()


    cursor.close()
    conn.close()


    return redirect("/")



# ==================================================
# HTML - MOSTRAR EDITAR
# ==================================================

@app.route("/editar/<int:id_artista>")
def editar(id_artista):

    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("""
        SELECT
            a.id_artista,
            a.nombre,
            a.pais,
            a.genero,
            c.id_cancion,
            c.titulo,
            c.duracion,
            c.anio

        FROM artistas a

        LEFT JOIN canciones c
        ON a.id_artista=c.id_artista

        WHERE a.id_artista=%s

    """,
    (id_artista,))


    artista = cursor.fetchone()


    cursor.close()
    conn.close()


    return render_template(
        "editar.html",
        artista=artista
    )



# ==================================================
# HTML - ACTUALIZAR
# ==================================================

@app.route("/actualizar/<int:id_artista>", methods=["POST"])
def actualizar(id_artista):

    nombre=request.form["nombre"]
    pais=request.form["pais"]
    genero=request.form["genero"]

    titulo=request.form["titulo"]
    duracion=request.form["duracion"]
    anio=request.form["anio"]


    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute("""
        UPDATE artistas

        SET nombre=%s,
            pais=%s,
            genero=%s

        WHERE id_artista=%s

    """,
    (
        nombre,
        pais,
        genero,
        id_artista
    ))



    cursor.execute("""
        UPDATE canciones

        SET titulo=%s,
            duracion=%s,
            anio=%s

        WHERE id_artista=%s

    """,
    (
        titulo,
        duracion,
        anio,
        id_artista
    ))



    conn.commit()


    cursor.close()
    conn.close()


    return redirect("/")



# ==================================================
# HTML - ELIMINAR
# ==================================================

@app.route("/eliminar/<int:id_artista>")
def eliminar(id_artista):

    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute("""
        DELETE FROM canciones

        WHERE id_artista=%s

    """,
    (id_artista,))


    cursor.execute("""
        DELETE FROM artistas

        WHERE id_artista=%s

    """,
    (id_artista,))


    conn.commit()


    cursor.close()
    conn.close()


    return redirect("/")



# ==================================================
# API GET - THUNDER CLIENT
# ==================================================

@app.route("/api/artistas", methods=["GET"])
def api_get():

    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute("""
        SELECT
            a.id_artista,
            a.nombre,
            a.pais,
            a.genero,
            c.titulo,
            c.duracion,
            c.anio

        FROM artistas a

        LEFT JOIN canciones c

        ON a.id_artista=c.id_artista

    """)


    datos=cursor.fetchall()


    lista=[]


    for d in datos:

        lista.append({
            "id_artista":d[0],
            "nombre":d[1],
            "pais":d[2],
            "genero":d[3],
            "cancion":d[4],
            "duracion":d[5],
            "anio":d[6]
        })


    cursor.close()
    conn.close()


    return jsonify(lista)



# ==================================================
# API POST - THUNDER CLIENT
# ==================================================

@app.route("/api/artistas", methods=["POST"])
def api_post():

    datos=request.json


    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute("""
        INSERT INTO artistas
        (nombre,pais,genero)

        VALUES(%s,%s,%s)

        RETURNING id_artista

    """,
    (
        datos["nombre"],
        datos["pais"],
        datos["genero"]
    ))


    id_artista=cursor.fetchone()[0]


    cursor.execute("""
        INSERT INTO canciones
        (titulo,duracion,anio,id_artista)

        VALUES(%s,%s,%s,%s)

    """,
    (
        datos["titulo"],
        datos["duracion"],
        datos["anio"],
        id_artista
    ))


    conn.commit()


    cursor.close()
    conn.close()


    return jsonify({
        "mensaje":"Guardado correctamente"
    })



# ==================================================
# API PUT - THUNDER CLIENT
# ==================================================

@app.route("/api/artistas/<int:id_artista>", methods=["PUT"])
def api_put(id_artista):

    datos=request.json


    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute("""
        UPDATE artistas

        SET nombre=%s,
            pais=%s,
            genero=%s

        WHERE id_artista=%s

    """,
    (
        datos["nombre"],
        datos["pais"],
        datos["genero"],
        id_artista
    ))


    cursor.execute("""
        UPDATE canciones

        SET titulo=%s,
            duracion=%s,
            anio=%s

        WHERE id_artista=%s

    """,
    (
        datos["titulo"],
        datos["duracion"],
        datos["anio"],
        id_artista
    ))


    conn.commit()


    cursor.close()
    conn.close()


    return jsonify({
        "mensaje":"Actualizado correctamente"
    })



# ==================================================
# API DELETE - THUNDER CLIENT
# ==================================================

@app.route("/api/artistas/<int:id_artista>", methods=["DELETE"])
def api_delete(id_artista):

    conn=get_connection()
    cursor=conn.cursor()


    cursor.execute("""
        DELETE FROM canciones
        WHERE id_artista=%s
    """,
    (id_artista,))


    cursor.execute("""
        DELETE FROM artistas
        WHERE id_artista=%s
    """,
    (id_artista,))


    conn.commit()


    cursor.close()
    conn.close()


    return jsonify({
        "mensaje":"Eliminado correctamente"
    })



if __name__=="__main__":
    app.run(debug=True)