__author__ = 'cristian'

import data
import pilas
import duinobot


class OpcionLibre():
    def __init__(self,config):
        self.config=config
        self.time()
        self.speed()
        tarea=pilas.mundo.agregar_tarea_siempre(1,self._ok)

    def time(self):
        self.time=pilas.interfaz.IngresoDeTexto(self.config.timevirtual,x=350,y=250)
        self.time.solo_numeros()

    def speed(self):
        self.speed=pilas.interfaz.IngresoDeTexto(self.config.speedvirtual,x=350,y=150)
        self.speed.solo_numeros()

    def _ok(self):
        self.config.speedvirtual=int (self.speed.texto)
        self.config.timevirtual=int(self.time.texto)
        return True
