Javadoc's inheritDoc
=========================================

:date: 2018-08-13 20:00
:author: Luke Frisken
:slug: code/javadoc-inheritdoc
:image: {photo}/.jpg
:dropcap:


Talk about how inheritdoc works

Parent Class, this will be used in all examples.
.. code-block:: java

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

TODO: Talk about non-javadoc comments. Find the references for its purpose.

.. code-block:: java

	/* (non-Javadoc)
	* @see com.inheritdoc.ParentClass
	*/
	@Override
	public boolean testMethod(boolean test)
	{
		...
	}

insert image 



.. code-block:: java

	/**
	* Change to the text
	*/
	@Override
	public boolean testMethod(boolean test)
	{
		...
	}

insert image 

.. code-block:: java

	/**
	* @return change to the return
	*/
	@Override
	public boolean testMethod(boolean test)
	{
		...
	}

insert image 


.. code-block:: java

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

insert image