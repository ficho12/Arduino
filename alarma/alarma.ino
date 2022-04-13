//#include <TimeLib.h>
#include <Keypad.h>

float distancia, val;
//time_t Tini, Tfin, Tnow;

int const tamanhoClave = 4, PIR = 10, BOCINA = 11, LED = 13, LEDKEY = 12;
int numIntrod = 0;
char key;
String clave = {"1234"};
String claveKeypad = {""};
String claveSerial = {""};

bool alarma = false;

// Códigos de envio serial
//0 = Alarma
//1 = Contraseña correcta por keypad
//2= contraseña incorrecta
//3= Contraseña correcta
                    

const byte rows = 4; //4 filas
const byte cols = 4; //4 columnas
char keys[rows][cols] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[rows] = {9, 8, 7, 6}; //conecta con la fila de pins del keypad
byte colPins[cols] = {5, 4, 3, 2}; //conecta con la columna de pins del keypad
Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, rows, cols );

void setup() {
    pinMode(BOCINA, OUTPUT);
    pinMode(PIR, INPUT);
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
}

void loop() {
  
  if(alarma)
  {
    digitalWrite(BOCINA, HIGH);
    digitalWrite(LED, HIGH);
    //delay(1000);
            
    //Recibir clave
    //Por Keypad
    key = keypad.getKey();

    if(key != NO_KEY)
    {
      //Serial.println(key);

      numIntrod++;
      
      if(numIntrod==1)
      {}
         //Tini = now();

       //Tnow = now();
       
      if((numIntrod>tamanhoClave)) //|| (Tnow-Tini>10000))
      {
        numIntrod = 0;
        claveKeypad.remove(0);
      }else{
        claveKeypad.concat(key);
        Serial.print(key);
          
        if(claveKeypad.equals(clave))
        {
          alarma=false;
          Serial.print(1, DEC);
        }
      }    
    //key = keypad.getKey();
    }
    //Por puerto serie
  
    if (Serial.available()>0) 
   {   
      char option = Serial.read();
      if (option == '3')
      {
         alarma = false;
      }
   }
    
  }else if (!alarma){
    digitalWrite(BOCINA, LOW);
    digitalWrite(LED, LOW);
  
  //CAMBIAR A PIR
  
    if(digitalRead(PIR) == HIGH)
    {
      alarma = true;
      
      //Mandar Mensaje
      Serial.print(0, DEC);

    }
    
  }

  //digitalWrite(BOCINA, LOW);
  //digitalWrite(LED, LOW);
  //delay(1000);
  
}
