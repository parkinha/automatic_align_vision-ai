#include <Stepper.h>
#include <Arduino.h>
const int stepsPerRevolution = 500;
const float stepAngle = 0.72;
const float microStepResolution =0.1;
  
const int CPX =2;
const int CCPX = 3;
const int CPY = 8;
const int CCPY = 9;
  
Stepper myStepperX(stepsPerRevolution, CPX, CCPX);
Stepper myStepperY(stepsPerRevolution, CPY, CCPY);

void setup(){
  
  
  myStepperX.setSpeed(50);
  myStepperY.setSpeed(50);
  pinMode(CPX, OUTPUT);
  pinMode(CCPX, OUTPUT);
  pinMode(CPY, OUTPUT);
  pinMode(CCPY, OUTPUT);
  Serial.begin(9600);
}
void loop(){
  char input_data;
  int i=0;
  int j=0;
  //while( Serial.available()){
    input_data=Serial.read();
  if (input_data =='0') //if wrong place=> Serial input=1
  {  

    //if (i<21)
      i=i+1;
      myStepperX.setSpeed(50);
      myStepperY.setSpeed(50);
      rotateClockwiseX(100);
    
    //else if (i==7)
    //{
    //  rotateClockwiseY(100);
    //  delay(100);
    //  j+1
    //}
    //else if(j<12)
    //{ j=j+1;
    // rotateClockwiseY(100);
    // delay(100);}
  }
  else if (input_data == '1'){
    delay(300);
    //myStepperX.setSpeed(1);
    //rotateClockwiseX(1);
    //break;
  }
  }

    
void rotateClockwiseX(float distance){
  digitalWrite(CPX, HIGH);
  digitalWrite(CCPX, LOW);
  int microSteps = distance * (1.0/microStepResolution);
  myStepperX.step(microSteps);
}

void rotateCounterClockwiseX(float distance){
  digitalWrite(CPX, LOW);
  digitalWrite(CCPX, HIGH);
  
  int microSteps=distance * (1.0 / microStepResolution);
  myStepperX.step(-microSteps);
}

void rotateClockwiseY(float distance){
  digitalWrite(CPY, HIGH);
  digitalWrite(CCPY, LOW);
  
  int microSteps = distance * (1.0 / microStepResolution);
  myStepperY.step(microSteps);
}

void rotateCounterClockwiseY(float distance){
  digitalWrite(CPY, LOW);
  digitalWrite(CCPY, HIGH);
  
  int microSteps = distance * (1.0 / microStepResolution);
  myStepperY.step(-microSteps);
}
