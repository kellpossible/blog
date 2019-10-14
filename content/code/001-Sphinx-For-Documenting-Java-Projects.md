+++
title = "Sphinx For Documenting Java Projects"
date = 2017-01-28
author = "Luke Frisken"
slug = "sphinx-for-documenting-java-projects"
image = "{photo}Sphinx/FinalYearProject1.jpg"
+++

Last year I had the pleasure of using Sphinx for documenting my [final
year software project](https://github.com/kellpossible/libgdx-atc-sim)
at university. The project was primarily java, but also included a
number of python utilities and the requirement of documenting the
central algorithm clearly. For the benefit of others I thought I would
document our experience using it and the configuration we ended up with.

## What is Sphinx?

Sphinx is a piece of software designed to generate documents and
websites from plain text files. A configuration file is used by Sphinx
to interpret the structure and content of the document and to produce
the desired output. The primary use case of Sphinx is that of official
documentation, with one of the earliest and largest projects using it
being the the Python Programming Language.

Sphinx supports output to html using template themes, and to latex/pdf
using latex templates. A large array of sphinx plugins are available for
easy install from the python package index.

Sphinx has a powerful system for cross referencing documents, external
documents, software apis, bibliographies, glossaries, searching and
more. This helps to ensure consistency and utility of the documents
produced.

Some of the key benefits of using Sphinx I noticed over something like a
microsoft word or google docs document:

  - Many powerful documentation generation/linking/cross referencing
    features
  - Source code highlighting with [many available
    lexers](http://pygments.org/docs/lexers/)
  - Changes to the documentation are easy to track because they are in
    plain text, in source control
  - Because documentation is in plain text, it is easy to lock the
    documentation to the software version, and even maintain seperate
    branches
  - HTML website output with a fantastic mobile friendly theme available
    over at
    [sphinx\_rtd\_theme](https://github.com/snide/sphinx_rtd_theme)
  - Latex formatted PDF output
  - Conditional output

## Markdown vs reStructuredText

There are a number of plain text file formats/standards, but the most
popular right now is Markdown. Unfortuneately, while Markdown is
extremely simple and easy to learn, it is also a rather loosely defined
format, and lacks many useful features.

Many of our team members were already familiar with the Markdown format
so I spent a fair amount of time investigating the possibility of using
Markdown files as input to Sphinx documentation.

It turns out that while Markdown support is not built in by default for
sphinx, only minor changes to the configuration are required to enable
support for this document type after installing the recommonmark
package.

I recommend creating a "requirements.txt" in the root of your project
and using that to install all your packages required with a single "pip
install" command. So the following would be added to "requirements.txt":

``` bash
sphinx
recommonmark
pygments-markdown-lexer
```

``` python
from recommonmark.parser import CommonMarkParser

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_parsers = {'.md': CommonMarkParser}
source_suffix = ['.rst', '.md']
```

This is also outlined in the [Sphinx documentation about
markdown](http://www.sphinx-doc.org/en/stable/markdown.html).

Using the recommonmark AutoStructify package, there also exists the
possibility of injecting reStructuredText into the Markdown to gain
access to some of Sphinx's more advanced features.

A basic config for this to put in your conf.py is:

``` python
from recommonmark.transform import AutoStructify

def setup(app):
    app.add_transform(AutoStructify)
```

Then in your markdown you can do

```` md
```eval_rst
.. your:: rst

    stuff
```
````

A better overview of the configuration options and features avaialable
for AutoStructify is available in the [AutoStructify
documentation](http://recommonmark.readthedocs.io/en/latest/auto_structify.html).

The problem was that, while all this worked fine for displaying simple
documents, as the documents evolved, I found myself converting more an
more of the document into the reStructuredText format to the point where
it would have made more sense just to write it in reStructuredText in
the first place\!

For this reason, I'd recommend only enabling the Markdown format for
backwards compatibility to existing documents, and to use
reStructuredText for anything new.

## javasphinx

[javasphinx](https://github.com/bronto/javasphinx) is a python package
which extends Sphinx to enable you to document java projects in Sphinx.
While it does include a java domain for sphinx which enables java api
documentation to be specified directly in sphinx documents, I found that
the most useful feature was that of automatic referencing to existing
compiled javadoc html.

The javasphinx-apidoc utility can be used to automatically generate java
domain restructured text documents from the javadoc html to be compiled
into the sphinx documentation. The problem with this is that:

  - it's slow, effectively requiring the documentation to be processed
    twice
  - it looks, and acts foreign to java developer who are used to regular
    javadoc api documentation.

Thankfully, javasphinx also includes a super useful feature which
enables you to quickly link to javadoc pages in your documents using a
syntax like this in your reStructuredText:

``` rst
:java:type:`JavaClass`
```

Before you can reference external javadoc classes like this however you
need to define the package context:

``` rst
.. java:package:: com.my.package
    :noindex:
```

Classes within this package can then be referenced with just the class
name, and classes in nested packages within this package can be
referenced with their package name prepended:

``` rst
:java:type:`nested.JavaClass`
```

You can also specify the absolute package/class context to link to
classes outside the currently specified java package:

``` rst
:java:type:`com.my.other.package.JavaClass`
```

If you want to link to a package page:

``` rst
:java:extdoc:`com.your.package`
```

The following needs to be added to your conf.py to enable this feature:

``` python
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'javasphinx'
]

javadoc_url_map = {
    'com.your.base.package': ('http://url.to.your/apidocs/', 'javadoc'),
}
```

For our project we wanted to package the javadoc html with the sphinx
generated html. So, firstly I created an empty sphinx document called
"index.rst" in it's own folder called "javadoc" as a placeholder so that
the menu references would be created by sphinx. This document also
contains a single heading "Java API (All Packages)", also for use in the
sphinx generated table of contents and links.

Then, an additional bash script was created to be executed after the
initial html build and referenced in the makefile:

``` bash
pushd ../src/My_Java_Project/
    ./gradlew -info alljavadoc
popd

mkdir -p _build/html/My_Java_Project/javadoc/
cp -r ../src/My_Java_Project/build/docs/javadoc/* _build/html/My_Java_Project/javadoc/                          
```

Effectively, this generates the javadoc html using gradle (because our
project used gradle), and then copies the documentation into the sphinx
html build output folder, replacing the placeholder index.html

In order to get this local linking to work I had to create a fork of the
javasphinx project on github, hopefully some of these fixes will
eventually be introduced into the mainline when I get the time to submit
a proper pull request. You can install the fork using python's pip by
adding the following to your "requirements.txt":

``` bash
git+https://github.com/kellpossible/javasphinx#egg=javasphinx
```

## PlantUML Integration

We used [plantuml](http://plantuml.com/) extensively for documentation
and design diagrams in the project. Having the diagram images generated
along with the rest of the sphinx documentation (instead of being
static) would be very useful. A package called
[sphinxcontrib-plantuml](https://pypi.python.org/pypi/sphinxcontrib-plantuml)
is available which allows you to embed plantuml documents within sphinx
documents very easily.

Going one step further, we also generated plantuml dependency diagrams
of the project to embed in the documentation using
[planuml-depend](http://plantuml-depend.sourceforge.net/command_line/command_line.html).
This was done by creating a script which was executed before the sphinx
html build. The diagram is also generated such that it only refers to
the packages defined by a regex filter.

``` bash
rem generate and copy over javadoc
cd ../src/Your_Java_Project/
java -jar
../../documentation/tools/plantuml-dependency-cli-1.4.0-jar-with-dependencies.jar
-b . -i **/*.java -o ../../documentation/Your_Java_Project/Diagram.puml -dp ^.*com[.]your[.]package.*$
cd ../../documentation
```

## Jupyter Integration

I used [Jupyter](http://jupyter.org/) for protyping one of the
algorithms in the project, and wanted to include the notebook in our
Sphinx documentation.

This was extremely easy (and very cool) with the
[nbsphinx](https://nbsphinx.readthedocs.io/en/0.2.12/) package.

## TODOs

A reminder for which parts of the documentation need attention can be
injected using the [sphinx todo
directive](http://www.sphinx-doc.org/en/1.5.1/ext/todo.html).

## External Links

Sometimes you might have extensive links to other web pages which
follows a pattern, such as issues in our issue tracker. One tool that
can help to reduce the verbosity of such links in your Sphinx documents
is [extlinks](http://www.sphinx-doc.org/en/1.5.1/ext/extlinks.html).

## Conditional Output

One of the requirements for our documentation was that it had two
audiences, the university assessors, and the client. There were specific
sections of our documentation which was appropriate and relevant to
them. Ideally, the documentation could have a switch, enabling a
customized build for the client and a customized build for the
univeristy which would only contain what was required for each.

This can be done using the Sphinx tags in conjunction with the [only
directive](http://www.sphinx-doc.org/en/stable/markup/misc.html#including-content-based-on-tags).
Unfortunately this method has no way to exclude documents within a tree.
To get around this, the following was done in our conf.py:

``` python
if not tags.has("university"):
exclude_patterns += ['University_Specific_Documents/**']
```

This excludes entire document trees based on a sphinx tag, the same tag
can also be used for the only directive.

## Translation

While we didn't use any of Sphinx's translation features in our project,
[the option is
available](http://www.sphinx-doc.org/en/stable/intl.html).

## Our Experience

Overall, I was very happy with the quality of the documentation
produced. Once set up, writing documentation with sphinx can be very
productive, and even fun. Team members made use of some of the most
useful features available, but not all. I'm not sure whether this was
down to lack of training, lack of awareness of the features, difficulty
of use or a lack of enthusiasm.

Some key problems/issues were encountered:

  - Setup/installation/use in Windows is not pretty, requiring the use
    the command line, something many windows users, even developers are
    unfamiliar with and like to avoid. Many of the packages also receive
    less love on the Windows platform.
  - The javasphinx package needs a bit more work to make linking to and
    integrating locally generated javadoc more convenient.
  - javasphinx method referencing to javadoc doesn't work yet
  - In this day and age of wikis and google docs, having to install
    something just to edit documentation seems a bit rustic.

While a vm with everything installed, or a batch script to install all
the requirements might help with the deployment problem in a company
environment, this still leaves the realm of documentation on a steep
learning curve for those unfamliar with version control, and the command
line.

It seems like there is room for improvement. One idea I had was a CMS
which can perhaps even be integrated with continous integration like
Jenkins. The idea goes like this:

  - When the user logs in/connects, the CMS checks out the latest git
    version, and builds it. It then redirects the user to the index page
    of this freshly built documentation.
  - The CMS build of the documentation injects an extra link (next to
    the "view page source") called "edit".
  - The edit page shows the current source code for that page in a text
    edit dialog.
  - The edit page for the document would include a toolbar for inserting
    common elements and snippets (configurable per project).
  - A preview button is available, this triggers a rebuild of the
    documentation and a redirect to the rebuilt page.
  - Various git features like highlight changes, and document history
    could be integrated.
  - A simple form of git conflict resolution would be desireable
  - Integration with bitbucket, github, gitlab, gogs, etc pull request
    system and workflows
  - Translation workflow - perhaps integration with
    [transifex](https://www.transifex.com/),
    [poeditor](https://www.poeditor.com/) or a host of other gettext
    editing websites.
  - Commenting (without requiring git commits)
  - Pressing the save button takes you to an overview of what has been
    changed in the project. You can either continue editing or commit
    the changes.

With all these features, it would still be just a plain old Sphinx
project under the covers, with all the power and plugins that it
provides.

Have a look at the gogs project and see what they do [for editing
files](https://github.com/gogits/gogs/issues/1071).
