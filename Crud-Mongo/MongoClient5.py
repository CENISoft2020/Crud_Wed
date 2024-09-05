import tkinter as tk
from tkinter import messagebox
from bson.objectid import ObjectId
from pymongo import MongoClient

# Conexión a MongoDB
# Se crea una instancia del cliente MongoClient para conectarse a la base de datos de MongoDB que está corriendo en 'localhost' en el puerto 27017.
client = MongoClient('localhost', 27017)

# Selección de la base de datos 'mi_base_de_datos' en el cliente MongoDB.
db = client['car_database']

# Selección de la colección 'cars' dentro de la base de datos, donde se almacenarán los documentos relacionados con los carros.
cars_collection = db['cars']

def create_car():
    # Función para guardar un nuevo carro en la base de datos.
    def save_car():
        # Obtiene los valores ingresados en los campos de texto.
        license_plate = entry_license_plate.get()
        model_id = entry_model_id.get()
        owner_id = entry_owner_id.get()

        # Crea un diccionario que representa el nuevo documento a insertar en la colección.
        car = {
            'license_plate': license_plate,
            'model_id': model_id,  # Se guarda como string, sin conversión a ObjectId.
            'owner_id': owner_id   # Se guarda como string, sin conversión a ObjectId.
        }

        # Inserta el nuevo documento en la colección 'cars'.
        cars_collection.insert_one(car)

        # Muestra un mensaje de éxito y cierra la ventana de creación.
        messagebox.showinfo("Información", "Carro insertado con éxito.")
        create_car_window.destroy()

    # Crea una nueva ventana para la creación de un carro.
    create_car_window = tk.Toplevel(root)
    create_car_window.title("Crear Carro")

    # Añade widgets para ingresar los datos del carro.
    tk.Label(create_car_window, text="Placa del Carro:").pack()
    entry_license_plate = tk.Entry(create_car_window)
    entry_license_plate.pack()

    tk.Label(create_car_window, text="ID del Modelo:").pack()
    entry_model_id = tk.Entry(create_car_window)
    entry_model_id.pack()

    tk.Label(create_car_window, text="ID del Dueño:").pack()
    entry_owner_id = tk.Entry(create_car_window)
    entry_owner_id.pack()

    # Añade un botón para guardar el carro, que llama a la función save_car cuando se presiona.
    tk.Button(create_car_window, text="Guardar", command=save_car).pack()

def view_cars():
    # Función para mostrar todos los carros en la base de datos.
    cars = cars_collection.find()  # Obtiene todos los documentos de la colección 'cars'.
    
    # Crea una nueva ventana para mostrar la lista de carros.
    cars_window = tk.Toplevel(root)
    cars_window.title("Lista de Carros")

    # Recorre todos los carros y muestra cada uno en la ventana.
    for car in cars:
        # Formatea la información del carro en una cadena.
        car_info = f"Placa: {car['license_plate']}, Modelo: {car['model_id']}, Dueño: {car['owner_id']}"
        # Crea un widget de etiqueta para mostrar la información del carro.
        tk.Label(cars_window, text=car_info).pack()

def delete_car():
    # Función para eliminar un carro de la base de datos.
    def confirm_delete():
        # Obtiene el ID del carro a eliminar.
        car_id = entry_car_id.get()
        
        # Elimina el documento con el ID especificado de la colección 'cars'.
        cars_collection.delete_one({'_id': ObjectId(car_id)})

        # Muestra un mensaje de éxito y cierra la ventana de eliminación.
        messagebox.showinfo("Información", "Carro eliminado con éxito.")
        delete_car_window.destroy()

    # Crea una nueva ventana para eliminar un carro.
    delete_car_window = tk.Toplevel(root)
    delete_car_window.title("Eliminar Carro")

    # Añade widgets para ingresar el ID del carro a eliminar.
    tk.Label(delete_car_window, text="ID del Carro a Eliminar:").pack()
    entry_car_id = tk.Entry(delete_car_window)
    entry_car_id.pack()

    # Añade un botón para eliminar el carro, que llama a la función confirm_delete cuando se presiona.
    tk.Button(delete_car_window, text="Eliminar", command=confirm_delete).pack()

# Ventana principal
# Crea la ventana principal de la aplicación.
root = tk.Tk()
root.title("CRUD de Carros")

# Añade botones a la ventana principal para las diferentes operaciones CRUD.
tk.Button(root, text="Crear Carro", command=create_car).pack(pady=10)
tk.Button(root, text="Ver Carros", command=view_cars).pack(pady=10)
tk.Button(root, text="Eliminar Carro", command=delete_car).pack(pady=10)

# Inicia el bucle principal de la interfaz gráfica.
root.mainloop()