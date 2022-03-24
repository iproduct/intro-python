from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

@given('I search for a valid account "{account_id}"')
def step_impl(context, account_id):
    result = context.client.get(f'http://localhost:8000/accounts/{account_id}')
    context.response(result)

@then('I will see the account details for "{account_id}"')
def step_impl(context, account_id):
    assert context.response.status_code == 200
    assert getattr(context.response.json(), "id") == account_id
