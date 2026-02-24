---
title: Chapter X - Object Handles
weight: 5
---

# Chapter X - Object Handles

## What will you learn in this chapter
In this chapter you will learn:
- What are Value Types,
- What are References and how to use them,
- What are Reference Types.


Unfortunately, in this chapter you won't learn anything really interesting, but this knowledge is crucial to continue further. Data types in general are a very extensive subject, but you don't need to know everything. This chapter is supposed to teach you how to handle data in your script. Described below are various "types" of data types, and their differences.

---

## Object handles

Object handles are like smart pointers from C++, they don't actually hold data themselves, rather they hold an address in memory (reference) that can be used to locate the object they point to.

### Declaration
An object handle is declared by appending the **@** sign after the data type name, e.g.:
```cpp
object@ handle;
```
This code will create a handle of type `object` and point it to null (meaning that it doesn't actually point anywhere).

> [!CAUTION]
> It is not guaranteed that handles will actually point to valid data. Handles initialized like the one above point nowhere, and trying to perform any operation on them (such as calling methods) will cause an exception.

> [!NOTE]
> None of the Value Types (primitives) have object handles.

You can access the handle of any reference type by prepending the **@** symbol to the variable:
```cpp
object my_object;
@my_object; // This is a handle to my_object
```

### Expressions
In expressions, object handles are treated exactly the same as object variables themselves. For reference types they are essentially the same. Meaning that:
```cpp
object my_object;
object@ my_handle = @my_object;
my_handle is my_object // Is true

//Calling methods can be done like so (both ways are correct)
my_handle.Method();
my_object.Method();
```
In most of times the compiler will automatically know what you are trying to do, in order to explicitly call a handle operation you have to **prepend the variable name with the handle symbol (@)**.

```cpp
object obj1;
object@ objhandle;

objhandle = @obj1; // This will not work, and will make the script not compile.
@objhandle = @obj1; // This is a proper handle assignment, @objhandle gets set to point to obj1.
@objhandle = obj1; // This will also work because of object variables being handles internally, but is confusing to read, and so - not recommended.
```

---

The below section of the Object Handles subchapter contains more detailed information about the implementation of handles in AngelScript. If you don't feel like delving deeper into this subject you can skip the rest of this section for now, remember that you may always return here after you feel accustomed to object handles.

As an example, let's assume the `object` class implements opAssign, trying to do:
```cpp
my_object = 10;
```

Will result in an error, because you are not allowed to do value assignment on a reference type. However, you will be able to do:

```cpp
@my_object = 10;
```

Because that calls the internal opAssign method (which should return a reference to the `object` (us)), and so we are actually doing a handle assignment (that assigns the handle to the same object, but in which opAssign has modified the internal properties).

You can also initialize objects this way:
```cpp
object@ my_object = 10;
```
This is a completely valid way of declaring and initializing a variable. This code will call the default constructor, then opAssign(10).

---

## Reference types

