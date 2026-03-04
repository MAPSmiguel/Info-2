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
    def ingresarPaciente(self, paciente:Paciente):
        self.__listado.append(paciente)
    def numeroPacientes(self):
        print(f'El número de pacientes es: {len(self.__listado)}')
    def datosPaciente(self, cedula:int):
        for paciente in self.__listado:
            if paciente.getCedula() == cedula:
                return paciente
        print('Paciente no encontrado.')

def main():
    sistema = Sistema()
    while True:
        opcion = int(input('Ingrese una opción (1: Ingresar paciente, 2: Número de pacientes, 3: Datos de paciente, 4: Salir): '))
        if opcion == 1:
            print('A continuación se solicitarán los datos del paciente.')
            nombre = input('Ingrese el nombre del paciente: ')
            cedula = int(input('Ingrese la cédula del paciente: '))
            genero = input('Ingrese el género del paciente: ')
            servicio = input('Ingrese el servicio requerido por el paciente: ')
            paciente = Paciente()
            paciente.setNombre(nombre)
            paciente.setCedula(cedula)
            paciente.setGenero(genero)
            paciente.setServicio(servicio)
            sistema.ingresarPaciente(paciente)
        elif opcion == 2:
            sistema.numeroPacientes()
        elif opcion == 3:
            cedula = int(input('Ingrese la cédula del paciente a buscar: '))
            paciente = sistema.datosPaciente(cedula)
            print(f'Nombre: {paciente.getNombre()}')
            print(f'Cédula: {paciente.getCedula()}')
            print(f'Género: {paciente.getGenero()}')
            print(f'Servicio: {paciente.getServicio()}')
        elif opcion == 4:
            break
        else:
            print('Opción no válida. Intente nuevamente.')

if __name__ == '__main__':
    main()