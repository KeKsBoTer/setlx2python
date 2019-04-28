import setlx


class map:
    find = lambda k, self=None: self.mRelation[k]

    @staticmethod
    @setlx.procedure
    def insert(k, v, self=None):
        self.mRelation[k] = v

    @staticmethod
    @setlx.procedure
    def delete(k, self=None):
        self.mRelation[k] = None

    @staticmethod
    @setlx.procedure
    def f_str(self=None):
        return setlx.str(self.mRelation)

    @setlx.procedure
    def __init__(self):
        self.f_str = setlx.to_method(self, map.f_str)
        self.delete = setlx.to_method(self, map.delete)
        self.insert = setlx.to_method(self, map.insert)
        self.find = setlx.to_method(self, map.find)
        self.mRelation = mRelation = setlx.Set()


telefonBuch = map()
telefonBuch.insert('hugo', 123)
telefonBuch.insert('anton', 345)
telefonBuch.insert('gustav', 678)
setlx.print(f'telefonBuch = {telefonBuch}')
setlx.print(f'telefonBuch.find(\\"hugo\\")   = {telefonBuch.find(\'hugo\')}')
setlx.print(f'telefonBuch.find(\\"anton\\")  = {telefonBuch.find(\'anton\')}')
setlx.print(f'telefonBuch.find(\\"gustav\\") = {telefonBuch.find(\'gustav\')}')
telefonBuch.delete('hugo')
setlx.print(f'telefonBuch = {telefonBuch}')
setlx.print(f'telefonBuch.find(\\"hugo\\")   = {telefonBuch.find(\'hugo\')}')
setlx.print(f'telefonBuch.find(\\"anton\\")  = {telefonBuch.find(\'anton\')}')
setlx.print(f'telefonBuch.find(\\"gustav\\") = {telefonBuch.find(\'gustav\')}')

