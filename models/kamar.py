print("hello world")
#membuat class kamar sebagai base class 
class Kamar:
    #membuat constructor untuk class kamar dengan atribut nomor :str, dan harga :float
    def __init__(self, nomor:str, harga:float):
        self.nomor = nomor
        self.harga = harga
    
    #membuat method harga @property*	Getter: kembalikan _harga.
    @property
    def harga(self):
        return self._harga
