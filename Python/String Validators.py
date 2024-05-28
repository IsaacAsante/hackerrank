"""Author: Isaac Asante
 * HackerRank URL for this exercise: https://www.hackerrank.com/challenges/string-validators/problem
 * Original video explanation: https://www.youtube.com/watch?v=DQISDEt541g
 * Last verified on: May 28, 2024

 * IMPORTANT:
 * This code is meant to be used as a solution on HackerRank (link above).
 * It is not meant to be executed as a standalone program.
 */
"""

if __name__ == "__main__":
    s = input()
    # Don't add parentheses for functions
    criteria = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]

    # Call the functions on each character
    for function in criteria:
        print(any(function(char) for char in s))
