from helper import *
import sqlite3


connection = sqlite3.connect('assignment.sqlite')
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_name = cursor.fetchone()[0]

scrambled_image = Image.open('assignment.jpg')

width, height = scrambled_image.size
new_image = Image.new("RGB", (width, height))

# Create the new descrambles image
for row in cursor.execute(f"select * from ({table_name})"):
    curr_data = convertDataToPixels(row)
    src_position = curr_data[0], curr_data[1], curr_data[2], curr_data[3]
    dst_position = curr_data[4], curr_data[5], curr_data[6], curr_data[7]
    rearrangeSquare(src_position, dst_position, row[4], scrambled_image, new_image)

new_image.save("descrambled_image.jpg", quality=100)

new_image.close()
scrambled_image.close()

cursor.close()
connection.close()
