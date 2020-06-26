//Declaração das variaveis:
int LED1 = 2; //LED conectado ao pino 2
int LED2 = 4; //Botão conectado ao pino 3
int VAR = 0;

void setup()

{
 pinMode(LED1, OUTPUT); //Pino 2 do arduino como saída
 pinMode(LED2, OUTPUT); //Pino 4 do arduino como saí
}

void loop()

{
 if (Serial.available() > 0){
        if (Serial.read() == 1){ 
            digitalWrite(4, HIGH);
            digitalWrite(3, LOW);
        }else{
          digitalWrite(4, LOW);
          digitalWrite(3, HIGH);
        }
}
}
