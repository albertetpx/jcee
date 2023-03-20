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
    crearFestivo('2022-09-26','Festa de la Mercè','national')
    crearFestivo('2022-10-12','Dia de la Hispanitat','national')
    crearFestivo('2022-10-31','Lliure disposició','school')
    crearFestivo('2022-11-01','Festa de Tots Sants','national')
    crearFestivo('2022-12-06','Dia de la Constitució','national')
    crearFestivo('2022-12-08','Dia de la Immaculada','national')
    crearFestivo('2022-12-09','Lliure disposició','school')
    crearFestivo('2022-12-22','Vacances de Nadal','school')
    crearFestivo('2022-12-23','Vacances de Nadal','school')
    crearFestivo('2022-12-24','Vacances de Nadal','school')
    crearFestivo('2022-12-25','Dia de Nadal','national')
    crearFestivo('2022-12-26','Sant Esteve','national')
    crearFestivo('2022-12-27','Vacances de Nadal','school')
    crearFestivo('2022-12-28','Vacances de Nadal','school')
    crearFestivo('2022-12-29','Vacances de Nadal','school')
    crearFestivo('2022-12-30','Vacances de Nadal','school')
    crearFestivo('2022-12-31','Vacances de Nadal','school')
    crearFestivo('2023-01-01','Any Nou','national')
    crearFestivo('2023-01-02','Vacances de Nadal','school')
    crearFestivo('2023-01-03','Vacances de Nadal','school')
    crearFestivo('2023-01-04','Vacances de Nadal','school')
    crearFestivo('2023-01-05','Vacances de Nadal','school')
    crearFestivo('2023-01-06','Dia de Reis','national')
    crearFestivo('2023-01-07','Vacances de Nadal','school')
    crearFestivo('2023-01-08','Vacances de Nadal','school')
    crearFestivo('2023-02-20','Lliure disposició','school')
    crearFestivo('2023-03-17','Lliure disposició','school')
    crearFestivo('2023-04-03','Setmana Santa','school')
    crearFestivo('2023-04-04','Setmana Santa','school')
    crearFestivo('2023-04-05','Setmana Santa','school')
    crearFestivo('2023-04-06','Setmana Santa','school')
    crearFestivo('2023-04-07','Divendres Sant','national')
    crearFestivo('2023-04-08','Setmana Santa','school')
    crearFestivo('2023-04-09','Diumenge de Pasqua','national')
    crearFestivo('2023-04-10','Dilluns de Pasqua','national')
    crearFestivo('2023-05-01','Primer de Maig','national')
    crearFestivo('2023-05-02','lliure diposició','school')
    crearFestivo('2023-06-24','Sant Joan','national')
    return None