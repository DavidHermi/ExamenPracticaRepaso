import gi
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, SimpleDocTemplate

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ControlerPerfisUsuarios import *


class MainWindow(Gtk.Window):

    # Constructor
    def __init__(self):
        Gtk.Window.__init__(self, title="Examen")
        self.set_border_width(10)

        mainLayout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

        # region Usuarios

        usuariosBox = Gtk.Box()

        dniLabel = Gtk.Label("Dni")

        self.dniEntry = Gtk.Entry()

        usuariosBox.pack_start(dniLabel, True, True, 0)
        usuariosBox.pack_start(self.dniEntry, True, True, 0)

        mainLayout.pack_start(usuariosBox, True, True, 0)

        # endregion

        # region FrameAplicacions

        frameAplicacions = Gtk.Frame()

        boxFrame = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        gridEntry = Gtk.Grid()

        # Entry y botonoes

        entry1 = Gtk.Entry()
        entry2 = Gtk.Entry()
        entry3 = Gtk.Entry()
        entry4 = Gtk.Entry()
        entry5 = Gtk.Entry()

        listaPermisos=customQuery("SELECT nomePerfil FROM perfis")

        entry1.set_text(listaPermisos[0][0])
        entry2.set_text(listaPermisos[1][0])
        entry3.set_text(listaPermisos[2][0])
        entry4.set_text(listaPermisos[3][0])


        check1 = Gtk.CheckButton()
        check2 = Gtk.CheckButton()
        check3 = Gtk.CheckButton()
        check4 = Gtk.CheckButton()
        check5 = Gtk.CheckButton()

        check1.connect("toggled", self.checkPerfil)
        check2.connect("toggled", self.checkPerfil)
        check3.connect("toggled", self.checkPerfil)
        check4.connect("toggled", self.checkPerfil)
        check5.connect("toggled", self.checkPerfil)



        gridEntry.attach(entry1, 0, 0, 2, 1)
        gridEntry.attach(entry2, 0, 1, 2, 1)
        gridEntry.attach(entry3, 0, 2, 2, 1)
        gridEntry.attach(entry4, 0, 3, 2, 1)
        gridEntry.attach(entry5, 0, 4, 2, 1)

        gridEntry.attach(check1, 2, 0, 1, 1)
        gridEntry.attach(check2, 2, 1, 1, 1)
        gridEntry.attach(check3, 2, 2, 1, 1)
        gridEntry.attach(check4, 2, 3, 1, 1)
        gridEntry.attach(check5, 2, 4, 1, 1)

        boxFrame.pack_start(Gtk.Label("Aplicacions/perfis"), True, True, 0)
        boxFrame.pack_start(gridEntry, True, True, 0)

        mainLayout.pack_start(boxFrame, True, True, 0)

        # endregion

        #region treeview

        self.perfisListStore=Gtk.ListStore(str,int)

        self.treeView = Gtk.TreeView(self.perfisListStore)

        for i, colTitle in enumerate(["Perfil", "Permiso"]):

            render = Gtk.CellRendererText()

            column = Gtk.TreeViewColumn(colTitle, render, text=i)

            self.treeView.append_column(column)

        #Endregion


        #region notebook

        self.notebook = Gtk.Notebook()

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(self.treeView)
        self.notebook.append_page(self.page1, Gtk.Label("Perfís"))

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label())
        self.notebook.append_page(self.page1, Gtk.Label("Modulos Internos"))

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label())
        self.notebook.append_page(self.page1, Gtk.Label("Operaciones"))

        mainLayout.pack_start(self.notebook, True, True, 0)

        #endregion

        #region informe

        self.button = Gtk.Button(label="Informe")
        self.button.connect("clicked", self.buttonClicked)

        mainLayout.pack_start(self.button, True, True, 0)


        #endregion



        self.add(mainLayout)


    def checkPerfil(self, widget):

        self.perfisListStore.clear()
        dni=self.dniEntry.get_text()

        listaPermisos=customQuery("SELECT permiso from perfisUsuario where dniUsuario=?",dni)
        listaNomePerfis=customQuery("select nomePerfil from perfis where idPefil=(select idPerfil from perfisUsuario where dniUsuario=?)",dni)

        perfilPermiso=[listaNomePerfis[0][0],listaPermisos[0][0]]

        self.perfisListStore.append(list(perfilPermiso))


    def buttonClicked(self, widget):
        doc = SimpleDocTemplate('Examen.pdf', pagesize=A4)
        operacions = []

        datos = customQuery(
            "select dni,nome,departamento,correoe,perfis.nomePerfil,perfisUsuario.permiso from usuarios left join perfisUsuario on usuarios.dni= perfisUsuario.dniUsuario left join perfis on perfisUsuario.permiso=perfis.idPefil")

        datosCabecera=[("DNI","Nome","Departamento","Correoe","Nome Perfil", "Permiso")]

        for dato in datos:
            datosCabecera.append(dato)


        taboa = Table(datosCabecera, colWidths=100, rowHeights=30)


        operacions.append(taboa)

        doc.build(operacions)



Window = MainWindow()
Window.connect("delete-event", Gtk.main_quit)
Window.show_all()
Gtk.main()
