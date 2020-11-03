import psycopg2
from psycopg2 import errors


def add_elem(count, param_1, param_2, param_3):
    conn = psycopg2.connect("dbname=Train user=postgres password=3791215233745")
    cur = conn.cursor()
    try:
        if count == 0:
            cur.execute("INSERT INTO train (id, number_of_cars, year_in_which_it_was_made) VALUES (%s, %s, %s)",
                        (param_1, param_2, param_3))
        elif count == 1:
            cur.execute("INSERT INTO route (number, ending_station) VALUES (%s, %s)", (param_1, param_2))
        elif count == 2:
            cur.execute("INSERT INTO passenger (pid, name) VALUES (%s, %s)", (param_1, param_2))
        elif count == 3:
            cur.execute("INSERT INTO train_route (route_number, train_id) VALUES (%s, %s)", (param_1, param_2))
        elif count == 4:
            cur.execute("INSERT INTO train_passenger (train_id, passenger_id) VALUES (%s, %s)", (param_1, param_2))
    except errors.ForeignKeyViolation:
        print("You enter wrong data! psycopg2.errors.ForeignKeyViolation")
    else:
        print("You update element at database!")
    finally:
        conn.commit()
        cur.close()
        conn.close()


def update_elem(count, param_1, param_2, param_3, param_4):
    # param_4 - it's id_prev
    conn = psycopg2.connect("dbname=Train user=postgres password=3791215233745")
    cur = conn.cursor()
    try:
        if count == 0:
            cur.execute("UPDATE train SET (id, number_of_cars, year_in_which_it_was_made) = (%s, %s, %s) WHERE id = %s",
                        (param_1, param_2, param_3, param_4,))
        elif count == 1:
            cur.execute("UPDATE route SET (number, ending_station) = (%s, %s) WHERE number = %s",
                        (param_1, param_2, param_4,))
        elif count == 2:
            cur.execute("UPDATE passenger SET(pid, name) = (%s, %s) WHERE pid = %s", (param_1, param_2, param_4,))
        elif count == 3:
            cur.execute("UPDATE train_route SET (route_number, train_id) = (%s, %s) WHERE train_id = %s",
                        (param_1, param_2, param_4,))
        elif count == 4:
            cur.execute("UPDATE train_passenger SET (train_id, passenger_id) = (%s, %s) WHERE train_id = %s",
                        (param_1, param_2, param_4,))
    except psycopg2.errors.ForeignKeyViolation:
        print("You enter wrong data! psycopg2.errors.ForeignKeyViolation")
    else:
        print("You update element at database!")
    finally:
        conn.commit()
        cur.close()
        conn.close()


def delete_elem(count, param_1):
    conn = psycopg2.connect("dbname=Train user=postgres password=3791215233745")
    cur = conn.cursor()

    if count == 0:
        cur.execute("DELETE FROM train WHERE id = %s", (param_1,))
    elif count == 1:
        cur.execute("DELETE FROM route WHERE number = %s", (param_1,))
    elif count == 2:
        cur.execute("DELETE FROM passenger WHERE pid = %s", (param_1,))
    elif count == 3:
        cur.execute("DELETE FROM train_route WHERE train_id = %s", (param_1,))
    elif count == 4:
        cur.execute("DELETE FROM train_passenger WHERE train_id = %s", (param_1,))
    conn.commit()
    cur.close()
    conn.close()


def add_random_rows(count):
    conn = psycopg2.connect("dbname=Train user=postgres password=3791215233745")
    cur = conn.cursor()
    try:
        if count == 1:
            cur.execute("INSERT INTO train (id, number_of_cars, year_in_which_it_was_made) "
                        "SELECT trunc(random()*100)::int, trunc(random()*100)::int, trunc(random()*1000)::int FROM "
                        "generate_series(1,3)")
        elif count == 2:
            cur.execute("INSERT INTO route (number, ending_station) "
                        "SELECT trunc(random()*100)::int, chr(trunc(65 + random()*25)::int)||"
                        "chr(trunc(75 + random()*25)::int) FROM generate_series(1,3)")
        elif count == 3:
            cur.execute("INSERT INTO passenger (id, name)"
                        "SELECT trunc(random()*100)::int, chr(trunc(75 + random()*25)::int)||"
                        "chr(trunc(75 + random()*25)::int) FROM generate_series(1,3)")
        elif count == 4:
            cur.execute("INSERT INTO train_route (route_number, train_id) SELECT number, id FROM route TABLESAMPLE"
                        " bernoulli(30) , train TABLESAMPLE bernoulli(30)")
        elif count == 5:
            cur.execute("INSERT INTO train_passenger (train_id, passenger_id) "
                        "SELECT id, pid FROM train TABLESAMPLE bernoulli(30) , passenger TABLESAMPLE bernoulli(30)")
    except psycopg2.errors.UniqueViolation:
        print("You enter wrong data! psycopg2.errors.ForeignKeyViolation")
    else:
        print("You update element at database!")
    finally:
        conn.commit()
        cur.close()
        conn.close()


def find_elem(count, param_1):
    conn = psycopg2.connect("dbname=Train user=postgres password=3791215233745")
    cur = conn.cursor()
    try:
        if count == 1:
            cur.execute("SELECT * FROM train as g1 inner join train_route as s on g1.id = s.train_id where g1.id = %s",
                        (int(param_1),))
            row = cur.fetchone()
            print(" id  num year route_num train_id")
            print(row)
        elif count == 2:
            cur.execute("SELECT * FROM route as g1 inner join train_route as s on g1.number = s.route_number"
                        " where g1.number = %s", (int(param_1),))
            row = cur.fetchone()
            print(" num end_station route_num train_id")
            print(row)
        elif count == 3:
            cur.execute("SELECT * FROM passenger as g1 inner join train_passenger as s on g1.pid = s.passenger_id"
                        " where g1.pid = %s", (int(param_1),))
            row = cur.fetchone()
            print(" id name passenger_id train_id")
            print(row)
    except:
        print("You enter wrong data! Database hasn't an element whit this primary key")
    else:
        print("You find element at database!")
    finally:
        conn.commit()
        cur.close()
        conn.close()


def print_table(count):
    conn = psycopg2.connect("dbname=Train user=postgres password=3791215233745")
    cur = conn.cursor()
    try:
        if count == 1:
            cur.execute("SELECT * FROM train")
            rows = cur.fetchall()
            print(" id  num year")
            for row in rows:
                print(row)
        elif count == 2:
            cur.execute("SELECT * FROM route")
            rows = cur.fetchall()
            print(" num end_station")
            for row in rows:
                print(row)
        elif count == 3:
            cur.execute("SELECT * FROM passenger")
            rows = cur.fetchall()
            print(" pid      name")
            for row in rows:
                print(row)
        elif count == 4:
            cur.execute("SELECT * FROM train_route")
            rows = cur.fetchall()
            print(" route_num train_id")
            for row in rows:
                print(row)
        elif count == 5:
            cur.execute("SELECT * FROM train_passenger")
            rows = cur.fetchall()
            print(" train_id passenger_id")
            for row in rows:
                print(row)
    except:
        print("You enter wrong data! Database does not have element whit this primary key")
    finally:
        conn.commit()
        cur.close()
        conn.close()
