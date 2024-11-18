void setup() {
  Serial.begin(9600);  // Inicializa comunicación serial
  for (int i = 2; i < 10; i++) {
    pinMode(i, OUTPUT);
  }
}

void loop() {
  if (Serial.available()) {        // Si hay datos en el serial
    char command = Serial.read();  // Lee el comando
    if (command == 'F') {          // 'F' para encender LEDs hacia adelante
      for (int i = 2; i < 10; i++) {
        digitalWrite(i, HIGH);
        delay(500);
        digitalWrite(i, LOW);
        delay(500);
      }
    } else if (command == 'B') {  // 'B' para encender LEDs hacia atrás
      for (int i = 9; i > 1; i--) {
        digitalWrite(i, HIGH);
        delay(500);
        digitalWrite(i, LOW);
        delay(500);
      }
    }
  }
}
