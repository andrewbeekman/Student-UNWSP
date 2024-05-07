# Andrew Beekman 05/03/2024

import sqlite3

conn = sqlite3.connect('Student Info Group.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE students (
                    stu_ID Integer Primary Key,
                    stu_name Text,
                    stu_gender Text,
                    stu_age Integer,
                    stu_job Text,
                    stu_fav_cereal Text,
                    stu_benchpress Integer
                    )''')

data = [
    ('Andrew Beekman', 'Male', 18, 'Golf Course', 'Cinnamon Toast Crunch', 220),
    ('Seth Young', 'Male', 18, 'Landscaping', 'Honey Nut Cheerios', 165),
    ('Elias Blumer', 'Male', 18, 'Golf Course', 'Lucky Charms', 195),
    ('Louis Falardaoux', 'Male', 19, 'Landscaping', 'Coco Pebbles', 190),
    ('Elijah Hagen', 'Male', 18, 'Chef', 'Captain Crunch', 290),
    ('Noah Ross', 'Male', 18, 'Sporting Store Clerk', 'Golden Grahams', 225),
    ('Jaaron Konkel', 'Male', 18, 'Cashier', 'Captain Crunch', 285),
    ('Katherine Beekman', 'Female', 19, 'Golf Course', 'Coco Pebbles', 105),
    ('Eli Dekam', 'Male', 18, 'Fast Food', 'Cinnamon Toast Crunch', 120),
    ('Jaclyn Brouwer', 'Female', 18, 'Babysitting', 'Fruit Loops', 85)
]

cursor.executemany('INSERT INTO students (stu_name, stu_gender, stu_age, stu_job, stu_fav_cereal, stu_benchpress) VALUES (?, ?, ?, ?, ?, ?)', data)

conn.commit()

cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()