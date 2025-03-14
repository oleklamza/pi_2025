#include "LedControl.h"


LedControl disp = LedControl(12, 13, 11, 1);

const uint32_t V_MAX = 10000;
const uint32_t V_MAX_2 = V_MAX * V_MAX;
uint32_t p_square = 0;
uint32_t p_circle = 0;
float pi = 0;
const uint32_t DIGIT_WEIGHT[] = {10000000, 1000000, 100000, 10000, 1000, 100, 10, 1};

//
void setup() {
  disp.shutdown(0, false);
  disp.setIntensity(0, 1);
  disp.clearDisplay(0);
}

//
void loop() {
  // calculate
  uint32_t x = random(V_MAX);
  uint32_t y = random(V_MAX);

  p_square += 1;
  if (x*x + y*y < V_MAX_2) {
    p_circle += 1;
  }

  pi = 4.0 * p_circle / p_square;

  // update display
  uint32_t pii = pi * DIGIT_WEIGHT[0];

  for (int i=0; i<8; ++i) {
    uint8_t d = pii / DIGIT_WEIGHT[i];
    pii -= d * DIGIT_WEIGHT[i];
    disp.setDigit(0, 7-i, d, i==0);
  }   
  
  delay(50);  
}
