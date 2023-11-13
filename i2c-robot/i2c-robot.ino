#include <Wire.h>

const int pin1 = 12;
const int pin2 = 13;
const int pin3 = 10;
const int pin4 = 11;

void setup() {
  // put your setup code here, to run once:
  Wire.begin(0x8);
  Wire.onReceive(receiveEvent);
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
  pinMode(pin3, OUTPUT);
  pinMode(pin4, OUTPUT);

  digitalWrite(pin1, LOW);
  digitalWrite(pin2, LOW);
  digitalWrite(pin3, LOW);
  digitalWrite(pin4, LOW);

}

void forward() {
  digitalWrite(pin1, LOW);
  digitalWrite(pin2, HIGH);
  digitalWrite(pin3, LOW);
  digitalWrite(pin4, HIGH);
}

void backward() {
  digitalWrite(pin1, HIGH);
  digitalWrite(pin2, LOW);
  digitalWrite(pin3, HIGH);
  digitalWrite(pin4, LOW);
}

void stop() {
  digitalWrite(pin1, LOW);
  digitalWrite(pin2, LOW);
  digitalWrite(pin3, LOW);
  digitalWrite(pin4, LOW);
}

void left() {
  digitalWrite(pin1, LOW);
  digitalWrite(pin2, HIGH);
  digitalWrite(pin3, HIGH);
  digitalWrite(pin4, LOW);
}

void right() {
  digitalWrite(pin1, HIGH);
  digitalWrite(pin2, LOW);
  digitalWrite(pin3, LOW);
  digitalWrite(pin4, HIGH);
}

void receiveEvent(int howMany) {
  while (Wire.available()) {
    char c = Wire.read();
    if (c == 1) {
       forward();
    }
    if (c == 0) {
       stop();
    }
    if (c == 2) {
       backward();
    }
    if (c == 3) {
       left();
    }
    if (c == 4) {
       right();
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(100);

}
