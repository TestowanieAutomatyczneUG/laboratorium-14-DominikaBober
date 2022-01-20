Feature: FizzBuzz

    Scenario Outline: FizzBuzz gets <number>
    Given Play FizzBuzz
    When Give <number>
    Then Get <result>

    Examples:
        | number | result |
        | 15 | FizzBuzz |
        | 225 | FizzBuzz |
        | 3 | Fizz |
        | 9 | Fizz |
        | 5 | Buzz |
        | 25 | Buzz |
        | 8 | 8 |
