class Company:
    levels={1:'junior',2:'middle',3:'senior',4:'lead'}
    def __init__(self,index):
        self._index=index
        self._levels=Company.levels[self._index]
    def _level_up(self):
        self._index+=1
        self._levels=Company.levels[self._index]
    def is_lead(self):
        if self._levels=='lead':    print('final level')
class Programmer(Company):
    def __init__(self,name,age,index):
        super().__init__(index)
        self.name=name
        self.age=age
        self.index=index
    def work(self):
        print('working...')
        return self._level_up()
    def info(self):
        return [self.name,self.age,self._index]
    @staticmethod
    def knowlege_base():
        print('welcome to hell')
Oksana=Programmer('Oksana',31,1)
print(Oksana.info())
Oksana.work()
print(Oksana.info())
Programmer.knowlege_base()
