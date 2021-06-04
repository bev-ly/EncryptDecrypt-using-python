import pydoc

conn = pydoc.connect(r'Driver = Microsoft Access Driver (*.mdb, *.accdb)};DBQ =C:\Users\LENOVO\Documents\Final-Requirements.accdb')

cursor = conn.cursor()
cursor.excute('select * from Final-Requirements')

for row in cursor.fetchall():
                      print(row)