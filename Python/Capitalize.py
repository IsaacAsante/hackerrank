"""Author: Isaac Asante
 * HackerRank URL for this exercise: https://www.hackerrank.com/challenges/capitalize/problem
 * Original video explanation: https://www.youtube.com/watch?v=RSH33rrAF5s 
 * Last verified on: May 13, 2024

 * IMPORTANT:
 * This code is meant to be used as a solution on HackerRank (link above).
 * It is not meant to be executed as a standalone program.
 */
"""


def solve(s):
    # One-line solution
    return "".join(
        [c.capitalize() if c[0].isalpha() else c for c in re.split(r"(\s+)", s)]
    )
    # Using re.split(r'(\s+)', s) helps retain any number of whitespaces after joining back the tokens.
