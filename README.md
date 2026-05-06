# Taller APIs y SSH
## Nombre: Juan Felipe Fajardo Garzón

Para esta práctica se hizo uso de una maquina virtual ubuntu en virtualBox, donde descargamos todos los archivos necesarios para ejecutar la API en la maquina virtual (incluyendo node js)

Primeramente en la máquina virtual revisamos la dirección IP para la conexión por SSH

![alt text](media/1.png)

En nuestro dispositivo original en powershell ejecutamos la conexión ssh e ingresamos la contraseña del usuario

![alt text](media/2.png)

Localizamos los archivos dentro de la máquina virtual

![alt text](media/3.png)

Iniciamos el servidor de la api con node js

![alt text](media/4.png)

Instalamos powershell classic para poder ejecutar los comandos en ubuntu con la misma sintaxis de powershell

![alt text](media/5.png)

Iniciamos powershell en linux

![alt text](media/6.png)

Creamos el usuario con la sintaxis dada

![alt text](media/7.png)

Obtenemos el token al hacer el login con el usuario creado anteriormente

![alt text](media/8.png)

Creamos la tarea de prueba

![alt text](media/9.png)

Modificamos el registro para poner la tarea nueva

![alt text](media/10.png)

Ahora vamos a realizar la eliminación de la tarea

![alt text](media/11.png)

Para verificar que efectivamente se eliminó la tarea, consultamos todo el endpoint y observamos que se encuentra vacío

![alt text](media/12.png)