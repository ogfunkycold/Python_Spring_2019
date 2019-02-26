### 1.  Compound Interest   
The formula for compound interest is given by:  
![alt text]( interest_formula.png "Image Credit: http://openbookproject.net/thinkcs/python/english3e ")  

The file *interest_info.txt* contains information related to the user's bank account deposit. The first line contains the annual interest rate.  The second line contains the number of times the interest is compounded per year.   The third line contains the principal amount.   Suppose that the user wishes to know her current balance.    

Write a program that reads the information contained in this file and then asks the user how many years have passed since the initial deposit.    The program should then indicate the current balance in dollar/cents format (with 2 decimal points).  See session1_overview/formatting_numbers.py for some examples of how to format numeric output.

### 2.  Parity

Write a program that asks the user to enter three integers.   Have that program indicate which integers are odd, which are even, and the sum of the odd and even integers.   The program might generate output similar to the following:

Enter Integer 1: 1  
Enter Integer 2: 2  
Enter Integer 3: 3  

You supplied the numbers:  1 2 3  
Their sum is 6.  

There are 2 odd numbers.  
They are:  1  3  
Their sum is 4.  

There are 1 even numbers.  
They are:   2   
Their sum is 2.  

This might seem challenging at first since we have not dicussed conditionals yet.  Don't cheat and use an `if` construct.  

**Hint:**  You may find that the following code snippet gives you some ideas.  
```
msg = 'hello'  
msg2 = 3*msg    
print(msg2)  
