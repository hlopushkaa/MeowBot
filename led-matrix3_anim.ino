#include <FastLED.h>
#include "effects.h"

#define NUM_LEDS 256
#define DATA_PIN 13
#define BRIGHTNESS 30

CRGB leds[NUM_LEDS];

#define S1 2
#define S2 6
#define key 3
int prevS1;
int curS1, curS2;
int val = 100;
bool flag=false;
int curKey;
unsigned long whenKeyPress = 0;
int effectN = 0;
int effDelay=500;

byte frame=0;

void Rotate () {
  curS1 = digitalRead(S1);
  if (curS1!=prevS1){
    curS2 = digitalRead(S2);
    if (flag){
        if (curS2==curS1){
            val+=25;
         }
         else {
            val-=25;
         }
         if (val<0){
            val=0; 
         }

         if (val>500){
            val=500; 
         }
         Serial.print ("Value = ");
         Serial.println (val);
         flag=false;
         float x = 5.0/(val+5);// управления скоротью смены кадров анимации
         effDelay=ceil(10000*x);
         Serial.print ("effDelay = ");
         Serial.println (effDelay);
         
    }
    else {
      flag=true;
    }
  }
  prevS1=curS1;
}

void PressBtn () {
  int curKey = digitalRead(key);
  if (curKey == LOW) {
    if (millis() - whenKeyPress > 300) {
      effectN++;
      if (effectN>1){
          effectN=0;
      }
      FastLED.clear();
      FastLED.show();
    }
    whenKeyPress = millis();
  }
}

void setup() { 
   FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, NUM_LEDS);
    FastLED.setBrightness(BRIGHTNESS);//0-255

    pinMode (S1, INPUT);
    pinMode (S2, INPUT);
    pinMode (key, INPUT);
    prevS1 = digitalRead(S1); 

    attachInterrupt(0, Rotate, CHANGE);        
    attachInterrupt(1, PressBtn, CHANGE); 
    
    Serial.begin (9600);
    
}

void loop() { 
   
   if (effectN==0){//heart
     for (frame=0;frame<(sizeof(heart)/sizeof(heart[0]));frame++){
        setFrame(heart, frame);
        FastLED.show();
        delay(effDelay);
     }
     delay(effDelay+100);
     
   }
   if (effectN==1){//fire

     for (frame=0;frame<(sizeof(fire)/sizeof(fire[0]));frame++){
        Serial.println (frame);
        setFrame(fire, frame);
        FastLED.show();
        delay(effDelay);
     }

   }
}



void setFrame(const uint32_t imgArr[][256], byte frame) {
  int i;

  for (i=0;i<NUM_LEDS;i++){
    uint32_t ledColor=pgm_read_dword(&(imgArr[frame][i]));
    leds[i]=ledColor;
  }
  
}
