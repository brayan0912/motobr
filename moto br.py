class moto():
    def __init__ (self,name):
        self.nombre = name
    def prender (self):
        print("prender la motora", self.nombre)
    def rebasar (self):
        print("pase al bañuelo", self.nombre)
    def curvear (self):
        print("sin miedo", self.nombre)

yamahar3 = moto ("Brian")
rtx150 = moto ("Carlos")

yamahar3.prender()
rtx150.prender()
rtx150.rebasar()
yamahar3.curvear()
rtx150.curvear()