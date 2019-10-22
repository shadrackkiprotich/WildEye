void setup() {
   Serial.begin(9600); // begin transmission
}
void loop() {
  String animal;
  while (Serial.available() > 0) {
    animal = animal + (char)Serial.read(); // read data byte by byte and store it
  }
  Serial.print(animal); // send the received data back to raspberry pi
}