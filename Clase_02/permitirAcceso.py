# Vamos a importar
# la libreria que frena la ejecucion asi:
import time

# Vamos a declarar algunas variables globales
passwordFile = open('contraSecreta.txt')
secretPassword = passwordFile.read()

# Pedimos la contrasenia al usuairo
print('Ingresa tu contrasenia: ')
typedPassword = input()

# Comparamos que sea igual a la del 
# archivo de texto
if typedPassword == secretPassword:
    print('Acceso autorizado')

# Nos burlamos si es del 1 al 5 corrido
if typedPassword == '12345':
    print('Esa contrasenia no es Willy!.')
else:
    # Y si no es la del archivo
    # no le damos acceso
    print('Acceso no autorizado')

# Paramos la ejecucion para que no se cierre
time.sleep(10000)