
# esto es un metodo ya que el def esta dentro de un class, si fuera al revez seria una funcion.
class Persona: # el nombre de una clase se pone en PascalCase (palabras pegadas con la inicial de cada una en mayuscula)
    def __init__(self, id:int, nombre:str, apellido:str, edad:int) -> None:
        self.id = id
        self.nombre = nombre
        self._apellido = apellido # en python no hay protegido, pero al poner el _ lo debemos tratar como un protegido
        self.__edad = edad
    
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        if value > 0:
            self.__edad = value
    
    def saludar(self):
        print("Hola gente como va?")
    
    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.__edad} años"
    
class Empleado(Persona):
    def __init__(self, id: int, nombre: str, apellido: str, edad: int, sueldo: float) -> None:
        super().__init__(id, nombre, apellido, edad) # super seria la super clase, es la clase de la que estamos heredando (la clase padre)
        self.sueldo = sueldo

    def presentarse(self):
        cadena = super().presentarse()

        return (f"Hola soy un empleado, me llamo {self.nombre} y gano {self.sueldo} por mes") + cadena


# lista = []

persona_1 = Persona(1234, "Juan", "Perez", 34)


# lista.append(persona_1)
# lista.append(persona_2)

print(persona_1.presentarse())
print(persona_1.edad)
print(persona_1._apellido)

empleado_1 = Empleado(4545, "Valeria", "Gomez", 28, 540)

print(empleado_1.presentarse())









