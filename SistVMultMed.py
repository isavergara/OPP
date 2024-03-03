from datetime import datetime
#en clses medicamneto y mascota todos los detalles importantes están protegidos y solo se ven o se cambian por medio
# de funciones especiales llamadas "getter" y "setter". Esto es como tener una caja fuerte donde guardas tus cosas 
#más valiosas, y solo tú puedes abrir o cerrar la caja fuerte usando una llave especial.
#Definición de clase medicamento
class Medicamento:
    #construtor de la clase
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    #getters
    #los getters son como ventanas a través de las cuales puedes mirar lo que hay dentro de la caja fuerte sin abrir la caja misma.     
    def verNombre(self):
        return self.__nombre 
    
    def verDosis(self):
        return self.__dosis 
    #setters
    #Los "setters" son como puertas pequeñas por las que puedes introducir nuevas cosas en la caja sin abrirla por completo
    #así,se puede ver lo que hay dentro y cambiar cosas si es necesario, manteniendo todo seguro.
    def asignarNombre(self, med):
        self.__nombre = med 
    
    def asignarDosis(self, med):
        self.__dosis = med 
#definición de clase mascota
class Mascota:
    #constructor
    def __init__(self):
        self.__nombre = ""
        self.__historia = 0
        self.__tipo = ""
        self.__peso = ""
        self.__fecha_ingreso = None
        self.__lista_medicamentos = []
     #getters   
    def verNombre(self):
        return self.__nombre
    
    def verHistoria(self):
        return self.__historia
    
    def verTipo(self):
        return self.__tipo
    
    def verPeso(self):
        return self.__peso
    
    def verFecha(self):
        return self.__fecha_ingreso.strftime('%d/%m/%Y') if self.__fecha_ingreso else None
    
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
    #setters
    def asignarNombre(self, n):
        self.__nombre = n
    
    def asignarHistoria(self, nh):
        self.__historia = nh
    
    def asignarTipo(self, t):
        self.__tipo = t
    
    def asignarPeso(self, p):
        self.__peso = p
    #método setter creado para validacion
    def asignarFecha(self, fecha):
        try:
            self.__fecha_ingreso = datetime.strptime(fecha, '%d/%m/%Y')
        except ValueError as e:
            print("Error: La fecha debe estar en formato dd/mm/aaaa.")
            return False
        return True
    
    #setters
    def asignarLista_Medicamentos(self, n):
        self.__lista_medicamentos = n 
#definimos clase sistema
class sistemaV:
    #comnstructor de clase
    def __init__(self):
        self.__caninos = {}
        self.__felinos = {}
        self.__lista_mascotas = []
#polimorfismo y herencia
# los métodos para agregar mascotas, ya sea un perro o un gato, pueden trabajar con cualquier tipo de mascota sin 
# necesidad de camiar el codigo, como tener una llave que puede abrir varios tipos de cerradura.                        
#Diferentes métodos para agregar e interactuar 
    def agregar_canino(self, mascota):
        if mascota.verHistoria() in self.__caninos:
            print("Ya existe un canino con esa historia clínica.")
        else:
            self.__caninos[mascota.verHistoria()] = mascota
            self.__lista_mascotas.append(mascota)

    def agregar_felino(self, mascota):
        if mascota.verHistoria() in self.__felinos:
            print("Ya existe un felino con esa historia clínica.")
        else:
            self.__felinos[mascota.verHistoria()] = mascota
            self.__lista_mascotas.append(mascota)

    def verificarExiste(self, historia, tipo_mascota):
        if tipo_mascota == "canino":
            return historia in self.__caninos
        elif tipo_mascota == "felino":
            return historia in self.__felinos
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self, mascota):
        if mascota.verTipo() == "canino":
            self.agregar_canino(mascota)
        elif mascota.verTipo() == "felino":
            self.agregar_felino(mascota)

    def verFechaIngreso(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)
                return True  # eliminado con exito
        return False 

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu = int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu == 1:  # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia = int(input("Ingrese la historia clínica de la mascota: "))
            # Solicitar el tipo de mascota antes de usarlo
            tipo = input("Ingrese el tipo de mascota (felino o canino): ")
            if servicio_hospitalario.verificarExiste(historia, tipo) == False:
                nombre = input("Ingrese el nombre de la mascota: ")
                peso = int(input("Ingrese el peso de la mascota: "))
                fecha_valida = False
                while not fecha_valida:
                    fecha = input("Ingrese la fecha de ingreso de la mascota (dd/mm/aaaa): ")
                    mascota = Mascota()  # Creamos una nueva instancia de Mascota
                    fecha_valida = mascota.asignarFecha(fecha)  # Llamamos al método en la instancia de Mascota
                    if not fecha_valida:
                        print("Error: La fecha debe estar en formato dd/mm/aaaa.")
                nm = int(input("Ingrese cantidad de medicamentos: "))
                medicamentos_ingresados = 0
                lista_med = []
                nombre_medicamentos_ingresados = set()

                while medicamentos_ingresados < nm:
                    nombre_medicamento = input("Ingrese el nombre del medicamento: ")
                    if nombre_medicamento not in nombre_medicamentos_ingresados:
                        dosis = int(input("Ingrese la dosis: "))
                        medicamento = Medicamento()
                        medicamento.asignarNombre(nombre_medicamento)
                        medicamento.asignarDosis(dosis)
                        lista_med.append(medicamento)
                        nombre_medicamentos_ingresados.add(nombre_medicamento)
                        medicamentos_ingresados += 1
                        print("Medicamento agregado con éxito")
                    else:
                        print("Ya has agregado un medicamento con ese nombre. Intente nuevamente.")

                mas = Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)
            else:
                print("Ya existe la mascota con el número de historia clínica.")

        elif menu == 2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu == 3: # Ver número de mascotas en el servicio 
            numero = servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu == 4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con éxito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu == 6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, inténtelo nuevamente...")

if __name__ == '__main__':
    main()


            

                

