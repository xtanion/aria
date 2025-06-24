
#include <WebSocketsClient.h>
#include <WiFi.h>
#include "../display/display_utils.h"
#include "../config.h"

WebSocketsClient webSocket;

void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {
  switch (type) {
    case WStype_DISCONNECTED:
      logToDisplay("WebSocket: Disconnected");
      break;
    case WStype_CONNECTED:
      logToDisplay("WebSocket: Connected");
      webSocket.sendTXT("Hello Server!");
      break;
    case WStype_TEXT:
      logToDisplay(String((char*)payload));
      break;
    default:
      break;
  }
}

void initWebSocket() {
  webSocket.begin(websocket_server, websocket_port, "/");
  webSocket.onEvent(webSocketEvent);
  webSocket.setReconnectInterval(5000);
}

void updateWebSocket() {
  webSocket.loop();
}
