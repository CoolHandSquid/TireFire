import sqlite3

def show_all():
    conn    = sqlite3.connect('TireFire.db')
    c       = conn.cursor()
    c.execute("SELECT rowid, * FROM Main")
    items   = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

def add_one(name, port, description, cmd_name, cmd_description, cmd_command, cmd_comment, sub_display_order):
    conn    = sqlite3.connect('TireFire.db')
    c       = conn.cursor()
    c.execute("INSERT INTO Main VALUES (?,?,?,?,?,?,?,?)", (name, port, description, cmd_name, cmd_description, cmd_command, cmd_comment, sub_display_order))
    conn.commit()
    conn.close()

def add_many(list):
    conn    = sqlite3.connect('TireFire.db')
    c       = conn.cursor()
    c.executemany("INSERT INTO Main Values (?,?,?,?,?,?,?,?)", (list))
    conn.commit()
    conn.close()

def delete_one(id):
    #Although rowid is an int, pass a string
    conn    = sqlite3.connect('TireFire.db')
    c       = conn.cursor()
    c.execute("DELETE from Main Where rowid = (?)", id)
    conn.commit()
    conn.close()

def get_display_ttl():
    conn    = sqlite3.connect('TireFire.db')
    c       = conn.cursor()
    c.execute("SELECT * from TTL")
    items   = c.fetchall()
    conn.close()
    return items

def get_display_main():
    conn    = sqlite3.connect('TireFire.db')
    c       = conn.cursor()
    c.execute("SELECT Name, Port, Description from Main GROUP BY Name ORDER By Port ASC")
    items   = c.fetchall()
    conn.close()
    return items

def get_display_sub(proto):
    conn    = sqlite3.connect('TireFire.db')
    c       = conn.cursor()
    c.execute("SELECT Cmd_Name, SUBSTRING(Cmd_Description, 1, 50), SUBSTRING(replace(Cmd_Command, X'0A', ' '), 1, 50) AS Cmd_Command, CMD_Comment from Main WHERE Name = (?)", (proto,))
    items   = c.fetchall()
    conn.close()
    return items

def get_fullcommand(proto):
    conn    = sqlite3.connect('TireFire.db')
    c       = conn.cursor()
    c.execute("SELECT Cmd_Command from Main WHERE Name = (?)", (proto,))
    items   = c.fetchall()
    conn.close()
    return items
