import serial
import sys
LED_flag = False
with serial.Serial('COM5',9600, timeout=1) as serArd:
    print(f"The Arduino board is connect through {serArd.port}")
    while True:
        try:
            con_val = input(f"Enter 1 to turn on yellow LED, 2 turn on green LED, 0 to turn off LED : ")
            while not con_val in ['0', '1', '2', 'q']:
                print(f"Please enter 1 , 2 or 0")
                con_val = input(f"Enter 1, 2, 0 : ")
            print(f'You entered {con_val}')
            if serArd.writable() and con_val != 'q':
                serArd.write(con_val.encode())
                myData = serArd.readline().decode()
                print(myData)

            if con_val == 'q':
                print('Program is stopped!')
                break
        except serial.SerialException as er:
            print(er)

        except KeyboardInterrupt:
            sys.exit(0)
            