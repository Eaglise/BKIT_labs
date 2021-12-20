from behave import given, when, then
from bridge import *

@given(u'Chief starts cooking')
def step_impl(context):
    context.cook = SaladCook()
    context.chief = SaladChief(context.cook)
@when(u'Someone ordered a {order}')
def step_impl(context, order: str):
    if order == "meat salad":
        context.result = "Cooking meat salad..."
    elif order == "vegetarian salad":
        context.result = "Cooking vegetarian salad..."

@given(u'A meat salad')
def step_impl(context):
    context.cook = SaladCook()
    context.chief = SaladChief(context.cook)
    context.chief.cook_meat_salad()
@given(u'A vegetarian salad')
def step_impl(context):
    context.cook = SaladCook()
    context.chief = SaladChief(context.cook)
    context.chief.cook_vegetarian_salad()
@given(u'No salad')
def step_impl(context):
    context.cook = SaladCook()
    context.chief = SaladChief(context.cook)
@when(u'Someone asked the ingredients')
def step_impl(context):
    context.result = context.cook.salad.list_ingredients()

@then(u'The next result is expected: "{result}"')
def step_impl(context, result: str):
    assert context.result == result
