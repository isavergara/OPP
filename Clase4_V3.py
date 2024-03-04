#clase definida para representar pacientes del sistema
class Paciente:
    #constructos de la clase paciente
     # Encapsulamiento Los atributos están privados
    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
#métodos getters
        
    def verNombre(self):
        return self.__nombre 
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verServicio(self):
        return self.__servicio 
#métodos setters para asignar valores
    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarCedula(self,c):
        self.__cedula = c 
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarServicio(self,s):
        self.__servicio = s
#clase sistema para manejar info de pacientes
class Sistema:  
    #constructor de la clase  
    def __init__(self):
        self.__lista_pacientes = [] 
#metodos y acciones
    def verificarPaciente(self,cedula):
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():

                return True 
        return False

    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac)
        return True
#Polimorfismo, este método puede buscar pacientes por cédula o por nombre
    def verDatosPaciente(self, identifier):
        if isinstance(identifier, int):
            # Search by ID
            for p in self.__lista_pacientes:
                if identifier == p.verCedula():
                    return p
            return None
        else:
            # Search by name
            results = []
            for p in self.__lista_pacientes:
                if p.verNombre().startswith(identifier):
                    results.append(p)
            return results

    def verDatosPacienteNombre(self, nombre):
        results = []
        for p in self.__lista_pacientes:
            if p.verNombre().lower().startswith(nombre.lower()):
                results.append(p)
        return results

    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes")
def main():
    sis = Sistema() 
    #probemos lo que llevamos programado
    while True:
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente por cedula, \n3 ver Paciente por nombre\n\t--> ")) 

        if opcion == 1:
            print("A continuacion se solicitaran los datos ...") 
            #1. Se solicitan los datos
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                # 2. se crea un objeto Paciente
                pac = Paciente() 
                # como el paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                #3. se almacena en la lista que esta dentro de la clase sistema
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
        elif opcion == 2:
            #1. solicito la cedula que quiero buscar
            c = int(input("Ingrese la cédula de la paciente a buscar: ")) 
            #le pido al sistema que me devuelva en la variable p al paciente que tenga
            #la cedula c en la lista
            p = sis.verDatosPaciente(c) 
            #2. si encuentro al paciente imprimo los datos
            if p != None:
                print("Nombre: " + p.verNombre()) 
                print("Cedula: " + str(p.verCedula())) 
                print("Genero: " + p.verGenero()) 
                print("Servicio: " + p.verServicio()) 
            else:
                print("No existe un paciente con esa cedula") 
        elif opcion == 3:
            nombre = input("Ingrese el nombre de la paciente a buscar (puede ser completo o como recuerde): ")
            #le pido al sistema que me devuelva en la variable p los pacientes que inicien con el nombre dado
            p = sis.verDatosPacienteNombre(nombre)
            #2. si encuentro al paciente imprimo los datos
            if p != None:
                for paciente in p:
                    print("Nombre: " + paciente.verNombre()) 
                    print("Cedula: " + str(paciente.verCedula())) 
                    print("Genero: " + paciente.verGenero()) 
                    print("Servicio: " + paciente.verServicio()) 
                    print()
            else:
                print("No existe un paciente con ese nombre") 
        elif opcion !=0:
            continue 
        else:
            break 

#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main()
