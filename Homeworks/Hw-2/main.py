import sqlite3
from datetime import datetime, timezone

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return """
    <a href='/emails/create/'>/emails/create/</a>
    <br><br>
    <a href='/emails/read/'>/emails/read/</a>
    <br><br>
    <a href='/emails/update/'>/emails/update/</a>
    <br><br>
    <a href='/emails/delete/'>/emails/delete/</a>
    """


@app.route('/emails/create/')
def phones_create():
    try:
        name = request.args['name']
        phone = request.args['phone']
        joiningDate = str(datetime.now(timezone.utc).astimezone()).split()[0]
        joiningTime = str(datetime.now(timezone.utc).astimezone()).split()[1][:8]

        con = sqlite3.connect('emails.db')
        cur = con.cursor()

        sql = f'''
        INSERT INTO emails (name, phone, joiningDate, joiningTime)
        VALUES ('{name}', '{phone}', '{joiningDate}', '{joiningTime}' );
        '''
        cur.execute(sql)
        con.commit()
        con.close()
        return "Запись добавлена! <a href='/'>Вернуться на главную</a>"
    except:
        return 'Ошибка! Добавьте параметры в поисковую строку!'


@app.route('/emails/read/')
def phones_read():
    id_ = request.args.get('id')

    con = sqlite3.connect('emails.db')
    cur = con.cursor()

    if id_:
        sql = f'''SELECT * FROM emails WHERE id={id_};'''
    else:
        sql = f'''SELECT * FROM emails;'''
    cur.execute(sql)
    results = cur.fetchall()
    con.close()
    return str(results)


@app.route('/emails/update/')
def phones_update():
    try:
        id_ = request.args['id']
        name = request.args['name']
        phone = request.args['phone']

        con = sqlite3.connect('emails.db')
        cur = con.cursor()

        sql = f'''UPDATE emails SET name='{name}', phone='{phone}' WHERE id={id_};'''

        cur.execute(sql)
        con.commit()
        con.close()
        return "Запись обновлена! <a href='/'>Вернуться на главную</a>"
    except:
        return 'Ошибка! Добавьте параметры в поисковую строку!'


@app.route('/emails/delete/')
def phones_delete():
    try:
        con = sqlite3.connect('emails.db')
        cur = con.cursor()

        sql = '''DELETE FROM emails;'''
        cur.execute(sql)
        con.commit()
        con.close()
        return "Записи удалены! <a href='/'>Вернуться на главную</a>"
    except:
        return 'Ошибка!'

if __name__ == '__main__':
    app.run(debug=True)
