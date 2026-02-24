# Reflexión video STRIDE
## Enlace video: https://www.youtube.com/watch?v=J3V4x5QtFus
## Nombre: Juan Felipe Fajardo Garzón
## Resumen
 En la época actual, la ciberseguridad es uno de los apsectos más esenciales a la hora de diseñar cualquier sistema, para ello es fundamental conocer las amenazas a las cuales se puede enfrentar nuestro sistema o software, este proceso de identificar amenazas se conoce como threat modeling.

 Dentro del modelado de amenzas, existe una acrónimo que nos permite clasificar las amenzas según su tipo, este se conoce como el modelo STRIDE

 ## STRIDE
 ### Spoofing

El spoofing o suplantación es cuando un atacante finge ser otra persona o sistema, usualmente con el fin de acceder al sistema victima violando sus sistemas de autenticidad

### Tampering

El tampering consiste en modificar datos almacenados sin autorización, lo cual afecta la integridad de los mismos

### Repudiation

El repudio es cuando un dispositivo, persona o sistema realiza la acción y no reconoce haberla hecho, usualmente por falta de logs o documentación que relacionen acción con actor

### Information Disclosure

Ocurre cuando información sensible o privada es expuesta, violando la confidencialidad de la misma

### Denial of Service

La denegación del servicio ocurre cuando se sobrecargan dispositivos o se interrumpe su funcionamiento, esto genera que los sistemas no se encuentren disponibles todo el tiempo planeado

### Elevation of Privileg

Es cuando un atacante obtiene permisos y acceso no autorizado a funcionalidades exclusivas y de alto nivel

## Acciones a tomar para evitar cada ataque

 ### Spoofing

Utilizar "certificados" y otros métodos de autenticación

### Tampering

Monitorear constantemente la información y realizar validaciones de los cambios en esta

### Repudiation

Llevar registros de sistema sobre cada acción que se realiza en la red y su actor

### Information Disclosure

Encriptar la información y gestionar accesos a la misma 

### Denial of Service

Mantener un control del flujo de paquetes y distribuir la carga, por ejemplo de servidores, entre varios dispositivos

### Elevation of Privileg

Mantener ususarios y esquema de cero privilegios, o privilegios bajos