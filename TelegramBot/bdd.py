from behave import given, when, then
from functions import *

@given(u'An existing city')
def step_impl(context):
    context.city = "Moscow"
@given(u'A non-existing city')
def step_impl(context):
    context.city = "Мазква"
@when(u'Trying to check it')
def step_impl(context):
    context.result = str(city_check(context.city))
@given(u'A normal image request')
def step_impl(context):
    context.image_request = "cat"
@given(u'A weird image request')
def step_impl(context):
    context.image_request = "fgycsynvuyqcu8947qwyyfHuank"
@when(u'Finding image')
def step_impl(context):
    context.result = konachan(context.image_request)
@then(u'The next result is expected: "{result}"')
def step_impl(context, result: str):
    assert context.result == result
@then(u'We expect to receive an image')
def step_impl(context):
    assert context.result != "ERROR"

# behave features/bdd.feature