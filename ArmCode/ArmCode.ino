#include <Arduino.h>
#include <Servo.h>
 
Servo middle, left, right, claw;
bool running = false;
char action;
int midPos = 90;
int leftPos = 90;
int rightPos = 90;
int clawPos = 90;

void setup()
{
    Serial.begin(9600);

    middle.attach(11);
    left.attach(10);
    right.attach(9);
    claw.attach(6);

    middle.write(midPos);
    left.write(leftPos);
    right.write(rightPos);
    claw.write(clawPos);
}

void positions()
{
    String midPosStr = String(midPos);
    String leftPosStr = String(leftPos);
    String rightPosStr = String(rightPos);
    String clawPosStr = String(clawPos);

    
    String msg = ("Mid: " + midPosStr + " left: " + leftPosStr + " right: " + rightPosStr + " claw: " + clawPosStr);
    Serial.println(msg);
    delay(250);
}

void loop()
{
    if (Serial.available() > 0)
    {
        char input = Serial.read();

        switch (action)
        {
        if (input == 'L') {
            midPos -= 1;
            middle.write(midPos);
            break;
        }
        if (input == 'R') {        
            midPos += 1;
            middle.write(midPos);
            break;
        }
          if (input == 'B') {      
            leftPos -= 1;
            left.write(leftPos);
            
          }            
          if (input == 'F') {      
            leftPos += 1;
            left.write(leftPos);
            break;
          }
         if (input == 'D') {  
            rightPos -= 1;
            right.write(rightPos);
            break;
         }
         if (input == 'U') { 
            rightPos += 1;
            right.write(rightPos);
         }
        if (input == 'O') {
            clawPos -= 1;
            claw.write(clawPos);
            
        }
        if (input == 'C') {
            clawPos += 1;
            claw.write(clawPos);
        }
        default:
            positions();
        }
    }
}