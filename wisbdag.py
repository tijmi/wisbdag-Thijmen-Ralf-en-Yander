#door Thijmen de Groote, Yander van der Wurff en Ralf Bos
import math
x=0
aantalpi=0
aantalleeg=0
clostest1=0
aantalpibijg=0
aantalleegbijg=0
hoeveelverschil=3


while True:
  x+=math.pi
  aantalpi+=1
  if x>5:
    aantalleeg+=1
    x=x-5
    if abs(x-1)<hoeveelverschil:
        hoeveelverschil=abs(x-1)
        clostest1=x
        aantalleegbijg=aantalleeg
        aantalpibijg=aantalpi
        print("aantal kannen met pi gevuld= "+ str(aantalpibijg))
        print("aantal keer kan 5 liter leeggegooid= " + str(aantalleegbijg))
        print("getal =" + str(clostest1))
        print("het zit" + str(hoeveelverschil) "van 1 verwijderd")
        print("")
