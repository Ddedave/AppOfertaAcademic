import glob
import json
import mysql.connector

conexion = mysql.connector.connect(user ='root', password='', database='final')

cursor = conexion.cursor()

files = glob.glob('*.json')

def existe_clave(l):
    select = 'SELECT * FROM clave WHERE clave = %s'
    cursor.execute(select, (l['Codigo'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return  True
    else:
        return False
def existe_sec(l):
    select = 'SELECT * FROM seccion WHERE seccion = %s'
    cursor.execute(select, (l['Sec'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return  True
    else:
        return False
def existe_cr(l):
    select = 'SELECT * FROM credito WHERE cretido = %s'
    cursor.execute(select, (l['CR'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return  True
    else:
        return False
def existe_cup(l):
    select = 'SELECT * FROM cupo WHERE cupo = %s'
    cursor.execute(select, (l['CUP'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return  True
    else:
        return False
def existe_dis(l):
    select = 'SELECT * FROM disponible WHERE disponible = %s'
    cursor.execute(select, (l['DIS'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return  True
    else:
        return False
def existe_ses(l):
    select = 'SELECT * FROM ses WHERE ses = %s'
    cursor.execute(select, (l['Ses'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return  True
    else:
        return False
def existe_hora(l):
    select = 'SELECT * FROM hora WHERE hora = %s'
    cursor.execute(select, (l['Horario'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return  True
    else:
        return False
def existe_dia(l):
    select = 'SELECT *from dia WHERE dia = %s'
    cursor.execute(select, (l['Dias'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return  True
    else:
        return False
def existe_edificion(l):
    select = 'SELECT * FROM edificio WHERE edificio = %s'
    cursor.execute(select, (l['Edificio'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return  True
    else:
        return False
def existe_aula(l):
    select = 'SELECT * FROM aula WHERE aula = %s'
    cursor.execute(select, (l['Aula'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return  True
    else:
        return False
def existe_periodo(l):
    select = 'SELECT * FROM periodo WHERE periodo = %s'
    cursor.execute(select, (l['Periodo'],))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return  True
    else:
        return False

def insertar_clave(l):
    insert = 'INSERT INTO clave(clave) VALUES(%s)'
    cursor.execute(insert, (l['Codigo'],))
    conexion.commit()
    id_1 = cursor.lastrowid

    return  id_1
def insertar_seccion(l):
    insert = 'INSERT INTO seccion(seccion) VALUES(%s)'
    cursor.execute(insert, (l['Sec'],))
    conexion.commit()
    id_2 = cursor.lastrowid

    return  id_2
def insertar_credito(l):
    insert = 'INSERT INTO credito(cretido) VALUES(%s)'
    cursor.execute(insert, (l['CR'],))
    conexion.commit()
    id_3 = cursor.lastrowid

    return  id_3
def insertar_cupo(l):
    insert = 'INSERT INTO cupo(cupo) VALUES(%s)'
    cursor.execute(insert, (l['CUP'],))
    conexion.commit()
    id_4 = cursor.lastrowid

    return  id_4
def insertar_disponible(l):
    insert = 'INSERT INTO disponible(disponible) VALUES(%s)'
    cursor.execute(insert, (l['DIS'],))
    conexion.commit()
    id_5 = cursor.lastrowid

    return  id_5
def insertar_ses(l):
    insert = 'INSERT INTO ses(ses) VALUES(%s)'
    cursor.execute(insert, (l['Ses'],))
    conexion.commit()
    id_6 = cursor.lastrowid

    return  id_6
def insertar_hora(l):
    insert = 'INSERT INTO hora(hora) VALUES(%s)'
    cursor.execute(insert, (l['Horario'],))
    conexion.commit()
    id_7 = cursor.lastrowid

    return  id_7
def insertar_dia(l):
    insert = 'INSERT INTO dia(dia) VALUES(%s)'
    cursor.execute(insert, (l['Dias'],))
    conexion.commit()
    id_8 = cursor.lastrowid

    return  id_8
def insertar_edificio(l):
    insert = 'INSERT INTO edificio(edificio) VALUES(%s)'
    cursor.execute(insert, (l['Edificio'],))
    conexion.commit()
    id_9 = cursor.lastrowid

    return  id_9
def insertar_aula(l):
    insert = 'INSERT INTO aula(aula) VALUES(%s)'
    cursor.execute(insert, (l['Aula'],))
    conexion.commit()
    id_10 = cursor.lastrowid

    return  id_10
def insertar_periodo(l):
    insert = 'INSERT INTO periodo(periodo) VALUES(%s)'
    cursor.execute(insert, (l['Periodo'],))
    conexion.commit()
    id_11 = cursor.lastrowid

    return  id_11

def get_items(c,f,h):
    select = "SELECT ID FROM "+f+" WHERE "+h+" = %s"
    cursor.execute(select, (c,))
    rows = cursor.fetchall()
    return  rows[0][0]

def inse_maestro(m,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11):
    query = 'INSERT INTO registro(nrc,nombre,nombre_maestro,clave,sec,cr,cup,dis,ses,hora,dia,edif,aula,periodo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(query,(m['NRC'],m['Nombre carrera'],m['maestro'],q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11))
    conexion.commit()

for file in files:
    with open(file, encoding = 'utf-8') as f:
        maestros = json.load(f)
        for m in maestros:
            id_1 = 0
            id_2 = 0
            id_3 = 0
            id_4 = 0
            id_5 = 0
            id_6 = 0
            id_7 = 0
            id_8 = 0
            id_9 = 0
            id_10 = 0
            id_11 = 0
            if not existe_clave(m):
                id_1 = insertar_clave(m)
            else:
                id_1 = get_items(m['Codigo'],"clave","clave")
            if not existe_sec(m):
                id_2 = insertar_seccion(m)
            else:
                id_2 = get_items(m['Sec'],"seccion","seccion")
            if not existe_cr(m):
                id_3 = insertar_credito(m)
            else:
                id_3 = get_items(m['CR'],"credito","cretido")
            if not existe_cup(m):
                id_4 = insertar_cupo(m)
            else:
                id_4 = get_items(m['CUP'],"cupo","cupo")
            if not existe_dis(m):
                id_5 = insertar_disponible(m)
            else:
                id_5 = get_items(m['DIS'],"disponible","disponible")
            if not existe_ses(m):
                id_6 = insertar_ses(m)
            else:
                id_6 = get_items(m['Ses'],"ses","ses")
            if not existe_hora(m):
                id_7 = insertar_hora(m)
            else:
                id_7 = get_items(m['Horario'],"hora","hora")
            if not existe_dia(m):
                id_8 = insertar_dia(m)
            else:
                id_8 = get_items(m['Dias'],"dia","dia")
            if not existe_edificion(m):
                id_9 = insertar_edificio(m)
            else:
                id_9 = get_items(m['Edificio'],"edificio","edificio")
            if not existe_aula(m):
                id_10 = insertar_aula(m)
            else:
                id_10 = get_items(m['Aula'],"aula","aula")
            if not existe_periodo(m):
                id_11 = insertar_periodo(m)
            else:
                id_11 = get_items(m['Periodo'],"periodo","periodo")
            inse_maestro(m,id_1,id_2,id_3,id_4,id_5,id_6,id_7,id_8,id_9,id_10,id_11)
