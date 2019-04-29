import setlx


class map(setlx.SetlXClass):
    find = lambda k, self=None: self.mRelation[k]

    @staticmethod
    def insert(k, v, self=None):
        [k, v] = setlx.copy([k, v])
        self.mRelation[k] = setlx.copy(v)

    @staticmethod
    def delete(k, self=None):
        [k] = setlx.copy([k])
        self.mRelation[k] = None

    @staticmethod
    def f_str(self=None):
        return setlx.str(self.mRelation)

    def __init__(self):
        self.f_str = setlx.to_method(self, map.f_str, True)
        self.delete = setlx.to_method(self, map.delete, True)
        self.insert = setlx.to_method(self, map.insert, True)
        self.find = setlx.to_method(self, map.find, True)
        self.mRelation = setlx.Set()


telefonBuch = map()
telefonBuch.insert('hugo', 123)
telefonBuch.insert('anton', 345)
telefonBuch.insert('gustav', 678)
setlx.print(f'telefonBuch = {telefonBuch}')
setlx.print(f'telefonBuch.find("hugo")   = {telefonBuch.find(\'hugo\')}')
setlx.print(f'telefonBuch.find("anton")  = {telefonBuch.find(\'anton\')}')
setlx.print(f'telefonBuch.find("gustav") = {telefonBuch.find(\'gustav\')}')
telefonBuch.delete('hugo')
setlx.print(f'telefonBuch = {telefonBuch}')
setlx.print(f'telefonBuch.find("hugo")   = {telefonBuch.find(\'hugo\')}')
setlx.print(f'telefonBuch.find("anton")  = {telefonBuch.find(\'anton\')}')
setlx.print(f'telefonBuch.find("gustav") = {telefonBuch.find(\'gustav\')}')
