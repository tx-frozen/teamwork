#This class is used to store result after user finished the questionare.
class Trend:
    def __init__(self,keylist,valuelist):
        self.__error = False
        if (isinstance(keylist, list) == False or isinstance(valuelist, list) == False or keylist.__len__() != valuelist.__len__()):
            self.__error = True
            print('Error Param for initializing Trendency.')
            return
        self.length = valuelist.__len__()
        for i in range(0, self.length):
            if ((isinstance(valuelist[i], float) == False) and (isinstance(valuelist[i], int) == False)):
                print('Error Param(', valuelist[i], type(valuelist[i]), ') for Fruit!(', i, ')')
                return
        self.weight = {}
        for i in range(0,self.length):
            self.weight.setdefault(keylist[i],valuelist[i])
