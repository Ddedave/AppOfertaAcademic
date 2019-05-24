from flask import Flask,jsonify

app = Flask(__name__)

import mysql.connector
conexion = mysql.connector.connect(
user='root',
password ='',
database = 'final'

)
cursor = conexion.cursor()
@app.route('/')
def hello():
    query = "SELECT * FROM registro"
    cursor.execute(query)
    maestro = cursor.fetchall()
    lista_casas = []
    for m in maestro:
        query1_mu = "SELECT * FROM clave Where ID ="+str(m[3])
        cursor.execute(query1_mu)
        muni1 = cursor.fetchall()
        query2_mu = "SELECT * FROM seccion Where ID ="+str(m[4])
        cursor.execute(query2_mu)
        muni2 = cursor.fetchall()

        query3_mu = "SELECT * FROM credito Where ID = " + str(m[5])
        cursor.execute(query3_mu)
        muni3 = cursor.fetchall()

        query4_mu = "SELECT * FROM cupo Where ID ="+str(m[6])
        cursor.execute(query4_mu)
        muni4 = cursor.fetchall()

        query5_mu = "SELECT * FROM disponible Where ID ="+str(m[7])
        cursor.execute(query5_mu)
        muni5 = cursor.fetchall()

        query6_mu = "SELECT * FROM ses Where ID ="+str(m[8])
        cursor.execute(query6_mu)
        muni6 = cursor.fetchall()

        query7_mu = "SELECT * FROM hora Where ID ="+str(m[9])
        cursor.execute(query7_mu)
        muni7 = cursor.fetchall()

        query8_mu = "SELECT * FROM dia Where ID ="+str(m[10])
        cursor.execute(query8_mu)
        muni8 = cursor.fetchall()

        query9_mu = "SELECT * FROM edificio Where ID ="+str(m[11])
        cursor.execute(query9_mu)
        muni9 = cursor.fetchall()

        query10_mu = "SELECT * FROM aula Where ID ="+str(m[12])
        cursor.execute(query10_mu)
        muni10 = cursor.fetchall()

        query11_mu = "SELECT * FROM periodo Where ID ="+str(m[13])
        cursor.execute(query11_mu)
        muni11 = cursor.fetchall()
        list = []
        c={
         'NRC':m[0],
         'Mombre_materia':m[1],
         'Nombre_maestro':m[2],
         'clave':muni1[0][1],
         'seccion':muni2[0][1],
         'creditos':muni3[0][1],
         'cupos':muni4[0][1],
         'disponibles':muni5[0][1],
         'ses':muni6[0][1],
         'hora':muni7[0][1],
         'dia':muni8[0][1],
         'edif':muni9[0][1],
         'aula':muni10[0][1],
         'periodo':muni11[0][1]
        }
        lista_casas.append(c)
    return jsonify(Maestros=lista_casas)

app.run()
