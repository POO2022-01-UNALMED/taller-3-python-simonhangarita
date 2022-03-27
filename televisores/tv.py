class TV:
  _numTV=0
  def __init__(self,marca,estado):
    self._marca=marca
    self._estado=estado
    self._canal =1
    self._precio=500
    self._volumen =1
    self._control
    TV._numTV +=1
    
  def setMarca(self,marca):
    self._marca=marca
  def setControl(self,control2):
    self._control =control2
  def setPrecio(self,precio2):
    self._precio=precio2
  def setVolumen(self,volumen2):
    if (self.getEstado() and 1<=volumen2 and volumen2<=120):
      self._volumen=volumen2
  def setCanal(self,canal2):
    if (self.getEstado() and 0<=canal2 and canal2<=7):
      self._canal=canal2
  def getMarca(self):
    return self._marca
  def getControl(self):
    return self._control
  def getPrecio(self):
    return self._precio
  def getVolumen(self):
    return self._volumen
  def getCanal(self):
    return self._canal
  def getNumTV(self):
    return TV._numTV
  def setNumTV(self,num):
    TV._numTV=num
  def turnOn(self):
    if(self._estado==False):
      self._estado=True
  def turnOff(self):
    if self._estado==True:
      self._estado=False
  def getEstado(self):
    return self._estado
  def canalUp(self):
    if self.getEstado() and self._canal!=120:
      self._canal+=1
  def canalDown(self):
    if self.getEstado() and self._canal!=1:
      self._canal -=1
  def volumenUp(self):
    if self.getEstado() and self._volumen!=7:
      self._volumen+=1
  def volumenDown(self):
    if self.getEstado() and self._volumen!=0:
      self._volumen-=1

  

  
  
    
    


  
  
    
    
    
      
    
    