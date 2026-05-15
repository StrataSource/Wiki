---
title: Chapter 3 - Loops
weight: 3
---

# Chapter 3 - Loops

## What You Will Learn in This Chapter

In this chapter you will learn about:

- [While, do while loops](#while-do-while)
- [For loop](#for)
- [Foreach](#foreach)
- [Continue/Break keywords](#special-keywords)

> Loops are a way to make the code repeat itself a certain amount of times. The amount of repetitions may vary depending on what is going on in the code.

---

### Arrays - Short Introduction

> [!NOTE]
> This subsection is supposed to teach you the very basics of arrays. This is because in the following section you will be learning about loops, and loops are mostly useful for array manipulation.
> You won't learn in detail what an array is, nor how to do operations on them, but you will learn how to create one and access its elements.

An array is an ordered group of elements, of which there is a starting element and an element at the end.

Code-wise, it acts a template object - you'll need to specify of which data type its values will be. To create an array, you can use the **{element, element2, ...}** assignment:

```cpp
array<int>@ a = {0, 1, 2, 3, 4};
array<bool>@ b = {true, false, false, true, false};
array<float>@ c = {.1, .3, .5};
```

> [!NOTE]
> Since `array` and `dictionary` are value types, you initialize them as an object handle (the @ symbol). For now, just remember that you add that symbol after the type name - this will get explained later on.

To access elements in an array, you will use the index operator **[]**, where `[i]` will access the i'th element of the array (counting from 0):

```cpp
a[3] // = 3
b[1] // = false
b[0] // = .1
```

More on arrays will be covered in later parts of this guide.

---

## While, Do While

The `while (expression)` loop will execute code until the expression evaluates to false:

```cpp
int a = 10;
while (a > 0) {
    a--; // Decrement (subtract one from a) each time the code executes
    // Code in here will stop executing when a will be equal to 0
}

other_code(); // This will execute after the loop
```

The `while` loop will not execute the code (even once) if the condition evaluates to false from the very start.

A `do while` loop however, will first execute the code inside the loop and only *then* check if the condition is true to execute it once more:

```cpp
int a = 10;
do {
    a--;
} while (a > 0); // Note the semicolon
```

> [!WARNING]
> It is possible to create a never-ending loop. The easiest way to achieve this is with `while (true)`. Such loops are usually a programming error. However, these loops can be an intentional decision when **you are sure the loop will at some time stop executing**, either with the `break` statement (more on that in a bit) or through other ways.

> ### TASK 1:
> Write a program that will print out "Hello again!" to the console 10 times.

## For

A `for` loop is an advanced version of the `while` loop. It takes 3 arguments in its statement - `for (statement1; statement2; statement3) {...}`:

- Statement 1 - gets executed before the loop runs (but in the loop's variable scope), often used to initialize a local indexing variable, such as `int i = 0;`.
- Statement 2 - is a condition for the execution of the loop, checked before the loop executes the code inside.
- Statement 3 - is executed after a successful code execution inside the loop (every time).

An example of a `for` loop can be a loop that cycles through every character in a string:

```cpp
array<int>@ numbers = {1, 1, 2, 3, 5, 8, 13};
for (int i = 0; i < numbers.length(); i++) { // For every i until i is greater or equal to the array length (this will ensure i won't go out of bounds)
    numbers[i] // Represents the i'th number in the array
    // After executing code, do i++ (add one to i), so we can access the next element
}
```

> [!TIP]
> Statements 1 and 3 in for loops can be skipped. As an example, `for (;condition;)` is a valid form of a `for` loop, and so is `for (int a = 0;condition;)` etc.

> ### TASK 2:
>
> Given an array of integers, write a program that will add all of them together and print out the result.
> > [!NOTE]
> > Because of [variable scope](chapter3/#variable-scope), you will need to define a variable to store the sum outside of the loop.

## Foreach

A `foreach` loop can be used to perform code for each item in a container object. Container objects are objects that store values of other data types, such as the `array<T>` object or the `dictionary` object. Its structure (`foreach (vars : container_object)`) consists of two parts. `vars` contains declarations of the variable names, such as `int val`, and `container_object` acts as the container object. Some objects unpack more than one variable, such as `dictionary` objects, which unpack the key and the appropriate value.

```cpp
array<int>@ integers = {1, 2, 3, 4};
foreach (int i : integers) {
    // Code here, where i will cycle through every value in integers
}

dictionary@ mydict = {
    {"key1", value1},
    {"key2", value2},
    {"key3", value3}
};
foreach (auto value, auto key : mydict) { // NOTE: the order is flipped here compared to e.g. foreach in Squirrel (VScript). Value comes first
    // Loop through mydict
}

foreach (auto value : mydict) {...} // It is also possible to just loop over one of the elements to unpack
```

> ### TASK 3:
> Write a program that will print out every element of a given array.

## Special Keywords

These are the special keywords that can be used inside loops.

### Break Statement

The `break` statement is a way to exit a loop execution early. Calling it will cause the program to leave the loop early and continue executing code after the loop.

```cpp
int a = 10;
while (a > 0) {
    if (a == 5) {
        break;
    }
}
// This loop will stop executing when a equals 5
```

### Continue Statement

The `continue` statement will skip the current iteration, causing the loop to stop and go to the next element.

```cpp
int sum = 0;
for(int i = 0; i < 10; i++) {

    if (i == 4) { // If i is equal to 4, we are skipping it
        continue;
    }

    // This code will not execute for i = 4
    sum += i;
}
```

### Nested Loops and Special Keywords

Keywords like `break` and `continue` work on the bottom-most loop in nested code, meaning that if you have code like this:

```cpp
while (condition) {
    for (int a = 5; a < 10; a++) {

        if (a > 5) {
            break;
        }
    }
}
```

The code will break of the `for` loop, but not the `while` loop.


> ### TASK 4:
>
> Create a **while (true)** loop that adds all integers until 20.
