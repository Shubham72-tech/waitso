import os
import mysql.connector
def sql_delete():
        cnx = mysql.connector.connect(user='arham', password='12345678', host='192.168.29.96', database='waitso')
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM rpi_data WHERE 1")
        cnx.commit()
        print("deleted SQL successfully")

a=[0,1]
for i in a:
        os.system("sudo rm file.json")
        print("Deleted file.json")
        os.system("howmanypeoplearearound -o file.json -a wlan0mon -s 50 --allmacaddresses")
        print("Generated file.json")
        sql_delete()
        os.system("python json_to_sql.py")