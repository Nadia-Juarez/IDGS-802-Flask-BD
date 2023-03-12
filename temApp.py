from db import get_connection

try:
    connection=get_connection
    with connection.cursor() as cursor:
        cursor.execute("CALL CONSULTAR_TODOS")#SE PONE EL NOMBRE DEL PROCEDIMIENTO
        cursor.close()
        resultset=cursor.fetchall()
        for row in resultset:
            print(row)
    connection.close()
except Exception as ex:
    print("ERROR")


try:
    connection=get_connection
    with connection.cursor() as cursor:
        #SE PONE EL NOMBRE DEL PROCEDIMIENTO Y EL PARAMETRO CON EL QUE SE REALIZARA
        cursor.execute("CALL CONSULTAR_ALUMNOS(%)s",(2,))
        resultset=cursor.fetchall()
        for row in resultset:
            print(row)
    connection.close()
except Exception as ex:
    print("ERROR")

try:
    connection=get_connection
    with connection.cursor() as cursor:
        #SE PONE EL NOMBRE DEL PROCEDIMIENTO Y EL PARAMETRO CON EL QUE SE REALIZARA
        cursor.execute("CALL INSERTAR_ALUMNO(%s,%s,%s)",("Nadia","Juarez","als@gmail"))
        
        
        resultset=cursor.fetchall()
        for row in resultset:
            print(row)
    connection.commit()
    connection.close()
except Exception as ex:
    print("ERROR")    