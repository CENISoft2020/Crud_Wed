from pymongo import MongoClient

# Conectar a la base de datos MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['car_database']

# Colecciones
owners_collection = db['owners']
cars_collection = db['cars']
models_collection = db['models']

# Crear un dueño
def create_owner(name, address, phone):
    owner = {
        'name': name,
        'address': address,
        'phone': phone
    }
    owners_collection.insert_one(owner)
    print("Dueño insertado con éxito.")

# Crear un carro
def create_car(license_plate, model_id, owner_id):
    car = {
        'license_plate': license_plate,
        'model_id': model_id,
        'owner_id': owner_id
    }
    cars_collection.insert_one(car)
    print("Carro insertado con éxito.")

# Crear un modelo
def create_model(name, brand, year):
    model = {
        'name': name,
        'brand': brand,
        'year': year
    }
    models_collection.insert_one(model)
    print("Modelo insertado con éxito.")

# Leer información de un dueño por ID
def read_owner(owner_id):
    owner = owners_collection.find_one({'_id': owner_id})
    if owner:
        print(owner)
    else:
        print("Dueño no encontrado.")

# Leer información de un carro por ID
def read_car(car_id):
    car = cars_collection.find_one({'_id': car_id})
    if car:
        print(car)
    else:
        print("Carro no encontrado.")

# Leer información de un modelo por ID
def read_model(model_id):
    model = models_collection.find_one({'_id': model_id})
    if model:
        print(model)
    else:
        print("Modelo no encontrado.")

# Actualizar información de un dueño
def update_owner(owner_id, name=None, address=None, phone=None):
    update_fields = {}
    if name:
        update_fields['name'] = name
    if address:
        update_fields['address'] = address
    if phone:
        update_fields['phone'] = phone
    owners_collection.update_one({'_id': owner_id}, {'$set': update_fields})
    print("Dueño actualizado con éxito.")

# Actualizar información de un carro
def update_car(car_id, license_plate=None, model_id=None, owner_id=None):
    update_fields = {}
    if license_plate:
        update_fields['license_plate'] = license_plate
    if model_id:
        update_fields['model_id'] = model_id
    if owner_id:
        update_fields['owner_id'] = owner_id
    cars_collection.update_one({'_id': car_id}, {'$set': update_fields})
    print("Carro actualizado con éxito.")

# Actualizar información de un modelo
def update_model(model_id, name=None, brand=None, year=None):
    update_fields = {}
    if name:
        update_fields['name'] = name
    if brand:
        update_fields['brand'] = brand
    if year:
        update_fields['year'] = year
    models_collection.update_one({'_id': model_id}, {'$set': update_fields})
    print("Modelo actualizado con éxito.")

# Eliminar un dueño
def delete_owner(owner_id):
    owners_collection.delete_one({'_id': owner_id})
    print("Dueño eliminado con éxito.")

# Eliminar un carro
def delete_car(car_id):
    cars_collection.delete_one({'_id': car_id})
    print("Carro eliminado con éxito.")

# Eliminar un modelo
def delete_model(model_id):
    models_collection.delete_one({'_id': model_id})
    print("Modelo eliminado con éxito.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un modelo
    create_model("Civic", "Honda", 2021)
    
    # Crear un dueño
    create_owner("Juan Perez", "123 Calle Falsa", "555-1234")
    
    # Obtener los IDs creados (en un entorno real, esto debería hacerse con una consulta)
    model_id = models_collection.find_one({'name': "Civic"})['_id']
    owner_id = owners_collection.find_one({'name': "Juan Perez"})['_id']
    
    # Crear un carro
    create_car("XYZ-123", model_id, owner_id)
    
    # Leer un carro
    read_car(cars_collection.find_one({'license_plate': "XYZ-123"})['_id'])
    
    # Actualizar un dueño
    update_owner(owner_id, phone="555-5678")
    
    # Eliminar un carro
    delete_car(cars_collection.find_one({'license_plate': "XYZ-123"})['_id'])
    
    # Eliminar un dueño
    delete_owner(owner_id)
    
    # Eliminar un modelo
    delete_model(model_id)
