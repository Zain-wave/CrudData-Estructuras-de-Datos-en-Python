class CatalogoEstatico:

    def __init__(self):
        self.catalogo = (45, 12, 88, 5, 60, 21)

    def _mostrar_operacion(self, mensaje, lista_temporal):
        print(f"\n--- Mira cómo quedaría al: {mensaje} ---")
        print(f"Esta sería la tupla nueva: {tuple(lista_temporal)}")
        print(f"Pero no te olvides, la tupla original sigue intacta: {self.catalogo}")

    def mostrar_menu(self):
        print("\n--- Catálogo de Números Fijos ---")
        print("1. Simular agregar un número")
        print("2. Simular cambiar un número de sitio")
        print("3. Simular eliminar un número")
        print("4. Ver el catálogo completo y hacer el análisis")

    def ejecutar_accion(self, opcion):
        
        if opcion == 1:
            self._simular_agregar()
        elif opcion == 2:
            self._simular_reemplazar()
        elif opcion == 3:
            self._simular_eliminar()
        elif opcion == 4:
            self._mostrar_analisis()
        else:
            print("Esa opción no existe. Debes elegir del 1 al 4.")

    def _simular_agregar(self):
        if (nuevo_valor_str := input("Dame el número que quieres añadir al final: ").strip()).isdigit():
            nuevo_valor = int(nuevo_valor_str)
            
            lista_temporal = list(self.catalogo)
            lista_temporal.append(nuevo_valor)
            
            self._mostrar_operacion("AÑADIR ESTE VALOR", lista_temporal)
        else:
            print("Debes ingresar un número entero.")

    def _simular_reemplazar(self):
        
        print("Valores actuales:", self.catalogo)
        posicion_str = input(f"Dime la posición (0 a {len(self.catalogo) - 1}) que quieres modificar: ").strip()
        
        if posicion_str.isdigit() and 0 <= (posicion := int(posicion_str)) < len(self.catalogo):
            valor_actual = self.catalogo[posicion]
            nuevo_valor_str = input(f"El valor actual en esa posición es {valor_actual}. ¿Cuál es el número de reemplazo? ").strip()
            
            if nuevo_valor_str.isdigit():
                nuevo_valor = int(nuevo_valor_str)
                
                lista_temporal = list(self.catalogo)
                lista_temporal[posicion] = nuevo_valor
                
                self._mostrar_operacion("REEMPLAZAR UN VALOR", lista_temporal)
            else:
                print("El reemplazo debe ser un número entero.")
        else:
            print("No es un número válido o no existe en la tupla.")

    def _simular_eliminar(self):
        
        print("Valores actuales:", self.catalogo)
        posicion_str = input(f"Dime la posición (0 a {len(self.catalogo) - 1}) del número que quieres que desaparezca: ").strip()
        
        if posicion_str.isdigit() and 0 <= (posicion := int(posicion_str)) < len(self.catalogo):
            valor_eliminado = self.catalogo[posicion]
            
            lista_temporal = list(self.catalogo)
            lista_temporal.pop(posicion)
            
            self._mostrar_operacion(f"QUITAR VALOR ({valor_eliminado})", lista_temporal)
        else:
            print("¡Error! La posición no es un número válido o está fuera de los límites.")

    def _mostrar_analisis(self):
        print("\n--- Todos los números con su índice ---")
        
        for indice in range(len(self.catalogo)):
            print(f"En el puesto {indice}: {self.catalogo[indice]}")
        
        valor_mayor = self.catalogo[0]
        valor_menor = self.catalogo[0]
        suma_total = 0
        posicion_mayor = 0
        
        print("\n--- El Análisis Secreto ---")

        for indice in range(len(self.catalogo)):
            valor_actual = self.catalogo[indice]
            
            suma_total += valor_actual
            
            if valor_actual > valor_mayor:
                valor_mayor = valor_actual
                posicion_mayor = indice
                
            if valor_actual < valor_menor:
                valor_menor = valor_actual
        
        print(f"El número más grande de todos es: {valor_mayor}")
        print(f"El número más pequeño de todos es: {valor_menor}")
        print(f"Si los sumas todos, da: {suma_total}")
        print(f"El número más grande está en el puesto: {posicion_mayor}")

gestor = CatalogoEstatico()

print("¡Hola! La tupla estática de números es:", gestor.catalogo)

gestor.mostrar_menu()
opcion_str = input("Dime el número de tu elección: ")

if opcion_str.isdigit():
    opcion = int(opcion_str)
else:
    opcion = 0
    
gestor.ejecutar_accion(opcion)