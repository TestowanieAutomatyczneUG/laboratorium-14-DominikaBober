Feature: ISBN

    Scenario Outline: ISBN gets <number>
    Given Run ISBN
    When Give <number>
    Then Get <result>

    Examples:
        | number | result |
        | 978-3-16-148410-0 | 1 |
        | 978-1-4028-9462-6 | 1 |
        | 978-1-56619-909-4 | 1 |
        | 978-1-86197-876-9 | 1 |
        | 978-3-16-140010-0 | 1 |
        | 978-3-16-148410-0 | 1 |
        | 986-1-4028-9262-7 | 0 |
        | 940-1-4028-9472-7 | 0 |
        | 980-4-4028-9462-7 | 0 |
        | 980-1-4028 | 0 |
