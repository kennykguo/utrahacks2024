const int soilMoisturePin = A0;
const int leftPin= 9;
const int rightPin= 8;
const int trig = 13;
const int echo = 12;
int duration = 0;
int distance = 0;
int angle = 90;
int wetCounter = 0;
int dryCounter = 0;

const int emptyButton = 4;
const int resetButton = 3; 

int emptyButtonState = 0;
int resetButtonState = 0;

int emptying = 0;

int prevDry = 0;
int prevWet = 0;

#include <Servo.h>
Servo servo;

void turnright() {
  servo.write(150);
  delay(3000);
  dryCounter++;
  
  servo.write(angle);
  delay(2000);
}
void turnleft() {
  servo.write(20);
  delay(3000); 
  wetCounter++;

  servo.write(angle);
  delay(2000);
}

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(9600); 

  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);

  servo.write(angle);
  servo.attach(8);
  

  pinMode(emptyButton, INPUT);
  pinMode(resetButton, INPUT);
}

// the loop function runs over and over again forever
void loop() {
  int soilMoistureValue = analogRead(soilMoisturePin);

  // //int moisturePercentage = map(soilMoistureValue, 0, 1023, 100, 0);

  // Serial.print("Soil Moisture: ");
  // Serial.print(soilMoistureValue);
  // Serial.println("%");

  if (dryCounter != prevDry) {
    Serial.print("Total Dry Items: ");
    Serial.println(dryCounter);
    prevDry = dryCounter;
  }

  
  if (wetCounter != prevWet) {
    Serial.print("Total Wet Items: ");
    Serial.println(wetCounter);
    prevWet = wetCounter;
  }

  digitalWrite(trig , HIGH);
  delayMicroseconds(1000);
  digitalWrite(trig , LOW);

  duration = pulseIn(echo , HIGH);
  distance = (duration/2) / 28.5 ;
  // Serial.println(distance);
  delay(1000);

  // Serial.println(soilMoistureValue);  
  // Serial.println(map(soilMoistureValue,1023,0, 0, 100));

  if (emptying == 0) { // check to make sure garbage is not being emptied
    if(distance<11){
      // Serial.print(soilMoistureValue);  
      if(soilMoistureValue<550){
        turnleft();
      }
      else{
        turnright();
      }
    }
  }

  // delay(3000);

  emptyButtonState = digitalRead(emptyButton);
  resetButtonState = digitalRead(resetButton);

  if (emptyButtonState == HIGH) {
    servo.write(180);
    emptying = 1;
  }

  if (resetButtonState == HIGH) {
    servo.write(angle);
    delay(3000);
    emptying = 0;
  }

}
