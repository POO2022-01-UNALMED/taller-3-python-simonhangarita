from televisores.tv import TV
class Control:
  def __init__(self):
    self._tv=0
  def turnOn(self):
    self._tv.turnOn()
  def turnOff(self):
    self._tv.turnOff()
  def canalUp(self):
    self._tv.canalUp()
  def canalDown(self):
    self._tv.canalDown()
  def setCanal(self,i):
    self._tv.setCanal(i)
  def enlazar(self,tv):
    self._tv=tv
    self._tv.setControl(self)
  def getTv(self):
    return self._tv
  def setTv(self,tv):
    self._tv=tv