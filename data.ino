#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <ESP8266HTTPUpdateServer.h>

#ifndef STASSID
#define STASSID "HUAWEI MediaPad T5"
#define STAPSK "Uts2023@"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;
String payload = "";
String serverEcho = "";

unsigned long yandex_BLOCK = 0;

ESP8266WebServer httpServer(80);
ESP8266HTTPUpdateServer httpUpdater;

void setup(void) {
  Serial.begin(9600);
  Serial.println("Booting Sketch...");
  //-------------------------------------------------------------------------------------------------
  // Web - Update
  WiFi.mode(WIFI_AP_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    WiFi.begin(ssid, password);
  }
  //MDNS.begin(host);
  httpUpdater.setup(&httpServer);
  httpServer.begin();
  MDNS.addService("http", "tcp", 80);
  //==================================================================================================


  yandex_BLOCK = millis();
  Serial.println("End Booting");
}

void loop(void) {
  // WEB-Update =============================================
  httpServer.handleClient();
  MDNS.update();
  // ========================================================

  if (yandex_BLOCK >= 4294967294) yandex_BLOCK = 0;



  if (millis() > yandex_BLOCK) {
    //-------------------------------------------------------------
    //
    yandex_BLOCK = millis() + 3000;
    HTTPClient http;

    String serverPath = "https://pult50-arturlukianov.vercel.app/is_warmup";

    http.begin(serverPath.c_str());
    int httpResponseCode = http.GET();
    if (httpResponseCode > 0) {
      payload = http.getString();
      payload.trim();
      Serial.println(payload);
    }
    http.end();
  }


  // Loop
  // ========================================================
}
