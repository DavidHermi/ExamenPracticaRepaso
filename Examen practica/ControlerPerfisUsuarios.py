import DBConection

#Direccion de donde esta la base de datos
uri="perfisUsuarios.bd"


#region Querys Perfis
def getAllPerfis():

    conn=DBConection.createConnection(uri)

    cursor=conn.cursor()

    sql="select * from perfis"

    cursor.execute(sql)

    conn.close()

    return list(cursor.fetchall())

def getPerfisByID(key):

        conn=DBConection.createConnection(uri)
        cursor = conn.cursor()
        sql = "SELECT * FROM perfis WHERE id = ?"
        cursor.execute(sql, [key])
        conn.close()

        return cursor.fetchone()


#endregion

# region Querys PerfisUsuarios

def getAllPerfisUsuarios():

    conn=DBConection.createConnection(uri)

    cursor=conn.cursor()

    sql="select * from perfis"

    cursor.execute(sql)

    conn.close()

    return list(cursor.fetchall())

def getPerfisUsuariosByID(key):

        conn=DBConection.createConnection(uri)
        cursor = conn.cursor()
        sql = "SELECT * FROM perfis WHERE id = ?"
        cursor.execute(sql, [key])
        conn.close()

        return cursor.fetchone()


#endregion


# region Querys Usuarios

def getAllPerfis():

    conn=DBConection.createConnection(uri)

    cursor=conn.cursor()

    sql="select * from perfis"

    cursor.execute(sql)

    conn.close()

    return list(cursor.fetchall())

def getPerfisByID(key):

        conn=DBConection.createConnection(uri)
        cursor = conn.cursor()
        sql = "SELECT * FROM perfis WHERE id = ?"
        cursor.execute(sql, [key])
        conn.close()

        return cursor.fetchone()

# endregion

# region Custom Querys

def customQuery (sql):

    conn = DBConection.createConnection(uri)
    cursor = conn.cursor()

    cursor.execute(sql)

    conn.close()

    return list(cursor.fetchall())


def customQuery (consultaSQL, *parameters):

    try:

        conn = DBConection.createConnection(uri)
        cursor = conn.cursor()
        cursor.execute(consultaSQL, parameters)



    except:
        print("Error en la consulta")
        return None
    else:
        return list(cursor.fetchall())



# endregion





