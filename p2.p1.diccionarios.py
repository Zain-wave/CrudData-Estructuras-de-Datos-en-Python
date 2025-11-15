class GestorNombres:
    
    def __init__(self):
        self.nombres = ["Sebastian", "Diego", "Soto", "Zule", "Mechas"]

    def mostrar_menu(self):
        print("\n--- ¿Qué quieres hacer hoy? ---")
        print("1. Meter a alguien nuevo")
        print("2. Ver toda la lista")
        print("3. Cambiar el nombre de alguien")
        print("4. Sacar a alguien por su número")

    def ejecutar_accion(self, opcion):
        if opcion == 1:
            self._agregar_nombre()
        elif opcion == 2:
            self._mostrar_nombres()
        elif opcion == 3:
            self._cambiar_nombre()
        elif opcion == 4:
            self._eliminar_nombre()
        else:
            print("Mmm, esa opción no la conozco. Elige del 1 al 4, por favor.")

    def _agregar_nombre(self):
        if (nuevo_nombre := input("¿A quién quieres meter? ").strip()) in self.nombres:
            print(f"¡Ojo! '{nuevo_nombre}' ya está aquí. No valen duplicados.")
        elif nuevo_nombre == "":
            print("¡Escribe un nombre de verdad, por favor!")
        else:
            self.nombres.append(nuevo_nombre)
            print(f"¡Bien! '{nuevo_nombre}' se une al equipo.")
            print("Así quedó la lista:", self.nombres)

    def _mostrar_nombres(self):
        print("\n--- ¡Mira quién anda por aquí! ---")
        
        if not self.nombres:
            print("Uy, la lista está vacía. ¡Qué tristeza!")
        else:
            for i in range(len(self.nombres)):
                print(f"{i+1}. {self.nombres[i]}")

    def _cambiar_nombre(self):
        posicion_str = input(f"¿Qué número quieres cambiar? (del 1 al {len(self.nombres)}): ").strip()
        
        if posicion_str.isdigit() and 1 <= (posicion := int(posicion_str)) <= len(self.nombres):
            if (nuevo_nombre := input(f"¿Cómo se llama ahora la persona en el número {posicion} ({self.nombres[posicion-1]})? ").strip()) in self.nombres:
                print(f"¡Eh! '{nuevo_nombre}' ya lo tenemos. Busca otro nombre.")
            elif nuevo_nombre == "":
                print("¡No lo dejes vacío!")
            else:
                self.nombres[posicion - 1] = nuevo_nombre
                print(f"¡Listo! El número {posicion} ahora es '{nuevo_nombre}'.")
                print("Así quedó la lista:", self.nombres)
        else:
            print("Ese número no existe en la lista o no es un número. Fíjate bien.")

    def _eliminar_nombre(self):
        posicion_str = input(f"Dime el número (del 1 al {len(self.nombres)}) de la persona que se va: ").strip()
        
        if posicion_str.isdigit() and 1 <= (posicion := int(posicion_str)) <= len(self.nombres):
            nombre_eliminado = self.nombres.pop(posicion - 1)
            print(f"¡Adiós! '{nombre_eliminado}' se fue del número {posicion}.")
            print("Así quedó la lista:", self.nombres)
        else:
            print("Ese número está fuera de rango o no es un número. ¿Contaste bien?")


gestor = GestorNombres()

print("¡Hola! La lista inicial de gente es:", gestor.nombres)

gestor.mostrar_menu()
opcion_str = input("Dime el número de tu elección: ")

if opcion_str.isdigit():
    opcion = int(opcion_str)
else:
    opcion = 0
    
gestor.ejecutar_accion(opcion)