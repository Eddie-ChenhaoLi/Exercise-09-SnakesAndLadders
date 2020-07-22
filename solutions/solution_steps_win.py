from behave import *
from demo import *


@Given('I have a position {p:d}')
def step_impl(context, p):
    context.p = p


@When('the position is greater than or equal to 36')
def step_impl(context):
    context.w = win(context.p)


@Then('I should win the game {win:d}')
def step_impl(context, win):
    assert context.w == win
