/*
 * Created by ArduinoGetStarted.com
 *
 * This example code is in the public domain
 *
 * Tutorial page: https://arduinogetstarted.com/tutorials/arduino-temperature-humidity-sensor
 */

#include <DHT.h>
#define DHTPIN 5
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
const int sensorMin = 0;     // sensor minimum
const int sensorMax = 1024;  // sensor maximum


void setup() {
  Serial.begin(9600);
  dht.begin(); // initialize the sensor
}

void loop() {
  // wait a few seconds between measurements.
  delay(1000);

  float tempC = dht.readTemperature();
  float humi  = dht.readHumidity();
  // Serial.print("Temperature: ");
  // Serial.println(tempC);
  // Serial.print("Humidity: ");
  // Serial.println(humi);
    // read the sensor on analog A0:
	int sensorReading = analogRead(A8);
  // map the sensor range (four options):
  // ex: 'long int map(long int, long int, long int, long int, long int)'
	int range = map(sensorReading, sensorMin, sensorMax, 0, 3);
  
  // range value:
  switch (range) {
  case 0:    // A fire closer than 1.5 feet away.
    Serial.print("Fire Status: ");
    Serial.print("** Close Fire **");
    Serial.print(",");
    Serial.print("Temperature: ");
    Serial.print(tempC);
    Serial.print(",");
    Serial.print("Humidity: ");
    Serial.print(humi);
    break;
  case 1:    // A fire between 1-3 feet away.
    Serial.print("Fire Status: ");
    Serial.print("** Distant Fire **");
    Serial.print(",");
    Serial.print("Temperature: ");
    Serial.print(tempC);
    Serial.print(",");
    Serial.print("Humidity: ");
    Serial.print(humi);
    break;
  case 2:    // No fire detected.
    Serial.print("Fire Status: ");
    Serial.print("No Fire");
    Serial.print(",");
    Serial.print("Temperature: ");
    Serial.print(tempC);
    Serial.print(",");
    Serial.print("Humidity: ");
    Serial.print(humi);
    break;
  }
  Serial.println();
  delay(1);  // delay between reads
}
