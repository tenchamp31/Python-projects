import sqlite3
conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()                                                                             #creating database
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_lists(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_filename TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

fileList_tuple = ['information.docx' 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg']     #tuple list


for ext in fileList_tuple:                          #find the file name ending with .txt
    if ext.endswith('.txt'):
        with conn:
            cur = conn.cursor()

            cur.execute("INSERT INTO tbl_lists (col_filename) VALUES (?)", (ext,))
            print(ext)
conn.close()
            
