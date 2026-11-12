---
title: Chapter 9 - Other Features
weight: 9
---

## Enums

Enums are sets of values that act as stand ins for other values. Most common case of enums is using them to define various bit flag values or number values in general. Generally for every enum entry, starting at 0, values of entries increase by one unless specified otherwise directly. You can see examples of these in the `as.predefined` file dumped by the engine for enums such as `EConVarFlag` and `InputButtons`.

Enums only support numerical values and primitives like strings are not allowed. Compile time expressions that result in numerical values are allowed and enums can be set to the value of other enums.

```cpp
enum InputButtons
{
    IN_ATTACK, // IN_ATTACK value is assigned 0 as it's the first value in the enum.
    IN_JUMP,
    IN_DUCK,
    IN_FORWARD,
    IN_BACK,
    IN_USE,
    ...
}

// Enum values can be specified directly. The next enum value will always be +1 from the last.
enum Team
{
    ALL_TEAMS = -1,
    SP = 0,
    SPECTATOR = 1,
    PBODY = 2,
    ATLAS = 3
}

enum MyEnum
{
    Value0,
    Value2 = 2,
    Value3,
    Value200 = Value2 * 100 // Expressions can be used for the script to calculate enum values at compile time.
}

```

## Namespaces

Namespaces act as way of organizing various objects like classes, enums, and constants into their own categories. Namespaces serve have no actual literal value in code. Multiple namespaces can be used inside one another and provide separation from other objects that are named the same. When using objects defined inside namespaces, they must be used with the namespace put in front.

`using namespace` is a keyword that can be used on the global and local scope to remove the need to specify scope all the time for objects. Be careful though as the compiler won't know which object to grab for same named objects in the same scope if the prefix is ditched.

```cpp
namespace util
{
    CBaseEntity@ CreateEntityByName(const string&in className); // util::CreateEntityByName()
    T@ CreateEntityByNameT<T>(const string&in className); // util::CreateEntityByNameT<>()
    void TraceLine(const Vector&in start, const Vector&in end, uint mask, CBaseEntity@ ignore, int group, trace_t&out trace); // util::TraceLine()
    ...
}

CBaseEntity@ entity = util::CreateEntityByName("prop_physics");


int integer; // In the global scope.
string str;
namespace n1
{
    int integer; // Part of the namespace n1. Doesn't override the global scopes version!
    string str;
    namespace n2
    {
        int integer; // Different from n1::integer as it must be accessed by n1::n2::integer.
        void func()
        {
            // Objects from the outer namespace can be accessed by the inner
            integer = n1::integer;
            n2::integer = n1::integer; // Same as above.
            // n2::integer == integer

            // Objects under the same name in the global scope can be retrieved using double colons with nothing before it.
            n1::str = ::str;
        }
    }
}


namespace test1 { void testfunc() {} }
namespace test2 { namespace test3 { testfunc() {} } }

using namespace test2;
void func()
{
    // To get objects inside namespaces, it must use the full scope.
    int var = n1::n2::integer;

    test1::testfunc(); // Have to explicitly declare the scope.

    {
        using namespace test1;
        testfunc(); // Implicitly call the function because the prefix has been popped in this scope.
    }
    test1::testfunc(); // Leaving the scope drops the popped prefix so it must be specified again.

    test3::testfunc(); // The global space dropped the needed namespace prefix for test2 to access test3's testfunc().
}

```

## Exception Handling

Like any other language, AngelScript has error handling when it runs into a issue when compiling or running. Any errors will be logged in the console by the scripting system. Usually these messages can get lost in the console when ConVars like `developer` are enabled which cause more verbose console logging pushing out scripting system logs. There is a [dedicated Dev UI window](../../../modding/devui/categories/scripting#script-system-output) for AngelScript compilation and runtime errors that allows for viewing these errors.

Errors can be captured at runtime by using `try-catch` statements. Any code that would cause a error in the `try` section will be caught and the code in the `catch` section will be executed. AngelScript has a function to be able to get the caught error in the `catch` section `string getExceptionInfo()`. If errors need to be purposely thrown, `throw(string)` can be used to throw a exception with a string parameter describing the error.

```cpp

void func()
{

    try {
        CBaseEntity@ entity = EntityList().FindByName(null, "a_entity_that_doesnt_exist");
        Vector pos = entity.GetAbsOrigin(); // Will cause a exception because the entity handle is null!
    } catch {
        Msgl('Uh oh! Ran into a problem: "{}"'.format(getExceptionInfo())); // Will get the exception and add it to console message.
    }

    try {
        throw("Throwing a error because I said so!"); // Using throw outside of the try-catch in most cases will cause the whole script to stop execution!
    } catch {
        Msgl('A error occurred! Here is that error: "{}"'.format(getExceptionInfo()));
    }

}

```
