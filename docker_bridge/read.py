import serial

def main():
    # Replace 'COM3' with your serial port (e.g., '/dev/ttyUSB0' for Linux or 'COM3' for Windows)
    # Replace 9600 with the baud rate of your serial device
    serial_port = '/dev/ttyACM0'
    baud_rate = 9600

    try:
        # Open the serial connection
        with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
            print(f"Connected to {serial_port} at {baud_rate} baud.")
            print("Waiting for a message...")

            while True:
                # Read a line from the serial port
                message = ser.readline().decode('utf-8').strip()
                
                if message:
                    print(f"Received: {message}")
                    
                # Add a way to exit the program
                if message.lower() == "exit":
                    print("Exiting program.")
                    break

    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()