#include "mbed.h"
#include "../lib/thermal-printer/AdafruitThermal.h"
#include <iostream>
#include <string> 
#include "USBCDC.h"

using namespace std;
 
AdafruitThermal Printer(PA_10, PA_9);
BufferedSerial pi(USBTX, USBRX);

FILE* serial_file = fdopen(&pi,"r+");

int main() {

        char buffer[20] = {};
        Printer.begin();
        ThisThread::sleep_for(chrono::milliseconds(200));
        Printer.setDefault();
        ThisThread::sleep_for(chrono::milliseconds(200));
        

        

       while(true){

               char input = 0;
               int index = 0;
               while(true){
                       input = getc(serial_file);
                       if (input == '\n'){
                               break;
                       }
                       buffer[index] = input;
                       index++;
               }
               index = 0;
               printf("***%s***", buffer);

               char * OutputText = buffer;               

               Printer.print(OutputText);

               
                
                // ThisThread::sleep_for(chrono::milliseconds(200));
                // pi.write(buffer, 1);
                // ThisThread::sleep_for(chrono::milliseconds(200));
                // pi.read(buffer, 1);
                // ThisThread::sleep_for(chrono::milliseconds(200));
                // printf(buffer[0] + "\n");
                // char * output_pointer = buffer;
                // char *Output = output_pointer;

                // Printer.print(Output);
                
       }
}