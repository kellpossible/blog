+++
title = "Javadoc's inheritDoc"
date = 2019-01-28
slug = "javadoc-inheritdoc"
draft = true
[taxonomies]
categories = ["Code"]
tags = ["java"]
authors = ["Luke Frisken"]
+++

Talk about how inheritdoc works

Parent Class, this will be used in all examples.

```java
/**
* Documentation for the first method
*
* @param test the test parameter blah blah
* @return this returns something
*/
public boolean testMethod(boolean test)
{
    ...
}
```

TODO: Talk about non-javadoc comments. Find the references for its
purpose.

```java
/* (non-Javadoc)
* @see com.inheritdoc.ParentClass
*/
@Override
public boolean testMethod(boolean test)
{
    ...
}
```

insert image

```java
/**
* Change to the text
*/
@Override
public boolean testMethod(boolean test)
{
    ...
}
```

insert image

```java
/**
* @return change to the return
*/
@Override
public boolean testMethod(boolean test)
{
    ...
}
```

insert image

```java
/**
* {@inheritDoc} extended with the following <br>
* text
* @param test {@inheritDoc} extended with this
* @return {@inheritDoc} extended with that
*/
@Override
public boolean testMethod(boolean test)
{
    ...
}
```

insert image
