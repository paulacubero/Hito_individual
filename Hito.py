class Persona:
    def __init__(self) -> None:  # datos de entrada
        self.nombre = input('¿Cómo te llamas? ')
        self.numeroFalse = True  # variable de control
        while self.numeroFalse:
            try:
                self.telefono = int(input('¿Cual es tu teléfono? ')) # para que el usuario sepa que solo puede poner números
                self.numeroFalse = False
            except:
                print('Introduce solo numeros por favor: ')

        self.nif = input('¿Cual es tu NIF? ')
        self.correo = input('¿Cual es tu correo electrónico? ')
        self.dirección = input('¿Cual es tu dirección? ')
        self.pais = input('¿Cual es tu país de residencia? ')
        self.carrito = []  # en el carrito se almacenan los productos seleccionados
        print(f'\nHola {self.nombre.capitalize()}, has introducido los siguientes datos:\nTeléfono: {self.telefono}, NIF: {self.nif.upper()}, coreo: {self.correo.lower()}, dirección: {self.dirección.capitalize()}, país de residencia: {self.pais.capitalize()}\n') #datos de salida
        if self.pais.strip().lower() == 'españa': # if - else para saber que IVA aplicar, si el de España o el de un país.
            self.impuesto = 0.21
        else:
            self.impuesto = 0.35

    def compra(self): 
        totalItems = 0
        for item in self.carrito:
            totalItems += item  # = totalItems = totalItems + item
        totalCompra = totalItems + (totalItems * self.impuesto)
        confirmacion = input(
            f'\nEl precio final de compra con impuestos es {round(totalCompra, 2)} €\n Desea confirmar el pedido? y/n ') 
        if confirmacion.lower() == 'y':
            print(
                f'\nGracias por su pedido!\nSe ha mandado un sms de confirmación de pago al teléfono {self.telefono} y un pdf con la factura del pedido al correo {self.correo}') #datos de salida
        else:
            print('\nLe esperamos en otro momento') 
cliente = Persona() #creamos el objeto cliente que recoge la información de la clase persona 



class Producto(Persona): # Herencia
    def seleccion(Persona):
        continua = True
        productos = {'1 camisa': 15.95, '2 pantalón': 24.95, '3 camiseta': 12,
                     '4 abrigo': 50.50, '5 chaqueta': 30.15, '6 zapatillas': 70} #datos de salida

        while continua:
            print('\nPodructos:\n')
            for item, precio in productos.items():
                print(item, precio)
            # declaro la variable fuera del for-in para validar si existe o no el producto
            noExisteProducto = True
            # pedimos al cliente que seleccione el producto
            select = input(
                '\nseleccione un producto introduciento su número: ')
            for item, precio in productos.items():
                if select in item:  # comprobamos si existe el producto
                    noExisteProducto = False
                    # si existe el producto lo agregamos al carrito
                    Persona.carrito.append(precio)
            if noExisteProducto:  # en caso de que no exista el producto informamos al cliente
                print(
                    '\nNo disponemos de ese producto, por favor introduzca solo un número de la lista')
            totalItems = 0
            for item in Persona.carrito:
                totalItems += item
            # variable de control
            inputIncorrecto = True
            # while
            while inputIncorrecto:
                quiereContinuar = input(
                    f'\nTu compra asciende a {round(totalItems,2)} € sin impuestos, Quieres seguir comprando? y/n: ')
                if quiereContinuar.lower() == 'y':
                    inputIncorrecto=False
                    continua = True
                    break
                elif quiereContinuar.lower() == 'n':
                    inputIncorrecto=False
                    continua = False
                    break
                else:
                    print('Por favor escriba solo y o n')# para que el usuario sepa que solo puede poner 'y' o 'n'
                    inputIncorrecto = True


class Comercio: # recopila la información y llama a las clases anteriores.
    def compra(self): # dentro del método compra 
        print('\nBienvenido a nuestro gestor de pedidos\n')
        # cliente = Persona() #aquí estaba antes el objeto clinte 
        print('Comencemos con la compra\n')
        Producto.seleccion(cliente) # almacena la información que ha escogido el cliente en la clase Producto, mediante el metodo de selección.
        cliente.compra() # invocamos el método compra en cliente.


comercioRopa = Comercio() # se crea el objeto comercioRopa para que recoja toda la información de la clase comercio
comercioRopa.compra() # invocamos el método compra en comercioRopa


