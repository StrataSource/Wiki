---
title: Chapter 2 - Value Types, Declaration & Assignment
weight: 1
---

# Chapter 2 - Value Types, Declaration & Assignment

## What will you learn in this chapter
In this chapter you will learn about:
- [Value Types](#value-types),
- [Declaration and assignment of value types](#value-types),
- [Auto keyword](#auto-keyword),
- [Constants and the const keyword](#constants),
- [Integer size reference table](#integer-size-reference-table).

> The knowledge in this chapter is crucial to continue further. Data types are an extensive subject, but you don't need to know everything. This chapter's goal is to teach you how to handle value types in your script.

> [!NOTE]
> This chapter won't cover every detail of every data type. It is recommended you visit the [Data Types Section](../game/type) of the Wiki for more information.
> Alternatively, you can find references on the [AS Official Documentation](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_datatypes.html). Please note, however, that the Strata Wiki is a better reference, as some functionality may have been changed.

---

## Value Types
Value types are a more "primitive" type, and are only implemented in the backend inside the engine itself. These types include: `int`, `string`, `bool`, `float`, `double`, etc.

> [!WARNING]
> It is assumed you already know about these data types from other languages (mainly C++). This subsection will only provide information relevant to AngelScript itself.

### Declaration and Assignment
Value types can be easily assigned and can passed by value to functions. We'll get into that more later.
To create a value type, you will usually perform a declaration, an assignment, or both at once:
```cpp
int myInt; // Declaration
myInt = 20; // Assignment

string myString = "Hey!"; // Initialization
```

You can declare multiple variables of the same type at once:
```cpp
int myInt1, myInt2, myInt3;
```

Once declared, variables cannot change their type without redeclaration. This, for example, is not allowed:
```cpp
int myInt;
myInt = 3.2; // myInt is of type int, not float/double!
```

> ### TASK 1:
> 1. Create a program that will declare and assign variables of types `string`, `int`, `bool`, `double`, and then print them out to the console.
> 2. Do the same using variable initialization.

### Auto Keyword
Although not recommended, the `auto` keyword will make the compiler automatically determine the data type of the variable:
```cpp
auto i = 1; // Will set type of i to integer
auto s = "My string"; // Will set type s to string
auto var = functionThatWillReturnAnObjectWithAVeryLongName();

// Handles (described in later chapters) can also be declared with auto
auto@ handle = @obj;
```

The `auto` keyword is not recommended in many cases. Using `auto`, you cannot immediately see the data type of a returned object, especially from functions such the one above. We don't know what that function will return. Additionally, there is always a chance the compiler may guess incorrectly. This issue is especially prominent in cases such as integers, where there are multiple ways `1` could be described (e.g. int8/int16, both can describe `1`, as can `bool`).

--- 

### Constants
Constant variables are variables that cannot change over the lifetime of the [variable scope](chapter3) they are created in.
You can define a constant variable using the `const` keyword:
```cpp
const int size = 31;
const auto st = "string"; // const also works with the auto keyword
```

Constants can be useful as a sort of configuration of the script itself. Instead of reusing a statically-defined variable, you can define a global constant in its place. Changing one value will then change everything at once:
```cpp
const int MAX_SIZE = 16;

string mystring = "lorem ipsum";
my_func1(mystring, MAX_SIZE); // A function that does something with mystring, but also needs to have additional information
my_func2(mystring, MAX_SIZE) // Another function that does something else with mystring, but it also needs the same additional information
```

Constants also function as a way to optimize your code. If you know that a variable won't change (or shouldn't change) after its initialization, you should always make it a constant.
```cpp
bool function(string s, float i) {
    const float value = s.length() - i;
    return i > value;
}
```

> ### TASK 2:
> Write a program that initializes a constant variable with the `auto` keyword, and then tries to change it after. Observe the compilation error in the console.

---

### Integer Size Reference Table
The table below shows the minimum and maximum values for each integer subtype. It is not necessary to memorize this chart as you can always refer back to this page when necessary.
|Type|Short description|Minimum Value|Maximum Value|
|---|---|---|---|
|int8| Signed, 8 bits |-128 | 127 |
|int16| Signed, 16 bits |-32,768 | 32,767 |
|int| Signed, 32 bits |-2,147,483,648 | 2,147,483,647 |
|int64| Signed, 64 bits |-9,223,372,036,854,775,808 | 	9,223,372,036,854,775,807 |
|uint8| Unsigned, 8 bits, also represents characters (char) | 0 | 255 |
|uint16| Unsigned, 16 bits | 0 | 65,535 |
|uint| Unsigned, 32 bits | 0 | 4,294,967,295 |
|uint64| Unsigned, 64 bits | 0 | 18,446,744,073,709,551,615 |

> [!TIP]
> The official AngelScript documentation mentions that the scripting engine has been mostly optimized for 32 bit datatypes (int/uint). Using these is recommended for the most part (unless you are dealing with numbers that don't fit into int/uint).


