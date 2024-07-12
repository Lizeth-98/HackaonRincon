const int pHSensorPin = A0; // Pin analógico al que está conectado el sensor de pH
float voltage;
float pHValue;
float offset = 0.00; // Ajusta este valor según la calibración

void setup() {
  Serial.begin(9600);
  pinMode(pHSensorPin, INPUT);
  Serial.println("Calibrando sensor de pH...");
  Serial.println("Introduce el sensor en la solución de pH 7.0");
  delay(20000); // Espera 20 segundos para estabilizar la lectura

  float reading = analogRead(pHSensorPin);
  voltage = reading * 5.0 / 1024.0;
  pHValue = 7.0; // Valor de referencia para pH 7.0
  offset = voltage - 2.5; // Ajuste el offset
  Serial.print("Offset ajustado: ");
  Serial.println(offset);
}

void loop() {
  float reading = analogRead(pHSensorPin);
  voltage = reading * 5.0 / 1024.0;
  pHValue = 7.0 + ((voltage - 2.5) - offset) * 3.5; // Ecuación de calibración
  
  Serial.print("Voltaje: ");
  Serial.print(voltage, 2);
  Serial.print(" V, pH: ");
  Serial.println(pHValue, 2);
  delay(1000);
}

