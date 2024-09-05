import tkinter as tk
from tkinter import messagebox
from bson.objectid import ObjectId
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient('localhost', 27017)
db = client['mi_base_de_datos']
cars_collection = db['cars']

def create_car():
    def save_car():
        license_plate = entry_license_plate.get()
        model_id = entry_model_id.get()
        owner_id = entry_owner_id.get()

        car = {
            'license_plate': license_plate,
            'model_id': model_id,  # Guardar como string
            'owner_id': owner_id   # Guardar como string
        }

        cars_collection.insert_one(car)
        messagebox.showinfo("Información", "Carro insertado con éxito.")
        create_car_window.destroy()

    create_car_window = tk.Toplevel(root)
    create_car_window.title("Crear Carro")

    tk.Label(create_car_window, text="Placa del Carro:").pack()
    entry_license_plate = tk.Entry(create_car_window)
    entry_license_plate.pack()

    tk.Label(create_car_window, text="ID del Modelo:").pack()
    entry_model_id = tk.Entry(create_car_window)
    entry_model_id.pack()

    tk.Label(create_car_window, text="ID del Dueño:").pack()
    entry_owner_id = tk.Entry(create_car_window)
    entry_owner_id.pack()

    tk.Button(create_car_window, text="Guardar", command=save_car).pack()

def view_cars():
    cars = cars_collection.find()
    cars_window = tk.Toplevel(root)
    cars_window.title("Lista de Carros")

    for car in cars:
        car_info = f"Placa: {car['license_plate']}, Modelo: {car['model_id']}, Dueño: {car['owner_id']}"
        tk.Label(cars_window, text=car_info).pack()

def delete_car():
    def confirm_delete():
        car_id = entry_car_id.get()
        cars_collection.delete_one({'_id': ObjectId(car_id)})
        messagebox.showinfo("Información", "Carro eliminado con éxito.")
        delete_car_window.destroy()

    delete_car_window = tk.Toplevel(root)
    delete_car_window.title("Eliminar Carro")

    tk.Label(delete_car_window, text="ID del Carro a Eliminar:").pack()
    entry_car_id = tk.Entry(delete_car_window)
    entry_car_id.pack()

    tk.Button(delete_car_window, text="Eliminar", command=confirm_delete).pack()

# Ventana principal
root = tk.Tk()
root.title("CRUD de Carros")

tk.Button(root, text="Crear Carro", command=create_car).pack(pady=10)
tk.Button(root, text="Ver Carros", command=view_cars).pack(pady=10)
tk.Button(root, text="Eliminar Carro", command=delete_car).pack(pady=10)

root.mainloop()
