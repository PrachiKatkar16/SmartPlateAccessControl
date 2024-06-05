#include <Servo.h>

Servo servoMotor; // Create an instance of the Servo class

void setup() {
  Serial.begin(9600); // Begin serial communication
  servoMotor.attach(9); // Attach servo to pin 9
}

void loop() {
  if (Serial.available() > 0) {
    char incomingByte = Serial.read(); // Read serial input
    if (incomingByte == 'a') { // Check if input is 'a' (authorized)
      rotateServo(); // Rotate servo
    }
  }
}

void rotateServo() {
  servoMotor.write(150); // Rotate servo to 150 degrees (opposite direction)
  delay(5000); // Wait for 5 seconds
  servoMotor.write(90); // Rotate servo back to the mean position (usually 90 degrees)
}

