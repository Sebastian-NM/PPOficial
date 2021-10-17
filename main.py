import tkinter
from tkinter import *
from tkinter import ttk
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from datetime import date
from datetime import datetime
date = datetime.today()
year = date.strftime("%Y")


#===============================================================================[PRIMERA FUNCION]========================================================================================

def abrirVentana1():
    #Window properties
    vFuncion1 = Toplevel()
    vFuncion1.title("Depreciación Lineal")
    anchoVLogin = 1100
    altoVLogin = 800
    xPosicion = vFuncion1.winfo_screenwidth() // 2 - anchoVLogin // 2 #Posicionar ventana en centro de la pantalla
    yPosicion = vFuncion1.winfo_screenheight() // 2 - altoVLogin // 2 #Posicionar ventana en centro de la pantalla
    posicionPantalla = str(anchoVLogin) + "x" + str(altoVLogin) + "+" + str(xPosicion) + "+" + str(yPosicion)
    vFuncion1.geometry(posicionPantalla)
    vFuncion1['bg'] = '#FFFFFF'
    vFuncion1.resizable(0,0)


    #Go back button
    btnCalcularLineaRecta = Button(vFuncion1, text = "VOLVER", fg = "#FFFFFF", bg = "#1E56A0",font = "Segoe 10 bold", command = vFuncion1.destroy).place(x=50,y=700)
    #nombreVentana,nombreBoton, font, fondo, font = "tamano letra", command = funcionalidad que va a tener


    #Label to choose the method
    lblSeleccionarMetodo = tkinter.Label(vFuncion1, text = "Seleccione el método de depreciación:",font = "Segoe 13", bg  = "#FFFFFF")
    lblSeleccionarMetodo.place(x=45,y=90)


    #Label to explain the combobox
    lblEscogerCodigo = Label(vFuncion1, text="Seleccione el código de activo a mostrar:", font="Segoe 13", bg="#FFFFFF")
    lblEscogerCodigo.place(x=45,y=45)


    #Codes Combo box
    cmbCodigosDisponibles = ttk.Combobox(vFuncion1, values=["1","2","3","4","5","6","7"],state="readonly")
    cmbCodigosDisponibles.grid(column=0, row=1)
    cmbCodigosDisponibles.current(0)
    cmbCodigosDisponibles.place(x=360,y=48)


    def tratamientoDeDatosLineaRecta():
        llenarTablaLineaRecta(2019,6,7689300,450000)

    def tratamientoDeDatosSumaDigitos():
        llenarTablaSumaDigitos(2019,7689300,6,450000)


    #Linea Recta Button
    btnCalcularLineaRecta = Button(vFuncion1, text = "LÍNEA RECTA", fg = "#FFFFFF", bg = "#1E56A0",font = "Segoe 9",
                                   command = tratamientoDeDatosLineaRecta).place(x=360,y = 90)


    #Linea Recta Button
    btnCalcularSumaDigitos = Button(vFuncion1, text="SUMA DE DÍGITOS", fg="#FFFFFF", bg="#1E56A0", font="Segoe 9",
                                   command=tratamientoDeDatosSumaDigitos).place(x=455, y=90)


    #Suma de digitos Button
    lblTituloTabla = tkinter.Label(vFuncion1, text = "Tabla de proyección de depreciación anual", bg  = "#FFFFFF", font = 13,fg = "#1E56A0")
    lblTituloTabla.place(x=45,y=395)


    #Data labels
    lblNumeroActivo = tkinter.Label(vFuncion1, text="Número de activo:", font="Segoe 12", bg="#FFFFFF")
    lblNumeroActivo.place(x=45, y=150)
    showNumeroActivo = tkinter.Entry(vFuncion1, font="Segoe 12", bg= "#E5E5E5", state='disabled')
    showNumeroActivo.place(x=230, y=150)


    lblCategoria = tkinter.Label(vFuncion1, text="Categoría:", font="Segoe 12", bg="#FFFFFF")
    lblCategoria.place(x=45, y=180)
    showCategoria = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showCategoria.place(x=230, y=180)


    lblDetalle = tkinter.Label(vFuncion1, text="Detalle:", font="Segoe 12", bg="#FFFFFF")
    lblDetalle.place(x=45, y=210)
    showDetalle = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showDetalle.place(x=230, y=210)


    lblValorInicial = tkinter.Label(vFuncion1, text="Valor Inicial:", font="Segoe 12", bg="#FFFFFF")
    lblValorInicial.place(x=45, y=240)
    showValorInicial = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showValorInicial.place(x=230, y=240)


    lblFechaCompra = tkinter.Label(vFuncion1, text="Fecha de compra:", font="Segoe 12", bg="#FFFFFF")
    lblFechaCompra.place(x=45, y=270)
    showFechaCompra = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showFechaCompra.place(x=230, y=270)


    lblMoneda = tkinter.Label(vFuncion1, text="Moneda:", font="Segoe 12", bg="#FFFFFF")
    lblMoneda.place(x=45, y=300)
    showMoneda = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showMoneda.place(x=230, y=300)


    lblValorSalvamento = tkinter.Label(vFuncion1, text="Valor de salvamento:", font="Segoe 12", bg="#FFFFFF")
    lblValorSalvamento.place(x=45, y=330)
    showValorSalvamento = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showValorSalvamento.place(x=230, y=330)


    lblPeriodoRecuperacion = tkinter.Label(vFuncion1, text="Periodo de recuperación:", font="Segoe 12", bg="#FFFFFF")
    lblPeriodoRecuperacion.place(x=45, y=360)
    showPeriodoRecuperacion = tkinter.Entry(vFuncion1, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showPeriodoRecuperacion.place(x=230, y=360)


    #Table to show the data
    tblDepreciacion = ttk.Treeview(vFuncion1, columns = ("col1","col2","col3","col4")) #Anadir mas columnas
    tblDepreciacion.column("#0",width= 100)
    tblDepreciacion.column("col1",width=100)
    tblDepreciacion.column("col2", width=150)
    tblDepreciacion.column("col3", width=150)
    tblDepreciacion.column("col4", width=150)


    def determinarVidaUtil(periodoRecuperacion):
        vidaUtil = periodoRecuperacion * (periodoRecuperacion + 1) // 2
        return vidaUtil


    def tasaDepreciacion(periodoRecuperacion):
        tasaDepreciacion = 1 / periodoRecuperacion
        return tasaDepreciacion


    def llenarTablaLineaRecta(ano,periodoRecuperacion,valorInicial,valorSalvamento):
        tblDepreciacion.heading("#0", text="Año", anchor=CENTER)
        tblDepreciacion.heading("col1", text="Periodo", anchor=CENTER)
        tblDepreciacion.heading("col2", text="Depreciación", anchor=CENTER)
        tblDepreciacion.heading("col3", text="Tasa Depreciación", anchor=CENTER)
        tblDepreciacion.heading("col4", text="Valor en libros", anchor=CENTER)
        tblDepreciacion.place(x=50, y=430)
        tblDepreciacion.delete(*tblDepreciacion.get_children()) #Borrar datos de tabla

        ano += 1
        contador = 0
        vidaUtil = determinarVidaUtil(periodoRecuperacion)
        depreciacion = (valorInicial - valorSalvamento)/periodoRecuperacion
        valorLibros = valorInicial - depreciacion
        while contador < periodoRecuperacion:
            tblDepreciacion.insert("",END,text = str(ano),values = (str(contador+1),str(depreciacion),str(round(tasaDepreciacion(periodoRecuperacion),10)),str("{:,}".format(valorLibros))))
            valorInicial = valorInicial - depreciacion
            valorLibros = valorInicial - depreciacion
            contador+=1
            ano +=1


    def llenarTablaSumaDigitos(ano, costoInicial,periodoRecuperacion, valorSalvamento):
        tblDepreciacion.heading("#0", text="Año", anchor=CENTER)
        tblDepreciacion.heading("col1", text="Periodo", anchor=CENTER)
        tblDepreciacion.heading("col2", text="Depreciación Anual", anchor=CENTER)
        tblDepreciacion.heading("col3", text="Depreciación Acumulada", anchor=CENTER)
        tblDepreciacion.heading("col4", text="Valor en libros", anchor=CENTER)
        tblDepreciacion.place(x=50, y=430)
        tblDepreciacion.delete(*tblDepreciacion.get_children())  # Borrar datos de tabla
        vidaUtil = determinarVidaUtil(periodoRecuperacion)
        contador = 1
        contadorPeriodo = periodoRecuperacion
        depreciacionAcumulada = 0
        while contador <= periodoRecuperacion:
            depreciacionAnual = (contadorPeriodo/vidaUtil) * (costoInicial-valorSalvamento)
            depreciacionAcumulada += depreciacionAnual
            valorLibros = costoInicial - depreciacionAcumulada
            tblDepreciacion.insert("", END, text = ano+1, values = (str(contador), str("{:,}".format(round(depreciacionAnual,2))),
                                                                  str("{:,}".format(round(depreciacionAcumulada,2))), str("{:,}".format(round(costoInicial-depreciacionAcumulada,2)))))
            ano+=1
            contador+=1
            contadorPeriodo-=1


#===============================================================================[SEGUNDA FUNCION]========================================================================================

def abrirVentana2():

    #Window properties
    vFuncion2 = Toplevel()
    vFuncion2.title("Depreciacion de un activo especifico utilizando un metodo particular")
    anchoVLogin = 1100
    altoVLogin = 800
    xPosicion = vFuncion2.winfo_screenwidth() // 2 - anchoVLogin // 2 #Posicionar ventana en centro de la pantalla
    yPosicion = vFuncion2.winfo_screenheight() // 2 - altoVLogin // 2 #Posicionar ventana en centro de la pantalla
    posicionPantalla = str(anchoVLogin) + "x" + str(altoVLogin) + "+" + str(xPosicion) + "+" + str(yPosicion)
    vFuncion2.geometry(posicionPantalla)
    vFuncion2['bg'] = '#FFFFFF'
    vFuncion2.resizable(0,0)


    #Go back button
    btnCalcularLineaRecta = Button(vFuncion2, text = "VOLVER", fg = "#FFFFFF", bg = "#1E56A0",font = "Segoe 10 bold", command = vFuncion2.destroy).place(x=50,y=700)
    #nombreVentana,nombreBoton, font, fondo, font = "tamano letra", command = funcionalidad que va a tener


    #Label to choose the method
    lblSeleccionarMetodo = tkinter.Label(vFuncion2, text = "Seleccione el método de depreciación:",font = "Segoe 13", bg  = "#FFFFFF")
    lblSeleccionarMetodo.place(x=45,y=80)


    #Label to explain the combobox
    lblEscogerCodigo = tkinter.Label(vFuncion2, text="Seleccione el código de activo a mostrar:", font="Segoe 13", bg="#FFFFFF")
    lblEscogerCodigo.place(x=45,y=40)


    #Codes Combo box
    cmbCodigosDisponibles = ttk.Combobox(vFuncion2, values=["1","2","3","4","5","6","7"],state="readonly")
    cmbCodigosDisponibles.grid(column=0, row=1)
    cmbCodigosDisponibles.current(0)
    cmbCodigosDisponibles.place(x=360,y=48)


    def tratamientoDeDatosLineaRecta():
        llenarTablaLineaRecta(2019,6,7689300,450000)

    def tratamientoDeDatosSumaDigitos():
         llenarTablaSumaDigitos(2019,7689300,6,450000)


      #Linea Recta Button
    btnCalcularLineaRecta = Button(vFuncion2, text = "LÍNEA RECTA", fg = "#FFFFFF", bg = "#1E56A0",font = "Segoe 9",
                                   command = tratamientoDeDatosLineaRecta).place(x=360,y = 90)


    #Linea Recta Button
    btnCalcularSumaDigitos = Button(vFuncion2, text="SUMA DE DÍGITOS", fg="#FFFFFF", bg="#1E56A0", font="Segoe 9",
                                    command=tratamientoDeDatosSumaDigitos).place(x=455, y=90)


    #Suma de digitos Button
    lblTituloTabla = tkinter.Label(vFuncion2, text = "Tabla de proyección de depreciación anual", bg  = "#FFFFFF", font = 13,fg = "#1E56A0")
    lblTituloTabla.place(x=45,y=395)


    #Data labels
    lblNumeroActivo = tkinter.Label(vFuncion2, text="Número de activo:", font="Segoe 12", bg="#FFFFFF")
    lblNumeroActivo.place(x=45, y=150)
    showNumeroActivo = tkinter.Entry(vFuncion2, font="Segoe 12", bg= "#E5E5E5", state='disabled')
    showNumeroActivo.place(x=230, y=150)


    lblCategoria = tkinter.Label(vFuncion2, text="Categoría:", font="Segoe 12", bg="#FFFFFF")
    lblCategoria.place(x=45, y=180)
    showCategoria = tkinter.Entry(vFuncion2, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showCategoria.place(x=230, y=180)


    lblDetalle = tkinter.Label(vFuncion2, text="Detalle:", font="Segoe 12", bg="#FFFFFF")
    lblDetalle.place(x=45, y=210)
    showDetalle = tkinter.Entry(vFuncion2, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showDetalle.place(x=230, y=210)


    lblValorInicial = tkinter.Label(vFuncion2, text="Valor Inicial:", font="Segoe 12", bg="#FFFFFF")
    lblValorInicial.place(x=45, y=240)
    showValorInicial = tkinter.Entry(vFuncion2, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showValorInicial.place(x=230, y=240)


    lblFechaActual = tkinter.Label(vFuncion2, text="Fecha actual:", font="Segoe 12", bg="#FFFFFF")
    lblFechaActual.place(x=45, y=290)
    showFechaActual = tkinter.Entry(vFuncion2, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showFechaActual.place(x=260, y=290)


    lblFechaCompra = tkinter.Label(vFuncion2, text="Fecha de compra:", font="Segoe 12", bg="#FFFFFF")
    lblFechaCompra.place(x=45, y=270)
    showFechaCompra = tkinter.Entry(vFuncion2, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showFechaCompra.place(x=230, y=270)


    lblMoneda = tkinter.Label(vFuncion2, text="Moneda:", font="Segoe 12", bg="#FFFFFF")
    lblMoneda.place(x=45, y=300)   #dolares o colones
    showMoneda = tkinter.Entry(vFuncion2, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showMoneda.place(x=230, y=300)


    lblValorSalvamento = tkinter.Label(vFuncion2, text="Valor de salvamento:", font="Segoe 12", bg="#FFFFFF")
    lblValorSalvamento.place(x=45, y=330)
    showValorSalvamento = tkinter.Entry(vFuncion2, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showValorSalvamento.place(x=230, y=330)


    lblPeriodoRecuperacion = tkinter.Label(vFuncion2, text="Periodo de recuperación:", font="Segoe 12", bg="#FFFFFF")
    lblPeriodoRecuperacion.place(x=45, y=360)
    showPeriodoRecuperacion = tkinter.Entry(vFuncion2, font="Segoe 12", bg="#E5E5E5", state='disabled')
    showPeriodoRecuperacion.place(x=230, y=360)


    #Table to show the data
    tblDepreciacion = ttk.Treeview(vFuncion2, columns = ("col1","col2","col3","col4","col5")) #Anadir mas columnas
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

    
    def llenarTablaLineaRecta(ano,periodoRecuperacion,valorInicial,valorSalvamento):
        tblDepreciacion.heading("#0", text="Año", anchor=CENTER)
        tblDepreciacion.heading("col1", text="Periodo", anchor=CENTER)
        tblDepreciacion.heading("col2", text="Depreciación", anchor=CENTER)
        tblDepreciacion.heading("col3", text="Tasa Depreciación", anchor=CENTER)
        tblDepreciacion.heading("col4", text="Valor en libros", anchor=CENTER)
        tblDepreciacion.heading("col5", text="Tipo de Cambio", anchor=CENTER) #dolar
        tblDepreciacion.place(x=50, y=430)
        tblDepreciacion.delete(*tblDepreciacion.get_children()) #Borrar datos de tabla

        contador = 0
        vidaUtil = determinarVidaUtil(periodoRecuperacion)
        depreciacion = (valorInicial - valorSalvamento)/periodoRecuperacion
        valorLibros = valorInicial - depreciacion
        while (ano< int(year)):
            tblDepreciacion.insert("",END,text = str(ano),values = (str(contador+1),str(depreciacion),str(round(tasaDepreciacion(periodoRecuperacion),10)),str("{:,}".format(valorLibros))))
            valorInicial = valorInicial - depreciacion
            valorLibros = valorInicial - depreciacion
            ValorDolar= valorLibros * determinarPrecioDolar()
            contador+=1
            ano +=1


    def llenarTablaSumaDigitos(ano, costoInicial,periodoRecuperacion, valorSalvamento):
        tblDepreciacion.heading("#0", text="Año", anchor=CENTER)
        tblDepreciacion.heading("col1", text="Periodo", anchor=CENTER)
        tblDepreciacion.heading("col2", text="Depreciación Anual", anchor=CENTER)
        tblDepreciacion.heading("col3", text="Depreciación Acumulada", anchor=CENTER)
        tblDepreciacion.heading("col4", text="Valor en libros", anchor=CENTER)
        tblDepreciacion.heading("col5", text="Tipo de Cambio", anchor=CENTER)
        tblDepreciacion.place(x=50, y=430)
        tblDepreciacion.delete(*tblDepreciacion.get_children())  # Borrar datos de tabla
        vidaUtil = determinarVidaUtil(periodoRecuperacion)
        contador = 1
        contadorPeriodo = periodoRecuperacion
        depreciacionAcumulada = 0
        dolar = 631
        while (ano < int(year)):
            depreciacionAnual = (contadorPeriodo/vidaUtil) * (costoInicial-valorSalvamento)
            depreciacionAcumulada += depreciacionAnual
            valorLibros = costoInicial - depreciacionAcumulada
            valorDolar = valorLibros * dolar
            tblDepreciacion.insert("", END, text = ano+1, values = (str(contador), str("{:,}".format(round(depreciacionAnual,2))),
                                                                  str("{:,}".format(round(depreciacionAcumulada,2))), str("{:,}".format(round(costoInicial-depreciacionAcumulada,2))),str(round(valorDolar))))
            ano+=1
            contador+=1
            contadorPeriodo-=1


#===============================================================================[VENTANA PRINCIPAL]========================================================================================

vLogin = Tk()
def abrirVentanaPrincipal():


    #Main window properties
    vLogin.title("Login - Depreciación de Activos") #titulo ventana
    anchoVLogin = 1000
    altoVLogin = 700
    xPosicion = vLogin.winfo_screenwidth() // 2 - anchoVLogin // 2 #Posicionar ventana en centro de la pantalla
    yPosicion = vLogin.winfo_screenheight() // 2 - altoVLogin // 2 #Posicionar ventana en centro de la pantalla
    posicionPantalla = str(anchoVLogin) + "x" + str(altoVLogin) + "+" + str(xPosicion) + "+" + str(yPosicion)
    vLogin.geometry(posicionPantalla)
    vLogin['bg'] = '#FFFFFF'
    vLogin.resizable(0,0)


    #Title Label
    lblTitulo = Label(vLogin, text = "¡Bienvenido al sistema de \n depreciación de activos! \n Seleccione una de las siguientes opciones:",
                      fg = "#555555", bg = "#E8E8E8", font = "Segoe 20", height = 3, width = 35)
    lblTitulo.place(x=230, y=45)


    #Rectangle in the back
    lblRectangulo = Label(vLogin, fg = "#D6E4F0", bg = "#E8E8E8", font = "Segoe 25", height = 17, width = 42)
    lblRectangulo.lower()
    lblRectangulo.place(x=100, y=25)


    #Option buttons
    btnFuncion1 = Button(vLogin,text = "Proyección de depreciación de un activo \n específico usando un método particular"
                         ,fg = "#FFFFFF", bg = "#1E56A0", font = "Segoe 15", height = 2, width = 34, command = abrirVentana1).place(x=315,y=185)
    btnFuncion2 = Button(vLogin,text = "Depreciación acumulada de un activo\n específico usando un método particular",
                         fg = "#FFFFFF", bg = "#1E56A0", font = "Segoe 15", height = 2, width = 34,command= abrirVentana2).place(x=315,y=280)
    btnFuncion3 = Button(vLogin,text = "Reporte general de depreciación \nacumulada de todos los activos bajo \nun método de depreciación",
                         fg = "#FFFFFF", bg = "#1E56A0", font = "Segoe 15", height = 3, width = 34).place(x=315,y=370)
    btnFuncion4 = Button(vLogin,text = "Reporte general de proyección de\n depreciación de todos los activos de una\n categoría bajo un método de\n depreciación particular",
                         fg = "#FFFFFF", bg = "#1E56A0", font = "Segoe 15", height = 4, width = 34).place(x=315,y=480)


    #Invocator
    vLogin.mainloop()

abrirVentanaPrincipal() #Invocacion
