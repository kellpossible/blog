+++
title = "Java Methods in Constructors"
date = 2019-12-03
slug = "java-methods-in-constructors"
draft = true
[taxonomies]
categories = ["Code"]
tags = ["java"]
authors = ["Luke Frisken"]
+++

Avoiding the use of protected/public non-final methods in constructors. Generally for the safest option, prefer only calling static methods in constructors, failing that, only call private or final methods. A newsletter here about it: https://www.javaspecialists.eu/archive/Issue210.html
This is pitfall when it comes to inheritance (and also method call vs variable instantiation order), and I've encountered this problem a number of times in our code base. It's very confusing, especially considering the implicit default constructor calling.

e.g. `Parent` constructor is calling `method` which isn't final, and is public, able to be overridden in child classes, both no-no's. 

```java
class Parent
{
    Parent()
    {
        method();
    }
    
    public void method()
    {
        // do something
    }
}

class Child extends Parent
{
    private String test;

    Child()
    {
        test = "Hello World";
    }

    @Override
    public void method()
    {
        super();
        System.out.println(test.concat("!"));
    }
}
```

Upon calling `new Child()` this triggers a `NullPointerException` on the the `test.concat("!")` because `test` is uninitialized, which is often quite unexpected by the person working on the `Child` class. We now need to do a serious refactor on the `method()` and the constructor in the parent class, which could have been avoided by applying the suggested rule when designing the class in the first place.
    
Play with the example code here: https://code.sololearn.com/cVRUy2BwauK8
