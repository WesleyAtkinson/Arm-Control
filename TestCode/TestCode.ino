int ledPin1 = 2;
int ledPin2 = 3;
int ledPin3 = 4;
int ledPin4 = 5;


void setup() {
  Serial.begin(9600);
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);

}

void loop() {
  if (Serial.available() > 0) {
    char input = Serial.read();
    if (input == 'O') {
      digitalWrite(ledPin1, HIGH);
      Serial.println("LED 1 turned on");
    } else if (input == 'C') {
      digitalWrite(ledPin2, HIGH);
      Serial.println("LED 2 turned on");
    } else if (input == 'L') {
      digitalWrite(ledPin3, HIGH);
      Serial.println("LED 3 turned on");
    } else if (input == 'R') {
      digitalWrite(ledPin4, HIGH);
      Serial.println("LED 4 turned on");
    }
    
     else if (input == '0') {
      digitalWrite(ledPin1, LOW);
      digitalWrite(ledPin2, LOW);
      digitalWrite(ledPin3, LOW);
      digitalWrite(ledPin4, LOW);

      Serial.println("All LEDs turned off");
    } else {
      Serial.println("Invalid input");
    }
  }
}