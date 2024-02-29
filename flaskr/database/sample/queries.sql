-- CREATE 'items' AND 'board' TABLE

CREATE TABLE IF NOT EXISTS items(
    Item_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Item_Name TEXT NOT NULL,
    Img_Link TEXT,
    Description TEXT,
    Description_Url TEXT,
    Short_Description TEXT,
    Item_Type TEXT

);

CREATE TABLE IF NOT EXISTS board (
    Item_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Item_Name TEXT NOT NULL,
    Img_Link TEXT,
    Description TEXT,
    Description_Url TEXT,
    Short_Description TEXT,
    Item_Type TEXT

);

