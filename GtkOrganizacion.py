import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from reportlab.platypus import (SimpleDocTemplate,
                                PageBreak,
                                Image,
                                Spacer,
                                Paragraph,
                                Table,
                                TableStyle)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 13-04-2023")
        self.set_border_width(10)

        frmUsuarios = Gtk.Frame(label="Usuarios")
        lblNome = Gtk.Label(label="Nome")
        txtNome = Gtk.Entry()
        lblDni = Gtk.Label(label="Dni")
        txtDni = Gtk.Entry()
        lblDepartamento = Gtk.Label(label="Departamento")
        cmbDepartamento = Gtk.ComboBox()
        lblCorreoe = Gtk.Label(label="Correoe")
        txtCorreoe = Gtk.Entry()
        chkActivo = Gtk.CheckButton(label="Activo")


        frmPerfis = Gtk.Frame(label="Perfís aplicación")
        ntbPerfis = Gtk.Notebook()
        trvPerfis = Gtk.TreeView()
        trvTreeView = Gtk.TreeView()
        trvOperaciones = Gtk.TreeView()

        self.button = Gtk.Button(label="Xenerar informe")


        vboxArriba = Gtk.VBox()
        hboxHunoArriba = Gtk.HBox()
        hboxHdosArriba = Gtk.HBox()
        hboxHunoArriba.add(lblNome)
        hboxHunoArriba.add(txtNome)
        hboxHunoArriba.add(lblDni)
        hboxHunoArriba.add(txtDni)
        hboxHunoArriba.add(lblDepartamento)
        hboxHunoArriba.add(cmbDepartamento)
        hboxHdosArriba.add(lblCorreoe)
        hboxHdosArriba.add(txtCorreoe)
        hboxHdosArriba.add(chkActivo)
        frmUsuarios.add(hboxHunoArriba)
        frmUsuarios.add(hboxHdosArriba)
        vboxArriba.add(frmUsuarios)

        hboxAbajo = Gtk.HBox()
        vboxVabajoIzquierda = Gtk.vbox()
        vboxVabajoDerecha = Gtk.vbox()

        frmPerfis.add(vboxVabajoDerecha)
        frmPerfis.add(vboxVabajoIzquierda)

        hboxAbajo.add(frmPerfis)



        vboxMain = Gtk.VBox()
        vboxMain.add(vboxArriba)
        vboxMain.add(hboxAbajo)
        self.add(vboxMain)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Exame()
    Gtk.main()
