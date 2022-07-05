import requests
from Airport import Airport
from Country import Country
from Employee import Employee
from Language import Language

def leerArchivo():
    print("Tratando de leer el archivo...")
    try:
        archivo = open("Clientes.txt", "r")
        lineas = archivo.readlines()
        valores = []
        for linea in lineas:
            nombre, apellido, pais, idioma, aeropuerto = linea.strip().split(",")
            valores.append({"nombre": nombre, "apellido":apellido, "pais":pais, "idioma":idioma, "aeropuerto":aeropuerto})
        archivo.close()
        print("Se recuperon la información correctamente")
        return valores
    except FileNotFoundError as err:
        print("Error. ",err)
    except:
        print("Ocurrio un error al realizar la operación")

def enviarPeticion():

    try:
        api_url = "http://localhost:8080/apiv1/empleados/add"

        empleados = leerArchivo()

        for empleado in empleados:
            employee = Employee(empleado["nombre"].strip(), empleado["apellido"].strip())
            language = Language(empleado["idioma"].strip())
            country = Country(empleado["pais"].strip())
            airport = Airport(empleado["aeropuerto"].strip())

            employeeData = {
                "surname": employee.getSurname(),
                "firstname": employee.getFirstname(),
                "employeeLanguages": [
                    {
                        "code": language.getCode(),
                        "name": language.getName()
                    }
                ],
                "employeeCountry":
                {
                    "code": country.getCode(),
                    "name": country.getName(),
                    "airports": [
                        {
                            "name": airport.getName()
                        }
                    ]
                }
            }

            response = requests.post(api_url, json=employeeData)
            print("Repuesta en formato JSON: ", response.json())
    except:
        print("(Error). Ocurrio un error al tratar de realizar la operación")

enviarPeticion()