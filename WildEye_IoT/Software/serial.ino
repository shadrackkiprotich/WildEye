/*
 Name     :		Wild_Eye
 Created  :	  October 4, 2019 
 Sensor   :   
 Authors  :	  Joshua Ndemenge & Clinton Oduor
*/

#include <SigFox.h>
#include <ArduinoLowPower.h>
#include <Arduino.h>


void setup() 
{
   Serial.begin(9600); // begin transmission
   //Run This funtion to get the ID and PAC after which yoi can safely comment
   // getDeviceId();
}

void loop() 
{
  char animal;
  while (Serial.available() > 0) 
  {
    animal = animal + (char)Serial.read(); // read data byte by byte and store it
  }
  sendDataToSigFox(animal)
}

void getDeviceId()
{ 
  Serial.begin(9600);

  while(!Serial) {};

  if (!SigFox.begin())
  {
    Serial.println("Shield error or not present!");
  }

    String version = SigFox.SigVersion();
    String ID = SigFox.ID();
    String PAC = SigFox.PAC();

    // Display module informations
    Serial.println("MKRFox1200 Sigfox first configuration");
    Serial.println("SigFox FW version " + version);
    Serial.println("ID  = " + ID);
    Serial.println("PAC = " + PAC);

    Serial.println("");

    Serial.println("Register your board on https://backend.sigfox.com/activate with provided ID and PAC");

    delay(100);

    // Send the module to the deepest sleep
    SigFox.end();

  return;  
}

void sendDataToSigFox(char animalName)
{
  /*
  ATTENTION - the structure we are going to send MUST
  be declared "packed" otherwise we'll get padding mismatch
  on the sent data - see http://www.catb.org/esr/structure-packing/#_structure_alignment_and_padding
  for more details
  */

  typedef struct __attribute__ ((packed)) sigfox_message {
  char name;
  uint8_t lastMessageStatus;
  } SigfoxMessage;

  // stub for message which will be sent
  SigfoxMessage msg;

  if (!SigFox.begin()) {
      Serial.println("Shield error or not present!");
      return;
  }

  //start the module
  SigFox.begin();

  // Wait at least 30ms after first configuration (100ms before)
  delay(100);

  msg.name=animalName;        

  SigFox.status();
  delay(1);

  SigFox.beginPacket();
  SigFox.write((uint8_t*)&msg,12);

  msg.lastMessageStatus=SigFox.endPacket();

  Serial.println("status: "+ String(msg.lastMessageStatus));  
  Serial.println(String(msg.name)); 
}

