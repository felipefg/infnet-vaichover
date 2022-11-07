import json
from unittest.mock import patch

from behave import given, when, then

import rain.rain


@given('the forecast for precipitation is {forecast}')
def given_forecast(context, forecast):
    parsed_forecast = json.loads(forecast)

    ow_response = {
        "hourly": {
            "precipitation": parsed_forecast
        }
    }
    context.ow_response = ow_response


@given('the rain threshold is {threshold:f}')
def given_threshold(context, threshold):
    context.threshold = threshold


@when('I make a request')
def when_request(context):

    with patch('rain.rain.retrieve_forecast') as mock_forecast:
        mock_forecast.return_value = context.ow_response

        if "threshold" in context:
            threshold = context.threshold
        else:
            threshold = 0.0
        response = rain.rain.will_it_rain(threshold)

        context.response = response


@then('the response will contain "{response}"')
def response_contains(context, response):
    assert response in context.response
