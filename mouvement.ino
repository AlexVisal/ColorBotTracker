#include <Wire.h> 
#include <AFMotor.h> 
#include <Arduino_LSM6DS3.h> 
#include <MadgwickAHRS.h> 
#include <Math.h> 
// Motor pins 
// Motor A connections 
int enA = 9; 
int in1 = 8; 
int in2 = 7; 
// Motor B connections 
int enB = 3; 
int in3 = 5; 
int in4 = 4; 
//serial command
String command; 
unsigned long currentTime; 
unsigned long previousTime; 
// ------------------------------------------------------------------ // INITIAL SETUP 
// ------------------------------------------------------------------ 
void setup() 
{ 
Serial.begin(9600); 
while (!Serial); 
if(!IMU.begin()) { 
Serial.println("Failed to initialize IMU!"); 
while (1); 
} 
// Set all the motor control pins to outputs 
pinMode(enA, OUTPUT); 
pinMode(enB, OUTPUT); 
pinMode(in1, OUTPUT); 
pinMode(in2, OUTPUT); 
pinMode(in3, OUTPUT); 
pinMode(in4, OUTPUT); 
// Turn off motors - Initial state 
digitalWrite(in1, LOW); 
digitalWrite(in2, LOW); 
digitalWrite(in3, LOW); 
digitalWrite(in4, LOW); 
}
// ------------------------------------------------------------------- // MOVEMENT CONTROLLER 
// -------------------------------------------------------------------
void moveMotors(float speed) 
{ 
analogWrite(enA, speed); 
analogWrite(enB, speed); 
digitalWrite(in1, LOW); 
digitalWrite(in2, HIGH); 
digitalWrite(in3, LOW); 
digitalWrite(in4, HIGH);  
} 
// ------------------------------------------------------------------- // MAIN PROGRAM LOOP 
// ------------------------------------------------------------------- 
void loop() 
{ 
if(Serial.available()) 
{ 
command = Serial.readStringUntil('\n'); 
command.trim(); 
//Serial.println(command); 
if(command.equals("0")) 
{ 
moveMotors(75); 
}else if(command.equals("1")) 
{ 
moveMotors(85); 
}else if(command.equals("2")) 
{ 
moveMotors(95); 
}else if(command.equals("3")) 
{ 
moveMotors(105); 
}else if(command.equals("4")) 
{ 
moveMotors(115); 
}else if(command.equals("5")) 
{ 
moveMotors(125); 
}else if(command.equals("6")) 
{ 
moveMotors(135); 
}else if(command.equals("7"))
{ 
 moveMotors(145); 
}else if(command.equals("8")) { 
moveMotors(155); 
}else if(command.equals("9")) { 
moveMotors(165); 
}else if(command.equals("10")) { 
moveMotors(175); 
}else if(command.equals("11")) { 
moveMotors(185); 
}else if(command.equals("12")) { 
moveMotors(195); 
}else if(command.equals("13")) 
{ 
moveMotors(205); 
}else if(command.equals("14")) { 
moveMotors(215); 
}else if(command.equals("15")) { 
moveMotors(225); 
}else if(command.equals("16")) { 
moveMotors(235); 
}else if(command.equals("17")) { 
moveMotors(245); 
}else if(command.equals("18")) { 
moveMotors(255); 
}else if(command.equals("21")) { 
moveMotors(0); 
}else if(command.equals("20"))
{ 
analogWrite(enA, 150); 
analogWrite(enB, 0); 
digitalWrite(in1, HIGH); 
digitalWrite(in2, LOW); 
digitalWrite(in3, HIGH); 
digitalWrite(in4, LOW);  
}else 
{ 
moveMotors(0); 
} 
} 
}

