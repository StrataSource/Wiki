---
title: Chapter 3 - Statements, Functions & Variable Scope
weight: 2
---
# Chapter 3 - Statements, Functions & Variable Scope

## What will you learn in this chapter
In this chapter you will learn:
- What are Value Types,
- What is the Variable Scope.

## Functions

As you already know or not, functions are a way of implementing routines that operate on an input and produce a result. In Layman's terms, you give it some data, it processes the data and (may, but doesn't need to) give you an output.

A function declaration consists of 3 main parts: *return value*, *function name*, and the *parameters*.
These follow pretty much the same syntax as C++.


--

## Variable Scope

Variable Scope determines which data can be accessed from where. In AngelScript the Variable Scope behaves exactly as the one in C++.

In general the Variable Scope makes programs use less memory by not holding useless information inside memory, as an example:
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

A good practice is to avoid global variables altogether, and use different means of sharing information between functions such as returning values or &out references (more on that in later chapters).