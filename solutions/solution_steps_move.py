from behave import *
from demo import *


@Given('I have a position {p:d}')
def step_impl(context, p):
    context.p = p


@When('the dice rolls out of {i:d}')
def step_impl(context, i):
    context.i = i


@Then('I should move to new position {np:d}')
def step_impl(context, np):
    position = move(context.p, context.i)
    assert position == np
