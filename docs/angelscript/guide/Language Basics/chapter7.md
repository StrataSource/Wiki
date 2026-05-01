---
title: Chapter 7 - Object Oriented Programming
weight: 7
---

# Chapter 7 - Object Oriented Programming

## What You Will Learn in This Chapter

In this chapter you will learn about:

- [Object handles](#object-handles)
- [Object handle declaration](#declaration)
- [Object handle expressions](#expressions)
- [The Initialization Problem](#the-initialization-problem)
- [Handle reference counting](#reference-counting)
- [Object handle usage in functions](#handles-and-functions)

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

## Methods and `this` keyword.

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

### Unary operators

### Comparison operators

### Assignment operators

### Binary operators

### Index operator

### Functor operator

### Type conversion operators

### Foreach loop operators




The list of function names and their corresponding operators can be found in the [AngelScript documentation](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_script_class_ops.html), where `op` is the operator, and `opfunc` is the method name used.

Here's an example of overloading operators:
```cpp
class MyClass {

    int a;
    int b;

    // Constructors
    MyClass() {...}

    // Operator overloads
    MyClass& opAdd()


}


```