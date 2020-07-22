from behave import *
from demo import *


@Given('I have a position {p:d}')
def step_impl(context, p):
    context.p = p


@When('the position is on the bottom of a ladder {bottom:d}')
def step_impl(context, bottom):
    context.bottom = bottom


@Then('I should move to the top {top:d}')
def step_impl(context, top):
    new_position = move_ladders(context.p)
    assert new_position == top
