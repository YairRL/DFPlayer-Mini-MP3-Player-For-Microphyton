#---------------Lectura CO2------------------------------------------------------------------------
 
    
def Sensor_C02():
    global C02
    UART_S8.write(b"\xFE\x44\x00\x08\x02\x9F\x25")
    sleep(3)
    if UART_S8.any() > 0:
        respuesta = UART_S8.read()
        HIGH = int(respuesta[3])
        LOW = int(respuesta[4])
        C02 = (HIGH*256) + LOW
        print('Dioxido de carbono:', C02)
        sleep(.1)
