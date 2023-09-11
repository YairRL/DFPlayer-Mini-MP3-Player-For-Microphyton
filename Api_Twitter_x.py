def tweet():
    # Verifica si hay una conexión a internet disponible
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('No hay conexión a internet disponible no se puede mandar tuit')
        
        return
    # Configura tus credenciales de API de ThingTweet
    oled_ssd1306()
    api_key = '8T29HC3NDKBIJ4WP'
    message = 'LOS NIVELES DE CO2 SON DE RIESGO : {} Ppm, la temperatura es {} C, la humedad es {} y la Presión atmosferica es {}hPa'.format(C02, temp, hum, pres)
    url = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = 'api_key={}&status={}'.format(api_key, message)
    response = urequests.post(url, headers=headers, data=data)
    print(response.content)
    