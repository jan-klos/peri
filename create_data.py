import os
import sqlite3
from random import randint
import time


db = sqlite3.connect("/home/komp/peri_db/peri.db", check_same_thread=False)
cursor = db.cursor()

cursor.execute('''SELECT time FROM luminosity ORDER BY time DESC''')
last_time = cursor.fetchall()[0][0]
i = 1
while i < 10:
    r = randint(0, 100)
    cursor.execute("INSERT INTO luminosity VALUES (?, ?)", (last_time + i, r))
    i += 1
db.commit()