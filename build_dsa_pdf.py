"""Generate dsaSheet1.pdf with 20 DSA problem statements (full text)."""
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 8, "DSA Sheet 1 - 20 Problems", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def section_title(self, title: str):
        self.set_font("Helvetica", "B", 11)
        self.multi_cell(0, 6, title)
        self.ln(1)

    def body_text(self, text: str):
        self.set_font("Helvetica", "", 9)
        self.multi_cell(0, 4.5, text)
        self.ln(1.5)


def main():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=16)
    pdf.add_page()

    # Full problem text from specification (ASCII-safe)
    problems = r"""
--- Problem 1: Sum of Array Elements ---
Problem Statement
You are given an array of integers. Your task is to calculate the sum of all elements present in the array.
This is a basic operation frequently used in programming and helps in building a strong foundation for solving more complex problems.

Input: An array of integers.
Output: A single integer representing the sum of all elements in the array.

Input Format
The first line contains an integer n - the number of elements in the array.
The second line contains n space-separated integers representing the array elements.

Output Format
Print a single integer - the sum of all elements in the array.

Example 1
Input:
6
1 2 3 4 5 6
Output: 21
Explanation: 1 + 2 + 3 + 4 + 5 + 6 = 21

Example 2
Input:
3
5 10 15
Output: 30
Explanation: 5 + 10 + 15 = 30


--- Problem 2: Linear Search ---
Problem Statement
You are given an array of integers arr[] of size n and a target element x. Your task is to search for the element x in the array.
If the element is present, return its index (0-based indexing). If the element is not found, return -1.
This problem is based on the Linear Search technique, where each element is checked one by one.

Input: An array of integers; A target integer x
Output: An integer representing the index of element x if found; Otherwise, -1

Input Format
The first line contains an integer n - number of elements in the array
The second line contains n space-separated integers
The third line contains an integer x - the element to search

Output Format
Print a single integer: Index of x (0-based), if present; -1 if not present

Example 1
Input:
10
10 20 30 40 50 60 70 80 90 100
70
Output: 6
Explanation: Element 70 is found at index 6 (0-based indexing).

Example 2
Input:
9
1 2 3 4 5 6 7 8 9
6
Output: 5
Explanation: Element 6 is found at index 5.

Example 3 (Not Found Case)
Input:
5
2 4 6 8 10
7
Output: -1
Explanation: Element 7 is not present in the array.


--- Problem 3: Contains Duplicate ---
Problem Statement
You are given an integer array nums. Your task is to determine whether any value appears at least twice in the array.
If any element is repeated, return true. If all elements are distinct (unique), return false.
This problem helps in understanding basic array traversal and duplicate detection.

Input: An array of integers.
Output: Return true if any value appears at least twice; Return false if all elements are distinct

Input Format
The first line contains an integer n - number of elements in the array
The second line contains n space-separated integers representing the array

Output Format
Print true or false

Example 1
Input:
6
1 2 1 3 4 5
Output: true
Explanation: The element 1 appears more than once (at index 0 and 2), so the output is true.

Example 2
Input:
7
1 2 3 4 5 6 7
Output: false
Explanation: All elements are unique, so the output is false.


--- Problem 4: Two Sum ---
Problem Statement
You are given an array of integers nums and an integer target. Your task is to find two distinct indices such that the numbers at those indices add up to the target.
Return the indices (0-based) of the two numbers. If no such pair exists, return -1 (or an empty result, depending on requirement).
This is a classic Two Sum problem.

Input: An array of integers nums; An integer target
Output: A pair of indices [i, j] such that nums[i] + nums[j] = target. If no such pair exists, return -1

Input Format
The first line contains an integer n - number of elements in the array
The second line contains n space-separated integers
The third line contains an integer target

Output Format
Print two space-separated integers representing the indices. If no solution exists, print -1

Example 1
Input:
4
2 7 11 15
9
Output: 0 1
Explanation: nums[0] = 2 and nums[1] = 7; 2 + 7 = 9 matches target

Example 2
Input:
4
2 7 11 15
18
Output: 1 2
Explanation: nums[1] = 7 and nums[2] = 11; 7 + 11 = 18

Example 3 (No Solution)
Input:
4
1 2 3 4
10
Output: -1
Explanation: No two numbers sum to 10.


--- Problem 5: Intersection of Two Arrays ---
Problem Statement
You are given two integer arrays nums1 and nums2. Your task is to return an array representing their intersection.
Each element in the result must be unique. The result can be returned in any order.

Input: Two arrays of integers: nums1 and nums2
Output: An array containing unique common elements present in both arrays

Input Format
The first line contains an integer n - number of elements in nums1
The second line contains n space-separated integers
The third line contains an integer m - number of elements in nums2
The fourth line contains m space-separated integers

Output Format
Print the array containing unique intersection elements (space-separated or in list format)

Example 1
Input:
3
4 9 5
5
9 4 9 8 4
Output: 4 9
Explanation: Common elements are 4 and 9. Even though they appear multiple times, we include them only once.

Example 2
Input:
6
1 2 3 4 5 6
5
2 4 5 2 9
Output: 2 4 5
Explanation: Common unique elements are 2, 4, and 5.


--- Problem 6: Maximum and Minimum in Array ---
Problem Statement
You are given an array of integers arr[] of size N. Your task is to find the maximum and minimum elements in the array.
The maximum element is the largest value in the array. The minimum element is the smallest value in the array.

Input: An array of integers.
Output: Print the maximum element; Print the minimum element

Input Format
The first line contains an integer N - number of elements in the array
The second line contains N space-separated integers

Output Format
Print two lines:
Maximum Number is: <value>
Minimum Number is: <value>

Example 1
Input:
9
1 2 3 4 5 6 7 8 9
Output:
Maximum Number is: 9
Minimum Number is: 1
Explanation: The largest element is 9 and the smallest element is 1.

Example 2
Input:
5
6 7 18 3 9
Output:
Maximum Number is: 18
Minimum Number is: 3
Explanation: The largest element is 18 and the smallest is 3.


--- Problem 7: Perfect Square ---
Problem Statement
You are given a positive integer num. Your task is to determine whether the number is a perfect square.
A number is called a perfect square if it can be expressed as the product of an integer multiplied by itself (i.e., x * x = num).
Return true if num is a perfect square; Otherwise, return false

Input: A single positive integer num
Output: Print true if the number is a perfect square; Print false otherwise

Input Format: A single integer num
Output Format: Print true or false

Example 1
Input: 81
Output: true
Explanation: 81 = 9 * 9 - perfect square

Example 2
Input: 64
Output: true
Explanation: 64 = 8 * 8 - perfect square

Example 3
Input: 10
Output: false
Explanation: 10 cannot be expressed as x * x for any integer x


--- Problem 8: Factorial ---
Problem Statement
You are given a positive integer n. Your task is to calculate the factorial of the number.
The factorial of a number n is defined as: n! = n * (n-1) * (n-2) * ... * 1

Input: A single positive integer n
Output: A single integer representing the factorial of n

Input Format: A single integer n
Output Format: Print the value of n!

Example 1
Input: 5
Output: 120
Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120

Example 2
Input: 6
Output: 720
Explanation: 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720


--- Problem 9: Armstrong Number ---
Problem Statement
You are given a positive integer num. Your task is to determine whether the number is an Armstrong number.
An Armstrong number (also called a Narcissistic number) is a number in which the sum of its digits each raised to the power of the number of digits is equal to the number itself.

Input: A single positive integer num
Output: Print true if the number is an Armstrong number; Print false otherwise

Input Format: A single integer num
Output Format: Print true or false

Example 1
Input: 153
Output: true
Explanation: Number of digits = 3; 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153. So, it is an Armstrong number.

Example 2
Input: 370
Output: true
Explanation: Number of digits = 3; 3^3 + 7^3 + 0^3 = 27 + 343 + 0 = 370.

Example 3
Input: 123
Output: false
Explanation: 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36 != 123.


--- Problem 10: Subarrays with Sum Equal to Target ---
Problem Statement
You are given an integer array arr[] and an integer target. Your task is to find all continuous subarrays whose sum is equal to the given target.
A subarray is a sequence of elements that are contiguous (next to each other) in the array.

Input: An array of integers arr[]; An integer target
Output: Print all subarrays whose sum equals the target. Each subarray should be printed separately.

Input Format
The first line contains an integer n - number of elements in the array
The second line contains n space-separated integers
The third line contains an integer target

Output Format
Print each valid subarray on a new line

Example 1
Input:
7
2 5 -3 1 4 -2 3
6
Output:
2 5 -3 1 4 -2
5 -3 1 4 -2 3
1 4 -2 3
3 1 4 -2

Explanation: The following subarrays have sum = 6:
[2, 5, -3, 1, 4, -2], [5, -3, 1, 4, -2, 3], [1, 4, -2, 3], [3, 1, 4, -2]
All are continuous parts of the array.


--- Problem 11: Missing Number ---
Problem Statement
You are given an array nums[] containing n distinct numbers taken from the range [0, n]. Your task is to find the only number missing from this range.

Constraints
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All elements in nums are unique

Input: An array of integers nums[]
Output: A single integer representing the missing number

Input Format
The first line contains an integer n - number of elements
The second line contains n space-separated integers

Output Format
Print the missing number

Example 1
Input:
3
3 0 1
Output: 2
Explanation: Numbers should be from 0 to 3 -> {0, 1, 2, 3}. But 2 is missing.

Example 2
Input:
4
0 1 2 3
Output: 4
Explanation: Numbers should be from 0 to 4 -> {0, 1, 2, 3, 4}. But 4 is missing.


--- Problem 12: Sum of Square Numbers ---
Problem Statement
You are given a non-negative integer c. Your task is to determine whether there exist two integers a and b such that:
a^2 + b^2 = c
Return true if such integers exist; Otherwise, return false

Constraints: 0 <= c <= 2^31 - 1

Input: A single non-negative integer c
Output: Print true if there exist integers a and b satisfying the condition; Print false otherwise

Input Format: A single integer c
Output Format: Print true or false

Example 1
Input: 5
Output: true
Explanation: We can take a = 1, b = 2; 1^2 + 2^2 = 1 + 4 = 5

Example 2
Input: 3
Output: false
Explanation: There are no integers a and b such that a^2 + b^2 = 3


--- Problem 13: Valid Anagram ---
Problem Statement
You are given two strings s and t. Your task is to determine whether t is an anagram of s.
An anagram means both strings contain: The same characters; With the same frequency; But possibly in a different order.
Return true if t is an anagram of s; Otherwise, return false

Constraints: 1 <= s.length, t.length <= 5 * 10^4; s and t consist of lowercase English letters

Input: Two strings s and t
Output: Print true if t is an anagram of s; Print false otherwise

Input Format: First line contains string s; Second line contains string t
Output Format: Print true or false

Example 1
Input:
anagram
nagaram
Output: true
Explanation: Both strings contain the same characters with the same frequency.

Example 2
Input:
rat
car
Output: false
Explanation: Characters and frequencies do not match.


--- Problem 14: Isomorphic Strings ---
Problem Statement
You are given two strings s and t. Your task is to determine whether the two strings are isomorphic.
Two strings are isomorphic if:
Each character in s can be mapped to a character in t
The mapping is consistent
No two characters in s map to the same character in t
A character may map to itself
The order of characters must be preserved
Return true if the strings are isomorphic; Otherwise, return false

Constraints: 1 <= s.length <= 5 * 10^4; t.length == s.length; s and t consist of valid ASCII characters

Input: Two strings s and t
Output: Print true if the strings are isomorphic; Print false otherwise

Input Format: First line contains string s; Second line contains string t
Output Format: Print true or false

Example 1
Input:
egg
add
Output: true
Explanation: e -> a, g -> d. Mapping is consistent and valid.

Example 2
Input:
foo
bar
Output: false
Explanation: o maps to two different characters - invalid mapping.


--- Problem 15: String to Integer (atoi) ---
Problem Statement
Implement a function myAtoi(string s) that converts a given string into a 32-bit signed integer.
The conversion follows these rules:
Ignore leading whitespaces
Check sign ('+' or '-')
Default is positive if no sign is present
Read digits until a non-digit character is found
If no digits are found, return 0
Clamp the result within the 32-bit signed integer range:
Minimum: -2^31
Maximum: 2^31 - 1

Constraints: 0 <= s.length <= 200; s consists of English letters, digits, '+', '-', '.', and whitespace

Input: A string s
Output: A 32-bit signed integer after conversion

Input Format: A single string s
Output Format: Print the converted integer

Example 1: Input 42 -> Output 42
Example 2: Input "   -42" -> Output -42 (leading spaces ignored, negative sign)
Example 3: Input "4193 with words" -> Output 4193 (stops at non-digit)
Example 4: Input "words and 987" -> Output 0 (no valid number at start)
Example 5 (Overflow): Input 91283472332 -> Output 2147483647 (clamped to 2^31 - 1)


--- Problem 16: Second Smallest and Second Largest ---
Problem Statement
You are given an array of integers arr[]. Your task is to find:
The second smallest element; The second largest element
If duplicate values exist, consider distinct elements only while determining the result.

Input: An array of integers arr[]
Output: Print the second smallest element; Print the second largest element

Input Format
The first line contains an integer n - number of elements in the array
The second line contains n space-separated integers

Output Format
Print two lines:
Second Smallest: <value>
Second Largest: <value>

Example 1
Input:
5
3 1 5 2 4
Output:
Second Smallest: 2
Second Largest: 4
Explanation: Sorted distinct array -> {1, 2, 3, 4, 5}; Second smallest = 2; Second largest = 4

Example 2
Input:
5
10 10 20 20 30
Output:
Second Smallest: 20
Second Largest: 20
Explanation: Distinct elements -> {10, 20, 30}; Second smallest = 20; Second largest = 20


--- Problem 17: Fibonacci Number ---
Problem Statement
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
F(0) = 0, F(1) = 1
F(n) = F(n-1) + F(n-2), for n > 1

You are given an integer n. Your task is to compute the n-th Fibonacci number.

Constraints: 0 <= n <= 30

Input: A single integer n
Output: Print the value of the n-th Fibonacci number

Input Format: A single integer n
Output Format: Print F(n)

Example 1
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1

Example 2
Input: 10
Output: 55
Explanation: Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55. So F(10) = 55


--- Problem 18: Pow(x, n) ---
Problem Statement
Implement a function pow(x, n) that calculates the value of a number x raised to the power n, i.e., x^n

Constraints:
-100.0 < x < 100.0
-2^31 <= n <= 2^31 - 1
n is an integer
Either x != 0 or n > 0
-10^4 <= x^n <= 10^4

Input: A floating-point number x; An integer n
Output: A floating-point number representing x^n

Input Format: First line contains a floating-point number x; Second line contains an integer n
Output Format: Print the result of x^n

Example 1
Input:
2.00000
10
Output: 1024.00000
Explanation: 2^10 = 1024

Example 2
Input:
2.10000
3
Output: 9.26100
Explanation: 2.1^3 = 2.1 * 2.1 * 2.1 = 9.261

Example 3
Input:
2.00000
-2
Output: 0.25000
Explanation: 2^(-2) = 1 / (2^2) = 1/4 = 0.25


--- Problem 19: Search a 2D Matrix ---
Problem Statement
You are given an m x n integer matrix matrix with the following properties:
Each row is sorted in non-decreasing order
The first element of each row is greater than the last element of the previous row
You are also given an integer target. Your task is to determine whether the target exists in the matrix.
You must solve the problem with time complexity O(log(m * n)).

Return true if the target exists; Otherwise, return false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4

Input: A 2D array (matrix) of integers; An integer target
Output: Print true if target is found; Print false otherwise

Input Format
First line contains two integers m and n
Next m lines each contain n space-separated integers
Last line contains integer target

Output Format: Print true or false

Example 1
Input:
3 4
1 3 5 7
10 11 16 20
23 30 34 60
3
Output: true
Explanation: The element 3 is present in the matrix.

Example 2
Input:
3 4
1 3 5 7
10 11 16 20
23 30 34 60
13
Output: false
Explanation: The element 13 is not present in the matrix.


--- Problem 20: Power of Three ---
Problem Statement
You are given an integer n. Your task is to determine whether the number is a power of three.
A number is a power of three if there exists an integer x such that: n = 3^x
Return true if n is a power of three; Otherwise, return false

Constraints: -2^31 <= n <= 2^31 - 1

Input: A single integer n
Output: Print true if n is a power of three; Print false otherwise

Input Format: A single integer n
Output Format: Print true or false

Example 1
Input: 27
Output: true
Explanation: 27 = 3^3 - power of three

Example 2
Input: 0
Output: false
Explanation: 0 cannot be expressed as 3 raised to any power.

Example 3
Input: 9
Output: true
Explanation: 9 = 3^2 - power of three
"""

    pdf.set_font("Helvetica", "", 9)
    # Split into titled chunks for slightly nicer breaks at problem headers
    chunks = problems.strip().split("\n\n--- ")
    for i, chunk in enumerate(chunks):
        if i == 0:
            text = chunk.strip()
        else:
            text = "--- " + chunk.strip()
        pdf.multi_cell(0, 4.5, text)
        pdf.ln(2)

    out_path = r"c:\Users\murali\Desktop\DSASheet\dsaSheet1.pdf"
    pdf.output(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
