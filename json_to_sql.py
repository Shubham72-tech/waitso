import mysql.connector

cnx = mysql.connector.connect(user='arham', password='12345678',
                              host='192.168.29.96',
                              database='waitso')
cursor = cnx.cursor()
opt = ['company', 'mac', 'rssi']

file = "file.json"
json_data = eval(open(file).read())
cellphones = json_data["cellphones"]
for i in range(len(cellphones)):
    cursor.execute("SELECT * FROM rpi_data;")
    mac_ids = [row[1] for row in cursor]
    cnx.commit()
    data = [cellphones[i][j] for j in opt]
    if data[1] not in mac_ids:
        cmd = "INSERT INTO rpi_data VALUES (%s, %s, %s); "
    else:
        cmd = "UPDATE rpi_data SET rssi = %s WHERE mac = %s;"
        data = (data[2], data[1])
    cursor.execute(cmd, data)
    cnx.commit()

print('updated SQL')
cursor.close()
cnx.close()
