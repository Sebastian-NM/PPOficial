import tkinter
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd


#===============================================================================[PRIMERA FUNCION]========================================================================================

def abrirVentana1():
    # Window properties
    vFuncion1 = Toplevel()
    vFuncion1.title("Depreciación Lineal")
    anchoVLogin = 900
    altoVLogin = 750
    xPosicion = vFuncion1.winfo_screenwidth() // 2 - anchoVLogin // 2  # Posicionar ventana en centro de la pantalla
    yPosicion = vFuncion1.winfo_screenheight() // 2 - altoVLogin // 2  # Posicionar ventana en centro de la pantalla
    posicionPantalla = str(anchoVLogin) + "x" + str(altoVLogin) + "+" + str(xPosicion) + "+" + str(yPosicion)
    vFuncion1.geometry(posicionPantalla)
    vFuncion1['bg'] = '#FFFFFF'
    vFuncion1.resizable(0, 0)

    # Go back button
    btnCalcularLineaRecta = Button(vFuncion1, text="VOLVER", fg="#FFFFFF", bg="#1E56A0", font="Segoe 10 bold",
                                   command=vFuncion1.destroy).place(x=50, y=700)

    # Label to choose the method
    lblSeleccionarMetodo = tkinter.Label(vFuncion1, text="Seleccione el método de depreciación:", font="Segoe 13",
                                         bg="#FFFFFF")
    lblSeleccionarMetodo.place(x=45, y=90)

    # Label to explain the combobox
    lblEscogerCodigo = Label(vFuncion1, text="Seleccione el código de activo a mostrar:", font="Segoe 13", bg="#FFFFFF")
    lblEscogerCodigo.place(x=45, y=45)

    #Function that fills the combo box with the codes
    def crearListaComboBox():
        archivo = pd.read_html("datos.html")
        cuadroInformacion = archivo[0]
        lista = []
        indice = 1
        while indice < archivo[0].shape[0]:
            lista.append(int(cuadroInformacion[0][indice]))
            indice += 1
        return lista

    #Function that searches the selected code in the rows in the matrix
    def encontrarProducto(codigo):
        archivo = pd.read_html("datos.html")
        indice = 1
        cuadroInformacion = archivo[0]
        while indice < archivo[0].shape[0]:
            if int(cuadroInformacion[0][indice]) == codigo:
                return indice
            indice += 1
        return -1

    # Codes Combo box
    cmbCodigosDisponibles = ttk.Combobox(vFuncion1, values=crearListaComboBox(), state="readonly")
    cmbCodigosDisponibles.grid(column=0, row=1)
    cmbCodigosDisponibles.current(0)
    cmbCodigosDisponibles.place(x=360, y=48)
    texto = StringVar()
    texto2 = StringVar()
    texto3 = StringVar()
    texto4 = StringVar()
    texto5 = StringVar()
    texto6 = StringVar()
    texto7 = StringVar()
    texto8 = StringVar()
    def tratamientoDeDatosLineaRecta():
        archivo = pd.read_html("datos.html")
        cuadroInformacion = archivo[0]
        numeroActivo = cuadroInformacion[0][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto.set(numeroActivo)
        categoria = cuadroInformacion[1][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto2.set(categoria)
        nombre = cuadroInformacion[2][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto3.set(nombre)
        valorInicial = cuadroInformacion[3][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto4.set("{:,}".format(int(valorInicial)))
        fechaDeCompra = cuadroInformacion[4][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto5.set(fechaDeCompra)
        moneda = cuadroInformacion[5][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto6.set(moneda)
        valorSalvamento = cuadroInformacion[6][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto7.set("{:,}".format(int(valorSalvamento)))
        periodoRecuperacion = cuadroInformacion[7][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto8.set(periodoRecuperacion)
        ano = fechaDeCompra[6:]
        llenarTablaLineaRecta(int(ano), int(periodoRecuperacion), int(valorInicial), int(valorSalvamento))


    def tratamientoDeDatosSumaDigitos():
        archivo = pd.read_html("datos.html")
        cuadroInformacion = archivo[0]
        numeroActivo = cuadroInformacion[0][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto.set(numeroActivo)
        categoria = cuadroInformacion[1][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto2.set(categoria)
        nombre = cuadroInformacion[2][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto3.set(nombre)
        valorInicial = cuadroInformacion[3][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto4.set("{:,}".format(int(valorInicial)))
        fechaDeCompra = cuadroInformacion[4][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto5.set(fechaDeCompra)
        moneda = cuadroInformacion[5][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto6.set(moneda)
        valorSalvamento = cuadroInformacion[6][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto7.set("{:,}".format(int(valorSalvamento)))
        periodoRecuperacion = cuadroInformacion[7][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto8.set(periodoRecuperacion)
        ano = fechaDeCompra[6:]
        llenarTablaSumaDigitos(int(ano), int(valorInicial), int(periodoRecuperacion), int(valorSalvamento))

    # Linea Recta Button
    btnCalcularLineaRecta = Button(vFuncion1, text="LÍNEA RECTA", fg="#FFFFFF", bg="#1E56A0", font="Segoe 9",
                                   command=tratamientoDeDatosLineaRecta).place(x=360, y=90)

    # Linea Recta Button
    btnCalcularSumaDigitos = Button(vFuncion1, text="SUMA DE DÍGITOS", fg="#FFFFFF", bg="#1E56A0", font="Segoe 9",
                                    command=tratamientoDeDatosSumaDigitos).place(x=455, y=90)

    #Label for title of the table
    tituloTable = StringVar()
    tituloTable.set("Tabla de proyección de depreciación anual")
    lblTituloTabla = tkinter.Label(vFuncion1, textvariable = tituloTable, bg="#FFFFFF", font=13, fg="#1E56A0")
    lblTituloTabla.place(x=45, y=395)

    # Data labels
    lblNumeroActivo = tkinter.Label(vFuncion1, text="Código de activo:", font="Segoe 12", bg="#FFFFFF")
    lblNumeroActivo.place(x=45, y=150)
    showNumeroActivo = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled',textvariable = texto, width = 40)
    showNumeroActivo.place(x=230, y=150)

    lblCategoria = tkinter.Label(vFuncion1, text="Categoría:", font="Segoe 12", bg="#FFFFFF")
    lblCategoria.place(x=45, y=180)
    showCategoria = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled',textvariable = texto2, width = 40)
    showCategoria.place(x=230, y=180)

    lblDetalle = tkinter.Label(vFuncion1, text="Detalle:", font="Segoe 12", bg="#FFFFFF")
    lblDetalle.place(x=45, y=210)
    showDetalle = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled',textvariable = texto3, width = 40)
    showDetalle.place(x=230, y=210)

    lblValorInicial = tkinter.Label(vFuncion1, text="Valor Inicial:", font="Segoe 12", bg="#FFFFFF")
    lblValorInicial.place(x=45, y=240)
    showValorInicial = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled',textvariable = texto4, width = 40)
    showValorInicial.place(x=230, y=240)

    lblFechaCompra = tkinter.Label(vFuncion1, text="Fecha de compra:", font="Segoe 12", bg="#FFFFFF")
    lblFechaCompra.place(x=45, y=270)
    showFechaCompra = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled',textvariable = texto5, width = 40)
    showFechaCompra.place(x=230, y=270)

    lblMoneda = tkinter.Label(vFuncion1, text="Moneda:", font="Segoe 12", bg="#FFFFFF")
    lblMoneda.place(x=45, y=300)
    showMoneda = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled',textvariable = texto6, width = 40)
    showMoneda.place(x=230, y=300)

    lblValorSalvamento = tkinter.Label(vFuncion1, text="Valor de salvamento:", font="Segoe 12", bg="#FFFFFF")
    lblValorSalvamento.place(x=45, y=330)
    showValorSalvamento = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled',textvariable = texto7, width = 40)
    showValorSalvamento.place(x=230, y=330)

    lblPeriodoRecuperacion = tkinter.Label(vFuncion1, text="Periodo de recuperación:", font="Segoe 12", bg="#FFFFFF")
    lblPeriodoRecuperacion.place(x=45, y=360)
    showPeriodoRecuperacion = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled',textvariable = texto8, width = 40)
    showPeriodoRecuperacion.place(x=230, y=360)

    # Table to show the data
    tblDepreciacion = ttk.Treeview(vFuncion1, columns=("col1", "col2", "col3", "col4"))  # Anadir mas columnas
    tblDepreciacion.column("#0", width=100)
    tblDepreciacion.column("col1", width=100)
    tblDepreciacion.column("col2", width=150)
    tblDepreciacion.column("col3", width=150)
    tblDepreciacion.column("col4", width=150)

    def determinarVidaUtil(periodoRecuperacion):
        vidaUtil = periodoRecuperacion * (periodoRecuperacion + 1) // 2
        return vidaUtil

    def tasaDepreciacion(periodoRecuperacion):
        tasaDepreciacion = 1 / periodoRecuperacion
        return tasaDepreciacion

    def llenarTablaLineaRecta(ano, periodoRecuperacion, valorInicial, valorSalvamento):
        if periodoRecuperacion == 0:
            tblDepreciacion.delete(*tblDepreciacion.get_children())
            tituloTable.set("⚠️ Tabla de proyección no disponible, el activo no se deprecia ⚠️")
            lblTituloTabla.config(fg = "#B4092D", font = 'bold')
        else:
            tblDepreciacion.heading("#0", text="Año", anchor=CENTER)
            tblDepreciacion.heading("col1", text="Periodo", anchor=CENTER)
            tblDepreciacion.heading("col2", text="Depreciación", anchor=CENTER)
            tblDepreciacion.heading("col3", text="Tasa Depreciación", anchor=CENTER)
            tblDepreciacion.heading("col4", text="Valor en libros", anchor=CENTER)
            tblDepreciacion.place(x=50, y=430)
            tblDepreciacion.delete(*tblDepreciacion.get_children())  # Borrar datos de tabla
            tituloTable.set("Tabla de proyección de depreciación")
            lblTituloTabla.config(fg="#1E56A0")

            ano += 1
            contador = 0
            vidaUtil = determinarVidaUtil(periodoRecuperacion)
            depreciacion = (valorInicial - valorSalvamento) / periodoRecuperacion
            valorLibros = valorInicial - depreciacion
            while contador < periodoRecuperacion:
                tblDepreciacion.insert("", END, text=str(ano), values=(
                str(contador + 1), str(depreciacion), str(round(tasaDepreciacion(periodoRecuperacion), 10)),
                str("{:,}".format(valorLibros))))
                valorInicial = valorInicial - depreciacion
                valorLibros = valorInicial - depreciacion
                contador += 1
                ano += 1

    def llenarTablaSumaDigitos(ano, costoInicial, periodoRecuperacion, valorSalvamento):
        if periodoRecuperacion == 0:
            tblDepreciacion.delete(*tblDepreciacion.get_children())
            tituloTable.set("⚠️ Tabla de proyección no disponible, el activo no se deprecia ⚠️")
            lblTituloTabla.config(fg = "#B4092D")
        else:
            tblDepreciacion.heading("#0", text="Año", anchor=CENTER)
            tblDepreciacion.heading("col1", text="Periodo", anchor=CENTER)
            tblDepreciacion.heading("col2", text="Depreciación Anual", anchor=CENTER)
            tblDepreciacion.heading("col3", text="Depreciación Acumulada", anchor=CENTER)
            tblDepreciacion.heading("col4", text="Valor en libros", anchor=CENTER)
            tblDepreciacion.place(x=50, y=430)
            tblDepreciacion.delete(*tblDepreciacion.get_children())  # Borrar datos de tabla
            tituloTable.set("Tabla de proyección de depreciación")
            lblTituloTabla.config(fg="#1E56A0")

            vidaUtil = determinarVidaUtil(periodoRecuperacion)
            contador = 1
            contadorPeriodo = periodoRecuperacion
            depreciacionAcumulada = 0
            while contador <= periodoRecuperacion:
                depreciacionAnual = (contadorPeriodo / vidaUtil) * (costoInicial - valorSalvamento)
                depreciacionAcumulada += depreciacionAnual
                valorLibros = costoInicial - depreciacionAcumulada
                tblDepreciacion.insert("", END, text=ano + 1,
                                       values=(str(contador), str("{:,}".format(round(depreciacionAnual, 2))),
                                               str("{:,}".format(round(depreciacionAcumulada, 2))),
                                               str("{:,}".format(round(costoInicial - depreciacionAcumulada, 2)))))
                ano += 1
                contador += 1
                contadorPeriodo -= 1


#===============================================================================[SEGUNDA FUNCION]========================================================================================


def abrirVentana2():

    #Window properties
    vFuncion2 = Toplevel()
    vFuncion2.title("Depreciacion de un activo especifico utilizando un metodo particular")
    anchoVLogin = 900
    altoVLogin = 750
    xPosicion = vFuncion2.winfo_screenwidth() // 2 - anchoVLogin // 2 #Posicionar ventana en centro de la pantalla
    yPosicion = vFuncion2.winfo_screenheight() // 2 - altoVLogin // 2 #Posicionar ventana en centro de la pantalla
    posicionPantalla = str(anchoVLogin) + "x" + str(altoVLogin) + "+" + str(xPosicion) + "+" + str(yPosicion)
    vFuncion2.geometry(posicionPantalla)
    vFuncion2['bg'] = '#FFFFFF'
    vFuncion2.resizable(0,0)


    #Go back button
    btnCalcularLineaRecta = Button(vFuncion2, text = "VOLVER", fg = "#FFFFFF", bg = "#1E56A0",font = "Segoe 10 bold", command = vFuncion2.destroy).place(x=50,y=700)


    #Label to choose the method
    lblSeleccionarMetodo = tkinter.Label(vFuncion2, text = "Seleccione el método de depreciación:",font = "Segoe 13", bg  = "#FFFFFF")
    lblSeleccionarMetodo.place(x=45,y=60)


    # Function that fills the combo box with the codes
    def crearListaComboBox():
        archivo = pd.read_html("datos.html")
        cuadroInformacion = archivo[0]
        lista = []
        indice = 1
        while indice < archivo[0].shape[0]:
            lista.append(int(cuadroInformacion[0][indice]))
            indice += 1
        return lista


    #Label to explain the combobox
    lblEscogerCodigo = tkinter.Label(vFuncion2, text="Seleccione el código de activo a mostrar:", font="Segoe 13", bg="#FFFFFF")
    lblEscogerCodigo.place(x=45,y=20)


    # Function that searches the selected code in the rows in the matrix
    def encontrarProducto(codigo):
        archivo = pd.read_html("datos.html")
        indice = 1
        cuadroInformacion = archivo[0]
        while indice < archivo[0].shape[0]:
            if int(cuadroInformacion[0][indice]) == codigo:
                return indice
            indice += 1
        return -1


    # Codes Combo box
    cmbCodigosDisponibles = ttk.Combobox(vFuncion2, values=crearListaComboBox(), state="readonly")
    cmbCodigosDisponibles.grid(column=0, row=1)
    cmbCodigosDisponibles.current(0)
    cmbCodigosDisponibles.place(x=360, y=21)
    texto = StringVar()
    texto2 = StringVar()
    texto3 = StringVar()
    texto4 = StringVar()
    texto5 = StringVar()
    texto6 = StringVar()
    texto7 = StringVar()
    texto8 = StringVar()


    def tratamientoDeDatosLineaRecta():
        archivo = pd.read_html("datos.html")
        cuadroInformacion = archivo[0]
        numeroActivo = cuadroInformacion[0][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto.set(numeroActivo)
        categoria = cuadroInformacion[1][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto2.set(categoria)
        nombre = cuadroInformacion[2][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto3.set(nombre)
        valorInicial = cuadroInformacion[3][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto4.set("{:,}".format(int(valorInicial)))
        fechaDeCompra = cuadroInformacion[4][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto5.set(fechaDeCompra)
        moneda = cuadroInformacion[5][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto6.set(moneda)
        valorSalvamento = cuadroInformacion[6][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto7.set("{:,}".format(int(valorSalvamento)))
        periodoRecuperacion = cuadroInformacion[7][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto8.set(periodoRecuperacion)
        ano = fechaDeCompra[6:]
        llenarTablaLineaRecta(int(ano), int(periodoRecuperacion), int(valorInicial), int(valorSalvamento), str(moneda))


    def tratamientoDeDatosSumaDigitos():
        archivo = pd.read_html("datos.html")
        cuadroInformacion = archivo[0]
        numeroActivo = cuadroInformacion[0][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto.set(numeroActivo)
        categoria = cuadroInformacion[1][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto2.set(categoria)
        nombre = cuadroInformacion[2][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto3.set(nombre)
        valorInicial = cuadroInformacion[3][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto4.set("{:,}".format(int(valorInicial)))
        fechaDeCompra = cuadroInformacion[4][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto5.set(fechaDeCompra)
        moneda = cuadroInformacion[5][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto6.set(moneda)
        valorSalvamento = cuadroInformacion[6][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto7.set("{:,}".format(int(valorSalvamento)))
        periodoRecuperacion = cuadroInformacion[7][encontrarProducto(int(cmbCodigosDisponibles.get()))]
        texto8.set(periodoRecuperacion)
        ano = fechaDeCompra[6:]
        llenarTablaSumaDigitos(int(ano),int(valorInicial),int(periodoRecuperacion),int(valorSalvamento),moneda)



      #Linea Recta Button
    btnCalcularLineaRecta = Button(vFuncion2, text = "LÍNEA RECTA", fg = "#FFFFFF", bg = "#1E56A0",font = "Segoe 9",
                                   command = tratamientoDeDatosLineaRecta).place(x=360,y = 61)


    #Suma Digitos Button
    btnCalcularSumaDigitos = Button(vFuncion2, text="SUMA DE DÍGITOS", fg="#FFFFFF", bg="#1E56A0", font="Segoe 9",
                                    command=tratamientoDeDatosSumaDigitos).place(x=455, y=61)

    # Label for title of the table
    tituloTable = StringVar()
    tituloTable.set("Tabla de proyección de depreciación anual")
    lblTituloTabla = tkinter.Label(vFuncion2, textvariable=tituloTable, bg="#FFFFFF", font=13, fg="#1E56A0")
    lblTituloTabla.place(x=45, y=395)


    #Data labels
    lblNumeroActivo = tkinter.Label(vFuncion2, text="Número de activo:", font="Segoe 12", bg="#FFFFFF")
    lblNumeroActivo.place(x=45, y=105)
    showNumeroActivo = tkinter.Label(vFuncion2, font="Segoe 12", bg= "#E5E5E5", height = 1, textvariable = texto, width = 40)
    showNumeroActivo.place(x=230, y=105)

    lblCategoria = tkinter.Label(vFuncion2, text="Categoría:", font="Segoe 12", bg="#FFFFFF")
    lblCategoria.place(x=45, y=135)
    showCategoria = tkinter.Label(vFuncion2, font="Segoe 12", bg="#E5E5E5", height = 1, textvariable = texto2, width = 40)
    showCategoria.place(x=230, y=135)

    lblDetalle = tkinter.Label(vFuncion2, text="Detalle:", font="Segoe 12", bg="#FFFFFF")
    lblDetalle.place(x=45, y=165)
    showDetalle = tkinter.Label(vFuncion2, font="Segoe 12", bg="#E5E5E5", height = 1, textvariable = texto3, width = 40)
    showDetalle.place(x=230, y=165)

    lblValorInicial = tkinter.Label(vFuncion2, text="Valor Inicial:", font="Segoe 12", bg="#FFFFFF")
    lblValorInicial.place(x=45, y=195)
    showValorInicial = tkinter.Label(vFuncion2, font="Segoe 12", bg="#E5E5E5", height = 1, textvariable = texto4, width = 40)
    showValorInicial.place(x=230, y=195)

    date = datetime.today()
    def formatoInversoFecha(fecha):
        return fecha[8:] + "-" + fecha[5:7] + "-" + fecha[0:4]

    lblFechaActual = tkinter.Label(vFuncion2, text="Fecha actual:", font="Segoe 12", bg="#FFFFFF")
    lblFechaActual.place(x=45, y=225)
    showFechaActual = tkinter.Label(vFuncion2, font="Segoe 12",text = formatoInversoFecha(str(date)[:10]), height = 1, width = 40)
    showFechaActual.place(x=230, y=225)

    lblFechaCompra = tkinter.Label(vFuncion2, text="Fecha de compra:", font="Segoe 12", bg="#FFFFFF")
    lblFechaCompra.place(x=45, y=255)
    showFechaCompra = tkinter.Label(vFuncion2, font="Segoe 12", bg="#E5E5E5", height = 1, textvariable = texto5, width = 40)
    showFechaCompra.place(x=230, y=255)

    lblMoneda = tkinter.Label(vFuncion2, text="Moneda:", font="Segoe 12", bg="#FFFFFF")
    lblMoneda.place(x=45, y=285)   #dolares o colones
    showMoneda = tkinter.Label(vFuncion2, font="Segoe 12", bg="#E5E5E5", height = 1, textvariable = texto6, width = 40)
    showMoneda.place(x=230, y=285)

    lblValorSalvamento = tkinter.Label(vFuncion2, text="Valor de salvamento:", font="Segoe 12", bg="#FFFFFF")
    lblValorSalvamento.place(x=45, y=315)
    showValorSalvamento = tkinter.Label(vFuncion2, font="Segoe 12", bg="#E5E5E5", height = 1, textvariable = texto7, width = 40)
    showValorSalvamento.place(x=230, y=315)

    lblPeriodoRecuperacion = tkinter.Label(vFuncion2, text="Periodo de recuperación:", font="Segoe 12", bg="#FFFFFF")
    lblPeriodoRecuperacion.place(x=45, y=345)
    showPeriodoRecuperacion = tkinter.Label(vFuncion2, font="Segoe 12", bg="#E5E5E5", height = 1, textvariable = texto8, width = 40)
    showPeriodoRecuperacion.place(x=230, y=345)


    #Table to show the data
    tblDepreciacion = ttk.Treeview(vFuncion2, columns = ("col1","col2","col3","col4","col5"))
    tblDepreciacion.column("#0",width= 100)
    tblDepreciacion.column("col1",width=100)
    tblDepreciacion.column("col2", width=150)
    tblDepreciacion.column("col3", width=150)
    tblDepreciacion.column("col4", width=150)
    tblDepreciacion.column("col5", width=150)


    def determinarVidaUtil(periodoRecuperacion):
        vidaUtil = periodoRecuperacion * (periodoRecuperacion + 1) // 2
        return vidaUtil


    def tasaDepreciacion(periodoRecuperacion):
        tasaDepreciacion = 1 / periodoRecuperacion
        return tasaDepreciacion


    def formatearPrecioDolar(precioDolar):
        nuevaVersion = ""
        for i in range(len(precioDolar)):
            if precioDolar[i] == ",":
                nuevaVersion += "."
            if (precioDolar[i]).isdigit():
                nuevaVersion += precioDolar[i]
        return float(nuevaVersion)


    def determinarPrecioDolar():
        urlBanco = 'https://gee.bccr.fi.cr/indicadoreseconomicos/Cuadros/frmVerCatCuadro.aspx?idioma=1&CodCuadro=%20400'
        page = requests.get(urlBanco)
        soup = BeautifulSoup(page.content, 'html.parser')
        tipoCambio = soup.find_all('td', class_='celda400')
        dolar = tipoCambio[89].text
        return formatearPrecioDolar(dolar)


    def llenarTablaLineaRecta(ano,periodoRecuperacion,valorInicial,valorSalvamento, moneda):
        if periodoRecuperacion == 0:
            tblDepreciacion.delete(*tblDepreciacion.get_children())
            tituloTable.set("⚠️ Tabla de proyección no disponible, el activo no se deprecia ⚠️")
            lblTituloTabla.config(fg = "#B4092D", font = 'bold')
        else:
            if (moneda == "Colones"):
                tituloMoneda = "Dólares"
            else:
                tituloMoneda = "Colones"
            fecha = datetime.today()
            anoActual = fecha.strftime("%Y")
            tblDepreciacion.heading("#0", text="Año", anchor=CENTER)
            tblDepreciacion.heading("col1", text="Periodo", anchor=CENTER)
            tblDepreciacion.heading("col2", text="Depreciación", anchor=CENTER)
            tblDepreciacion.heading("col3", text="Tasa Depreciación", anchor=CENTER)
            tblDepreciacion.heading("col4", text="Valor en libros", anchor=CENTER)
            tblDepreciacion.heading("col5", text = tituloMoneda, anchor=CENTER) #dolar
            tblDepreciacion.place(x=50, y=430)
            tblDepreciacion.delete(*tblDepreciacion.get_children()) #Borrar datos de tabla
            tituloTable.set("Tabla de proyección de depreciación")
            lblTituloTabla.config(fg="#1E56A0")
            ano += 1
            contador = 0
            vidaUtil = determinarVidaUtil(periodoRecuperacion)
            depreciacion = (valorInicial - valorSalvamento) / periodoRecuperacion
            valorLibros = valorInicial - depreciacion
            valorMonedaContraria = 0
            while (ano <= int(anoActual)):
                if valorLibros == valorSalvamento:
                    while(ano < int(anoActual)-1):
                        tblDepreciacion.insert("", END, text=str(ano), values=(str(contador + 1),
                                                                               str(depreciacion),
                                                                               str(round(tasaDepreciacion(
                                                                                   periodoRecuperacion), 10)),
                                                                               str("{:,}".format(valorLibros)),
                                                                               str("{:,}".format(round(valorMonedaContraria, 2)))))
                        contador += 1
                        ano += 1
                if (moneda == "Colones"):
                    valorMonedaContraria = valorLibros / determinarPrecioDolar()
                else:
                    valorMonedaContraria = valorLibros * determinarPrecioDolar()
                tblDepreciacion.insert("", END, text=str(ano), values=(str(contador + 1),
                                                                       str(depreciacion),
                                                                       str(round(tasaDepreciacion(periodoRecuperacion), 10)),
                                                                       str("{:,}".format(valorLibros)),
                                                                       str("{:,}".format(round(valorMonedaContraria,2)))))
                valorInicial = valorInicial - depreciacion
                valorLibros = valorInicial - depreciacion
                contador+=1
                ano +=1


    def llenarTablaSumaDigitos(ano, costoInicial,periodoRecuperacion, valorSalvamento, moneda):
        if periodoRecuperacion == 0:
            tblDepreciacion.delete(*tblDepreciacion.get_children())
            tituloTable.set("⚠️ Tabla de proyección no disponible, el activo no se deprecia ⚠️")
            lblTituloTabla.config(fg = "#B4092D", font = 'bold')
        else:
            if (moneda == "Colones"):
                tituloMoneda = "Dólares"
            else:
                tituloMoneda = "Colones"

            fecha = datetime.today()
            anoActual = fecha.strftime("%Y")
            tblDepreciacion.heading("#0", text="Año", anchor=CENTER)
            tblDepreciacion.heading("col1", text="Periodo", anchor=CENTER)
            tblDepreciacion.heading("col2", text="Depreciación Anual", anchor=CENTER)
            tblDepreciacion.heading("col3", text="Depreciación Acumulada", anchor=CENTER)
            tblDepreciacion.heading("col4", text="Valor en libros", anchor=CENTER)
            tblDepreciacion.heading("col5", text= tituloMoneda, anchor=CENTER)
            tblDepreciacion.place(x=50, y=430)
            tblDepreciacion.delete(*tblDepreciacion.get_children())  # Borrar datos de tabla
            tituloTable.set("Tabla de proyección de depreciación")
            lblTituloTabla.config(fg="#1E56A0")

            vidaUtil = determinarVidaUtil(periodoRecuperacion)
            contador = 1
            contadorPeriodo = periodoRecuperacion
            depreciacionAcumulada = 0
            while(ano < int(anoActual)):
                depreciacionAnual=(contadorPeriodo / vidaUtil) * (costoInicial - valorSalvamento)
                depreciacionAcumulada += depreciacionAnual
                valorLibros = costoInicial - depreciacionAcumulada
                if(moneda == "Colones"):
                    valorMonedaContraria= valorLibros / determinarPrecioDolar()
                else:
                    valorMonedaContraria = valorLibros * determinarPrecioDolar()

                if depreciacionAnual == 0:
                    while ano < int(anoActual)-1:
                        tblDepreciacion.insert("", END, text=ano + 1, values=(str(contador),
                                                                              str("{:,}".format(
                                                                                  round(depreciacionAnual, 2))),
                                                                              str("{:,}".format(
                                                                                  round(depreciacionAcumulada, 2))),
                                                                              str("{:,}".format(round(
                                                                                  costoInicial - depreciacionAcumulada,
                                                                                  2))),
                                                                              str("{:,}".format(
                                                                                  round(valorMonedaContraria, 2)))))
                        ano+=1
                        contador+=1

                tblDepreciacion.insert("", END, text= ano +1, values= (str(contador),
                                                                       str("{:,}". format(round(depreciacionAnual, 2))),
                                                                       str("{:,}".format(round(depreciacionAcumulada, 2))),
                                                                       str("{:,}".format(round(costoInicial - depreciacionAcumulada, 2))),
                                                                       str("{:,}".format (round(valorMonedaContraria,2)))))
                ano +=1
                contador +=1
                contadorPeriodo -=1

#===============================================================================[TERCERA FUNCION]========================================================================================

def abrirVentana3():

    #Window properties
    vFuncion3 = Toplevel()
    vFuncion3.title("Reporte General de depreciación acumulada")
    anchoVLogin = 900
    altoVLogin = 750
    xPosicion = vFuncion3.winfo_screenwidth() // 2 - anchoVLogin // 2 #Posicionar ventana en centro de la pantalla
    yPosicion = vFuncion3.winfo_screenheight() // 2 - altoVLogin // 2 #Posicionar ventana en centro de la pantalla
    posicionPantalla = str(anchoVLogin) + "x" + str(altoVLogin) + "+" + str(xPosicion) + "+" + str(yPosicion)
    vFuncion3.geometry(posicionPantalla)
    vFuncion3['bg'] = '#FFFFFF'
    vFuncion3.resizable(0,0)


    #Go back button
    btnCalcularLineaRecta = Button(vFuncion3, text = "VOLVER", fg = "#FFFFFF", bg = "#1E56A0",font = "Segoe 10 bold", command = vFuncion3.destroy).place(x=50,y=700)

    #Label for title
    lblNumeroActivo = tkinter.Label(vFuncion3, text="🢂 Reporte general de depreciación", font="Segoe 14", bg="#FFFFFF", fg = "#1E56A0")
    lblNumeroActivo.place(x=15, y=15)



#===============================================================================[VENTANA PRINCIPAL]========================================================================================

vLogin = Tk()
def abrirVentanaPrincipal():


    #Main window properties
    vLogin.title("Login - Depreciación de Activos") #titulo ventana
    anchoVLogin = 650
    altoVLogin = 700
    xPosicion = vLogin.winfo_screenwidth() // 2 - anchoVLogin // 2 #Posicionar ventana en centro de la pantalla
    yPosicion = vLogin.winfo_screenheight() // 2 - altoVLogin // 2 #Posicionar ventana en centro de la pantalla
    posicionPantalla = str(anchoVLogin) + "x" + str(altoVLogin) + "+" + str(xPosicion) + "+" + str(yPosicion)
    vLogin.geometry(posicionPantalla)
    vLogin['bg'] = '#FFFFFF'
    vLogin.resizable(0,0)


    #Title Label
    lblTitulo = Label(vLogin, text = "¡Bienvenido al sistema de \n depreciación de activos! \n Seleccione una de las siguientes opciones:",
                      fg = "#555555", bg = "#E8E8E8", font = "Segoe 17", height = 3, width = 35)
    lblTitulo.place(x=135, y=45)


    #Option buttons
    btnFuncion1 = Button(vLogin,text = "Proyección de depreciación de un activo \n específico usando un método particular"
                         ,fg = "#FFFFFF", bg = "#1E56A0", font = "Segoe 14", height = 2, width = 34, command = abrirVentana1).place(x=138,y=185)
    btnFuncion2 = Button(vLogin,text = "Depreciación acumulada de un activo\n específico usando un método particular",
                         fg = "#FFFFFF", bg = "#1E56A0", font = "Segoe 14", height = 2, width = 34,command= abrirVentana2).place(x=138,y=280)
    btnFuncion3 = Button(vLogin,text = "Reporte general de depreciación \nacumulada de todos los activos bajo \nun método de depreciación",
                         fg = "#FFFFFF", bg = "#1E56A0", font = "Segoe 14", height = 3, width = 34, command= abrirVentana3).place(x=138,y=370)
    btnFuncion4 = Button(vLogin,text = "Reporte general de proyección de\n depreciación de todos los activos de una\n categoría bajo un método de\n depreciación particular",
                         fg = "#FFFFFF", bg = "#1E56A0", font = "Segoe 14", height = 4, width = 34).place(x=138,y=480)


    #Invocator
    vLogin.mainloop()

abrirVentanaPrincipal()