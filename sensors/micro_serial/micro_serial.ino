#include <DHT_U.h>

namespace {
const auto ID = 1;

const uint8_t DHT_PIN = 2; 

const uint8_t MQ135_PIN = A0;
const uint8_t MQ9_PIN = A2;
const uint8_t MQ7_PIN = A3;


const DHT_Unified DTH(DHT_PIN, DHT22);

int mq135_resistance_value = 0;
int mq9_resistance_value = 0;
int mq7_resistance_value = 0;



float dht_temperature_sensor_value = 0.0;
float dht_humidity_sensor_value = 0.0;


void read_data_from_sensor()
{
  mq135_resistance_value = analogRead(MQ135_PIN);
  mq9_resistance_value = analogRead(MQ9_PIN);
  mq7_resistance_value = analogRead(MQ7_PIN);

  sensors_event_t event;
  
  DTH.temperature().getEvent(&event);
  dht_temperature_sensor_value = event.temperature;
  
  DTH.humidity().getEvent(&event);
  dht_humidity_sensor_value = event.relative_humidity;
}

void print_data_to_serial_port()
{
  Serial.print("{");
  Serial.print("id: ");
  Serial.print(ID);
  Serial.print(", \"temperature\": ");
  Serial.print(dht_temperature_sensor_value);
  Serial.print(", \"humidity\": ");
  Serial.print(dht_humidity_sensor_value);
  
  Serial.print(", \"mq135\": ");
  Serial.print(mq135_resistance_value);
  Serial.print(", \"mq9\": ");
  Serial.print(mq9_resistance_value);
  Serial.print(", \"mq7\": ");
  Serial.print(mq7_resistance_value);
  Serial.print("}\n");
}

} // namespace

void setup() {
  Serial.begin(9600);
  DTH.begin();
}

void loop() {
  read_data_from_sensor();
  
  print_data_to_serial_port();

  delay (1000);
}
