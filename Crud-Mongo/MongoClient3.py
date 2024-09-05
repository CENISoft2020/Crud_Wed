from pymongo import MongoClient
from bson.objectid import ObjectId

from bson.errors import InvalidId 

# Conectar a la base de datos MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['car_database']

# Colecciones
owners_collection = db['owners']
cars_collection = db['cars']
models_collection = db['models']

# Crear un dueño
def create_owner():
    name = input("Ingrese el nombre del dueño: ")
    address = input("Ingrese la dirección del dueño: ")
    phone = input("Ingrese el teléfono del dueño: ")
    
    owner = {
        'name': name,
        'address': address,
        'phone': phone
    }
    owners_collection.insert_one(owner)
    print("Dueño insertado con éxito.")

# Crear un carro
def create_car():
    license_plate = input("Ingrese la placa del carro: ")
    model_id = input("Ingrese el ID del modelo: ")
    owner_id = input("Ingrese el ID del dueño: ")

    car = {
        'license_plate': license_plate,
        'model_id': model_id,  # Se guarda como string, sin convertir a ObjectId
        'owner_id': owner_id   # Se guarda como string, sin convertir a ObjectId
    }

    cars_collection.insert_one(car)
    print("Carro insertado con éxito.")
        
# Crear un modelo
def create_model():
    name = input("Ingrese el nombre del modelo: ")
    brand = input("Ingrese la marca del modelo: ")
    year = input("Ingrese el año del modelo: ")
    
    model = {
        'name': name,
        'brand': brand,
        'year': year
    }
    models_collection.insert_one(model)
    print("Modelo insertado con éxito.")

# Leer información de un dueño por ID
def read_owner():
    owner_id = input("Ingrese el ID del dueño: ")
    owner = owners_collection.find_one({'_id': ObjectId(owner_id)})
    if owner:
        print(owner)
    else:
        print("Dueño no encontrado.")

# Leer información de un carro por ID
def read_car():
    car_id = input("Ingrese el ID del carro: ")
    car = cars_collection.find_one({'_id': ObjectId(car_id)})
    if car:
        print(car)
    else:
        print("Carro no encontrado.")

# Leer información de un modelo por ID
def read_model():
    model_id = input("Ingrese el ID del modelo: ")
    model = models_collection.find_one({'_id': ObjectId(model_id)})
    if model:
        print(model)
    else:
        print("Modelo no encontrado.")

# Actualizar información de un dueño
def update_owner():
    owner_id = input("Ingrese el ID del dueño: ")
    name = input("Ingrese el nuevo nombre (o deje en blanco para no cambiar): ")
    address = input("Ingrese la nueva dirección (o deje en blanco para no cambiar): ")
    phone = input("Ingrese el nuevo teléfono (o deje en blanco para no cambiar): ")
    
    update_fields = {}
    if name:
        update_fields['name'] = name
    if address:
        update_fields['address'] = address
    if phone:
        update_fields['phone'] = phone
    
    owners_collection.update_one({'_id': ObjectId(owner_id)}, {'$set': update_fields})
    print("Dueño actualizado con éxito.")

# Actualizar información de un carro
def update_car():
    car_id = input("Ingrese el ID del carro: ")
    license_plate = input("Ingrese la nueva placa (o deje en blanco para no cambiar): ")
    model_id = input("Ingrese el nuevo ID del modelo (o deje en blanco para no cambiar): ")
    owner_id = input("Ingrese el nuevo ID del dueño (o deje en blanco para no cambiar): ")

    update_fields = {}

    if license_plate:
        update_fields['license_plate'] = license_plate

    if model_id:
        try:
            update_fields['model_id'] = ObjectId(model_id)
        except InvalidId:
            print(f"Error: '{model_id}' no es un ObjectId válido. No se actualizará el ID del modelo.")
    
    if owner_id:
        try:
            update_fields['owner_id'] = ObjectId(owner_id)
        except InvalidId:
            print(f"Error: '{owner_id}' no es un ObjectId válido. No se actualizará el ID del dueño.")

    try:
        cars_collection.update_one({'_id': ObjectId(car_id)}, {'$set': update_fields})
        print("Carro actualizado con éxito.")
    except InvalidId:
        print(f"Error: '{car_id}' no es un ObjectId válido. No se pudo actualizar el carro.")

# Actualizar información de un modelo
def update_model():
    model_id = input("Ingrese el ID del modelo: ")
    name = input("Ingrese el nuevo nombre (o deje en blanco para no cambiar): ")
    brand = input("Ingrese la nueva marca (o deje en blanco para no cambiar): ")
    year = input("Ingrese el nuevo año (o deje en blanco para no cambiar): ")
    
    update_fields = {}
    if name:
        update_fields['name'] = name
    if brand:
        update_fields['brand'] = brand
    if year:
        update_fields['year'] = year
    
    models_collection.update_one({'_id': ObjectId(model_id)}, {'$set': update_fields})
    print("Modelo actualizado con éxito.")

# Eliminar un dueño
def delete_owner():
    owner_id = input("Ingrese el ID del dueño: ")
    owners_collection.delete_one({'_id': ObjectId(owner_id)})
    print("Dueño eliminado con éxito.")

# Eliminar un carro
def delete_car():
    car_id = input("Ingrese el ID del carro: ")
    cars_collection.delete_one({'_id': ObjectId(car_id)})
    print("Carro eliminado con éxito.")

# Eliminar un modelo
def delete_model():
    model_id = input("Ingrese el ID del modelo: ")
    models_collection.delete_one({'_id': ObjectId(model_id)})
    print("Modelo eliminado con éxito.")

# Listar todos los dueños
def list_owners():
    owners = owners_collection.find()
    print("\nLista de Dueños:")
    for owner in owners:
        print(owner)

# Listar todos los carros
def list_cars():
    cars = cars_collection.find()
    print("\nLista de Carros:")
    for car in cars:
        print(car)

# Listar todos los modelos
def list_models():
    models = models_collection.find()
    print("\nLista de Modelos:")
    for model in models:
        print(model)

# Menú para interactuar con el CRUD
def menu():
    while True:
        print("\nCRUD de Dueños, Carros y Modelos")
        print("1. Crear dueño")
        print("2. Crear carro")
        print("3. Crear modelo")
        print("4. Leer dueño")
        print("5. Leer carro")
        print("6. Leer modelo")
        print("7. Actualizar dueño")
        print("8. Actualizar carro")
        print("9. Actualizar modelo")
        print("10. Eliminar dueño")
        print("11. Eliminar carro")
        print("12. Eliminar modelo")
        print("13. Listar todos los dueños")
        print("14. Listar todos los carros")
        print("15. Listar todos los modelos")
        print("16. Salir")

        option = input("Seleccione una opción: ")

        if option == '1':
            create_owner()
        elif option == '2':
            create_car()
        elif option == '3':
            create_model()
        elif option == '4':
            read_owner()
        elif option == '5':
            read_car()
        elif option == '6':
            read_model()
        elif option == '7':
            update_owner()
        elif option == '8':
            update_car()
        elif option == '9':
            update_model()
        elif option == '10':
            delete_owner()
        elif option == '11':
            delete_car()
        elif option == '12':
            delete_model()
        elif option == '13':
            list_owners()
        elif option == '14':
            list_cars()
        elif option == '15':
            list_models()
        elif option == '16':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()
