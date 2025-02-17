from fastapi import FastAPI  # Importing FastAPI

# Creating an instance of the FastAPI application
app = FastAPI()

# Defining a GET endpoint at the root ("/") that returns a welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

# Defining a POST endpoint to create an item
@app.post("/items")
def create_item(name: str, price: float):
    """
    Creates an item with a given name and price.
    :param name: Name of the item (string)
    :param price: Price of the item (float)
    :return: A dictionary with the item details
    """
    return {"name": name, "price": price}

# Defining a PUT endpoint to update an existing item by item_id
@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    """
    Updates an existing item based on its ID.
    :param item_id: The ID of the item to update (integer)
    :param name: Updated name of the item (string)
    :param price: Updated price of the item (float)
    :return: A dictionary with the updated item details
    """
    return {"item_id": item_id, "name": name, "price": price}

# Defining a DELETE endpoint to remove an item by item_id
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """
    Deletes an item based on its ID.
    :param item_id: The ID of the item to delete (integer)
    :return: A success message indicating item deletion
    """
    return {"message": f"Item {item_id} deleted successfully"}
