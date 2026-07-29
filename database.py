import psycopg2


    return psycopg2.connect(
        host="localhost",
        database="GESTION DE MUSICA",
        user="postgres",
        password="12345",
        port="5432"
    )