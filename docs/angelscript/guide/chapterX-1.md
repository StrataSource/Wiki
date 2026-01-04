---
title: Chapter X - Reference Types
weight: 4
---


# Chapter X - Reference types

### Declaring template objects
Sometimes objects are described with a template, such as the `array<T>` object. Because the `array` class is supposed to be versatile, it can support different types of data for it's values; you can have an array of integers, an array of floats, an array of strings, etc. There is no need to re-create the array class for each and every available data type, as this is where the template functionality is used for.

When declaring an array you need to specify the data type of its values, like so:
```cpp
array<string> string_array = {"string1", "string2", "string3"}; // Create an array of strings
array<int> myArray = {1, 2, 3, 4}; // Create an array of integers
```

Functions can be templates too, an example of such function can be the cast function, which converts one data type to another (if possible) (more on the cast function later):
```cpp
obj1 myobj1;
obj2 myobj2;
@myobj1 = cast<obj1>(@myobj2); // Cast function will convert obj2 into obj1
```

> [!NOTE]
> It is currently not possible to create your own custom template objects, although this functionality is planned for future releases of AngelScript.

