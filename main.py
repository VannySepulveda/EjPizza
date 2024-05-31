
from masa import tipo_masa 
from salsa import tipo_salsa
from add import agregar_ingrediente
from remove import quitar_ingrediente
from tiempo import estimar_tiempo
from show import mostrar_ingredientes
from  datos import *
import time
import os
import sys

clear ='cls' if sys.platform=='win32' else 'clear'
os.system(clear)
ingredientes_orden = ingredientes

print("---¡GRACIAS POR ORDENAR CON NOSOTROS!---")
print(f'Nuestra pizza base es : {ingredientes_orden}') 
while True:
   opcion=int(input(menu))
   if  opcion == 1:
         os.system(clear)    
         print (type(opcion), opcion)    
         eleccion=input(T_MASA).upper()
         ingredientes_orden=tipo_masa(ingredientes_orden,eleccion)
         print('')
   elif  opcion == 2:
         os.system(clear)
         print (type(opcion), opcion)  
         eleccion=input(T_SALSA).upper()
         ingredientes_orden=tipo_salsa(ingredientes_orden,eleccion)
         print('')
   elif  opcion == 3:
         os.system(clear)
         print (type(opcion), opcion) 
         eleccion=int(input(AG_INGREDIENTE))
         ingredientes_orden=agregar_ingrediente(ingredientes_orden,eleccion)
         print('')
   elif  opcion == 4:      
         os.system(clear)
         print (type(opcion), opcion) 
         eleccion=int(input(QT_INGREDIENTE))
         ingredientes_orden=quitar_ingrediente(ingredientes_orden,eleccion)
         print('')
   elif  opcion == 5:
         print (type(opcion), opcion) 
         os.system(clear)
         print ("Gracias por ordenar con Pizzas JAT")
         print ("Disfrute su Pizza ^.^")
         mostrar_ingredientes(ingredientes_orden)
         estimar_tiempo(ingredientes_orden)
         print ("\n\ ^.^ Disfrute su Pizza ^.^")
   else:
          os.system(clear)   
          print("Su pedido ha sido cancelado, gracias por contactarse con Pizza JAT")
          time.sleep(3)
          exit()