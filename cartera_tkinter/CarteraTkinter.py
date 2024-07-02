from tkinter import *
from tkinter import ttk, messagebox

class CarteraTkinter():
    def __init__(self):

        # Instanciar la clase Tk
        self.app = Tk()
        self.app.title("Cartera Tkinter")
        # Definir las variables con los valores que establecen el ancho y alto de la ventana principal de la aplicación respectivamente
        self.ancho_app = 400
        self.alto_app = 450
        self.app.geometry("%dx%d" % (self.ancho_app, self.alto_app))
        # Llamar al metodo centrar ventana y pasarle los argumentos de ancho y alto
        self.centrar_ventana(self.app, self.ancho_app, self.alto_app)
        self.app.resizable(False, False)
        self.app.config(bg="#001933")

        # Definir la variable valor_actual e inicializarla como una variable de control de tipo double con el valor inicial 0.0
        self.valor_actual = DoubleVar(value=0.0)
        # Definir la variable posicion_lista e inicializarla en 0 porque sera un contador
        self.posicion_lista = 0

        # Crear imagen para el título de la app
        self.img_titulo = PhotoImage(file="cartera.png")

        # Crear el título de la aplicación
        self.titulo = ttk.Label(self.app,
        text="Cartera Tkinter",
        font=("Arial", 11, "bold"),
        background="#001933",
        foreground="#e5c67a",
        width=400,
        justify="left",
        image=self.img_titulo,
        compound="left")

        # Crear imagen para el saldo actual en la app
        self.img_dinero = PhotoImage(file="dinero.png")

        # Crear la etiqueta que muestra el saldo actual de la cartera del usuario
        self.valor_saldo = ttk.Label(self.app,
        textvariable=self.valor_actual,
        font=("Arial", 20, "bold"),
        background="#001933",
        foreground="#fff",
        image=self.img_dinero,
        compound="left",)

        # Crear imagen para el botón ingresar
        self.img_ingresar = PhotoImage(file="ingresar.png")

        # Crear el botón para ingresar un valor
        self.btnIngresos = ttk.Button(self.app,
        text="Ingresar",
        image=self.img_ingresar,
        compound="left",
        command=self.ingresar)

        # Crear imagen para el botón retirar
        self.img_retirar = PhotoImage(file="retirar.png")

        # Crear el botón para retirar un valor
        self.btnRetiros = ttk.Button(self.app,
        text="Retirar",
        image=self.img_retirar,
        compound="left",
        command=self.retirar)

        self.img_movimientos = PhotoImage(file="movimientos.png")

        # Crear la etiqueta movimientos
        self.etiqueta_movimientos = ttk.Label(self.app,
        text="Movimientos",
        image=self.img_movimientos,
        compound="left",
        font=("Arial", 16, "bold"),
        background="#001933",
        foreground="#c7ddd6")

        # Crear caja lista en la que se mostrarán los movimientos de los ingresos y retiros
        self.movimientos = Listbox(self.app,
        height=8,
        borderwidth=0,
        bg="#fff",
        fg="#001933",
        activestyle="none",
        highlightcolor="#003f7f",
        highlightbackground="#003f7f",
        selectbackground="#003f7f",
        selectforeground="#fff",
        font=("Arial", 12, "bold"))

        # Crear el estilo para todos los botones de la aplicación
        self.estilo_botones = ttk.Style()
        self.estilo_botones.configure("TButton",
        foreground="#001933",
        background="#003f7f",
        font=("Arial", 16))

        # Crear el estilo para los botones cancelar
        self.estilo_btn_cancelar = ttk.Style()
        self.estilo_btn_cancelar.configure("btn_cancelar.TButton",
        foreground="red",
        background="red")

        # Establecer la posicón de los elementos mediante el gestor de posicionamiento grid
        self.titulo.grid(column=0, row=0, padx=10, columnspan=2)
        self.valor_saldo.grid(column=0, row=1, columnspan=2)
        self.btnIngresos.grid(column=0, row=2, padx=5, pady=10, ipady=10, sticky=(E, W))
        self.btnRetiros.grid(column=1, row=2, padx=10, pady=10, ipady=10, sticky=(E, W))
        self.etiqueta_movimientos.grid(column=0, row=3, columnspan=2)
        self.movimientos.grid(column=0, row=4, columnspan=2, padx=10, ipadx=10, ipady=10, sticky=(E, W))

        self.app.columnconfigure(0, weight=1)
        self.app.rowconfigure(0, weight=1)
        self.app.columnconfigure(0, weight=1)
        self.app.columnconfigure(1, weight=1)
        self.app.rowconfigure(0, weight=1)
        self.app.rowconfigure(1, weight=1)
        self.app.rowconfigure(2, weight=1)
        self.app.rowconfigure(3, weight=1)
        self.app.rowconfigure(4, weight=1)
    
        # Ejecutar la ventana
        self.app.mainloop()

    # Crear metodo para centrar las ventanas de la aplicación con respecto al tamaño de la pantalla del equipo deonde se ejecuta el programa
    def centrar_ventana(self, ventana, ancho, alto):
        # Obtener y almacenar el ancho de la ventana de la variable ancho_pantalla
        self.ancho_pantalla = ventana.winfo_screenwidth()
        # Obtener y almacenar la altura de la ventana en la variable altura_pantalla
        self.altura_pantalla = ventana.winfo_screenheight()

        # Almacenar en la variable x el cociente del ancho de la ventana obtenido y lo divide en 2
        # para restarlo al cociente obtenido entre el ancho establecido dividido en 2
        self.x = (self.ancho_pantalla // 2) - (ancho // 2)
        self.y = (self.altura_pantalla // 2) - (alto // 2)
        
        # Establecer la posición de la ventana con los valores almacenados en las variables x y y
        ventana.geometry(f"+{self.x}+{self.y}")

    # Crear el metodo ingresar
    def ingresar(self):
        # Crear ventana de dialogo para función ingresar
        self.ingresar = Toplevel()
        self.ingresar.title("Ingresar dinero")
        self.ingresar.config(bg="#e5c67a")
        self.ingresar.resizable(False, False)
        # Definir las variables con los valores que establecen el ancho y alto de la ventana de dialogo ingresar
        self.ancho_ingresar = 300
        self.alto_ingresar = 180
        self.ingresar.geometry("%dx%d" % (self.ancho_ingresar, self.alto_ingresar))
        # Llamar al metodo centrar ventana y pasarle los argumentos de ancho y alto
        self.centrar_ventana(self.ingresar, self.ancho_ingresar, self.alto_ingresar)
        
        # crear el título de la ventana emergente ingresar
        self.ingresar_titulo = ttk.Label(self.ingresar,
        text="Ingresar",
        font=("Arial", 18, "bold"),
        background="#e5c67a",
        foreground="#001933")

        # Validar que solo se ingresen caracteres de tipo númerico al campo de texto
        validate_entry = lambda text: text.isdecimal()
        # Crear el campo de texto para digitar el nuevo saldo a ingresar
        self.ingresar_valor = ttk.Entry(self.ingresar,
        font=("Arial", 18, "bold"),
        validate="key",
        justify="center",
        foreground="#001933",
        validatecommand=(self.ingresar.register(validate_entry), "%S"),)

        # Crear el botón para aceptar el valor digitado en el campo de texto
        self.ingresar_aceptar = ttk.Button(self.ingresar,
        text="Aceptar",
        command=self.aceptar_ingresos)

        # Crear el botón para cancelar el valor digitado en el campo de texto
        self.ingresar_cancelar = ttk.Button(self.ingresar,
        text="Cancelar",
        style="btn_cancelar.TButton",
        # Cerrar la ventana de dialogo ingresar
        command=self.ingresar.destroy)

        # Establecer la posicón de los elementos de la ventana de dialogo ingresar mediante el gestor de posicionamiento grid
        self.ingresar_titulo.grid(column=0, row=0, columnspan=2)
        self.ingresar_valor.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky=(E, W))
        self.ingresar_aceptar.grid(column=0, row=2, padx=10, pady=10, ipady=10, sticky=(E, W))
        self.ingresar_cancelar.grid(column=1, row=2, padx=10, pady=10, ipady=10, sticky=(E, W))

        self.ingresar.columnconfigure(0, weight=1)
        self.ingresar.rowconfigure(0, weight=1)
        self.ingresar.columnconfigure(0, weight=1)
        self.ingresar.columnconfigure(1, weight=1)
        self.ingresar.rowconfigure(0, weight=1)
        self.ingresar.rowconfigure(1, weight=1)
        self.ingresar.rowconfigure(2, weight=1)

        # Impedir abrir mas de una ventana de dialogo ingresar
        self.ingresar.grab_set()
        #Impedir cerrar la ventana principal si la ventana de dialogo ingresar esta abierta
        self.ingresar.wait_window(self.ingresar)

    # Crear el metodo retirar
    def retirar(self):
        # Crear ventana de dialogo para función retirar
        self.retirar = Toplevel()
        self.retirar.title("Retirar dinero")
        self.retirar.config(bg="#e5c67a")
        self.retirar.resizable(False, False)
        # Definir las variables con los valores que establecen el ancho y alto de la ventana de dialogo retirar
        self.ancho_retirar = 300
        self.alto_retirar = 180
        self.retirar.geometry("%dx%d" % (self.ancho_retirar, self.alto_retirar))
        # Llamar al metodo centrar ventana y pasarle los argumentos de ancho y alto
        self.centrar_ventana(self.retirar, self.ancho_retirar, self.alto_retirar)

        # crear el título de la ventana emergente retirar
        self.retirar_titulo = ttk.Label(self.retirar,
        text="Retirar",
        font=("Arial", 18, "bold"),
        background="#e5c67a",
        foreground="#001933")

        # Validar que solo se ingresen caracteres de tipo númerico al campo de texto
        validate_entry = lambda text: text.isdecimal()
        # Crear el campo de texto para digitar el nuevo saldo a retirar
        self.retirar_valor = ttk.Entry(self.retirar,
        font=("Arial", 18, "bold"),
        validate="key",
        foreground="#001933",
        justify="center",
        validatecommand=(self.retirar.register(validate_entry), "%S"),)

        # Crear el botón para aceptar el valor digitado en el campo de texto
        self.retirar_aceptar = ttk.Button(self.retirar,
        text="Aceptar",
        command=self.aceptar_retiros)

        # Crear el botón para cancelar el valor digitado en el campo de texto
        self.retirar_cancelar = ttk.Button(self.retirar,
        text="Cancelar",
        style="btn_cancelar.TButton",
        # Cerrar la ventana de dialogo retirar
        command=self.retirar.destroy)

        # Establecer la posicón de los elementos de la ventana de dialogo retirar mediante el gestor de posicionamiento grid
        self.retirar_titulo.grid(column=0, row=0, columnspan=2)
        self.retirar_valor.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky=(E, W))
        self.retirar_aceptar.grid(column=0, row=2, padx=10, pady=10, ipady=10, sticky=(E, W))
        self.retirar_cancelar.grid(column=1, row=2, padx=10, pady=10, ipady=10, sticky=(E, W))

        self.retirar.columnconfigure(0, weight=1)
        self.retirar.rowconfigure(0, weight=1)
        self.retirar.columnconfigure(0, weight=1)
        self.retirar.columnconfigure(1, weight=1)
        self.retirar.rowconfigure(0, weight=1)
        self.retirar.rowconfigure(1, weight=1)
        self.retirar.rowconfigure(2, weight=1)

        # Impedir abrir mas de una ventana de dialogo retirar
        self.retirar.grab_set()
        #Impedir cerrar la ventana principal si la ventana de dialogo retirar esta abierta
        self.retirar.wait_window(self.retirar)

    # Establecer la variable posicion_lista como global
    global posicion_lista
    # Inicializar la variable en 0 porque sera un contador
    posicion_lista = 0

    # Crear el metodo aceptar ingresos
    def aceptar_ingresos(self):
        global posicion_lista

        # Validar la longitud del valor ingresado y obtenido de la variable ingresar_valor
        # Si la longitud es diferente a 0
        if len(self.ingresar_valor.get()) != 0:
            # Establecer un nuevo valor para la etiqueta que muestra el saldo actual
            # Sumar el valor actual con el digitado en el campo de texto ingresar valor
            # Como el valor ingresado en el campo de texto es una cadena de texto, se castea a float para que se pueda sumar al valor actual
            self.valor_actual.set(self.valor_actual.get() + float(self.ingresar_valor.get()))
            # Asignar texto a la variable tipo_movimiento
            self.tipo_movimiento = "Se han ingresado "
            # Asignar el valor obtenido a la variable agregar_movimiento
            # Se castea el valor obtenido a float para que se visualice como un número decimal
            self.agregar_movimiento = float(self.ingresar_valor.get())
            # Llamar al metodo listar movimientos para mostrar el valor ingresado en la caja lista
            self.listar_movimientos()
            # El color del item de la lista en la posición actual será de color verde
            self.movimientos.itemconfigure(posicion_lista, fg="green")
            # Sumar en 1 la variable global posicion_lista
            posicion_lista += 1
            # Cerrar la ventana de dialogo ingresar
            self.ingresar.destroy()
        # De lo contrario, si la longitud es 0
        else:
            # Mostrar mensaje de advertencia
            messagebox.showinfo("Error", "No ingresó ningún valor")

    # Crear el metodo aceptar retiros
    def aceptar_retiros(self):
        global posicion_lista

        # Validar la longitud del valor ingresado y obtenido de la variable ingresar_valor
        # Si la longitud es diferente a 0
        if len(self.retirar_valor.get()) != 0:
            # Si el valor digitado en el campo de texto retirar valor es menor o igual al valor actual
            # Como el valor ingresado en el campo de texto es una cadena de texto, se castea a float para que se pueda restar al valor actual
            if float(self.retirar_valor.get()) <= self.valor_actual.get():
                # Restar al valor actual el valor obtenido del campo de texto retirar valor
                self.valor_actual.set(self.valor_actual.get() - float(self.retirar_valor.get()))
                # Asignar texto a la variable tipo_movimiento
                self.tipo_movimiento = "Se han retirado "
                # Asignar el valor obtenido a la variable agregar_movimiento
                # Se castea el valor obtenido a float para que se visualice como un número decimal
                self.agregar_movimiento = float(self.retirar_valor.get())
                # Llamar al metodo listar movimientos para mostrar el valor ingresado en la caja lista
                self.listar_movimientos()
                # El color del item de la lista en la posición actual será de color rojo
                self.movimientos.itemconfigure(posicion_lista, fg="red")
            # Si el valor digitado en el campo de texto retirar valor es mayor al valor actual
            else:
                messagebox.showinfo("Error", "Saldo insuficiente")
                # Asignar texto a la variable tipo_movimiento
                self.tipo_movimiento = "Intento de retiro fallido"
                self.agregar_movimiento = ""
                # Llamar al metodo listar movimientos para mostrar el valor ingresado en la caja lista
                self.listar_movimientos()
            # Sumar en 1 la variable global posicion_lista
            posicion_lista += 1
            # Cerrar la ventana de dialogo ingresar
            self.retirar.destroy()
        # De lo contrario, si la longitud es 0
        else:
            # Mostrar mensaje de advertencia
            messagebox.showinfo("Error", "No ingresó ningún valor")

    # Crear metodo listar movimientos
    def listar_movimientos(self):
        global posicion_lista
        # Insertar en la caja lista el tipo de movimeinto y el valor digitado en el campo de texto ingresar/retirar
        # La variable posicion_lista establece la posicion del elemento/moviemiento en la lista
        # Se castea la variable agregar_movieminto para que se concatene con la variable de texto tipo_movimiento
        self.movimientos.insert(posicion_lista, self.tipo_movimiento + str(self.agregar_movimiento))

# Crear el metodo main 
def main():
    # Instanciar la clase CarteraTkinter
    app = CarteraTkinter()
    
# Ejecutar el metodo main para ejecutar el programa
if __name__ == "__main__":
    main()