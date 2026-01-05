---
title: Chapter 3 - Statements, Expressions, Conditions & Variable Scope
weight: 2
---
# Chapter 3 - Statements, Expressions, Conditions & Variable Scope


## What will you learn in this chapter
In this chapter you will learn about:
- [Expression statements](#expression-statements),
- [Comparison operators](#comparison-operators),
- [Logic operators](#logic-operators),
- [If/else block](#ifelse-block),
- [Switch statement](#switch-statement),
- [Variable Scope](#variable-scope).

> Statements, expressons, conditions and the variable scope are the foundation of every program or script.
---

## Basic statements

Your code is like a recipe, and statements are the individual steps.

Statements are a way to tell the script engine what it needs to do, we already used them in previous chapters, such as the assignment or declaration.

### Expression statements
Any expression can be placed on a line as a statement. Examples of expressions include:
- Function call **()** operator - calls a function (more on functions later),
- Equals **=** operator - performs assignment,
- Add **+** operator - adds two values together,
- Substraction **-** operator - substracts two values from each other,
- Many more, such as **+=**, **-=**, **++**, etc. are available. More about them can be found in the [expression reference table](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_expressions.html).

Such statements need to end with the semicolon (`;`):
```cpp
b = a + b;
func();
a += b;
```

AngelScript follows a specific instruction of operation order. Function calls are evaluated first bottom to top, then AS sticks to order of operations as specified in the [Operator Precedence](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_operator_precedence.html) reference.

You can force an order of operations by using parenthesis:
```cpp
float a = 1 + 1.0 / 2; // This will return 1,5
float b = (1 + 1.0) / 2; // This will return 1
```

> [!TIP]
> Order of how operators are evaluated for standard math operators such as **+**, **-**, **\***, **/**, etc. follow the standard Order of Operations.

> ### TASK 1:
> Given `float a = 4; float b = 5;` Write a program that calculates the number c given by the equation: `c = (a - 2)^2 + (b + 1) / 2`.


### Comparison operators
Comparison operators are operators of which expressions evaluate to the `true` or `false` boolean values. An example of a comparsion operator is the equals (**==**) operator, which checks if the two values on boths sides of such operator are equal. Another type of a condition operator is the greater than operator (**>**), which checks if the value on the left side is greater than the value on the right side. For comparison operator reference please check the [expression reference table](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_expressions.html).
```cpp
int a = 1;
int b = 2;
a == b; // Will return false, but it won't save the value anywhere, treat this as a whole: (a == b)

b = 1;
bool result = a == b; // Result now stores the information if a and b were equal when it was defined.
```

### Logic operators
Logic operators are a way to combine comparison expressions in order to achieve one result:
- NOT - denoted as `!`, evaluates to true, if value is false and vice versa,
- AND - denoted as `&&`, evaluates to true, if both values are true,
- OR - denoted as `||`, evaluates to true, if even one of the values is true, else false if both are false,
- XOR - denoted as `^^`, evaluates to true, if and only if **one** of the values is true.

```cpp
a && b; // AND
a && b || c; // A combination of AND and OR, a AND b is going to get evaluated first
a && (b || c); // You can use parenthesis to specify which operator should get evaluated first, here OR will get evaluated first
```
> [!NOTE]
> Although AngelScript supports Python-like logic operator notation (and, or, ...) it is recommended to stick to the C-like notation. This is mainly because AS is much more similar to C in it's syntax, and also not every extension adding AS support for your IDE has support for the Python-like notation.


---

## Conditions
Conditions are a way to tell the engine to execute specific code only if a specific condition is met. For example, only add numbers if they are positive.
They should contain an expression that evalues to true or false, and they can be any sort of valid combination of comparison operators and logic operators, etc.

### If/else block
The `if`/`else if`/`else` block is used to run specific code only on certain conditions. The `else if` and `else` are not required, but the block must start with an `if` statement.
```cpp
if ( a > 10 ) { // Condition 1
    // Run the code in here
} else if ( a < 10 ) { // Condition 2
    // If we haven't met condition 1, but have met condition 2, execute the code in here
} else if ( condition3 ) {
    // We haven't met neither condition 1, nor condition 2, but we have met condition 3
} else {
    // If none of the conditions were met, execute this code
}
```

> ### TASK 2:
> Given two numerical values *a* and *b* (defined statically in your script) prints out an absolute value of their difference.


### Switch statement
The switch statement is a very useful tool for situations where you need to compare to a lot of different cases. It performs the *is equal* operation comparing a value to every value specified in case blocks. It is also much faster than a block of the `if`/`else if`/`else` statements.
```cpp
switch ( value ) {
    case 0:
        // Do if value == 0
        break; // Required keyword to go out of the switch block
    
    case 2:
    case 3:
        // Execute if value == 2 or value == 3
        break;

    default:
        // Execute if neither cases were met
}
```
> [!CAUTION]
> Each case requires a `break` statement after finishing code execution. This is because switch behaves more like the `goto` (C++) functionality, meaning that it doesn't stop executing code after finishing a specific case. The `break` statement will tell the code to go out of the `switch` block. This is also why in the upper example `case 2:` and `case 3:` can be used to both execute the same lines of code.

> ### TASK 3:
> Given a string as a value (statically defined), write a program that would simulate a command-like behaviour using the switch statement. If the string is equal to:
> - "hello" - print "HelloWorld" to the console
> - "engine" - print "Strata Source" to the console
> - "name" - print "My name is Chell" to the console
> - on any other string - print "Command not recognized!" to the console


---

## Variable Scope

Variable Scope determines which data can be accessed from where. In AngelScript the Variable Scope behaves exactly as the one in C++.
In general the Variable Scope makes programs use less memory by not holding expired (not useful anymore) information inside the memory, as an example:
```cpp
int number = 10;

void my_func1() {
    int my_number = 21;
}

void my_func2() {
    number = 20; // Success, number has been reassigned to 20
    my_number = 80; // Error, my_number has not been declared
}
```
In this case my_number doesn't exist inside *my_func2*, it only exists inside *my_func1* and only for the duration of that function's execution.

Statements such as `if`, `else`, `for`, `while`, `try`, etc. create local variable scopes each time, meaning that variables declared inside them cannot be accessed outside of them, contrary to how for example Python handles it (where scopes are only created inside functions).

In AS, global variables are allowed, however:

> [!NOTE]
> From the official documentation: *Variables of primitive types are initialized before variables of non-primitive types. This allows class constructors to access other global variables already with their correct initial value. The exception is if the other global variable also is of a non-primitive type, in which case there is no guarantee which variable is initialized first, which may lead to null-pointer exceptions being thrown during initialization.*

> [!TIP]
> A good practice is to avoid global variables altogether, and use different means of sharing information between functions such as returning values or &out references (more on that in later chapters).