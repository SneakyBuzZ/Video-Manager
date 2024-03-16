import sqlite3

conn = sqlite3.connect('yt_vidoes.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXIST videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT FULL,
               time TEXT NOT NULL
    )
''')


def list_vidoes():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name,time))
    conn.commit()

def update_video(id , name , time):
    cursor.execute("UPDATE videos SET name = ? time = ? WHERE id = ?",(name,time,id))
    conn.commit()

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(id,))
    conn.commit()



def main():
    while True:
        print(" ")
        print(" Youtube Manager | Choose an option ")
        print(" 1 - Listing videos")
        print(" 2 - Adding video")
        print(" 3 - Update video")
        print(" 4 - Delete video")
        print(" 5 - Exit app")
        choice = input("Enter choice : ")
        print(" ")
        match choice:
            case '1':
                list_vidoes()
            case '2':
                add_name = input("Enter name: ")
                add_time = input("Enter time: ")
                add_video(add_name,add_time)
            case '3':
                edit_id = int(input("Enter video id to update: "))
                edit_name = input("Enter name: ")
                edit_time = input("Enter time: ")
                update_video(edit_id,edit_name,edit_time)
            case '4':
                delete_id = int(input("Enter video id to delete: "))
                delete_video(delete_id)
            case '5':
                break
            case _:
                print("Enter correct choice : ")
    

    conn.close()


if __name__ == '__main__':
    main()