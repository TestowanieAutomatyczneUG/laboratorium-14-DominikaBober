import sys
sys.path.append('./zadanie1')
from behave import *
from src.FizzBuzz import FizzBuzz

use_step_matcher("re")

@given('Play FizzBuzz')
def step_impl(context):
    context.FizzBuzz = FizzBuzz()

@when('Give (?P<number>.+)')
def step_impl(context, number):
    context.result = context.FizzBuzz.play(int(number))

@then('Get (?P<result>.+)')
def step_impl(context, result):
    assert context.result == result
