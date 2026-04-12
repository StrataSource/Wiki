---
title: Chapter 7 - Object Handles
weight: 6
---

# Chapter 7 - Object Handles

## What will you learn in this chapter
In this chapter you will learn about:
- [Object handles](#object-handles)
- [Object handle declaration](#declaration),
- [Object handle expressions](#expressions),
- [The Initialization Problem](#the-initialization-problem),
- [Handle reference counting](#reference-counting),
- [Object handle usage in functions](#handles-and-functions)

> Object handles are like smart pointers from C++, they don't actually hold an object themselves, rather they hold an address in memory (reference) that can be used to locate the object they point to.

---

## Object handles
These are objects that hold the address of an object, rather than the object itself. Meaning that by using object handles, you are manipulating the information about addresses of objects that are somewhere else, not ""in"" the variable itself.


## Declaration
An object handle is declared by appending the **@** sign after the data type name, e.g.:
```cpp
type@ handle;
// Or more explicitly:
type@ handle = null;
```
This code will create a handle of type `type` and point it to null (meaning that it doesn't actually point anywhere).

> [!CAUTION]
> It is not guaranteed that handles will actually point to valid data. Handles initialized like the one above point nowhere, and trying to perform any operation on them (such as calling methods) will cause an exception.

> [!NOTE]
> Primitive types don't support object handles.

You can access the handle of any reference type by prepending the **@** symbol to the variable:
```cpp
type my_object;
@my_object; // This is a handle to my_object

type@ objhandle = @my_object; // Store the object handle in a handle variable
```

## Expressions
In expressions, object handles are treated *almost always* exactly the same as object variables themselves, which is something very specific to the AngelScript language. This means that:
```cpp
type my_object;
type@ my_handle = @my_object;

// Calling methods can be done like so (both ways are correct)
my_handle.Method(); // In C++, you would need to use the -> operator here, but this is not the case with AngelScript.
my_object.Method();
```
In most of times the compiler will automatically know what you are trying to do, however, in order to explicitly call a handle operation you have to **prepend the variable name with the handle symbol (@)**.

```cpp
type obj1;
type@ objhandle;

objhandle = @obj1; // This will not work, and will make the script not compile.
@objhandle = @obj1; // This is a proper handle assignment, @objhandle gets set to point to obj1.
@objhandle = obj1; // This will also work because of object variables being handles internally, but is confusing to read, and so - not recommended.
```

---

## The Initialization Problem

As explained in chapter 6, initializing value types with the assign operator is well performant.
As an example, let's assume the `object` class implements opAssign (assignement operator method), doing:
```cpp
type my_object = 10;
```

Will result in the previously explained behaviour, which is **not recommended**, however, doing:

```cpp
type@ my_object = 10;
// more specific example:
Vector@ vec_handle = @Vector(1, 2, 3);
// or
array<int>@ array_handle = {1, 2, 3};
```
**Is fine to do**, because here an object gets created once, and assignment is done on the object handle, not the object itself!
This doesn't result in so many calls being made, because that calls the internal opAssign method (which should return a reference to the `type` type (us)), and so, we are actually doing a handle assignment (that assigns the handle to the same object, but in which opAssign has modified the internal properties). This is a completely valid way of declaring and initializing a value type. This code will call the default constructor, then opAssign(10). It depends on the implementation, but the performance hit here should be marginal (mainly because we're doing way less memory writes/reads).

---

## Reference counting

Object handles are reference counted, meaning that if somewhere in the memory, exists a handle to an object, it is safe to assume that object will **always** be accessible, and **will not** be removed after exiting from the variable scope it was created in. Objects are only removed from memory when all handles to them have been removed first.

```cpp
// Returns a vector with coordinates [1, 2, 3]
Vector@ MagicVector() {
    // Create the vector
    Vector v1(1, 2, 3);

    //Return the handle
    return @v1;
}

... {

    Vector@ magic_vector = MagicVector();

    // v1 object created in MagicVector has not been removed! It is safe to use magic_vector
    float magic_vector_length = magic_vector.length(); // = 3.74...

    magic_vector = null;
    // Since this was the only handle pointing to the v1 object, it got deleted.

}
```

This gets especially useful when initializing reference types (the most advanced of data type), because you can initialize them directly to a handle:
```cpp
my_type@ my_handle = @my_type(...);
```
There is no need to separately intialize my_type to a variable (`my_type my_obj(...);`).


## Handles and functions.

In this regard, handles behave very similarly to primitives. You can pass them as arguments, specify them as parameters, return them, etc...

```cpp
void scale(Vector@ v1_handle, const int factor) {
    v1 *= factor;
}
```
> [!NOTE]
> In the example above, the object passed with the handle **will** get modified outside the function. Here what gets copied is the handle, **not** the object underneath!

> [!NOTE]
> Handles also support passing by reference, meaning that specifying e.g. `Vector@&out` will be valid.
> #### TODO: Do the same restrictions as for primitives (no &in) apply? 