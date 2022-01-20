import sys
sys.path.append('./zadanie3')
from behave import *
from src.check_ISBN import ISBN

use_step_matcher("re")

@given('Run ISBN')
def step_impl(context):
    context.ISBN = ISBN()

@when('Give (?P<number>.+)')
def step_impl(context, number):
    context.result = context.ISBN.check_ISBN(number)

@then('Get (?P<result>.+)')
def step_impl(context, result):
    assert context.result == bool(int(result))
