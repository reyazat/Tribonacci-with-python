# Tribonacci-with-python
The famous and important Fibonacci series is deϐined to start with values (1, 1) and from there, each element in the sequence equals the sum of the previous two elements. However, a cute variation aptly called the Tribonacci series works otherwise the same way, but starts with a triple of values (1, 1, 1) and from there, each element equals the sum of the previous three elementsThe famous and important Fibonacci series is deϐined to start with values (1, 1) and from there, each element in the sequence equals the sum of the previous two elements. 
However, a cute variation aptly called the Tribonacci series works otherwise the same way, but starts with a triple of values (1, 1, 1) and from there, each element equals the sum of the previous three elements.
Tribonacci numbers grow quite a bit faster than Fibonacci numbers, the ϐirst twenty being 1, 1, 1, 3,5, 9, 17, 31, 57, 105, 193, 355, 653, 1201, 2209, 4063, 7473, 13745, 25281, and 46499.
Given the element position n and optionally some other starting triple of values than (1, 1, 1), compute and return the element in the position n of the resulting Tribonacci series. As usual, the position numbering in a sequence starts from zero. Since n can get pretty large, you can't solve this problem with recursion, since your function would crash with a stack overϐlow once the recursion
limit is exceeded. Instead, you need to remember the three most recent values, and in a loop, use them to compute the next value of the sequence .

|    n   | start     |     Expected result                  |
|    0   | (1, 1, 1) |     1                                |
|    10  | (1, 1, 1) |     193                              |
|    10  | (4, 3, 2) |     542                              |
|    100 | (2, 2, 2) |     254143235774005504298869962      |

|    Date    |                 Challenge(s)                 |
| ---------  |   -----------------------------------------  |
| 1/4/2019   |       ryerson_letter_grade, is_ascending     |