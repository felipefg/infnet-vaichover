from behave import given, when, then


@given('the forecast for precipitation is {forecast}')
def given_forecast(context, forecast):
    pass


@given('the rain threshold is {threshold}')
def given_threshold(context, threshold):
    pass


@when('I make a request')
def when_request(context):
    pass


@then('the response will contain "{response}"')
def response_contains(context, response):
    pass
