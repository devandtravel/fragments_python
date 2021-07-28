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
        <td><pre>afrhnjil
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
    </tr>
    <tr>
        <td>filling_list_by_iterator</td>
        <td>Creates a sheet from the entered lines until the entered line equals "."</td>
        <td><pre>aaaaaa
bbbbbb
cccccc
.
# ['aaaaaa', 'bbbbbb', 'cccccc']
</pre></td>
    </tr>
</table>
