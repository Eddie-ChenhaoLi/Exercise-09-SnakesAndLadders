Feature: snakes and ladders

  Scenario Outline: move
    Given I have a position <p>
    When the dice rolls out of <i>
    Then I should move to new position <np>

    Examples: move
      | p  | i | np |
      | 1  | 6 | 7  |
      | 7  | 5 | 12 |
      | 12 | 4 | 16 |

  Scenario Outline: ladders
    Given I have a position <p>
    When the position is on the bottom of a ladder <bottom>
    Then I should move to the top <top>

    Examples: ladders
      | p  | bottom | top |
      | 12 | 12     | 25  |
      | 2  | 2      | 16  |
      | 5  | 5      | 20  |

  Scenario Outline: snakes
    Given I have a position <p>
    When the position is on the head of a snake <head>
    Then I should move to the tail <tail>

    Examples: snakes
      | p  | head | tail |
      | 35 | 35   | 23   |
      | 28 | 28   | 21   |
      | 22 | 22   | 15   |

  Scenario Outline: win
    Given I have a position <p>
    When the position is greater than or equal to 36
    Then I should win the game <win>

    Examples: win
      | p  | win |
      | 28 | 0   |
      | 36 | 1   |
      | 40 | 1   |