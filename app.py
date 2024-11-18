import serial
import time

# Configura el puerto serial (ajusta el puerto según tu sistema operativo)
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=1)  # Cambia 'COM#' por tu puerto

def send_command(command):
    arduino.write(command.encode())  # Envía el comando al Arduino
    time.sleep(0.1)  # Pequeña pausa para procesar

try:
    while True:
        print("Control de LEDs")
        print("1. Encender LEDs hacia adelante")
        print("2. Encender LEDs hacia atrás")
        print("3. Salir")
        
        option = input("Elige una opción: ")
        
        if option == '1':
            send_command('F')  # Envía comando 'F' al Arduino
        elif option == '2':
            send_command('B')  # Envía comando 'B' al Arduino
        elif option == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")
except KeyboardInterrupt:
    print("\nPrograma interrumpido")
finally:
    arduino.close()  # Cierra el puerto serial
