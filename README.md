# Basic SpeedTest


Basic SpeedTest tiene como objetivos llevar un registro de su servicio proveedor de internet de la siguiente
manera. Básicamente esto enmarca tres servicios, uno es el 'speedtest cli' ofrecido por Ookla Brands que
realiza una medición de Bajada, Subida y pérdida de paquetes cada determinada cantidad de tiempo. Estos datos
son pasados al segundo servicio MySql (una base de datos relacional) para ser almacenados y poder
ser visualizados de manera gráfica en nuestro tercer servicio Grafana.

Dentro de la base de datos también se guardan el 'serverName' donde se está realizando la medición junto
a su 'isp' que hace referencia al ID del servidor invocado y la 'url' con el registro para ser visualizado
en la página de Ookla. Todo esto puede ser un dato relevante si desea realizar un reclamo a su proveedor
de internet exportando toda la información necesaria desde el panel de Grafana en diferentes formatos.






## Puesta en marcha

Paso 1

Primero debe realizar una copia del archivo 'envExample' dentro de otro con el nombre '.env' (sin comillas, y
es fundamental no olvidar el punto '.' delante como parte del nombre del archivo). Esto es muy importante, ya
que dentro se encuentran todo el set de configuración. Tómese un tiempo para revisar este archivo y evaluar
si desea modificar algún valor.



Paso 2

Para iniciar solo debe ejecutar el siguiente comando:

docker compose up -d

Para detener el servicio:

docker compose down



## ENVIRONMENTS

A continuacion se detalla el set de variables y referencias:

MySql (base de datos)

ROOT_PASS=securerootpassword -> contraseña para el usuario root
DB_NAME=db -> nombre de la base de datos                  
DB_USER=dbuser -> usuario 
PASS=secret -> contraseña, es RECOMENDABLE QUE MODIFIQUE ESTO
TIME_ZONE=America/Argentina/Buenos_Aires -> zona horaria



speedtest cli

TIME_SPEEDTEST=10 -> cada cuanto tiempo se realizara la medicion (en minutos)



Grafana

GRAFANA_USER=gfuser -> usuario pordefecto para ingresar al panel, puede modificarlo por uno de su agrado.
GRAFANA_PASS=gfsecret -> contraseña por defecto, se recomienda modificarla.
GF_PORT=3001 -> puerto por defecto donde Grafana es invocado desde su navegador. 

Ej: http://localhost:3001 -> si lo esta corriendo en su maquina.

Ej: http://ipServidor:3001 -> si lo esta corriendo desde un servidor.
