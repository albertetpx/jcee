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
    crearFestivo('2025-09-11','Diada de Catalunya','national')
    crearFestivo('2025-09-24','Festa de la Mercè','national')
    crearFestivo('2025-10-10','Lliure disposició','school')
    crearFestivo('2025-11-03','Lliure disposició','school')
    crearFestivo('2025-12-08','Dia de la Immaculada','national')
    crearFestivo('2025-12-22','Vacances de Nadal','school')
    crearFestivo('2025-12-23','Vacances de Nadal','school')
    crearFestivo('2025-12-24','Vacances de Nadal','school')
    crearFestivo('2025-12-25','Dia de Nadal','national')
    crearFestivo('2025-12-26','Sant Esteve','national')
    crearFestivo('2025-12-29','Vacances de Nadal','school')
    crearFestivo('2025-12-30','Vacances de Nadal','school')
    crearFestivo('2025-12-31','Vacances de Nadal','school')
    crearFestivo('2026-01-01','Any Nou','national')
    crearFestivo('2026-01-02','Vacances de Nadal','school')
    crearFestivo('2026-01-05','Vacances de Nadal','school')
    crearFestivo('2026-01-06','Dia de Reis','national')
    crearFestivo('2026-01-07','Vacances de Nadal','school')
    crearFestivo('2026-02-16','Lliure disposició','school')
    crearFestivo('2026-03-30','Setmana Santa','school')
    crearFestivo('2026-03-31','Setmana Santa','school')
    crearFestivo('2026-04-01','Setmana Santa','school')
    crearFestivo('2026-04-02','Setmana Santa','school')
    crearFestivo('2026-04-03','Divendres Sant','national')
    crearFestivo('2026-04-06','Dilluns de Pasqua','national')
    crearFestivo('2026-04-30','Lliure disposició','school')
    crearFestivo('2026-05-01','Primer de Maig','national')
    crearFestivo('2026-05-25','Pasqua Granada','national')
    crearFestivo('2026-06-24','Sant Joan','national')
    return None