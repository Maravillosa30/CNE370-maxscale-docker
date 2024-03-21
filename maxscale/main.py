# Rosa Hulbert
#CNE370 Final Assigment
# 03/19/2024
# This python script connects to  the Maxscale instance.
# Collaborated with Rasmane Sawagodo


import mysql.connector

conn = mysql.connector.connect(user = "maxuser", password= "maxpwd", host = "127.0.0.1", port = "4000")

cursor = conn.cursor()

# Zipcodes_one Queries:

# Query 1: The largest zipcode in zipcodes_one
cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one")
largest_zipcode = cursor.fetchall()
for zipcode in largest_zipcode:
        print("The largest zipcode in zipcodes_one:", largest_zipcode)
        break
        
# Query 2: All zipcodes where state=KY (Kentucky)
cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one  WHERE state='KY'")
ky_zipcodes = cursor.fetchall()
print("All zipcodes where state=KY (Kentucky):")
for row in ky_zipcodes:
    print(row)
    break

# Query 3: All zipcodes between 40000 and 41000
cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000")
zipcodes_between = cursor.fetchall()
print("All zipcodes between 40000 and 41000:")
for row in zipcodes_between:
    print(row)
    break
        
# Query 4: The TotalWages column where state=PA (Pennsylvania)
cursor.execute("SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE state='PA'")
total_wages_pa = cursor.fetchall()
print("The TotalWages column where state=PA (Pennsylvania):")
for row in total_wages_pa:
    print(row[0])
    break
        
# Zipcodes_two Queries: 

# Query 1: The largest zipcode in zipcodes_two
cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two")
largest_zipcode = cursor.fetchall()
for zipcode in largest_zipcode:
        print("The largest zipcode in zipcodes_two:", largest_zipcode)
        break
        
# Query 2: All zipcodes where state=KY (Kentucky)
cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two  WHERE state='KY'")
ky_zipcodes = cursor.fetchall()
print("All zipcodes where state=KY (Kentucky):")
for row in ky_zipcodes:
    print(row)
    break

# Query 3: All zipcodes between 40000 and 41000
cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two WHERE zipcode BETWEEN 40000 AND 41000")
zipcodes_between = cursor.fetchall()
print("All zipcodes between 40000 and 41000:")
for row in zipcodes_between:
    print(row)
    break

# Query 4: The TotalWages column where state=PA (Pennsylvania)
cursor.execute("SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE state='PA'")
total_wages_pa = cursor.fetchall()
print("The TotalWages column where state=PA (Pennsylvania):")
for row in total_wages_pa:
    print(row[0])
    break

cursor.close()
conn.close()



