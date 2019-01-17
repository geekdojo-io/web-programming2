# Web Programming Course II

## Curriculum
This course takes a deeper dive from the Web Programming Course I. Similar to the Web Programming Course I, each class is 2 hours long with the first hour devoted to algorithms/programming challenges and the rest devoted to web programming.

#### Algorithms/Programming Challenges

- Binary Numbers / Number Theory
- Binary Search
- Big O notation
- Sort
- Recursion
- Dictionary

#### Web Programming

- Cloud Computing with Amazon AWS
- Learn how Bootstrap can make dealing with CSS easier
- Learn web forms
- Learn database and database programming
- Build your own web applications
- Build a large web application with team

## Textbook

#### Algorithms/Programming Challenges
This course will use Grokking Algorithms by Aditya Y. Bhanrgava as a textbook for web programming.

#### Web Programming
This course will use Flask Web Development, 2nd edition by Miguel Grinberg as a textbook for web programming.

---
## Week1 - Refresh Previous Course

### Review of Binary Numbers

#### Power of 2s
|  Power of 2 | Exact Value   | Approx. Value   | MB, GB, etc.  |
|---|---|---|---|
| 7  | 128  |   |   |
| 8  | 256  |   |   |
| 10  | 1,024  | 1 thousand  | 1 K  |
| 16  | 65,536  |   | 64 K  |
| 20  | 1,048,576  | 1 million  | 1 MB  |
| 30  | 1,073,741,824  | 1 billion  | 1 GB  |
| 32  | 4,294,967,296  |  | 4 GB  |
| 40  | 1,099,511,627,776  | 1 trillion | 1 TB  |

#### Bitwise AND (&)

| A | B | A & B |
|--|--|--|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

Example:

13 & 11
```
13          0001101
11          0001011
13 & 11     0001001
```

#### Bitwise AND (&)

### Prime Numbers

```python

import math

# Simple approach
def isPrime1(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Slightly optimized
def isPrime2(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True 

# More optimized
def isPrime3(n):
    if n < 2:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True 

N = int(input())
print(isPrime3(N))

```


#### Routes and Templates

#### CSS

#### Flask Template 

---

## Week2 - AWS Lambda - Slack Notification

### Binary Numbers - Base Conversion

```python

def convertToBase2(n):
    s = ''
    while n > 0:
        if n % 2 == 0:
            s = '0' + s
        else:
            s = '1' + s
        n >>= 1
    return s

def convertBinaryToBase10(s):
    n = 0
    digit = 1
    for i in reversed(range(len(s))):
        n += int(s[i]) * digit
        digit <<= 1
    return n

N = int(input('Enter base10 integer, i.e. 13: '))
print(convertToBase2(N))
s = input('Enter binary string, i.e. 1010: ')
print(convertBinaryToBase10(s))


```
### AWS Lambda for Slack Notification
```python
import json
from botocore.vendored import requests

print('Loading function')

def lambda_handler(event, context):

    BASE_URL = 'https://hooks.slack.com/services'
    
    API_PATH = '{YOUR_API_PATH}'
    msg = '{some message}'
    
    
    data = '{{"text":"{}"}}'.format(msg)
    
    wekbook_url =  '{}/{}'.format(BASE_URL, API_PATH)    

    response = requests.post(wekbook_url, data=data, headers={'Content-Type': 'application/json'})    

    print('Response: ' + str(response.text))
    print('Response code: ' + str(response.status_code))

```

---

## Week3 - Web Forms

Web Forms

Web Forms in Python

---

## Week4 - Database Programming

Database

SQL

SQL vs. NoSQL

MySQL

MySQL in Python

---

## Week5 - Email

Sending an email

---

## Week6 - Large App Structure

Project structure

---

## Week7 - Project 1

Pet-Rescue

---

## Week8 - Project 2



---

## Week9 - Project 3

---

## Week10 - Project 4
