import os
import sqlite3


def user_db_insertion():
    wanted = True
    print("Insert a record into the database for statistics.")
    while wanted:
        try:
            possibilities = int(input("Amount of possibilities: "))
            tag = str(input("short tag: "))
            info = str(input("information about the probability: "))
            source = str(input("reference to the source of information: "))
            insert_record(possibilities, tag, info, source)
        except:
            print("database insertion failed")
            user_db_insertion()
        wanted = int(input("another one (1 or 0)?"))
    print("database insertion finished")


def insert_record(probability, tag, info, source):
    connection = sqlite3.connect("statistics.db")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO statistics (probability, tag, info, source) VALUES (?,?,?,?);""",
                   (int(probability), str(tag), str(info), str(source)))
    connection.commit()
    connection.close()


def increment_participants(statistics_id):
    connection = sqlite3.connect("statistics.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT participants FROM statistics WHERE id=?""", (int(statistics_id),))
    participants = cursor.fetchone()
    cursor.execute("""UPDATE statistics SET participants=? WHERE id=?""",
                   (int(participants + 1), int(statistics_id)))
    connection.commit()
    connection.close()


def increment_winners(statistics_id):
    connection = sqlite3.connect("statistics.db")
    cursor = connection.cursor()
    cursor.execute("""SELECT winners FROM statistics WHERE id=?""", (int(statistics_id),))
    winners = cursor.fetchone()
    cursor.execute("""UPDATE statistics SET winners=? WHERE id=?""",
                   (int(winners + 1), int(statistics_id)))
    connection.commit()
    connection.close()


def create_db():
    connection = sqlite3.connect("statistics.db")
    cursor = connection.cursor()

    sql = "CREATE TABLE statistics(" \
          "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
          "probability INTEGER, " \
          "tag TEXT, " \
          "info TEXT, " \
          "participants INTEGER DEFAULT 0, " \
          "winners INTEGER DEFAULT 0, " \
          "source TEXT, " \
          "timestamp DEFAULT CURRENT_TIMESTAMP)"

    cursor.execute(sql)
    connection.close()


if __name__ == "__main__":
    if not os.path.exists("statistics.db"):
        create_db()

    user_db_insertion()
    # TODO: input def calls here
