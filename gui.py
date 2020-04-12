import tkinter as tk
import tkinter.ttk as ttk
from sense_emu import SenseHat

sense = SenseHat()

class hatgui:
    def __init__(self):
        self.Valor=0
        self.Periodo=1000
        self.ventana=tk.Tk()
        self.ventana.title("Practica sensehat GUI")
        # Menu
        self.menubar = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menubar)
        self.opciones = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Opciones", menu=self.opciones)
        self.opciones.add_command(label="Configurar", command=self.ventanaconfig)
        self.opciones.add_separator()
        self.opciones.add_command(label="Salir", command=self.ventana.quit)
        # Tabs
        self.tabs = ttk.Notebook(self.ventana)
        self.tabMonitor = ttk.Frame(self.tabs)
        self.tabs.add(self.tabMonitor, text="Monitorización")
        self.tabs.grid(column=0, row=0)
        # Label control
        self.lfcontrol=ttk.LabelFrame(self.tabMonitor, text="Control")
        self.lfcontrol.grid(column=0, row=0, padx=10, pady=10)
        self.control()
        # Label medidas
        self.lfmedidas=ttk.LabelFrame(self.tabMonitor, text="Medidas:")
        self.lfmedidas.grid(column=0, row=2, padx=5, pady=10)
        self.medidas()
        # Listado datos históricos
        self.lftableHist = tk.LabelFrame(self.tabMonitor, text="Historico:")
        self.lftableHist.grid(column=0, row=4, padx=5, pady=10)
        self.listahistorico()
        # Launch
        self.ventana.mainloop()

    def control(self):
        self.boton=ttk.Button(self.lfcontrol, text="Iniciar", command=self.getValue)
        self.boton.grid(column=0, row=0)
        self.labelperiodo=ttk.Label(self.lfcontrol, text="Periodo: ")
        self.labelperiodo.grid(column=0, row=1)
        self.labelperiodovalue=ttk.Label(self.lfcontrol, text="1000")
        self.labelperiodovalue.grid(column=1, row=1)

    def medidas(self):
        self.Dato=ttk.Label(self.lfmedidas, text=self.Valor)
        self.Dato.grid(column=1, row=1)
        self.Metrica=tk.IntVar(value=1)
        self.radTemp=tk.Radiobutton(self.lfmedidas, text="Temperatura",variable=self.Metrica, value=1)
        self.radTemp.grid(column=0, row=2)
        self.radPres=tk.Radiobutton(self.lfmedidas, text="Presión",variable=self.Metrica, value=2)
        self.radPres.grid(column=1, row=2)
        self.radHum=tk.Radiobutton(self.lfmedidas, text="Humedad",variable=self.Metrica, value=3)
        self.radHum.grid(column=2, row=2)

    def listahistorico(self):
        self.listaH = ttk.Treeview(self.lftableHist, columns=4, height=12)
        self.listaH.grid(row=4, column=0, columnspan=3)
        self.listaH["columns"] = ('Valor', 'Fecha', 'Tipo')
        self.listaH.heading('#0', text='#Num')
        self.listaH.heading('Valor', text='Valor')
        self.listaH.heading('Fecha', text='Fecha/Hora')
        self.listaH.heading('Tipo', text='Tipo')
        # Botones inferiores
        self.botlimpiar = tk.Button(self.lftableHist, text='Limpiar', command=self.limpiarListaH())
        self.botlimpiar.grid(row=5, column=0, sticky=tk.E+tk.W)
        self.botcalcmedia = tk.Button(self.lftableHist, text='Calcular Media', command=self.limpiarListaH())
        self.botcalcmedia.grid(row=5, column=1, sticky=tk.E+tk.W)
        self.botexportar = tk.Button(self.lftableHist, text='Exportar', command=self.limpiarListaH())
        self.botexportar.grid(row=5, column=2, sticky=tk.E+tk.W)

    def limpiarListaH(self):
        pass

    def getValue(self):
        if self.Metrica.get()==1: # Temp
            self.getValueTemp()
        if self.Metrica.get()==2: # Pres
            self.getValuePres()
        if self.Metrica.get()==3: # Hum
            self.getValueHumed()
        pass

    def getValueTemp(self):
        self.Valor=sense.temp
        self.Dato.configure(text=self.Valor)

    def getValuePres(self):
        self.Valor=sense.pressure
        self.Dato.configure(text=self.Valor)

    def getValueHumed(self):
        self.Valor=sense.humidity
        self.Dato.configure(text=self.Valor)

    def guardarPeriodo(self,Periodo):
        PerValue=Periodo
        self.labelperiodovalue['text']=str(PerValue)
        self.Periodo=PerValue
        self.ventanaconfig1.destroy()

    def ventanaconfig(self):
        # TODO
        self.ventanaconfig1=tk.Tk()
        self.ventanaconfig1.title("Configuración")
        self.ventanaconfig1.geometry("280x120")
        self.labelgetperiodo=ttk.Label(self.ventanaconfig1, text="Introduce el valor de Periodo: ")
        self.labelgetperiodo.grid(column=0, row=1)
        CustomPeriodo=tk.StringVar()
        self.entrygetperiodo=ttk.Entry(self.ventanaconfig1, width=10, textvariable=CustomPeriodo)
        self.entrygetperiodo.grid(column=1,row=1)
        self.botonguardar=ttk.Button(self.ventanaconfig1, text="Guardar", command=lambda: self.guardarPeriodo(CustomPeriodo))
        self.botonguardar.grid(column=0, row=2, sticky=tk.W)
        self.ventanaconfig1.mainloop()

#### MAIN ####
aplicacion1=hatgui()