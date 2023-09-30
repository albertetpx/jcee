import sqlite3

def initBD():
    bd = sqlite3.connect("db/jcee.db")
    cursor = bd.cursor()
    try:
        query = '''CREATE TABLE IF NOT EXISTS festivos(id integer primary key autoincrement,name varchar(255), date date, type varchar(10));''' #Type: national,school
        cursor.execute(query)        
    except Exception as e:
        print("Error initializing database: ", e)
    bd.commit()
    bd.close()
    return

def consultarFestivos():
    bd = sqlite3.connect("db/jcee.db")
    cursor = bd.cursor()
    query = 'SELECT date,name,type FROM festivos ORDER BY date ASC;'
    cursor.execute(query)
    results = cursor.fetchall()
    bd.close()
    return results

def crearFestivo(date,name,type):
    bd = sqlite3.connect("db/jcee.db")
    cursor = bd.cursor()
    try:
        query = f"INSERT INTO festivos(name,date,type) VALUES('{name}','{date}','{type}');"
        # print(query)
        cursor.execute(query)
    except Exception as e:
        print("Database error: ", e)
    bd.commit()
    bd.close()

def eliminarFestivo(date,name):
    bd = sqlite3.connect("db/jcee.db")
    cursor = bd.cursor()
    try:
        query = f"SELECT id FROM festivos WHERE date='{date}';"
        cursor.execute(query)
        id = cursor.fetchall()[0][0]
        print(id)
        
        query = f"DELETE FROM festivos WHERE id={id};"
        cursor.execute(query)
    except Exception as e:
        print("Database error: ", e)
    bd.commit()
    bd.close()

def defaultHolidays():
    festivos = consultarFestivos()
    if festivos != []:
        return    
    crearFestivo('2023-09-11','Diada de Catalunya','national')
    crearFestivo('2023-09-25','Festa de la Mercè','national')
    crearFestivo('2023-10-12','Festa del Pilar','national')
    crearFestivo('2023-10-13','Lliure disposició','school')
    crearFestivo('2023-11-01','Festa de Tots Sants','national')
    crearFestivo('2023-12-06','Dia de la Constitució','national')
    crearFestivo('2023-12-07','Lliure disposició','school')
    crearFestivo('2023-12-08','Dia de la Immaculada','national')
    crearFestivo('2023-12-21','Vacances de Nadal','school')
    crearFestivo('2023-12-22','Vacances de Nadal','school')
    crearFestivo('2023-12-25','Dia de Nadal','national')
    crearFestivo('2023-12-26','Sant Esteve','national')
    crearFestivo('2023-12-27','Vacances de Nadal','school')
    crearFestivo('2023-12-28','Vacances de Nadal','school')
    crearFestivo('2023-12-29','Vacances de Nadal','school')
    crearFestivo('2023-12-30','Vacances de Nadal','school')
    crearFestivo('2024-01-01','Any Nou','national')
    crearFestivo('2024-01-02','Vacances de Nadal','school')
    crearFestivo('2024-01-03','Vacances de Nadal','school')
    crearFestivo('2024-01-04','Vacances de Nadal','school')
    crearFestivo('2024-01-05','Vacances de Nadal','school')
    crearFestivo('2024-01-06','Dia de Reis','national')
    crearFestivo('2024-02-12','Lliure disposició','school')
    crearFestivo('2024-03-25','Setmana Santa','school')
    crearFestivo('2024-03-26','Setmana Santa','school')
    crearFestivo('2024-03-27','Setmana Santa','school')
    crearFestivo('2024-03-28','Setmana Santa','school')
    crearFestivo('2024-03-29','Divendres Sant','national')
    crearFestivo('2024-03-31','Diumenge de Pasqua','national')
    crearFestivo('2024-04-01','Dilluns de Pasqua','national')
    crearFestivo('2024-04-26','Lliure disposició','school')
    crearFestivo('2024-05-01','Primer de Maig','national')
    crearFestivo('2024-05-20','Pasqua Granada','national')
    crearFestivo('2024-06-24','Sant Joan','national')
    return None