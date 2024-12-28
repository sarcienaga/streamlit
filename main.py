import network
import machine
import time
import urequests

# Configuración del sensor en GPIO 36 (cambiar el GPIO)
sensor_pin = 36
adc = machine.ADC(machine.Pin(sensor_pin))

# Configuración de la red WiFi
ssid = 'nombre de la red Wifi'
password = 'clave de la red'

# Conectar a la red WiFi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    pass

print('Conexión exitosa')
print(station.ifconfig())

# URL del script de Google Apps Script
google_script_url = "https://script.google.com/macros/s/AKfycbwtTI2HgTD9GvcYE3h_qaTNK1xcK2igr33ooPcNU-E-UiHQ9ywSCGKioAMVLSFyWzrwUg/exec"
# Bucle principal
while True:
    sensor_value = adc.read()
    response = urequests.get(f"{google_script_url}?sensor_value={sensor_value}")
    print(response.text)
    time.sleep(1)  # Envía datos cada 60 segundos
