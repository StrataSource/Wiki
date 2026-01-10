---
title: Chapter 5 - Functions
weight: 4
---

# Chapter 5 - Functions

## What will you learn in this chapter
In this chapter you will learn about:
- [Declaring functions and calling functions](#syntax),
- [Calling methods on built-in objects](#calling-methods-on-objects),
- [Default parameters](#default-parameters),
- [References and passing variables by reference to functions (`&in`/`&out`)](#references---short-intro),
- [Returning references and when it can be done](#returning-references),
- [Function overloads](#function-overloads).

> Functions are a way to split up the code into re-usable parts.

---

## Functions - Basics

### Syntax

As you already know or not, functions are a way of implementing routines that operate on an input and produce a result. In Layman's terms, you give it some data, it processes the data and (may, but doesn't need to) give you an output.

A function declaration consists of 3 main parts: *return value*, *function name*, and the *parameters*.
These follow pretty much the same syntax as C++:

```cpp
// return_value func_name(parameters),
// examples:

int myCoolFunction() { // This function returns an integer
    ...
    return integer_variable;
}

void myFunction() {
    ...
    // No return statement
    
    // or return statement without a value (useful if you want to return early)
    return;
}

bool myFunction(int a, int b) {
    ...
    return bool_variable;
}
```

Each function **must** have a return statement in each of its "paths". What that basically means, is that whatever you do in your function, it will always end with a return statement. The only exception is the `void` return type (which means return nothing), in which you can skip the `return` keyword entirely, or use the `return;` statement when you want to exit the function early.


### Calling functions

Calling functions in code is very simple, you use the **function call `()`** operator, `func(arguments)`. In it, you include every needed argument:

> [!NOTE]
> ""Variables"" in a function declaration are called **parameters**, while ""variables"" in a function call are called **arguments**.

```cpp
int sum(int a, int b) { // a, b are parameters
    return a + b;
}

int just5() {
    return 5;
}

int a = sum(1, 2); // 1, 2 are arguments

a = sum(a, just5()); // just5 will get evaluated first, then its result will get passed to sum
// a = 5
```

Calling a function is a statement, which means it can be freely used in expressions in every combination. You can treat `func(p)` as a value that you do operations with.

### Calling methods on objects
Some objects such as `string` or `array` implement methods. For now, you can think of methods as functions that sit inside the object (variable), and operate on that object. You can invoke them by using the `.` operator and then the function call.
```cpp
string mystr = "ABC";

mystr.length(); // Returns the length of this string (3)
```

For a list of available methods per each type please refer to the [types section](../game/type) of this wiki.
> [!NOTE]
> Primitive types (`int`, `float`, `bool`, etc.) don't implement any methods.

### Recursiveness

Like in any other language, a function can call itself. This is function is then called a *recursive* function. 

---

## Parameters

Function parameters in AngelScript can be a bit confusing, since AS has custom keywords and custom behaviors for different types of parameters.

### Default parameters
Sometimes you want to add additional functionality to your function, but for most cases you already know what it should do, although you still want to include a customizable option for fine-tuning. You can do that by default parameters.

Each parameter can have a default value assigned to it, like so:
```cpp
void myFunc(int a = 5, int b = 1) {...}
```

This function can be called with *0*, *1*, and *2* arguments, and each call will be valid.
Calling it with 0 arguments will mean that `a` will be set to `5`, and `b` to `1`. Calling it with one argument will set a to that arguments value and so on.
```cpp
myFunc(); // a = 5, b = 1
myFunc(2); // a = 2, b = 1
myFunc(2, 5); // a = 2, b = 5
```

> [!NOTE]
> It is currently not possible to explicitly set each parameter to a specific argument. In Python for example, doing `myFunc(b=2)` is allowed and will set `b` equal to `2`, however this is not the case in AngelScript.
> > [!TIP]
> > You can use [function overloads](#function-overloads) to overcome this issue.

### Constant parameters

Constant parameters work just like constant variables. If declare a certain parameter constant, you won't be able to change it in any way.
```cpp
void myFunc(const int a, const bool y = true) // Default parameters can also be constants
```

One important note is that declaring a const parameter will make the compiler not copy the object (if it ensures the object's lifetime). More on that will be in the next chapters.

> ### TASK 1:
> Create a function that computes the nth number of the fibonnaci sequence. It should take uint as the parameter (n) and return an uint (the number). You can tackle this problem recursively (using recursion) or iteratively (using a loop). It is recommend to try out both.

### References - short intro
Before we delve into the next subchapter, you need to know what *references* are. In each computer, variables are stored in memory. You can visualize computers memory as a some sort of a box with labels. Each label has some space that it describes, and there can be an item in each label. Such items are our variables, and these labels are memory addresses. In such way, the computer knows where to look for these variables when it needs to find them.

References are just the labels we have been comparing to, they *are* the address of the variable they correspond to.

They are denoted with the **&** symbol. Conceptually:
```cpp
string mystring = "lorem ipsum";
&mystring // Memory address of mystring
```

In angelscript you cannot directly manipulate references, but you can do many useful things when you combine functions and references. The AngelScript compiler will automatically manage referencing (getting a variables adress) and dereferencing (looking up a variable from an adress).

### Reference parameters
Functions can be set to use references as parameters. 

In the examples shown above every argument was **copied**. Here's a better example:
```cpp
void func(int c) {...}

int a = 1; 
func(a);
```
In this example, before `c` gets assigned a value from `a`, the value of `a` gets copied first, and only after that the assignment occurs. This happens, so that doing any operations on `c` in `func` will not cause `a` outside the function to change in any way.

However, passing by reference changes that mechanism. Since now, the thing that gets copied is the memory address, not the actual variable value. Meaning that if we were to pass by reference in `func` above, doing any operation such as `c = 5;` would cause `a` to change accordingly (a = 5).

Telling the compiler that you want to pass by reference gets done in the function parameters declaration, like so:
```cpp
void func(int& c) // This is a pass by reference
```

No special syntax for calling is needed:
```cpp
int a = 1;
func(a); // a gets passed by reference
```

AngelScript implements more functionality to passing by reference, and that includes 2 options:

#### &in
This marks the parameter as an input to the function. This option provides little to no benefit as to just passing by value (copying), as the compiler still has to ensure the object won't get modified outside the function, and the only way to do that is to make a copy.

> [!TIP]
> Combining `&in` with `const` can however, yield a way more optimized code. `&in` should almost always be used whenever you are using a `const` parameter.



#### &out
This option specifies that this parameter is an output of a function. This is especially useful whenever you have functions that need to have multiple output values. At the start of a function's execution, this reference will point to an uninitialized variable. After the function returns, the value assigned to this variable will be copied over to the appropriate argument.

Example usage of passing by reference of all 3 options:
```cpp
// Example of &in usage
void PrintMessage(const string&in msg) { // This will make the compiler try to not copy the argument when calling the function, as we are not modifying it in any way.
    Msg(msg + "\n"); // Convenience function that prints the message with \n appended
}

// Example usage of &out
bool WholeDivision(int a, int b, int&out result, int&out rest) {
    // Calculates the whole part of a/b and the rest
    // Returns true if the operation can be done.
    if (b == 0) {
        return false; // We cannot divide by zero
    }

    result = a / b;
    rest = a % b;

    return true;
}


int myresult, myrest;
WholeDivision(10, 3, myresult, myrest); //This will set myresult and myrest to the appropriate  (3 and 1 respecitvely).
```

> [!NOTE]
> AngelScript also supports a 3rd mode, `&inout` or `&`, but this is only allowed for reference types (more on that later), and additionally, Strata Source is configured to only pass reference types by reference (pass by value is disabled), which means that there is no need to specify pass by reference for these types anyway.


---

## Returning references

Functions can also *return* references. Meaning that they return an address to an object, rather than the object itself. In previous examples we have discussed functions that return by value, meaning that the value of the variable that gets returned, gets copied to a temporary location and then gets "transfered" over to the variable outside the function:
```cpp
int func(int a) {
    return a * 2;
}

int b;
b = func(2); // Result of func(2) gets stored in a temporary location and then copied over to b.

func(2) = 1; // This will not work.
```

Returning references works in a different way, we return an address, that means the actual value of the variable never gets copied which saves on performance. Additionally, it allows you to do operations on the return value of a function. To declare a function that returns a reference, you append the `&` symbol at the end of the type name in the return type.

Before we overview examples, there is one more thing to discuss about returning references. Not every variable can get it's reference returned. In general, variables that don't exist outside the function will not be able to get returned by reference, because they will get erased once the code gets out of the function.

#### 1. References to global variables are allowed.
Returning references to global variables is allowed, because the variable won't get destroyed outside the function. Example:
```cpp
int a = 1;

int& addToA(int b) {
    a + b;
    return a; // Like in reference parameters, no additional syntax is needed.
}

//This will allow us to do something like:
addToA(1) = 3; // We add 1 to a, but then we change a to be equal to 3.
```

#### 2. References to class members and `this` are allowed.
> [!NOTE]
> This information will be useful once we get to custom classes and reference types, so if you don't know what these are you can skip this for now.

References to class members (properties) and to ourselves (`this`) are allowed to be returned by methods.

```cpp
class myclass {
    int myvar;

    int& GetMyVarRef() {
        return this.myvar;
    }

    myclass& GetMe() { // Note: this will automatically translate to myclass@& (reference to the handle of myclass)
        return this;
    }
}
```

#### 3. Returning a reference to a local variable is not allowed.
Returning a reference to a local variable is not allowed, this is because the variable will not exist after the function returns.
```cpp
int& myFunc() {
    int a = 1;
    return a; // a will not exist outside of myFunc, this is not allowed
}
```

#### 4. Returning a reference to a deferred parameter is not allowed.
Values passed by reference into a function cannot be returned by reference. This is because AS does additional cleanup after the function returns, hence why there is no guarantee that an object passed by `&in`/`&out` will exist after the function returns.

```cpp
int& func(int a&in ) {
    return a; // This is not allowed
}
```

> ### TASK 2:
> Create a function that splits a string into two same-length parts. It should take a string and return a boolean if the string can be split (if the strings length is not divisible by two you cannot create two equal-length parts), and it should also return these two parts (use `&out`).

---

## Function overloads
Function overloading is a very powerful concept, as it allows you to declare a function multiple times, each time with a different set of parameters. The compiler will then attempt to choose the best "fit" for which exact function to call (the criteria of how it does so are available on the [official documentation](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_script_func_overload.html)).

This is mainly used for functions that can accept multiple combinations and types of parameters, but produce a similar result.
```cpp
void myFunc(int a) {...}
void myFunc(string a) {...}

myFunc(10); // Will call the first option
myFunc("a"); // Will call the second option
myFunc(10.5); // Will call the first option (but float will get converted to int)
myFunc(false); // Will cause an error since none of the options specify bool as a parameter
```

Default parameters are also allowed to be used in overloading, but you have to be careful whilst doing so. If you define your function wrong, the compiler will not be able to decide whether it should use an overload or use a default parameter.

```cpp
void myFunc(int a, int b = 2) {...}
void myFunc(int a) {...}

myFunc(1, 3); // Will work, since there is only one option.
myFunc(1); // Will not work, since the compiler doesn't know which option to choose (should it use the first and set the default parameter or should it use the second?)

void myFunc(string a) {...}
void myFunc(int a, string c = "C") {...} // Same goes for different types of default parameters

myFunc("A"); // Will work, there is only one option
myFunc(1); // Now there are 3 options to choose from and none are more important
myFunc(1, "A"); // Will work
```

> [!WARNING]
> Different return types are allowed for overloads, e.g. one function can return an int, whilst other can return a string (the auto keyword is useful here); however the compiler will not take the return type as a criteria for deciding which overload to use.

> ### TASK 3:
> In the default parameters section there was a problem mentioned about how you cannot explicitly set custom parameters. Given a function:
> ```cpp
> int printXTimes(string msg, string end = "\n", int x = 1) {
>   for (int i = 0; i < x; i++) {
>       Msg(msg + end);
>   }   
> }
> ```
> Find a way to use it to print 10 times the message "CONSOLE SPAM!" **without specifying a value for the `end` parameter!**
> > [!TIP]
> > You can call an overload to a different function in an overloaded function:
> > ```cpp
> > void myFunc(int a) {...}
> >
> > void myFunc(int a, int b) {
> >     myFunc(a);
> > }
> > ```

> [!NOTE]
> If you completed the task above, congratulations! This was one of the harder tasks. However, please note that this way of solving that problem is only viable when your default parameters have different types, because if they don't, the overload will not work.