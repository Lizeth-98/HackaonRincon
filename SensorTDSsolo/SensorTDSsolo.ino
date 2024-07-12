const int TDSSensorPin = A1; // Pin analógico al que está conectado el sensor TDS
const float VoltageReference = 5.0; // Voltaje de referencia del Arduino (normalmente 5V)
const float ADCResolution = 1024.0; // Resolución del ADC (10 bits, es decir, 1024 niveles)
const float TdsFactor = 0.5; // Factor de conversión de TDS

void setup() {
  Serial.begin(9600);
  pinMode(TDSSensorPin, INPUT);
}

void loop() {
  int sensorValue = analogRead(TDSSensorPin);
  float voltage = sensorValue * VoltageReference / ADCResolution;
  float tdsValue = (voltage * TdsFactor) * 1000; // Convierte el voltaje a TDS en ppm
  
  Serial.print("Voltaje: ");
  Serial.print(voltage, 2);
  Serial.print(" V, TDS: ");
  Serial.print(tdsValue, 2);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
  Serial.println(" ppm");
  
  delay(2000);
}
