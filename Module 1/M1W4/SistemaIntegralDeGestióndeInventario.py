import os
from datetime import datetime

"""
Title: Comprehensive inventory management system.
Can add, search, update and delete products of the inventory.
"""

"""
List of Products. This have a dict with the stucture of the products
product = {
    "title": str,
    "autor": str,
    "category": str,
    "price": float,
    "stock": int 
}

client = {
    "id": int, (ID personal identification)
    products_sold: [
        {
            "title": str,
            "price": int,
            "quantity": int,
            "date": datetime,
            "discount": int
        }
    ]
}

categories = [str]

"""

products = [
    {
        "title": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "category": "Literatura infantil",
        "price": 20.50,
        "stock": 10
    },
    {
        "title": "El moderno Prometeo",
        "autor": "Mary Shelley",
        "category": "Terror",
        "price": 10.30,
        "stock": 5
    },
    {
        "title": "1984",
        "autor": "George Orwell",
        "category": "Ciencia ficcion",
        "price": 15.0,
        "stock": 3
    },
    {
        "title": "El tunel",
        "autor": "Ernesto Sabato",
        "category": "Novela",
        "price": 8.50,
        "stock": 5
    },
    {
        "title": "La rueda del tiempo",
        "autor": "Robert Jordan",
        "category": "Novela",
        "price": 25.00,
        "stock": 10
    }
]

clients = []

"""
Main functions for the inventory manage.
Allow add, search, update and delete products. (CRUD).
"""

def add_product(title: str, autor: str, category: str, price: float, stock: int) -> bool:
    """
    Adds a new product to the inventory.
    
    :param name: Name of the product.
    :param price: Price of the product.
    :param stock: Available stock.
    :return: Return True if is created, False if not.
    """
    try:
        products.append({
            "title": title,
            "autor": autor,
            "category": category,
            "price": price,
            "stock": stock
        })
        return True
    
    except:
        print("Error adding product")
        return False

def search_product(title: str) -> dict:
    """
    Search for a product by their name.
    
    :param name: Name of the product to search.
    :return: Return the dict if found, return None if not.
    """

    for product in products:
        if product["title"] == title:
                return product
    return None

def update_product(title: str, autor: str = None, category: str = None, price: float = None, stock: int = None) -> bool:
    """
    Update a product data if exist.
    
    :param name: Name of the product to update (Necesary to search the product).
    :param price: New price (optional).
    :param stock: New stock (optional).
    :return: Return True if is updated, False if not
    """

    for product in products:
        if product["title"] == title:
            if autor is not None:
                product["autor"] = (autor)
            if category is not None:
                product["category"] = (category)
            if price is not None:
                product["price"] = (price)
            if stock is not None:
                product["stock"] = (stock)
            return True
    return False

def delete_product(title: str) -> bool:
    """
    Delete a product if exist.
    
    :param name: Name of the product to search.
    :return: Return True if is deleted, False if not
    """

    for i, product in enumerate(products):
        if product["title"] == title:
            del products[i]
            return True
    return False

"""
Client Management Main Functions
"""

def add_client (id: int) -> bool:
    """
    Add a new user with the ID
    :param id: New client personal identification.
    :return: bool. True if was created. False if we have any exception
    """
    try: 
        clients.append(
            {
                "id": id,
                "products_sold": []
            }
        )
        return True
    except:
        print("Error adding the client")
        return False
    
def add_purchase (id: int, purchases: list[dict]) -> list:
    """
    Add a new purchase in the list of one client.
    :param id: Client personal identification.
    :param purchases: List of dict with the information of the purchases.

    purchases = [{
        "title": str,
        "price": int,
        "quantity": int,
        "date": datetime,
        "discount": int
    }]

    :return: Return the new list of purchases of the client. Or None if the client not exist.
    """

    client = search_client(id)

    if client is None:
        return None
    
    for purchase in purchases:
        client["products_sold"].append(purchase)
    
    return client["products_sold"]

def search_client (id: int) -> dict:
    """
    Check if the client has been registered in the store.
    :param id: Client personal identification.
    :return: Dict. return the client dict if exist, None if not. 
    """

    for client in clients:
        if client["id"] == id:
            return client
    return None

def verify_client_to_buy (id: int, purchases: list[dict]) -> list[dict]:
    """
    Verify if the user exist.
    Then add a new purchases to the List.

    If the client not exist, create a new client with the new ID number.
    And then add the purchases to the new client.  

    :param id: Client personal identification.
    :param purchases: List of dict with the purchases of the client.
    :return: Return the list of purchases of the client if exist and if not. 
    Return None if the client not exist and have occured an error creating the new uclient

    purchases = [{
        "title": str,
        "price": int,
        "quantity": int,
        "date": datetime,
        "discount": int
    }]

    """

    if search_client(id):
        return add_purchase(id, purchases) 
    else:
        if add_client(id):
            return add_purchase(id, purchases)
        else:
            return None
"""
Sales statistics functions
"""

def top_sales () -> list[dict]:
    """
    This function return the tip sales by autor

    :return: Return a list with the top 3 sales by title
    """
    sales = []
    for client in clients:
        for key, value in client.items():
            if key == "products_sold":
                for item in value:
                    if find_value_in_diccionary(sales, item["title"]):
                        for venta in sales:
                            if venta["title"] == item["title"]:
                                venta["quantity"] += item["quantity"]
                                
                    else:
                        sales.append({
                            "title": item["title"],
                            "quantity": item["quantity"]
                        })
    
    top = sorted(sales, key=lambda item: item["quantity"])

    return top[-3:]

def total_sales () -> list[dict]:
    """
    This function return all the sales of the store by autor.

    :return: Return a list with all the sales of the store by autor
    """
    sales = []
    for client in clients:
        for key, value in client.items():
            if key == "products_sold":
                for item in value:
                    if find_value_in_diccionary(sales, item["autor"]):
                        for venta in sales:
                            if venta["autor"] == item["autor"]:
                                venta["quantity"] += item["quantity"]
                                
                    else:
                        sales.append({
                            "autor": item["autor"],
                            "quantity": item["quantity"]
                        })
    return sales

"""
Function for inventory price.
"""

def invetory_price_with_discount() -> float:
    total_sum = 0


    for client in clients:
        for clave, valor in client.items():
            if clave == "products_sold":
                for item in valor:
                    total_sum += item["price"] * (1 -(item["discount"][1] / 100)) * item["quantity"]

    return total_sum

def invetory_price_without_discount() -> float:
    total_sum = 0


    for client in clients:
        for clave, valor in client.items():
            if clave == "products_sold":
                for item in valor:
                    total_sum += item["price"] * item["quantity"]

    return total_sum


"""
User action handling functions.
"""


def option_add() -> None:
    """
    Allows the user to add a new product to the inventory.
    Requests the product name, unit price, discount percentage, and stock availability.
    """

    title = UI_strInput("Enter the book title")
    autor = UI_strInput("Enter the book autor")
    category = UI_strInput("Enter the category")
    price = UI_parseFloat("Enter the price")
    stock = UI_parseInt("Enter the stock of products")

    if search_product(title):
        print(UI(f"The book {title} alrealy exist."))
        input()
        return 

    if add_product(title, autor, category, price, stock):
        print(UI(f"Book {title} added successfully."))
    else:
        print(UI("Error adding product. Please try again."))

    input()

def option_search() -> None:
    """
    Allows the user to search for a product by name.
    Requests the name of the product to search for.
    If the product is found, displays its details.
    """
    title = UI_strInput("Enter the title of the book to search")

    product = search_product(title)

    if product:
        print(UI(f"Book found: {product}")) 
    else:
        print(UI(f"Book {title} nor found."))
    input()

def option_update() -> None:
    """
    Allows the user to update an existing product.
    Requests the name of the product to update and the new values (price, discount, stock).
    If the product is found, updates its details.s
    """

    title = UI_strInput("Enter the book title to update")

    if not search_product(title):
        print(UI(f"Book {title} not found."))
        input()
        return

    # Pedir los nuevos valores (pueden dejarse en blanco para no actualizar)
    autor = UI_strInput("Enter the new autor")
    category = UI_strInput("Enter the new category")
    price = UI_parseFloat("Enter the new price")
    stock = UI_parseInt("Enter the new stock")

    # Procesar los valores ingresados

    if update_product(title, autor, category, price, stock):
        print(UI(f"Book {title} successfully updated."))
    else:
        print(UI("Error updating product. Please try again."))
    
    input()

def option_delete() -> None:
    """
    Allows the user to delete a product from the inventory.
    Requests the name of the product to delete.
    If the product is found, it is deleted from the inventory.
    """

    title = UI_strInput("Enter the book name to delete")

    if delete_product(title):
        print(UI(f"Book {title} successfully removed."))
    else:
        print(UI("Error deleting product. Please try again."))

    input()

"""
Client action handling functions.
"""

def option_client_purchase() -> None:
    purchases = []
    exit = False    

    id = UI_parseInt("Enter the client document.")

    while exit is False:
        name = UI_strInput("Enter the book title")
        product = search_product(name)

        print(product)

        if product is None:
            print(UI("Product not found"))
            input()
            continue

        quantity = UI_parseInt("Enter the quantity of products the customer wants to purchase")
        
        if UI_strInput("Do you want to add a discount? (y/n)").strip().lower() == 'y':
            discount = UI_parseInt("Enter the discount of these products in %")
        else:
            discount = 0

        purchases.append({
            "title": product["title"],
            "price": product["price"],
            "quantity": quantity,
            "date": datetime.now(),
            "discount": discount
        })

        option = input(f"{UI("You want to continue? (y/n): ")}\nUser -> ").strip().lower()
        
        if option == 'y':
            continue
        elif option == 'n':
            exit = True
        else:
            print(UI("Invalid option... The process will be stopped"))
            input()
            exit = True
        
    print(UI(add_purchase(id, purchases)))
    print(UI())

"""
Utility functions for user interface management.
"""

def clear(): 
    os.system("clear")

def UI (msj: str) -> str:
    # Const variables in the menu build
    #clear()
    size = 100
    border_char = "∙"
    fill_char = "⎯"
    line_char = " "
    side_char_l = "⎢"
    side_char_r = "⎥"
    
    # Building head of the menu
    message = f"{border_char}{fill_char * (size - 2)}{border_char}"
    
    # Separate each message in a List
    for line in msj.splitlines():
        line_length = len(line) 

        # Adjust the line if it is odd
        if line_length % 2 == 1:
            #Add a space to coincide
            line += " "
            
        line_length = len(line)
        
        # Calculate padding
        total_padding = size - 2 - line_length
        padding = total_padding // 2
        
        # Add a line to menu 
        message += f"\n{side_char_l}{line_char * padding}{line}{line_char * padding}{side_char_r}"
    
    # Building the footer of the menu
    message += f"\n{border_char}{fill_char * (size - 2)}{border_char}"
    
    return message

def UI_strInput(message: str) -> str:
    """
    Contains validations for the str type.

    :param message: Message displayed to the user when requesting data.
    :return: Returns the data if it passed the validations.
    """

    value = input(f"{UI(message)}\nUser -> ")

    if not value:
        print(UI("The requested data cannot be empty."))
        UI_strInput(message)
    else: 
        return value
    
def UI_parseInt(message: str) -> int:
    """
    Validates if the type of data entered by the user is int.

    :param message: Message displayed to the user when requesting data.
    :return: Returns the data transformed into an integer.
    :raises: If the entered data is not an integer, the user is prompted again.
    """
    #clear()
    
    try: 
        value = int(input(f"{UI(message)}\nUser -> ")) 

        if value < 0 and not value is None:
            print(UI("You must enter a positive integer. Please try again."))
            input()
            return UI_parseInt(message)

        return value 

    except:
        print(UI("You must enter a valid number. Please try again."))
        input()
        return UI_parseInt(message)
    
def UI_parseFloat(message: str) -> float:
    """
    Validates if the type of data entered by the user is Float.

    :param message: Message displayed to the user when requesting data.
    :return: Returns the data transformed into an Float.
    :raises: If the entered data is not an integer, the user is prompted again.
    """
    #clear()
    
    try: 
        value = float(input(f"{UI(message)}\nUser -> ")) 

        if value < 0 and not value is None:
            print(UI("You must enter a positive integer float. Please try again."))
            input()
            return UI_parseFloat(message)

        return value 

    except:
        print(UI("You must enter a valid number. Please try again."))
        input()
        return UI_parseFloat(message)

"""
Others
"""

def find_value_in_diccionary(dictionaries, value):
    """
    Finds if a specific value exists in at least one dictionary in a list.

    :param diccionaries: A list of dictionaries
    :param value: Value to find
    :return: True if the value is found in at least one dictionary, False otherwise.
    """
    return any(value in diccionary.values() for diccionary in dictionaries)


"""
Menu functions.
"""

def main_menu(option: int = 1) -> bool:
    """
    Displays the options menu and handles user selection.
    :param option: Option selected by the user.
    :return: Returns True if the user wants to continue, False if they want to exit.
    :raises: If the option is invalid, the menu is displayed again.
    """
    
    try: 
        match option:
            case 1:
                option_add()    
            case 2:
                option_search()    
            case 3:
                option_update()    
            case 4:
                option_delete()    
            case 5:
                print(UI(f"{invetory_price_with_discount()}"))
                input()
            case 6:
                print(UI(f"{invetory_price_without_discount()}"))                
                input()
            case 7:
                option_client_purchase()
            case 8:
                return False
            case _:
                print(UI("Invalid option, please try again."))
        
        # Ask the user to countinue
        continue_option = input(f"{UI("Do you want to continue? (y/n): ")}\nUser -> ").strip().lower()
        
        if continue_option == 'y':
            return True
        elif continue_option == 'n':
            return False
        else:
            print(UI("Invalid option... Restaring menu."))
            input()
            return True
    except:
        # If we have a error, ask the user to continue in the program
        try:
            continue_option = input(f"{UI("Invalid option. Do you want to exit the program? (y/n)")}\nUser -> ").strip().lower()
            
            if continue_option == 'y':
                return False
            else:
                return True
        except:
            print(UI("Invalid option. Exiting the program"))
            input()
            return False

"""
Main code.
"""

def main():
    """
    Main function that launches the inventory management program.
    Displays a welcome message and the options menu.        
    """
    
    menu = ("Welcome to the Comprehensive inventory management system.\n\n"
            "Select an option\n\n"
            "1. Add product\n"
            "2. Search product\n"
            "3. Update product\n"
            "4. Delete product\n\n"
            "5. Calculate net income\n"
            "6. Calculate gross income\n\n"
            "7. Make a purchase from a customer\n\n"
            "8. Exit program\n\n")

    #If the menu function returns True, the menu is displayed again to select a new option
    #If it returns False, the program exits
    while main_menu(UI_parseInt(menu)):
        pass


    print(UI("Thank you for using the inventory management system."))
    input()   

if __name__ == "__main__":
    main()
