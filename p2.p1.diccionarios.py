class GestorInventario:

    def __init__(self):
        self.inventario = {
            "Teclado mecánico": 85.50,
            "Ratón inalámbrico": 30.00,
            "Monitor 27 pulgadas": 250.99,
            "Disco SSD 1TB": 65.75
        }

    def _mostrar_resumen(self):
        total_productos = len(self.inventario)
        
        if total_productos > 0:
            suma_precios = 0
            for precio in self.inventario.values():
                suma_precios += precio
            
            promedio_precios = suma_precios / total_productos
            
            print("\n--- Resumen del Inventario ---")
            print(f"Total de productos en stock: {total_productos}")
            print(f"El precio promedio de todos los artículos es: ${promedio_precios:.2f}")
        else:
            print("\nEl inventario está vacío. No hay precios para promediar.")

    def mostrar_menu(self):
        print("\n--- ¿Qué quieres hacer con el inventario? ---")
        print("1. Agregar un producto nuevo")
        print("2. Consultar precio de un producto")
        print("3. Modificar precio de un producto")
        print("4. Eliminar un producto")

    def ejecutar_accion(self, opcion):
        if opcion == 1:
            self._agregar_producto()
        elif opcion == 2:
            self._consultar_precio()
        elif opcion == 3:
            self._modificar_precio()
        elif opcion == 4:
            self._eliminar_producto()
        else:
            print("Elige del 1 al 4, por favor.")
            
        self._mostrar_resumen()

    def _agregar_producto(self):
        if (nuevo_producto := input("Dime el nombre del producto: ").strip()) in self.inventario:
            print(f"¡Ojo! '{nuevo_producto}' ya está en el inventario.")
        elif nuevo_producto == "":
            print("¡No puedes agregar un nombre vacío!")
        else:
            precio_str = input(f"¿Qué precio tiene '{nuevo_producto}'? (Ej. 10.50): ").strip()
            
            if (precio_str.replace('.', '', 1)).isdigit():
                self.inventario[nuevo_producto] = float(precio_str)
                print(f"¡Genial! '{nuevo_producto}' agregado con precio ${float(precio_str):.2f}.")
            else:
                print("El precio que ingresaste no parece un número válido. No se agregó nada.")

    def _consultar_precio(self):
        if (producto_consultar := input("Dime el producto que quieres buscar: ").strip()) in self.inventario:
            precio = self.inventario[producto_consultar]
            print(f"El precio de '{producto_consultar}' es: ${precio:.2f}")
        else:
            print(f"¡Ups! '{producto_consultar}' no se encuentra en el inventario.")

    def _modificar_precio(self):
        if (producto_modificar := input("¿Qué producto quieres actualizar? ").strip()) not in self.inventario:
            print(f"No puedo modificar '{producto_modificar}' porque no existe.")
        else:
            precio_actual = self.inventario[producto_modificar]
            print(f"El precio actual de '{producto_modificar}' es: ${precio_actual:.2f}")
            nuevo_precio_str = input("Dime el nuevo precio (Ej. 10.50): ").strip()
            
            if (nuevo_precio_str.replace('.', '', 1)).isdigit():
                self.inventario[producto_modificar] = float(nuevo_precio_str)
                print(f"¡Precio actualizado! '{producto_modificar}' ahora cuesta: ${float(nuevo_precio_str):.2f}.")
            else:
                print("El precio que ingresaste no parece un número válido. No se realizó el cambio.")

    def _eliminar_producto(self):
        if (producto_eliminar := input("Dime el producto que quieres eliminar: ").strip()) in self.inventario:
            del self.inventario[producto_eliminar]
            print(f"¡Hecho! '{producto_eliminar}' ha sido eliminado del inventario.")
        else:
            print(f"No puedo eliminar '{producto_eliminar}' porque no lo encuentro.")

gestor = GestorInventario()

print("Inventario inicial es:", gestor.inventario)

gestor.mostrar_menu()
opcion_str = input("Dime el número de tu elección: ")

if opcion_str.isdigit():
    opcion = int(opcion_str)
else:
    opcion = 0
    
gestor.ejecutar_accion(opcion)