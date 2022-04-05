#include <Keypad.h>

float distancia, val;
time_t Tini, Tfin;

int const tamanhoClave = 4;
int numIntrod = 0;
char key;
char clave[tamanhoClave] = {"1234"};
char claveIntrod[tamanhoClave] = {""};
bool alarma;


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
    pinMode(12, INPUT);
    pinMode(11, OUTPUT);
    pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  
  
  
  if(alarma)
  {
  digitalWrite(12, HIGH);
    digitalWrite(13, HIGH);
    delay(1000);
    
    //Mandar Mensaje

    //Recibir clave
    //Por Keypad
    key = keypad.getKey();
    
    while(key != NO_KEY)
    {
       if(key != NO_KEY)
       {
         numIntrod++;
         if(numIntrod>tamanhoClave)
         {
           numIntrod = 0;
           claveIntrod = "";
         }else{
           claveIntrod = claveIntrod + key;

           if(claveIntrod==clave)
             alarma=false;
         }    
       }
      key = keypad.getKey();
    }
    
    //Por puerto serie
    
    
  }
    
  }else if (!alarma){
    digitalWrite(12, LOW);
    digitalWrite(13, LOW);
  
    pulseIn(12, HIGH, 69);
    Tini = now();

    val = analogRead(11);
    Tfin = now();

    if(val<10)
    {
      distancia = 0;
    }else
    {
      distancia = Tfin-Tini * 171.5;

      if(distancia<10)
      {
        alarma = true;
      }
    }
  }

  digitalWrite(12, LOW);
  delay(1000);
}
