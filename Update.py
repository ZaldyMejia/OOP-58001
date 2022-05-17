import pyodbc

try:
    connect = pyodbc.connect(r'Driver= {Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Pug\Downloads\Database1.accdb;')
    print("Connected to a Database")

    Laboratory = 100
    user_id = 5

    record = connect.cursor()
    record.execute('UPDATE Table1 SET Laboratory = ? WHERE id=?',(Laboratory,user_id))
    record.commit()
    print("Data is updated")

except pyodbc.Error as e:
    print("Error in Connection")