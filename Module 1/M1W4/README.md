Test M1 

Título: Comprehensive Inventory and Sales Management System with Dynamic Reports

Description:

As the digital manager of a national bookstore, you need a robust system that not only records sales and products, 
but also generates detailed reports, applies customer discounts, aggregates statistics by author, and evaluates inventory performance based on sales.

Essential Features

1. Inventory management

    Added functions to add, read, update and delete products.
    The product dict structure is:

    product = {
        "title": str,
        "autor": str,
        "category": str,
        "price": float,
        "stock": int 
    } 

2. Sales registration and consultation

    Allows you to record product sales, associating: customer, product sold, quantity, date, and discount (if applicable).
    This is by a fuctiont called option_client_purchase

    The stucture of the clients and sales is: 
    clients =[
        
    ]
    
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
    Every new client can purchase automatically

3. Report module

    Function to show the most purchased products
    Function to generate a report of total sales grouped by author.
    Functions to calculate net and gross income (with and without discounts).

Contains a main menu to perform all operations





