    # Actividad de Completar - Programación Orientada a Objetos
    # Completa los espacios marcados con ______ según las instrucciones

    # PASO 1: Define una clase base llamada 'Vehiculo' con un constructor que reciba marca y modelo
    class ______:
        def _____(_, ______, ______):
            self.marca = marca
            self.modelo = modelo
            self.__encendido = False  # Variable privada para encapsulamiento
        
        # PASO 2: Define un método para encender el vehículo que cambie el estado del atributo '__encendido'
        def encender(self):
            ______
            print(f"{self.marca} {self.modelo} ha sido encendido")
        
        # PASO 3: Se define un método abstracto para mover el vehículo (esta implementado por las subclases)
        def mover(self):
            raise NotImplementedError("Este método debe ser implementado por la subclase")
        
        # PASO 4: Retorna un mensaje que diga "Esta es la clase base para todos los vehículos"
        @staticmethod
        def info_clase():
            return _____
        
        # PASO 5: Implementa el método especial __str__ para mostrar información del vehículo
        def _____(_):
            return f"Vehículo: {self.marca} {self.modelo} - Encendido: {self.__encendido}"

    # PASO 6: Crea una clase Coche que herede de Vehiculo
    class _____(_):
        def _____(_, ______, ______, ______):
            # PASO 7: Llama al constructor de la clase padre
            _____.__(_, ______)
            self.num_puertas = num_puertas
            self.__kilometraje = 0  # Variable privada
        
        # PASO 8: Implementa el método mover para incrementar el kilometraje
        def mover(self, km):
            ______
            print(f"El coche {self.marca} {self.modelo} se ha movido {km} km")
        
        # PASO 9: Aplica polimorfismo sobrescribiendo el método encender
        def encender(self):
            ______
            print(f"El coche {self.marca} {self.modelo} está listo para conducir")
        
        # PASO 10: Crea un metodo que llame el atributo '__kilometraje'
        @property
        def kilometraje(self):
            return _____
        
        # PASO 11: Retorna el tipo de transporte
        @staticmethod
        def tipo_vehiculo():
            return ___

    # PASO 12: Crea una clase Moto que herede de Vehiculo
    class _____(_):
        def ______(self, marca, modelo, cilindraje):
            ______
            self.cilindraje = cilindraje
        
        # PASO 13: Implementa el método mover para la moto
        def mover(self, km):
            print(f"La moto {self.marca} {self.modelo} ha recorrido {km} km")
        
        # PASO 14: Aplica polimorfismo en el método encender
        def encender(self):
            ______
            print(f"La moto {self.marca} {self.modelo} está encendida y rugiendo")

    # PASO 15: Demostración de polimorfismo - completa la función
    def probar_vehiculo(vehiculo):
        vehiculo.encender()
        vehiculo.mover(50)
        print(vehiculo)
        print("---")

    # PASO 16: Crea instancias y prueba el código
    if ______ == ______:
        # Crear instancias
        mi_coche = ______("Toyota", "Corolla", 4)
        mi_moto = ______("Honda", "CBR", 600)
        
        # Probar polimorfismo
        ______(mi_coche)
        ______(mi_moto)
        
        # Probar encapsulamiento intentando acceder directamente a __kilometraje
    # Esto debería generar un error
    # print(mi_coche.__kilometraje)
    
    # En su lugar, usamos el getter
    print(f"Kilometraje del coche: {___} km")
    
    # Probar métodos estáticos
    print(___.info_clase())
    print(___.tipo_vehiculo())
