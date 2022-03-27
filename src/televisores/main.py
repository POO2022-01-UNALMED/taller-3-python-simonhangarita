class Marca:
  def __init__(self,nombre):
    self.nombre=nombre
  def getNombre(self):
    return self.nombre
  def setNombres(self,nombre1):
    self.nombre=nombre1
class TV:
  numTV=0
  def __init__(self,marca,estado):
    self.marca=marca
    self.estado=estado
    self.canal =1
    self.precio=500
    self.volumen =1
    self.control
    TV.numTV +=1
    
  def setMarca(self,marca):
    self.marca=marca
  def setControl(self,control2):
    self.control =control2
  def setPrecio(self,precio2):
    self.precio=precio2
  def setVolumen(self,volumen2):
    if (self.getEstado() and 1<=volumen2 and volumen2<=120):
      self.volumen=volumen2
  def setCanal(self,canal2):
    if (self.getEstado() and 0<=canal2 and canal2<=7):
      self.canal=canal2
  def getMarca(self):
    return self.marca
  def getControl(self):
    return self.control
  def getPrecio(self):
    return self.precio
  def getVolumen(self):
    return self.volumen
  def getCanal(self):
    return self.canal
  def getNumTV(self):
    return TV.numTV
  def setNumTV(self,num):
    TV.numTV=num
  def turnOn(self):
    if(self.estado==False):
      self.estado=True
  def turnOff(self):
    if self.estado==True:
      self.estado=False
  def getEstado(self):
    return self.estado
  def canalUp(self):
    if self.getEstado() and self.canal!=120:
      self.canal+=1
  def canalDown(self):
    if self.getEstado() and self.canal!=1:
      self.canal -=1
  def volumenUp(self):
    if self.getEstado() and self.volumen!=7:
      self.volumen+=1
  def volumenDown(self):
    if self.getEstado() and self.volumen!=0:
      self.volumen-=1
class Control:
  def __init__(self,tv):
    self.tv=tv
  def turnOn(self):
    tv.turnOn()
  def turnOff(self):
    tv.turnOff()
  def canalUp(self):
    tv.canalUp()
  def canalDown(self):
    tv.canalDown()
  def setCanal(self,i):
    tv.setCanal(i)
  def enlazar(self,tv):
    self.tv=tv
    self.tv.setControl(self)
  def getTv(self):
    return self.tv
  def setTv(self,tv):
    self.tv=tv
  

  
  
    
    


  
  
    
    
    
      
    
    