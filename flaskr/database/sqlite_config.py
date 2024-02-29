import sqlite3

"""
add here path DB
"""

PATH_SQL = r"C:\Users\Art\Desktop\MOODIC MUSE\flaskr\database\sample\MUSE"
# gesu = "POST"
# try:
#     if gesu == "POST":
#         conx = sqlite3.connect(PATH_SQL)
#         cursor = conx.cursor()
#         # Adding form data in a list
#         request_list = ["altair", "napoli", 99, "dark", "blue"]
#         my_data = list()
#         for x in request_list:
#             # doing query for each item and save in 'my_data'
#             QUERY = f"SELECT * FROM items WHERE Description LIKE '%{x}%' LIMIT 3"
#             cursor.execute(QUERY)
#             res = cursor.fetchall()
#             print(res)
#             if res:
#                 for x in res:
#                     my_data.append(x[1:])
#         QUERY_ins = """INSERT INTO board (Item_Name, Img_Link, Description, Description_Url, Short_Description, Item_Type)
#         VALUES (?, ?, ?, ?, ?, ?)"""
#         print(my_data)
#         cursor.executemany(QUERY_ins, my_data)
#         conx.commit()
#         conx.close()
#         print("MADONNA LAIDA")
# except Exception as e:
#     print(f"An error occurred: {e}")
