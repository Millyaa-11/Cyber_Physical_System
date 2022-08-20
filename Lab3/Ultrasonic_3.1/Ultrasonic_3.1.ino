const int trigPin = 9;
const int echoPin = 10;
long dur;
int Timer = 1000;

void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin,INPUT);
  pinMode(13,OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readString();
    Timer = data.toInt();
    Serial.println(data);
  }
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);

  dur = pulseIn(echoPin,HIGH);

  Serial.println(dur);
  delay(Timer-1);
} 
