/*
 *  This sketch sends data via HTTP GET requests to data.sparkfun.com service.
 *
 *  You need to get streamId and privateKey at data.sparkfun.com and paste them
 *  below. Or just customize this script to talk to other HTTP servers.
 *
 */

#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <ESP32Servo.h>


Servo myservo1;
Servo myservo2;
Servo myservoL;
Servo myservoR;

const char* ssid     = "shersh";
const char* password = "ARMAgedon";

const char* test_root_ca= \
     "-----BEGIN CERTIFICATE-----\n" \
"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\n" \
"-----END CERTIFICATE-----\n";

void setup()
{
    myservo1.attach(27);
    myservo2.attach(14);
    myservoL.attach(12);
    myservoR.attach(26);
    Serial.begin(115200);
    delay(10);

    // We start by connecting to a WiFi network

    Serial.println();
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}

void dance() { 
  myservoL.write(200);
  myservoR.write(200);
  delay(250);  
  myservoL.detach();
  myservoR.detach();  
  delay(500); 
  myservo1.write(-360); 
  myservo2.write(360);
  delay(1000);
  myservo1.write(360); 
  myservo2.write(360);
  delay(3000);
  myservo1.write(-360); 
  myservo2.write(-360);
  delay(3000);
  myservo1.write(-360); 
  myservo2.write(360);
  delay(1500);
  myservo1.write(360); 
  myservo2.write(-360);
  delay(1500);


  myservoL.attach(12);
  myservoR.attach(26);    
  myservoL.write(200);
  myservoR.write(200);
  delay(250);  
  myservoL.detach();
  myservoR.detach();  
  delay(500); 
  myservoL.attach(12);
  myservoR.attach(26);  
  myservoL.write(360);
  myservoR.write(-360);
  delay(250);
  myservoL.detach();
  myservoR.detach();  
  myservo1.write(-360); 
  myservo2.write(360);
  delay(1500);
  myservo1.write(360); 
  myservo2.write(-360);
  delay(1500);  
}


void loop(){
    delay(10000);

    Serial.print("connecting to ");
    Serial.println("pult50-arturlukianov.vercel.app");

    // Use WiFiClient class to create TCP connections
    WiFiClientSecure client;
    client.setInsecure();
    //client.setCACert((uint8_t*)test_root_ca, sizeof(test_root_ca)-1);
    if (!client.connect("pult50-arturlukianov.vercel.app", 443)) {
        Serial.println("connection failed");
        return;
    }

    // We now create a URI for the request
    String url = "/is_warmup";

    Serial.print("Requesting URL: ");
    Serial.println(url);

    // Make a HTTP request:
    client.println("GET " + url + " HTTP/1.0");
    client.println("Host: pult50-arturlukianov.vercel.app");
    client.println("Connection: close");
    client.println();
    unsigned long timeout = millis();
    while (client.available() == 0) {
        if (millis() - timeout > 5000) {
            Serial.println(">>> Client Timeout !");
            client.stop();
            return;
        }
    }

    // Read all the lines of the reply from server and print them to Serial
    String lastStr;
    while(client.available()) {
        String line = client.readStringUntil('\r');
        lastStr = line.substring(1);
    }

    Serial.println("is warmup?");
    Serial.println(lastStr);
    if (lastStr == "ok") {
      Serial.println("Now dance!");  
      dance();    
    }
    Serial.println("closing connection");

    if (millis() - previousMillis >= 500){
      
    }
}

