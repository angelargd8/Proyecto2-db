import psycopg2
def conexiones():
    Password1 = "123456"
    Password2 = "123456" #sus paswords
    Password3 = "123456"#sus paswords

    try:
        conexion= psycopg2.connect(
            host = "localhost",
            database = "Proyecto1",
            user = "postgres",
            password = Password1, 
            port = "5432" #SELECT * FROM pg_settings WHERE name = 'port';
        )
        print("conexion exitosa")
        return conexion

    except Exception as e:
        print(e)
        print("error en la conexion")
        return None