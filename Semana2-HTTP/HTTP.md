### Peticiones HTTP

| Método | Función |
| ------ | ------ |
| **GET** | El método GET  solicita una representación de un recurso específico. Las peticiones que usan el método GET sólo deben recuperar datos. |
| **HEAD** | El método HEAD pide una respuesta idéntica a la de una petición GET, pero sin el cuerpo de la respuesta. |
| **POST** | El método POST se utiliza para enviar una entidad a un recurso en específico, causando a menudo un cambio en el estado o efectos secundarios en el servidor. |
| **PUT** | El modo PUT reemplaza todas las representaciones actuales del recurso de destino con la carga útil de la petición. |
| **DELETE** | El método DELETE borra un recurso en específico. |
| **CONNECT** | El método CONNECT establece un túnel hacia el servidor identificado por el recurso. |
| **OPTIONS** | El método OPTIONS es utilizado para describir las opciones de comunicación para el recurso de destino. |
| **TRACE** | El método TRACE  realiza una prueba de bucle de retorno de mensaje a lo largo de la ruta al recurso de destino. |
| **PATCH** | El método PATCH  es utilizado para aplicar modificaciones parciales a un recurso. |

### Respuestas HTTP
| Código | Significado |
| ------ | ------ |
| Códigos con formato 1xx | Respuestas informativas. Indica que la petición ha sido recibida y se está procesando. |
| Códigos con formato 2xx | Respuestas correctas. Indica que la petición ha sido procesada correctamente. |
| Códigos con formato 3xx | Respuestas de redirección. Indica que el cliente necesita realizar más acciones para finalizar la petición. |
| Códigos con formato 4xx | Errores causados por el cliente. Indica que ha habido un error en el procesado de la petición a causa de que el cliente ha hecho algo mal. |
| Códigos con formato 5xx | Errores causados por el servidor. Indica que ha habido un error en el procesado de la petición a causa de un fallo en el servidor. |
