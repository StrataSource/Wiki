---
title: Chapter 6 - Value Types
weight: 5
---


# Chapter 6 - Value Types

## What will you learn in this chapter
In this chapter you will learn about:
- [Value types](#value-types---short-introduction)
- [Constructors](#constructors),
- [Value type initialization](#initializing-a-value-type),
- [Template value types initialization](#initializing-template-value-types)

> Value types are a step above primitive types, basically.

---

## Value types - short introduction
Value types are types that behave a bit differently in AngelScript compared to primitives. They are in some ways similar to primitive types mentioned before, however the main differences are:
- Although it might not always be the case, value types take up (much) more memory,
- They support object handles, and should be passed via them,
- They have methods, meaning functions that are bound to their type,
- They support the `&in` and `&inout` passing by reference in functions.

One example of a value type is the `Vector` type.

You can easily distinguish value types from primitive types based on a simple rule. Value types are described as literals, such as `1`, `true`, `3.14`, etc.
Whenever you see a literal, you are **sure** that this literal represents a **specific** value. However, when you see a value type used in code, you can be unsure of the value it represents, for example, `1` represents the number one, but there is no guarantee what `Vector()` represents. It can represent a 0 vector, but it can also be anything. There are also no literals that would represent any value type (one might suggest an example of: `const Vector ZERO_VEC(0, 0, 0);`, but that would be a constant global variable, not a literal).

> [!NOTE]
> Value types can only be defined inside the application itself, you cannot create your own value types in AngelScript. User created types are called *reference types*, more on that in further chapters.

## Using value types

### Constructors
Constructors are functions that are ran on value type initialization, when an object gets created. They are often overloaded, meaning that you can create an object using different arguments, different types etc. Each type can have their own constuctors defined, thus you should refer to the each type's documentation on the constructors available.

As an example, the `Vector` type has 3 different constructors:
```cpp
Vector(); // Calls the default constructor, meaning no arguments are passed
Vector(float x, float y, float z); // Constructs vector from 3 floats, respectively x, y, z
Vector(const Vector&in vec); // So-called copy constructor, constructs copying data from another vector
```

### Initializing a value type

Initializing a value type is done by using parenthesis, after the variable name, like so:

```cpp
Vector v1(1, 2, 3); // Creates a vector v1
Vector v2(v1); //Creates a vector v2, copying data from v1
```

> [!CAUTION]
> #### Common mistake - initializing with the assign operator.
> It is a common mistake to initialize an object using the assign operator, like so:
> ```cpp
> Vector v1 = Vector(1, 2, 3);
> ```
> This is, indeed, a valid (in the language sense) method to initialize, although this should be avoided if possible. This is because, underneath, what the server is doing is:
> 1. Creating the object `Vector(1, 2, 3);`
> 2. Creating the `v1` Vector using the default constructor.
> 3. Calling the assign operator on v1, using data from the right side of the operator
> 4. Deleting the right object (`Vector(1, 2, 3)`)
> 
> **This is much more inefficient than just calling the appropriate constructor (which would perform only one of the operations listed above!).**


#### Initializing template value types
Sometimes objects are described with a template, such as the `array<T>` object. Because the `array` class is supposed to be versatile, it can support different types of data for it's values; you can have an array of integers, an array of floats, an array of strings, etc. There is no need to re-create the array class for each and every available data type, as this is where the template functionality is used for.

When declaring an array you need to specify the data type of its values, like so:
```cpp
array<string>@ string_array = {"string1", "string2", "string3"}; // Create an array of strings
array<int>@ myArray = {1, 2, 3, 4}; // Create an array of integers
// Or, by using a constructor
array<int>@ myArray2(10, 5); // Array: {10, 10, 10, 10, 10}
```
