class Paciente():
    def __init__(self):
        self.__nombre:str = ''
        self.__cedula:int = 0
        self.__genero:str = ''
        self.__servicio:str = ''
    
    def setNombre(self,n:str):
        self.__nombre = n
    def setCedula(self,n:int):
        self.__cedula = n
    def setGenero(self,n:str):
        self.__genero = n
    def setServicio(self,n:str):
        self.__servicio = n
    
    def getNombre(self)->str:
        return self.__nombre
    def getCedula(self)->int:
        return self.__cedula
    def getGenero(self)->str:
        return self.__genero
    def getServicio(self)->str:
        return self.__servicio

class Sistema():
    def __init__(self):
        self.__listado = []
    def ingresarPaciente(self):
        nombre = input('Ingrese el nombre del paciente: ')
        cedula = int(input('Ingrese la cedula del paciente: '))
        genero = input('Ingrese el genero del paciente: ')
        servicio = input('Ingrese el servicio del paciente: ')
        paciente = Paciente()
        paciente.setNombre(nombre)
        paciente.setCedula(cedula)
        paciente.setGenero(genero)
        paciente.setServicio(servicio)
        self.__listado.append(paciente)
    def numeroPacientes(self):
        return len(self.__listado)
    def datosPaciente(self):
        cedula = int(input('Ingrese la cédula a buscar: '))
        for paciente in self.__listado:
            if paciente.getCedula() == cedula:
                print(f'Nombre: {paciente.getNombre()}')
                print(f'Cédula: {paciente.getCedula()}')
                print(f'Género: {paciente.getGenero()}')
                print(f'Servicio: {paciente.getServicio()}')
                return
        print('Paciente no encontrado.')

sistema = Sistema()

while True:
    opcion = int(input('Ingrese una opción (1: Ingresar paciente, 2: Número de pacientes, 3: Datos de paciente, 4: Salir): '))
    if opcion == 1:
        sistema.ingresarPaciente()
    elif opcion == 2:
        print(f'El número de pacientes es: {sistema.numeroPacientes()}')
    elif opcion == 3:
        sistema.datosPaciente()
    elif opcion == 4:
        break
    else:
        print('Opción no válida. Intente nuevamente.')