import pymongo

# Conectar a MongoDB (asegúrate de tener MongoDB corriendo localmente)
cliente = pymongo.MongoClient("localhost", 27017)

# Crear la base de datos "matriculas"
db = cliente["matriculas"]

# Crear colecciones para matriculas de vehículos y alumnos
coleccion_vehiculos = db["matriculas_vehiculos"]
coleccion_alumnos = db["matriculas_alumnos"]

# Datos de ejemplo para matrículas de vehículos y alumnos
datos_vehiculos = [
    {"tipo": "coche", "matricula": "ABC123", "propietario": "Juan"},
    {"tipo": "moto", "matricula": "XYZ789", "propietario": "María"},
    {"tipo": "camión", "matricula": "DEF456", "propietario": "Pedro"}
]
datos_alumnos = [
    {"nombre": "Ana", "apellido": "Gómez", "matricula": "20230001"},
    {"nombre": "Carlos", "apellido": "Pérez", "matricula": "20230002"},
    {"nombre": "Luisa", "apellido": "Martínez", "matricula": "20230003"}
]
# Insertar datos de vehículos y alumnos en las colecciones
coleccion_vehiculos.insert_many(datos_vehiculos)
coleccion_alumnos.insert_many(datos_alumnos)
# Mostrar los datos por consola
print("Matrículas de vehículos:")
for vehiculo in coleccion_vehiculos.find():
    print(vehiculo)

print("\nMatrículas de alumnos:")
for alumno in coleccion_alumnos.find():
    print(alumno)