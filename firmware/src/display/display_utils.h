
#ifndef DISPLAY_UTILS_H
#define DISPLAY_UTILS_H

#include <Adafruit_SH110X.h>
#include <Wire.h>

extern Adafruit_SH1106G display;

void initDisplay();
void logToDisplay(String message);

#endif
