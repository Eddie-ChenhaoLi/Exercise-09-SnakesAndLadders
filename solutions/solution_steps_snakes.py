from behave import *
from demo import *


@Given('I have a position {p:d}')
def step_impl(context, p):
    context.p = p


@When('the position is on the head of a snake {head:d}')
def step_impl(context, head):
    context.head = head


@Then('I should move to the tail {tail:d}')
def step_impl(context, tail):
    new_position = move_snakes(context.head)
    assert new_position == tail
