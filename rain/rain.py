def retrieve_forecast():
    """Comunicar com o OpenWeather retornar o json completo"""


def get_rain_status(forecast, threshold=0.0):
    """Determinar se vai chover baseado no forecast"""
    precip = forecast["hourly"]["precipitation"]
    return any(x > threshold for x in precip)


def will_it_rain(threshold=0.0):
    """Funcao principal que vai retornar o texto se chove ou nao"""
    forecast = retrieve_forecast()
    rain = get_rain_status(forecast, threshold)

    if rain:
        return "Vai chover sim"

    return "Nao vai chover"
