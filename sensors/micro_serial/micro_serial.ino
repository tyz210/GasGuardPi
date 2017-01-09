#include <DHT_U.h>
#include <MQ135.h>

namespace {
const auto id = 1;
const uint8_t DHT_PIN = 6;
const auto DHT_TYPE = DHT11; // TODO: Update sensor to DHT21

const uint8_t MQ135_PIN = A3;


const DHT_Unified dht(DHT_PIN, DHT_TYPE);
const MQ135 mq135(MQ135_PIN);

float mq135_resistance_value = 0.0;

float mq135_co = 0.0;
float mq135_co2 = 0.0;
float mq135_ethanol = 0.0;
float mq135_nh4 = 0.0;
float mq135_toluene = 0.0;
float mq135_acetone = 0.0;

uint8_t dht_temperature_sensor_value = 0;
uint8_t dht_humidity_sensor_value = 0;

void read_data_from_sensor()
{
  mq135_resistance_value = mq135.getResistance();

  mq135_co = mq135.getCO(mq135_resistance_value);//co ppm
  mq135_co2 = mq135.getCO2(mq135_resistance_value);//co2 ppm
  mq135_ethanol = mq135.getEthanol(mq135_resistance_value);//ethanol ppm
  mq135_nh4 = mq135.getNH4(mq135_resistance_value); //NH4 ppm
  mq135_toluene = mq135.getToluene(mq135_resistance_value); //toluene ppm
  mq135_acetone = mq135.getAcetone(mq135_resistance_value); //acetone ppm

  sensors_event_t event;
  dht.temperature().getEvent(&event);

  dht_temperature_sensor_value = event.temperature;

  dht.humidity().getEvent(&event);
  dht_humidity_sensor_value = event.relative_humidity;
}

void print_data_to_serial_port()
{
  Serial.print("{");
  Serial.print("id: ");
  Serial.print(id);
  Serial.print(", \"temperature\": ");
  Serial.print(dht_temperature_sensor_value);
  Serial.print(", \"humidity\": ");
  Serial.print(dht_humidity_sensor_value);
  
  Serial.print(", \"co\": ");
  Serial.print(mq135_co);
  Serial.print(", \"co2\": ");
  Serial.print(mq135_co2);
  Serial.print(", \"ethanol\": ");
  Serial.print(mq135_ethanol);
  Serial.print(", \"NH4\": ");
  Serial.print(mq135_nh4);
  Serial.print(", \"toluene\": ");
  Serial.print(mq135_toluene);
  Serial.print(", \"acetone\": ");
  Serial.print(mq135_acetone);
  
  Serial.print("}\n");
}

} // namespace

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  read_data_from_sensor();
  
  print_data_to_serial_port();

  delay (1000);
}
