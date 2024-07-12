// Definición de los pines analógicos
const int TDS_PIN = A0;
const int PH_PIN = A1;

// Variables para almacenar los valores leídos
float tdsValue = 0;
float phValue = 0;

void setup() {
  // Inicializar la comunicación serial
  Serial.begin(9600);
  
  // Configuración de los pines
  pinMode(TDS_PIN, INPUT);
  pinMode(PH_PIN, INPUT);
}

void loop() {
  // Leer valores de los sensores
  tdsValue = analogRead(TDS_PIN);
  phValue = analogRead(PH_PIN);

  // Convertir las lecturas analógicas a valores significativos
  tdsValue = map(tdsValue, 0, 1023, 0, 1000); // Ejemplo de conversión de TDS (ppm)
  phValue = (phValue * 5.0 / 1023) * 3.5; // Conversión a voltaje (0-5V) y luego a escala de pH (0-14)
  
  // Mostrar los valores en el monitor serial
  Serial.print("TDS: ");
  Serial.print(tdsValue);
  Serial.print(" ppm, ");
  
  Serial.print("pH: ");
  Serial.print(phValue);
  Serial.println();
  
  // Esperar un segundo antes de la próxima lectura
  delay(5000);
}
