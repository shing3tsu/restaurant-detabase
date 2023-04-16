import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Amhk1570",
    database="restaurant"
)

mycursor = mydb.cursor(buffered=True)

mycursor.execute("CREATE DATABASE IF NOT EXISTS restaurant")

mycursor.execute("CREATE TABLE IF NOT EXISTS menu "
                 "(type VARCHAR(255),"
                 " name VARCHAR(255),"
                 " price VARCHAR(255))")

menu = [
    ("Breakfast", "Eggs", "2.50"),
    ("Breakfast", "Bacon", "3.50"),
    ("Breakfast", "Toast", "1.50"),
    ("Breakfast", "Coffee", "1.50"),
    ("Breakfast", "Tea", "1.50"),
    ("Appetizer", "Soup", "3.50"),
    ("Appetizer", "Fries", "2.50"),
    ("Appetizer", "Onion Rings", "2.50"),
    ("Appetizer", "Mozzarella Sticks", "3.50"),
    ("Appetizer", "Nachos", "3.50"),
    ("Appetizer", "Wings", "3.50"),
    ("Salad", "Caesar", "4.50"),
    ("Salad", "Greek", "4.50"),
    ("Salad", "Caprese", "4.50"),
    ("Salad", "Cobb", "4.50"),
    ("Salad", "Garden", "4.50"),
    ("Main", "Steak", "10.50"),
    ("Main", "Chicken", "8.50"),
    ("Main", "Pork", "8.50"),
    ("Main", "Fish", "8.50"),
    ("Main", "Ribs", "10.50"),
    ("Main", "Burger", "6.50"),
    ("Main", "Sandwich", "5.50"),
    ("Main", "Pizza", "6.50"),
    ("Main", "Pasta", "6.50"),
    ("Dessert", "Ice Cream", "2.50"),
    ("Dessert", "Cheesecake", "3.50"),
    ("Dessert", "Brownie", "2.50"),
    ("Dessert", "Apple Pie", "2.50"),
    ("Dessert", "Chocolate Cake", "3.50"),
    ("Dessert", "Carrot Cake", "3.50"),
    ("Dessert", "Tiramisu", "3.50"),
    ("Dessert", "Cannoli", "3.50"),
    ("Dessert", "Profiteroles", "3.50"),
    ("Dessert", "Panna Cotta", "3.50"),
    ("Dessert", "Creme Brulee", "3.50"),
    ("Dessert", "Bread Pudding", "3.50"),
    ("Dessert", "Banana Split", "3.50"),
    ("Dessert", "Apple Crisp", "3.50"),
    ("Dessert", "Chocolate Mousse", "3.50"),
    ("Dessert", "Key Lime Pie", "3.50"),
    ("Dessert", "Lemon Meringue Pie", "3.50"),
    ("Dessert", "Peach Cobbler", "3.50"),
    ("Dessert", "Pumpkin Pie", "3.50"),
    ("Dessert", "Strawberry Shortcake", "3.50"),
    ("Dessert", "Tres Leches Cake", "3.50"),
    ("Dessert", "Turtle Cheesecake", "3.50"),
    ("Dessert", "White Chocolate Raspberry Truffle", "3.50"),
    ("Beverages", "Water", "1.50"),
    ("Beverages", "Soda", "1.50"),
    ("Beverages", "Tea", "1.50"),
    ("Beverages", "Coffee", "1.50"),
    ("Beverages", "Milk", "1.50"),
    ("Beverages", "Juice", "1.50"),
    ("Beverages", "Beer", "2.50"),
    ("Beverages", "Wine", "2.50"),
    ("Beverages", "Cocktail", "2.50"),
    ("Beverages", "Margarita", "2.50"),
    ("Beverages", "Martini", "2.50"),
    ("Beverages", "Mimosa", "2.50"),
    ("Beverages", "Bloody Mary", "2.50"),
    ("Beverages", "Sangria", "2.50"),
    ("Beverages", "Moscow Mule", "2.50"),
    ("Beverages", "Mojito", "2.50"),
    ("Beverages", "Long Island Iced Tea", "2.50"),
    ("Beverages", "Mai Tai", "2.50"),
    ("Beverages", "Whiskey Sour", "2.50"),
    ("Beverages", "Old Fashioned", "2.50"),
    ("Beverages", "Manhattan", "2.50"),
    ("Beverages", "Negroni", "2.50"),
    ("Beverages", "Gin and Tonic", "2.50"),
]

for x in menu:
    sql = "INSERT INTO menu (type, name, price) VALUES (%s, %s, %s)"
    val = x
    mycursor.execute(sql, val)
    mydb.commit()

def show_menu():
    mycursor.execute("SELECT * FROM menu")
    for x in mycursor:
        print(x)

