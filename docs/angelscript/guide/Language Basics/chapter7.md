---
title: Chapter 7 - Object Oriented Programming
weight: 7
---

# Chapter 7 - Object Oriented Programming

## What You Will Learn in This Chapter

In this chapter you will learn about:

- [Classes](#classes)
- [Methods and *this* keyword](#methods-and-this-keyword)
- [Constant methods](#constant-methods)
- [Constructors](#constructors)
- [Operator overloads](#operator-overloads)

> Object oriented programming is the second branch of programming you could say. Here you learn how to manipulate data in a more efficient way, by defining custom data types.

---

## Classes

Classes are definitions of your custom data types, that get initialized into objects. You can compare them to other data types by imagining that an entity in the Source Engine (e.g. logic_relay, prop_static, etc.) is your standard data type, like the integer or bool types. In this comparsion, a class would be an instance file. Something that you can reuse across multiple scripts (maps).

Classes hold properties and methods. Properties are the "variables" that the class holds. They can be any data type (including handles!).

Methods are functions that belong to a specific class. They live in one space, globally accessible to objects of this class.

Although not technically needed in a language sense, each class (that you later intend to initialize) needs **at least one constructor**. Otherwise, trying to intialize such class will result in an error.

Let's start by defining a simple class:

```cpp
class MyClass {

    // Properties
    int a;
    float b;
    bool c;

    // Default constructor (takes no parameters)
    MyClass() {
        a = 0;
        b = 0;
        c = false;
    }
}

// Then, this class can be used like so:

MyClass my_object();
my_object.a = 2;
my_object.b = 1;
my_object.c = my_object.a == 1;
```

---

## Methods and *this* keyword

As mentioned previously, methods are a way to bind specific functions to a class type. Additionally, you can use the `this` keyword inside declared methods, to reference the object the method was called on.

Methods are declared the same way functions are.

```cpp
class MyClass() {

    int a;
    int b;

    MyClass(int a, int b) {
        this.a = a; // Constructors also have access to `this`
        this.b = b; // Here we don't get a name conflict, because this.a explicitly points to "a" that resides in the object namespace.
    }

    void Mult(int c) {
        this.a *= c;
        this.b *= c;
    }

    int GetAB() {
        return this.a * this.b;
    }
} 

// Example usage:
MyClass obj(1, 5);

obj.Mult(3);
int k = obj.GetAB(); // k = 45

```
> [!NOTE]
> `this` keyword is technically not needed in most cases. However, for code readability, it's most often recommended, so that the reader knows that you are referencing something that's been declared inside this object.

---

## Constant Methods

Methods can also be declared constant. This has very big implications for both usage and performance. Constant methods declare the method as something that under no circumstances can modify anything inside the object. It can only read the data, and trying to write will result in a compiler error.

```cpp
class MyClass() {
    int a;
    int b;

    MyClass() {...}

    const int GetAB() {
        return this.a * this.b; // A very good usage of a constant method, no value is modified here.
    }

    /* Bad example that won't compile:
    const void Mult(int c) {
        this.a *= c; // ERROR: this is a write operation, in a constant method
        this.b *= c;
    }
    */

    void Mult(int c) {
        this.a *= c;
        this.b *= c;
    }
}

//...

MyClass obj(1, 5);

obj.Mult(3);
int k = obj.GetAB(); // k = 45

```

The code from above will behave the exact same way as before. However, there is a difference when an object is passed around in code as constant. For example, in constant handles, or as `&in` in functions. In these cases, **only the constant methods can be called!** Calling any other method that isn't declared as constant will result in an error:

```cpp
// Given code above...

const MyClass@ obj_handl = @obj;

int l = obj_handl.GetAB(); // l = 45

/*
    obj_handl.Mult(10); //ERROR
*/

void CoolFunction(MyClass&in val) {
    int z = val.GetAB(); // z = 45

    /*
        val.Mult(15); // ERROR
    */
}
```
---

## Constructors

Constructors have been mentioned previously, but they are a much broader topic than that. They can be divided into four types:

1. [Default Constructor](#default-constructor) - one constructor that doesn't have any parameters.
2. [Copy Constructor](#copy-constructor) - a constructor that takes an object of the same type. This is most often used to copy data from the argument object to us, hence the name.
3. [Type Conversion Constructors](#type-conversion-constructors) - constructors that can be used to implicitly convert other data types to our type. Always with one parameter.
4. [Other Constructors](#other-constructors) - other constructors accepting various parameters.

> [!NOTE]
> You cannot call other constructors from constructors. If you wish to share functionality between constructors, bundle it into a method, these can then be called from constructors.

### Default constructor

A default constructor is one that doesn't accept any parameters. It is the simplest of all, and is used to create a blank object.

```cpp
class MyClass {
    int a;
    int b;

    MyClass() {
        int.a = 0;
        int.b = 0;
    }
}

MyClass obj; // This will use the default constructor
MyClass obj2(); // This will too
```

### Copy constructor

The copy constructor is used to explicitly state the copying process. Without it, the compiler will use the default constructor, and then try to copy everything using the assign operator. A copy constructor is much more effective and performant though, besides that you can run additional code to ensure that things get properly initialized.

Copy constructors are most often defined with the `const &in` options. Most likely you don't want to modify the object **or accidentally copy by passing it as an argument**.

```cpp
class MyClass {
    int a;
    int b;

    MyClass() {...} //Default constructor

    MyClass(const MyClass&in them) { // Copy constructor
        this.a = them.a;
        this.b = them.b;
        //Additional code...
    }

}

// Example usage:

MyClass obj1;
...;

MyClass obj2(obj1); // Explicit call of the copy constructor

MyClass obj2 = obj1; // Implicit call of the copy constructor in the form of an assignment operator.
```

### Type Conversion Constructors

Type conversion constructors are used to perform, well, type conversions to the given type. They will be used by the compiler whenever it needs to perform such conversions, given an appropriate constructor is specified.

It is also possible to flag such a constructor with the `explicit` keyword, which will dissallow the compiler from using that constructor implicitly to perform type conversion. Then the constructor will only be called when initializing an object directly.

```cpp
class MyClass {
    int a;

    MyClass() {
        this.a = 0;
    }

    MyClass(int a) {
        this.a = a;
    }

    MyClass(float a) {
        this.a = a / 10;
        // Let's say that in case of converting from float, we divide by 10 and convert to int.
    }

    MyClass(string a) explicit { // Explicit constructor, compiler will not use this to convert string to MyClass.
        ...
    }
}

// Example usage:

void MyFunc(MyClass w) {
    ...
}

MyFunc(10); // Will initialize MyClass using the 'int' constructor.
MyFunc(5.5); // Will initialize MyClass using the 'float' constructor.
```

### Other Constructors
Besides the types specified above, constructors can accept any amount of parameters of any type. You can easily combine and overload constructors to your desire.

---

## Object Destructor

Similarly to constructors, an (**one**) object destructor can be specified, in order to explicitly perform operations when an objects gets erased from memory. However, it is important to note, that because AngelScript uses garbage collection for memory management, it is unknown *when* exactly a destructor will be called.

A destructor is declared the exact same way as a constructor, however with the tilde (`~`) symbol before the name:

```cpp
class MyClass() {
    //Properties
    ...

    // Constructors
    MyClass() {...}

    //Destructor
    ~MyClass() {
        this.property.CallDestroyed();
        // This example calls the CallDestroyed() method on the object stored in "property" to let it know that we've been removed.
    }
}
```

## Operator Overloads

In classes, you can overwrite the given operators and change their behaviour. For example the `+` operator, or the `/` operator, and many more! Operator overloads are defined as methods in the object with an appropriate name. They can also be overloaded by themselves, meaning that you can have different behaviours for different data types that are on the right side of the operator.

The list of function names and their corresponding operators can be found in the [AngelScript documentation](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_script_class_ops.html), where `op` is the operator, and `opfunc` is the method name used.

Here's an example of a class using operator overloads:
```cpp
class MyClass {

    int a;
    int b;

    // Constructors
    MyClass() {...}

    // Operator overloads
    MyClass opAdd(const MyClass&in other) {
        // Operation that adds two objects and returns a new one with the result
        MyClass newobj(this); // Use the copy constructor
        newobj.a += other.a;
        newobj.b += other.b;
        return newobj;
    }

    MyClass& opAddAssign(const MyClass&in other) {
        this.a += other.a;
        this.b += other.b;
        return this;

        // Notice how here we don't copy the object. It's because we're also doing assignment.
    }

    bool opEquals(const MyClass&in other) {
        return this.a == other.a && this.b == other.b;
    }

}
```


Although operator overloads behave mostly the same, there are a couple of differences between different types of operators.
Below is a short compilation of the most important things to know:

> [!NOTE]
> Whenever there is a mention of "us", it means the object the method is being called on.

### Unary operators

1. Prefixed unary operators should return a modified object (by reference)
2. Postfixed unary operators should return a copy of the object (make a copy, do modifications, return the copy). Alternatively, to avoid the overhead of copying a value when returning from a function, you can overload these operators based on handles (accept a handle as a parameter and return a handle).


### Comparison operators

1. opEquals operators should return a boolean.
2. In case of `opEquals` (`==` operator), the expression (`a == b`) is re-written as `a.opEquals(b)` or `b.opEquals(a)` depending on the available methods (best fit is used).
3. Comparison operators (`>`, `<`, ...) - \[opCmp method] should return an integer. If the argument is larger than us, the return value should be negative, else positive. If objects are equal the return value should be 0. (`a < b => a - b < 0`...) 

### Assignment operators

1. Assignment operators should return by reference, and in almost all cases, should return a reference to us, that is to allow operator chaining (e.g. `a = b = c`).
2. It depends on the specific use case, however `opAssign (=)` should in most cases, copy the properties of argument object to us.
3. The compiler will automatically generate an `opAssign` method if no is specified, that copies all properties. If this is not desired, you can explicitly disable this behaviour with `MyClass& opAssign(const MyClass &inout) delete;`.
4. All other assignment operators should only modify the object, not make copies!

### Binary operators

1. All binary operators have two methods that they can be overloaded on: `opX` and `opX_r`. This is because the compiler will try to rewrite the expression `a x b` as `a.opX(b)` or `o.opX_r(b)`, depending on the best fit. This can mean, that even if the class of `a` doesn't implement that operator, you can still perform `a x b` by using the `_r` method. This is especially useful for operations that are not alternating.

2. These operators should return a copy of objects, thus returning by value. Whether you copy `a` or `b`, doesn't matter much, however make sure to apply appropriate changes onto that copy.

3. In order to save on performance on returning a value, consider specifying the operators as handle based (meaning that they take a handle and return a handle). This way an object is not copied (besides the copy inside the method, that is done to not make changes on `a` or `b`). Additionally, you can specify two overloads, one for a handle input that returns a handle, and one that returns by value, example:
    1. `MyClass@ opAdd(MyClass@ other) {...}`
    2. `MyClass opAdd(const MyClass&in other) {...}`

### Index operator

1. Expression `a[i]` gets rewritten to `a.opIndex(i)`.
2. Multiple arguments are allowed, e.g. `a[i, j, k]` => `a.opIndex(i, j, k)`
3. The index operator can also be written as a pair of property accessors, `get_opIndex(...)` and `set_opIndex(...)`. These are called on getting a value and setting a property respectively. `get_opIndex` should generally have a return type of the value you're retrieving, and `set_opIndex` should return void.

### Functor operator

The expression `a(i, j, k, ...)` will get rewritten to `a.opCall(i, j, k, ...)`.

### Type conversion operators

#### Value conversions
1. Explicit conversions, e.g.: `type(a)` will make the compiler try:
    1. Constructing object of type `type` using a constructor that can accept the type of `a`.
    2. Try to call `opConv` on `a` that returns `type`.
    3. Try to call `opImplConv` on `a` that returns `type`.

2. Implicit conversions will try to also call the constructor first, then **skip** `opConv` and go to `opImplConv`
3. `opConv` and `opImplConv` methods get differentiated based on the return type.
4. The methods above are supposed to be used for value conversions, meaning that they should return a copy of the data with the appropriate type.

#### Reference casts
1. Reference casts are done on handles!
2. Casts can be overloaded with the `opCast` or `opImplCast` methods, for explicit and implicit casting.
3. On explicit casts the compiler will try to use `opCast` first, then `opImplCast`.
4. Implicit casts only use `opImplCast`.

### Foreach loop operators

You can override the behaviour of the `foreach` loop by overloading `opForBegin`, `opForEnd`, etc. It's best to look at the official documentation about this: 

> | op	                     |   opfunc   |
> |--------------------------|------------|
> | begin *foreach*	         | opForBegin |
> | end *foreach*	         | opForEnd   |
> | next *foreach iteration* | 	opForNext |
> | *foreach value*	         | opForValue, opForValue0, opForValue1, opForValue2...|
> 
> When the compiler tries to compile a foreach loop it will need a use a set of methods on the container type.
> ```cpp
>  foreach( auto val, auto key : expr )
>  {
>    ...
>  }
> ```
>
> The above will be compiled as if it was written as
> ```cpp
>  for( auto @container = expr, auto @it = container.opForBegin(); !container.opForEnd(it); @it = container.opForNext(it) )
>  {
>    auto val = container.opForValue0(it);
>    auto key = container.opForValue1(it);
>    ...
>  }
> ```
> 
> Where the types support handles the compiler will use handle assignments, otherwise it will use value assignments.
> 
> The iterator type returned by opForBegin, can be a simple integer for indexing, or an iterator class if more complex operations are needed for keeping track of the  iterations.
>
> If the container only supports a single value, then the operator opForValue can be used, otherwise multiple numbered opForValue# operators must be used.


### Operator overloads - misc

The list of function names and their corresponding operators can be found in the [AngelScript documentation](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_script_class_ops.html), where `op` is the operator, and `opfunc` is the method name used.

Here's an example of overloading operators:
```cpp
class MyClass {

    int a;
    int b;

    // Constructors
    MyClass() {...}

    // Operator overloads
    MyClass@ opAdd(MyClass@ other) {...} // Handle
    MyClass opAdd(const MyClass&in other) {...} // Value


}


```