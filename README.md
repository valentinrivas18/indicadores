Fecha de documentacion: 22/04/2024

- El error de dividir por cero ya fue corregido, el programa cumple con las expectativas, todos los resultados son igual a 0 cuando para dicha carrera no se ha realizado ninguna solicitud.

- La plantilla para crear los pdf ya funciona, solamente hace falta organizar los pdfs como tal, todavia no se decide si se crean 10 pdfs y luego se unen, o se crea 1 solo pdf de 10 paginas, mañana se trabajara con eso.

Fecha de documentacion: 21/04/2024

El programa ya esta casi terminado, las unicas cosas que le faltan son las siguientes:

- Crear una plantilla para crear los PDFs: El codigo para crear los pdf ya esta, sin embargo, quiero crear un esqueleto para crear una funcion que tenga un metodo que solamente me pida ingresar el numero de la carrera, y que automaticamente genere
  el pdf en base a esa carrera, ejemplo, si yo escribera
  d = plantilla.plant(101)
  automaticamente ese objeto creara el pdf de la carrera que tiene por nombre 101, entonces, de esta manera solo necesitaria escribir 10 lineas de codigo (porque son 10 carreras), o quiza con un ciclo for, pero el punto es, solamente con 1 objeto
  crear el pdf reemplazando los parametros, ya que eso es lo unico que va a variar, el parametro de la carrera, lo demas sera todo igual porque esta todo en la misma tabla

- Corregir el error de dividir por cero: Resulta que para aquellas carreras que tienen 0 solicitudes, la funcion del porcentaje intenta dividir las solicitudes de una solicitud entre el total de solicitudes, y cuando ambas son cero, el programa
  logicamente arroja un error porque 0/0 da cero, la solucion que se busca es que simplemente cuando la division sea 0/0, simplemente pase por alto esa tabla y que deje que todos sus valores sean 0, o que simplemente no la genere.
  La solucion que yo tenia en mente era la siguiente, con una excepcion verificar si se esta diviendo 0/0 y de ser asi, ignorar el codigo y simplemente no imprimir el pdf, o imprimir el pdf pero que todo sea 0.

- Permitir solamente numeros enteros en la ventana de agregar solicitud: En esta ventana el usuario es libre de ingresar el numero de cedula de quien realiza la solicitud, sin embargo, la caja de texto permite como dato de entrada cadenas de texto,
  lo cual no debe ser asi, entonces, lo que se quiere es que solamente el usuario pueda ingresar numeros enteros y que la longitud de ese numero no sea mayor a 8 digitos ya que las cedulas no exceden 8 digitos.

- Enumerar las paginas del pdf: Se busca que todas los reportes de los diferentes subprogramas(carreras) esten dentro del mismo archivo pdf, por lo tanto, sera necesario que cada pagina este enumerada.

- Rediseñar la interfaz grafica: No hay mucho que añadir, la interfaz esta fea y solo esta alli para propositos funcionales.

- Añadir un boton que permita limpiar la base de datos: Es decir, borrar todas las solicitudes hechas para que asi se puedan insertar los datos del nuevo periodo academico y asi no se unan los datos del semestre pasado con el actual, en pocas palabras,
  añadir un boton que elimine todos los datos de la tabla que almacena las solicitudes.

