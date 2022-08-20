const int LEDPin = 13;
char con_val = '0';

void setup() {
  Serial.begin(9600);
  pinMode(LEDPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    con_val = char(Serial.read());
    LEDcontrol(con_val);
  }
  delay(100);
}

void LEDcontrol(char con) {
  if (con == '1') {
    Serial.print("From Arduino, LED is on \n");
    digitalWrite(LEDPin, HIGH);
  }
  if (con == '0') {
    Serial.print("From Arduino, LED is off \n");
    digitalWrite(LEDPin, LOW);
  }

} 
