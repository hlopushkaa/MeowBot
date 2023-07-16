#include <Servo.h>
 
Servo myservo;
 
void setup() {
	myservo.attach(31);
}
 
void loop() {
	myservo.writeMicroseconds(1000);
}