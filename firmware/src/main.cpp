#include <Arduino.h>
#include <WiFi.h>
#include "config.h"
#include "display/display_utils.h"
#include "websocket/websocket_client.h"

void setup() {
  Serial.begin(115200);
  initDisplay();
  logToDisplay("Booting...");

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    logToDisplay("Connecting Wi-Fi...");
  }

  logToDisplay("Wi-Fi: Connected");
  initWebSocket();
}

void loop() {
  updateWebSocket();
}
