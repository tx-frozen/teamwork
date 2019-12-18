from Store import Store
from Fruit import Fruit
from Trendency import Trend
from Error import ParamError
import xml.etree.ElementTree as xtree
import os

#This class is main class,now it does not contains online work,it works by reading a XML(HTML) I have stored in file named "page.html"
#and this file is searching "苹果".
#You can see how the list of store is been sorted and Print.
#Emmm,it may do bot work now?
class Analysis:
    @classmethod
    def main(self):

        #Check if the XML file exists.A Error would be thrown if file is missing.
        if(os.path.exists('NutritionList.xml')==False):
            print('Error:Missing XML FILE(NutritionList)')
            return
        if(os.path.exists('Fruit.xml')==False):
            print('Error:Missing XML FILE(Fruit)')
            return
        #Collecting the kind of nutrition
        dom = xtree.parse('NutritionList.xml').getroot()
        root = xtree.parse("Fruit.xml").getroot()
        #Compare the version of two XML file
        if(dom.attrib.get('version') != root.attrib.get('version')):
            print('Dismatch the version with NutritionList.xml(',dom.attrib.get('version'),
                  ') and Fruit.xml(',root.attrib.get('version'),').')
            return
        fruits = []
        fruitkeys = []
        try:
            for item in dom.getchildren():
                fruitkeys.append(item.attrib.get('id'))
            #Getting class and its instance from XML.
            for fruit in root:
                fruits.append(Fruit(fruit.tag,fruit.attrib))
        except BaseException as e:
            for i in e.args:
                print(i,end='')
            return

        #Pretending the trendency is already figured out.
        customervalue = [0.2,0.2,0.2,0.2,0.2,0.2,0.2]
        storelist = []
        trend = Trend(fruitkeys, customervalue)

        try:
            #apple = Fruit('Apple',fruitkeys, fruitvalue)
            ##fruit.append(apple)
            for item in fruits:
                item.Calculate(trend)
            #Pretending Searched from network and Assess by the way.
            storelist.append(Store('FuShi Apple Store',1.3,0,200,fruits[0],'http://www.baidu.com'))
            storelist.append((Store('ChangBai Apple Store',1,10,1000,fruits[1],'http://www.baidu.com')))
            storelist.append((Store('Bad Apple Store',100,1,1,fruits[2],'http://www.baidu.com')))
            #Stragegy all stores
            for item in storelist:
                #print(item.Calculate())
                item.Print()
            print('-----------------------------------------------------------------------------------------------'
                '----------------------------------------------------------------------')
            #Sort all stores
            storelist = sorted(storelist,key = lambda store:store.attr['score'], reverse = True)
            #Display!!!
            for item in storelist:
               item.Print()
        except ParamError as e :
            for i in e.args:
                print(i,end = '')


#Analysis.main()