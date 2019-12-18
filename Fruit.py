from Trendency import Trend
from Error import ParamError

#This class is for fruit.It has method that construction a default object by Fruit().
#Besides,the name of method says all.

class Fruit:



    def __init__(self,name,nutrition):
        self.__error = False
        if(isinstance(nutrition, dict)== False):
            self.__error = True
            raise ParamError('Error Param for initializing Fruit.')
        self.attr = {'name':name,'nutrition': {}, 'score':0}
        #for i in nutrition.keys():
            #print(float(nutrition.get(i)))
            #if((isinstance(nutrition.get(i), float) == False) and (isinstance(nutrition.get(i), int) == False)):
            #    raise ParamError('Error Param('+str(nutrition.get(i))+str(type(nutrition.get(i)))+') for Fruit!('+i+')')

        self.attr['nutrition'] = nutrition

    def __init__(self):
        self.attr = {}
        self.name = 'Apple'
        self.attr.setdefault('VA', 0.4)
        self.attr.setdefault('VB', 0.7)
        self.attr.setdefault('VC', 1)
        self.attr.setdefault('VD', 0.1)
        self.attr.setdefault('Sugar', 0.5)
        self.attr.setdefault('Protein', 0.1)
        self.attr.setdefault('Fibre', 0.9)
        self.attr.setdefault('score',0)

    def Calculate(self,Trend):
        #Calculating the score each kind of fruit with collected trendency
        self.attr['score'] = 0
        for i in self.attr['nutrition'].keys():
            if(Trend.weight.get(i) == None):
                #raise BaseException('Default value:',i)
                self.attr['score'] = -9999
                return -9999;
            self.attr['score'] +=  float(Trend.weight.get(i)) * float(self.attr['nutrition'].get(i))
        return self.attr['score']

    def Print(self):
        print('<CLASS Fruit> ',self.attr)

    def ToString(self):
        return '<CLASS Fruit> ' + str(self.attr)
