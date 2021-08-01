# Fragments of Python code

This folder contains useful independent fragments of Python code.  
You can use this fragments in your applications to implement some pieces of functionality.

## Contents

<table border>
    <tr>
        <th>Folder name</th>
        <th>Description</th>
        <th>Usage</th>
    </tr>
    <tr>
        <td><h3>letcode</h3></td>
    </tr>
    <tr>
        <td>maxSubArray</td>
        <td>Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. A subarray is a contiguous part of an array.</td>
        <td><pre>nums = [-2,1,-3,4,-1,2,1,-5,4]<br/>
# 6</br>Explanation: [4,-1,2,1] has the largest sum = 6.
</pre></td>
    </tr>
    <tr>
        <td>max_profit</td>
        <td>You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0</td>
        <td><pre>prices = [7,1,5,3,6,4]<br/>
# 5
</pre></td>
    </tr>
    <tr>
        <td>climb_stairs</td>
        <td>You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?</td>
        <td><pre>n = 3<br/>
# 3
</pre></td>
    </tr>
    <tr>
        <td>single_number</td>
        <td>Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space</td>
        <td><pre>nums = [4,1,2,1,2]<br/>
# 4
</pre></td>
    </tr>
    <tr>
        <td>find_dissapeared_numbers</td>
        <td>Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums</td>
        <td><pre>nums = [4, 3, 2, 7, 8, 2, 3, 1]<br/>
# [5, 6]
</pre></td>
    </tr>
    <tr>
        <td>missing_number</td>
        <td>Returns missing number in given sequence of natural numbers</td>
        <td><pre>print(missingNumber([1, 7, 5, 2, 4, 3]))<br/>
# 6
</pre></td>
    </tr>
    <tr>
        <td>contains_duplicate</td>
        <td>Returns True if given nums list contains duplicate or False if given nums list does not contains duplicate</td>
        <td><pre>print(containsDuplicate([x for x in range(42)]))<br/>
# False
</pre></td>
    </tr>
    <tr>
        <td><h3>algorithms</h3></td>
    </tr>
    <tr>
        <td><h4>sort</h4></td>
    </tr>
    <tr>
        <td><h5>sort_bubble</h5></td>
    </tr>
    <tr>
        <td>sort_bubble_primitive</td>
        <td>Bubble sort like a dumb</td>
        <td><pre>[1, 56, 32, 6, 56, 34, 86798, 23, 54]
# [1, 6, 23, 32, 34, 54, 56, 56, 86798]</pre></td>
    </tr>
    <tr>
        <td>sort_bubble</td>
        <td>Bubble sort</td>
        <td><pre>[1, 56, 32, 6, 56, 34, 86798, 23, 54]
# [1, 6, 23, 32, 34, 54, 56, 56, 86798]</pre></td>
    </tr>
    <tr>
        <td>pig_it</td>
        <td>Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched</td>
        <td><pre>pig_it('Pig latin is cool')
# igPay atinlay siay oolcay
pig_it('Hello world !')
# elloHay orldway !</pre>
        </td>
    </tr>
    <tr>
        <td>find_repeating_symbols</td>
        <td>If symbols is repeated add "(" to return, else add ")" to return</td>
        <td><pre>print(find_repeating_symbols('qqQjaaaa'))
# ((()((((</pre></td>
    </tr>
    <tr>
        <td>array2phone</td>
        <td>Converts numbers array to phone number without verification</td>
        <td><pre>print(array2phone([9, 9, 9, 1, 2, 3, 4, 5, 6, 7]))
# (999) 123-4567</pre></td>
    </tr>
    <tr>
        <td>number2cells</td>
        <td>Converts number to cells without verification</td>
        <td><pre>Enter cells: 123456789
```
---------
| 1 2 3 |
| 4 5 6 |
| 7 8 9 |
---------
```</pre></td>
    </tr>
    <tr>
        <td>is_prime</td>
        <td>Is it number prime or not?</td>
        <td><pre>17
# This number is prime
8
# This number is not prime
</pre></td>
    </tr>
    <tr>
        <td>calculator</td>
        <td>Simple calculator with support of "+", "-", "/", "*", "mod", "pow", "div" operators</td>
        <td><pre>17
45
*
# 765.0
</pre></td>
    </tr>
    <tr>
        <td>vowel_and_consonant</td>
        <td>Defines vowels and consonants in a string</td>
        <td><pre>afrhnjil<br/>
```
vowel
consonant
consonant
consonant
consonant
consonant
vowel
consonant
```
</pre></td>
    </tr>
    <tr>
        <td>filling_list_by_iterator</td>
        <td>Creates a sheet from the entered lines until the entered line equals "."</td>
        <td><pre>aaaaaa
bbbbbb
cccccc
.<br/>
# ['aaaaaa', 'bbbbbb', 'cccccc']
</pre></td>
    </tr>
    <tr>
        <td>get_random_menu</td>
        <td>Creates a random menu from given dictionaries with dishes and prices</td>
        <td><pre>appetizers =<br/>{'country greens': 12, 'onion rings': 13, 'butterbrodt': 46}
main_courses =<br/>{'super potato': 612, 'soup': 143, 'curry': 436}
desserts =<br/>{'shugar': 1, 'donat': 8, 'cake': 4}<br/>
# ['butterbrodt', 'curry', 'cake'] [46, 436, 4] 486
</pre></td>
    </tr>
    <tr>
        <td>input_int_number</td>
        <td>Reads a line until an integer or stop word is entered</td>
        <td><pre>Please enter an integer:
> g
You have entered the wrong type of data.<br/>Enter an integer or the word "stop" to exit the program:
> 6<br/>
Please enter an integer:
> s
You have entered the wrong type of data.<br/>Enter an integer or the word "stop" to exit the program:
> stop
</pre></td>
    </tr>
    <tr>
        <td>show_time_of_pid</td>
        <td>Shows time of process id using regular expression parsing</td>
        <td><pre>show_time_of_pid(
"Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")<br/>
# Jul 6 14:03:01 pid:29440
</pre></td>
    </tr>
    <tr>
        <td>get_prime_numbers_list</td>
        <td>Returns prime numbers list from 0 to given number</td>
        <td><pre>number = 30
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
</pre></td>
    </tr>
    <tr>
        <td>args_parser</td>
        <td>Returns list of ingredients provided by command line arguments</td>
        <td><pre>python args_parser.py -i1 pasta -i2 rice<br/>-i3 potato -i4 carrot -i5 onion --salt --pepper True<br/>
# The ingredients you provided are:<br/>['pasta', 'rice', 'potato', 'carrot',<br/>'onion', 'salt', 'pepper']
</pre></td>
    </tr>
    <tr>
        <td>is_sequence_unic</td>
        <td>Returns True if given sequence is unic of False if given sequence is not unic</td>
        <td><pre>print(is_sequence_unic([x for x in range(42)]))<br/>
# True
</pre></td>
    </tr>
    <tr>
        <td>get_cumulative_sum_list</td>
        <td>Returns cumulative sum list from digits of given number</td>
        <td><pre>input a number
436546
# using numpy
[4, 7, 13, 18, 22, 28]</br>
input a number
3456347
# using list comprehension
[3, 7, 12, 18, 21, 25, 32]
</pre></td>
    </tr>
    <tr>
        <td>hangman</td>
        <td>Game. Guess the word letter by letter and survive</td>
        <td><pre>H A N G M A N
Type "play" to play the game, "exit" to quit: play

---

Input a letter: g
No such letter in the word

---

Input a letter: 6
It is not an ASCII lowercase letter

---

Input a letter: i
No such letter in the word

---

Input a letter: p

p-----
Input a letter: y

py----
Input a letter: h

py-h--
Input a letter: n

py-h-n
Input a letter: o

py-hon
Input a letter: t
You guessed the word python!
You survived!

Type "play" to play the game, "exit" to quit: exit

</pre></td>
    </tr>
    <tr>
        <td>hangman_oop</td>
        <td>OOP realisation of the HANGMAN game</td>
    </tr>
    <tr>
        <td>hangman_regex</td>
        <td>RegEx realisation of the HANGMAN game</td>
    </tr>
</table>
