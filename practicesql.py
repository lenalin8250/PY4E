import sqlite3


conn=sqlite3.connect('practicesql.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('''CREATE TABLE Ages (
  name VARCHAR(128),
  age INTEGER
)''')


def add_people(Name, Age):
    with conn:
        cur.execute("INSERT INTO Ages VALUES (:name, :age)", {'name':Name, 'age':Age})

People = [('Kylan', 32), ('Gytis', 25), ('Samira', 20), ('Kaidey', 23), ('Peyton', 16), ('Oluwadamilare', 24)]
for i in People:
    Name, Age = i
    add_people(Name, Age)


cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
print(cur.fetchall())
conn.commit()
cur.close()
