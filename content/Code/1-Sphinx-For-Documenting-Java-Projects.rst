Sphinx For Documenting Java Projects
====================================

:date: 2017-01-28 11:00
:author: Luke Frisken
:slug: code/sphinx-for-documenting-java-projects
:gallery: {photo}MountaineeringCourse
:image: {photo}MountaineeringCourse/20141222_062454.jpg
:dropcap: L

ast year I  had the pleasure of using Sphinx  for documenting my final
year software project at university.   The project was primarily java,
but also included a number of  python utilities and the requirement of
documenting the central algorithm clearly. For the benefit of others I
thought I would document our experience using it and the configuration
we ended up with.

What is Sphinx?
---------------

Sphinx  is a  piece of  software  designed to  generate documents  and
websites  from plain  text files.   A  configuration file  is used  by
Sphinx to interpret  the structure and content of the  document and to
produce the desired output.  The primary use case of Sphinx is that of
official documentation, with one of  the earliest and largest projects
using it being the the Python Programming Language.

Sphinx supports output to html using template themes, and to
latex/pdf using latex templates. A large array of sphinx
plugins are available for easy install from the python package index.

Sphinx has a powerful system for cross referencing documents, external
documents, software apis, bibliographies, glossaries and more. This
helps to ensure consistency and utility of the documents produced.

Markdown vs reStructuredText
----------------------------

There are a number of plain text file formats/standards, but the most
popular right now is Markdown. Unfortuneately, while Markdown is
extremely simple and easy to learn, it is also a rather loosely
defined format, and lacks many useful features.

Many of our team members were already familiar with the Markdown
format so I spent a fair amount of time investigating the possibility
of using Markdown files as input to Sphinx documentation.

It turns out that while Markdown support is not built in by default
for sphinx, only minor changes to the configuration are required to
enable support for this document type.

```
python code yay
```

Using this package, there also exists the possibility of injecting
reStructuredText into the Markdown to gain access to some of Sphinx's
more advanced features.

The problem was that, while this worked fine for displaying simple
documents, as the documents evolved, I found myself converting more an
more of the document into the reStructuredText format to the point
where it would have made more sense just to write it in
reStructuredText in the first place!

For this reason, I'd recommend only enabling the Markdown format for
backwards compatibility, and to use reStructuredText for anything new.


javasphinx
----------

PlantUML Integration
--------------------





Our Experience
--------------



Configuration
-------------





