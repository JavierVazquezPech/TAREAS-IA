### 1. Asistente virtual de voz.

- **Performance:** Lograr captar con exactitud lo que la persona diga para realizar la acción que se le pida por medio de la voz,
                   sin que este realice una acción completamente diferente.
- **Environment:** Casa donde hay flujo de personas y ruidos.
- **Actuators:** Encender y apagar electrodomesticos, Reproductor de música o video, cambiar o ponerle pausa, 
	         contestar preguntas que se le pueda hacer.
- **Sensors:** Micrófono, acceso a internet, acceso a las cuentas de las plataformas de música y video.

El environmentt es determinista, ya que el entorno no influye en las decisiones que se tomará, ya que el agente hará exactamente
lo que se le pida, es Episódico, porque una acción es independiente a otra, y discreto porque el agente ya tiene programado las acciones que hará.
 
### 2. Robot aspirador doméstico.
- **Performance:** Limpiar eficazmente el polvo y suciedad del suelo de la habitación donde opere, retirar la suciedad acumulada de su compartimiento en su estación para que siga funcionando, o mandar alerta que ya se llenó para que le retiren la basura.
- **Environment:** Habitación habitada por personas que salen y entran de la casa y puede que haya mascotas, que dejan residuos de polvo y pelo.
- **Actuators:** Succionar la suciedad que se detecte, moverse libremente en la habitación, esquivar obstaculos que se encuentre.
- **Sensors:** Camara que detecte donde esta limpio o sucio, sensor para checar si su compartimiento de basura ya esta lleno.

El environment es parcialmente observable, porque no sabe si en habitaciones cerradas hay suciedad, es episódicoy determinista ya que solo tiene dos estados, sucio o limpio,
es discreto ya que esta bien definido los estados y el momento para actuar.

### 3. Sistema de recomendación de streaming.

- **Performance:** De acuerdo a su historial, recomendar lo que le pueda interesar o gustar al usuario.
- **Environment:** Aplicación de streaming que esta en reproducción y puede depender del estado de animo del usuario.
- **Actuators:** Recomendar de forma de mensaje, notificación o sugerencia de "lo que podrias ver" en alguna sección de la aplicación.
- **Sensors:** Historial de Canciones, videos, peliculas o series vistas, analizador de lista de "ver más tarde" o "me gusta" y de generos que más ha visto o escuchado.

El environment es Dinámico porque los gustos puede cambiar de un momento a otro mientras el agente los analiza, es Determinista ya que no influye nada de forma de azar o suerte,
y es discreto ya que son estados fijos y definidos "lo que le puede gustar y lo que no le puede gustar".

### 4. Vehículo autónomo en ciudad.

- **Performance:** Llevar al pasajero de forma seguera y confortante a su destino, sin causar accidentes.
- **Environment:** La ciudad donde transitará el automovil, el tráfico que hay y los peatones que puedan estar cruzando.
- **Actuators:** Frenar, aceleradar, realizar un giro, estacionarse, respetar los señalamientos y reglas de transito, esquivar autos y baches, y detenerse si cruza
inesperadamente una persona, auto o animalito.
- **Sensors:** Camaras, gps, sensores de aceite, nivel de la llanta, termometro dentro del auto, sensores de movimiento.

El environment es parcialmente observable, ya que no se sabe que puede haber adelante de otro auto o si un arbol tapa a una persona, es estocástico porque hay factores de suerte que influyen como el clima, o la forma
de conducir de los humanos, es dinámico, porque el ambiente cambia constantemente mientras el auto se mueve, y es continuo porque las variaables van cambiando constantemente, (velocidad, tráfico, personas, etc.).

### 5. Agente de trading algorítmico en bolsa.

- **Performance:** Invertir y retirar inversión o vender dependiendo del estado de la bolsa.
- **Environment:** Páginas y aplicaciones de trading en la bolsa.
- **Actuators:** Invertir cuando haya el potencial y retirarse ymandar un alerta cuando se vea un peligro de perder lo invertido.
- **Sensors:** Analizador de gráficas.

El environment es Estocáisco ya que hay bolsas que son muy volatiles y a pesar que hay formulas matemáticas para analizar y medir, siempre hay factores fuera del alcance que afecten,
es dinámico, porque es un ambiente que va cambiando constantemente mientras el agente piensa.

### 6. Sistema de diagnóstico médico asistido por IA.

- **Performance:** Detectar enfermedades de manera precisa analizando sintomas e imágenes clinicas, disminuir los diagnósticos erroneos que puedan cometer los doctores ya que la computadora tiene mejor retención de memoría. 
- **Environment:** Hospitales y consultorios médicos donde al día se atienden cientos de personas, que tiene recopilado en su base de datos enfermedades con sintomas y un historial de sus pacientes.
- **Actuators:** Analizar sintomas, analizar historial del paciente, analizar imágenes clinicas, recopilar información de posibles enfermedades y dar el diagnostico final.
- **Sensors:** Camara para el analisis de imágenes, tener acceso a la base de datos del hospital para tener información del paciente y la información de las enfermedades.

El environment es determinista ya que se puede determinar de forma exacta una enfermedad al menos que sea nueva o super rara, es episódico porque el analisis de un paciente no debe afectar al de otro,
estático, los síntomas no cambian mientras el agente piensa.

### 7. Dron de inspección de infraestructura.

- **Performance:** Detectar fallos que puedan poner en peligro una estructura o construcción con la ayuda de los planos.
- **Environment:** Edificios en construcción o edificios que se necesita saber si tuvieron afectaciones durante un desastre natural.
- **Actuators:** Escanear la estructura, para ver si hay grietas, detectar la humedad para saber si hay fugas, y revisar si hay fallas electricas en la cableria.
- **Sensors:** Cámara, sensor de humedad, sensor infrarojo, multimetro para checar las lineas electricas.

El environment es parcialmente observable, ya que no se puede saber que hay dentro de todas las paredes, es estático ya que no hay una fuerza que haga que cambie el entorno constantemente.

### 8. Agente jugador de ajedrez

- **Performance:** Ganar una partida de ajedrez.
- **Environment:** Tablero de juego y posicion de las fichas.
- **Actuators:** Mover las fichas siguiendo las reglas del juego de manera que pueda llegar a vencer a su oponente, analizar la jugado del contricante para saber que movimiento hacer despues. 
- **Sensors:** Camara para ver los movimientos, sensores de aproximidad y movimiento para colocar la ficha en el lugar exacto.

El enviroment es totalmente observable ya que no hay nada que se oculte en el tablero, es determinista ya que no hay factor de suerte al mover una pieza, es estático
ya que no cambia constantemente mientras el agente piensa, y discreto ya que hay un número finito de jugadas a realizar.