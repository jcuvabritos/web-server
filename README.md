# Servidor HTTP con WSGI en Python
---
## Juan Cruz Uva Britos
### GET, POST, PATCH y DELETE

- **GET**: se utiliza para **obtener** datos almacenados en el servidor.
- **POST**: se utiliza para **enviar** y **crear** un nuevo registro en el servidor, por lo que será necesario usar el cuerpo de la request (body).
- **PATCH**: se utiliza para **actualizar** solo una parte de un registro existente en el servidor. Al igual que en el POST, también vamos a utilizar el body para enviar estos datos.
- **DELETE**: **Elimina** un registro del servidor.

#### Idempotencia:
La idempotencia es una propiedad que nos dice que luego de ejecutar varias veces una misma request, el resultado final es el mismo que si solo hubiéramos ejecutado la operación una única vez.

Las operaciones GET, DELETE y PATCH son **idempotentes**:
- GET realiza consultas sin modificar el estado del servidor, por lo que ejecutar una misma consulta varias veces no se diferenciaría en nada de ejecutarla solo una vez.
- DELETE modifica de manera permanente el estado del servidor eliminando un recurso y lógicamente, no podemos borrar más de una vez un mismo dato.
- PATCH es una operación un poco más difícil de clasificar debido a que depende mucho del diseño de esta operación y al uso que se le de. Aún así, si la utilizamos solo para enviar el campo exacto que queremos modificar, la operación es idempotente ya que al ejecutar dos PATCH iguales, el segundo no cambia absolutamnete nada en el servidor.

La operación POST **no** **es idempotente**:
Como se mencionó anteriormente, al utilizar POST creamos un **nuevo** recurso en el servidor, es decir, que si ejecutamos dos POST exactamente iguales, estos van a crear dos recursos distintos entre sí, lo que nos deja el servidor en un estado completamente diferente a que si solo lo hubiéramos ejecutado una vez. 
