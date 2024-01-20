a = 'Hello World!'
try:
 a + 10
except BaseException as error:
 print('Exception occurred: {}'.format(error))
 print('Exception occurred: {}'.format(type(error).__name__))


lIst = [5, 10, 20]
try:
 print(lIst[5])
except IndexError as error:
 print('Exception is: {}'.format(type(error).__name__))


