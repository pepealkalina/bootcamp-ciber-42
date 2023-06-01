# Tsunami preina-g

El tsunami consiste en abrir la  calculadora de windows xp a  traves de un programa vulnerable generando un bufferoverflow introduciendo codigo a traves de este.

Lo primero que hay que hacer es crear un programa vulnerable, en este caso es vuln.c, que contiene la funcion strcpy() esta al no controlar el numero de bytes que copia es bulnerablepor lo que se puede copiar mas de los establecidos en un buffer inicial.

El siguiente paso es averiguar el codigo para ejecutar la calculadora, a traves de ensamblador  creamos un codigo que nos dara los bytes necesarios para ejecutar kernel32.dll, la libreria donde se encuentra la funcion system(), y los bytes para ejecutar el programa calc.exe que es la caculadora.
El codigo se encuentra en shellcode.c. Estos bytes se encuentran en shellcode.obj cuando lo pasas a hexadecimal.

Para codificar nuesttro tsunami necesitamos un JMP ESP que se una salto en la pila para asi poder ejecutar nuestro codigo el cual estamos sobrescribiendo en nuestro programa vulnerable