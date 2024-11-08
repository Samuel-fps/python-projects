# Motion Detection Script

Este script utiliza OpenCV y Pandas para realizar detección de movimiento mediante una cámara web. Al detectar movimiento, registra los tiempos de inicio y fin, y los guarda en un archivo CSV.

## Requisitos

Este script requiere las siguientes bibliotecas:

- **OpenCV**: Para capturar video y procesar imágenes.
- **Pandas**: Para gestionar y almacenar datos en un DataFrame.
- **Datetime**: Para gestionar y registrar las marcas de tiempo.

Para instalar las dependencias, ejecuta los siguientes comandos:

```bash
pip install opencv-python pandas
```

## Descripción del Funcionamiento

1. **Captura de Video**: Usa la cámara (índice 0) para capturar video en tiempo real.
2. **Procesamiento de Imagen**:
   - Convierte cada frame a escala de grises.
   - Aplica desenfoque gaussiano para reducir ruido y hacer más precisos los cambios de detección.
3. **Detección de Movimiento**:
   - Guarda el primer frame como referencia para compararlo con los frames subsiguientes.
   - Calcula la diferencia absoluta entre el primer frame y el actual.
   - Aplica un umbral para identificar áreas donde ocurre movimiento y resalta esas áreas con un rectángulo.
4. **Registro de Tiempos de Movimiento**:
   - Si se detecta movimiento (cambio en el frame), registra el tiempo en el que comenzó y terminó el movimiento.
   - Al finalizar, guarda los datos de los tiempos en el archivo `Times.csv`.

## Uso

Para ejecutar el script:

```bash
python motion_detector.py
```

El script abrirá ventanas mostrando el video en tiempo real:

- **Gray**: Video en escala de grises.
- **Delta Frame**: Diferencia entre el primer y el frame actual.
- **Thresh Frame**: Umbral binario para detectar áreas de movimiento.
- **Color Frame**: Video en color con rectángulos alrededor de áreas con movimiento.

Para salir, presiona la tecla **q** en cualquier ventana.

## Archivo de Salida

El archivo `Times.csv` se crea al terminar el script. Contiene dos columnas:

- **Start**: Tiempo de inicio de un evento de movimiento.
- **End**: Tiempo de fin del evento de movimiento.

Este archivo permite analizar los momentos en los que se detectó movimiento.
