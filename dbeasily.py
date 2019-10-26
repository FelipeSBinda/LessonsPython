import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="mydatabase"
    )

mycursor = mydb.cursor()

'''mycursor.execute("CREATE TABLE IF NOT EXISTS matricula (mat_aluno INT AUTO_INCREMENT PRIMARY KEY, aluno VARCHAR(255), turno VARCHAR(255))")
'''
sql = "INSERT INTO matricula (aluno, turno) VALUES (%s, %s)"
val = ("John", "Integral")
mycursor.execute(sql, val)



