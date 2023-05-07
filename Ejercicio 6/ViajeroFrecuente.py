class ViajeroFrecuente:
    def __init__(self, num, dni, nombre, apellido, millas=0):
        self.numero = num
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.millas_acumuladas = millas
    
    def __gt__(self, otro_viajero):
        return self.millas_acumuladas > otro_viajero.millas_acumuladas
    
    
    def __add__(self, millas):
       self.millas_acumuladas += millas
       return self.__class__(self.numero, self.dni, self.nombre, self.apellido, self.millas_acumuladas)
   
    def __sub__(self, millas):
        if self.millas_acumuladas - millas < 0:
            raise ValueError("No se pueden canjear más millas de las que se tienen acumuladas.")
        self.millas_acumuladas -= millas
        return self.__class__(self.numero, self.dni, self.nombre, self.apellido, self.millas_acumuladas)