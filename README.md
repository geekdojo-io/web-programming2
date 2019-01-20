# Web Programming Course II

## Curriculum
This course takes a deeper dive from the Web Programming Course I. Similar to the Web Programming Course I, each class is 2 hours long with the first hour devoted to algorithms/programming challenges and the rest devoted to web programming.

#### Algorithms/Programming Challenges

- Binary Numbers / Number Theory
- Computers (Architecture & Compilers)
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
- Rest APIs
- Distributed computing

## Textbook

#### Algorithms/Programming Challenges
This course will use Grokking Algorithms by Aditya Y. Bhanrgava as a textbook for web programming.

#### Web Programming
This course will use Flask Web Development, 2nd edition by Miguel Grinberg as a textbook for web programming.

---
## Week1 - Refresh Previous Course

### Lecture Note
[Lecture Note for Week 1](https://github.com/geekdojo-io/web-programming2/blob/master/LectureNote_Week1.pdf)

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

---

## Week2 - Digital Circuits, Cloud Computing and AWS Lambda


### Lecture Note
[Lecture Note for Week 2](https://github.com/geekdojo-io/web-programming2/blob/master/LectureNote_Week2.pdf)

### Digitial Circuits

#### Bitwise OR (&) / AND Gate

![alt text](/images/and_gate.png)


#### Bitwise OR (|) / OR Gate

![alt text](/images/or_gate.png)


#### Bitwise XOR (^) / XOR Gate

![alt text](/images/xor_gate.png)



#### Bitwise NOT (~) / NOT Gate

![alt text](/images/not_gate.png)


#### Half Adder

##### Practice - Complete the Truth Table
![alt text](/images/half_adder1.png)


##### Truth Table for Half Adder
![alt text](/images/half_adder2.png)


#### Full Adder

##### Practice - Complete the Truth Table
![alt text](/images/full_adder1.png)

##### Truth Table for Full Adder
![alt text](/images/full_adder2.png)


### AWS Lambda

#### AWS Lambda for Slack Notification
```python
import json
from botocore.vendored import requests

print('Loading function')

def lambda_handler(event, context):
    
    URL = '[YOUR_SLACK_INCOMING_WEBHOOK_URL]'
    message = 'Hello from AWS Lambda'
    data = '{{"text":"{}"}}'.format(message)
    response = requests.post(URL, data=data, headers={'Content-Type': 'application/json'})
    
    print('Response: ' + str(response.text))
    print('Response code: ' + str(response.status_code))
    
    return {
        'statusCode': response.status_code,
        'body': response.text
    }
    
```

#### AWS Lambda for Price Check
```python
import json
from botocore.vendored import requests

print('Loading function')

def lambda_handler(event, context):
    
    URL = '[YOUR_SLACK_INCOMING_WEBHOOK_URL]'
    message = 'Hello from AWS Lambda'
    data = '{{"text":"{}"}}'.format(message)
    response = requests.post(URL, data=data, headers={'Content-Type': 'application/json'})
    
    print('Response: ' + str(response.text))
    print('Response code: ' + str(response.status_code))
    
    return {
        'statusCode': response.status_code,
        'body': response.text
    }
    
```

### AWS Lambda for Price Alert
```python

import json
from botocore.vendored import requests

def shouldAlert():
    URL = 'https://s3-us-west-2.amazonaws.com/fancy-store/index.html'
    response = requests.get(URL)
    
    print(response.status_code)
    print(response.text)
    
    if '<div>Available</div>' in response.text:
        return True
    else:
        return False

def alert(message):
    URL = '[YOUR_SLACK_INCOMING_WEBHOOK_URL]'
    data = '{{"mrkdwn":true, "text":"{}"}}'.format(message)
    response = requests.post(URL, data=data, headers={'Content-Type': 'application/json'})    

def lambda_handler(event, context):
    
    if shouldAlert():
        alert('*Price Alert* \n Price has changed :smile: :brain: :face-screaming-in-fear:')
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda completed!')
    }

```
##### Python modules (import)

##### JSON

##### Request

##### Method: Get/PUT/POST/DELETE/PATCH

##### Response

##### StatusCode

---

## Week3


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

### Web Forms

### Web Forms in Python

---

## Week4 - Database Programming

### Database

### SQL

### SQL vs. NoSQL

### MySQL

### MySQL in Python

---

## Week5 - Email

### Sending an email

---

## Week6 - Large App Structure

### Project structure

---

## Week7 - Project 1

### Pet-Rescue

---

## Week8 - Project 2



---

## Week9 - Project 3

---

## Week10 - Project 4
