


def KelvinToFahrenheit(Temperature):
    #
   assert (Temperature >= 0),"Exception created to test"
   return ((Temperature-273)*1.8)+32
try:
    print (KelvinToFahrenheit(-1))
    print (int(KelvinToFahrenheit(505.78)))
#print (KelvinToFahrenheit(-5))
except AssertionError as e:
    print("In assertion block",e)