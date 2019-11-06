+++
title = "Making Maps"
date = 2019-11-01
slug = "making-maps"
draft = true
[taxonomies]
categories = ["Code"]
tags = ["maps"]
authors = ["Luke Frisken"]
+++

A number of people have asked, and I\'ve been planning for a long time
to create a description/tutorial on how I\'ve been making topographic
maps using freely available data, and open source software.

A lot of credit to the processes outlined goes to various information
sources online, too many for me to remember or list here.

# Map Theory

## Why Learn Map Theory?

Before creating your own maps, if you intend to make accurate maps that
you wish to use for navigation, I think it\'s important to have at least
a basic understanding of map theory. It\'s entirely possible to follow a
step by step process on how to make a map outlined further in this
document, but without an understanding of how maps actually work, you
will struggle with:

-   Fixing problems with your map.
-   Bringing in different sources of map data.
-   Taking what you learn here and applying it to your own specific use
    cases.

## Identifiers

Many of the different technical attributes of a map (Projection, Datum,
etc) are commonly referenced using identifiers as part of a database. If
you see something like **ESPG:3785** in your mapping journeys, this is a
reference to item 3785 in the European Petroleum Survey Group\'s
database. ESPG:3785 happens to be the Web Mercator map projection.
Geographic data is almost always accompanied with these identifiers
which enable software to interpret the data correctly.

It should also be mentioned that there are also some other databases
such as OpenLayers, ESRI and OSGEO.

## Map Projections

### About Map Projections

As the early explorers and scientists discovered, the world is not flat,
but is in fact of a spherical shape. This greatly increased the
complexity of representing the known world on a flat map. To address
this problem of how to represent a spherical (and bumpy/lumpy) surface
on a flat, rectangular map, map projections were invented.

There are an infinite number of ways you could choose to map one shape
to another, and therefore, there are a [huge number of map
projections](https://en.wikipedia.org/wiki/List_of_map_projections) huge
number of map projections in existance already. Every projection has
positive and negative attributes and distort the Earth\'s surface in
different ways. Which projection you choose to use will depend heavily
on how you plan to use the map.

You can (and I recomend to) read more on this topic at [Wikipedia: Map
Projection](https://en.wikipedia.org/wiki/Map_projection).

There are a number of common (and important) map projections which you
will often encounter during the process of making a map, so I\'ve
provided a brief description of each here.

### Mercator Projection

The [Mercator
Projection](https://en.wikipedia.org/wiki/Mercator_projection) is
probably the most common, and well known projection. A Mercator
projection of Earth is very recogniseable, and everyone will be familiar
with it.

If you plot your course on a Mercator map, and you are following a
constant compass bearing (excluding the effects of magnetic
variation/deviation), this will turn out to be a straight line. This
feature of the Mercator Projection makes it very useful for navigation
maps intended to be used with a compass for navigating from point to
point because you can draw a line between these points, and measure the
bearing/angle on the map, this can followed on your compass to reach the
same point in the real world. For comparison, if you attempted the same
thing with say, a Gnomonic Projection, you would not end up at your
intended destination!

### Web Mercator

[Web Mercator](https://en.wikipedia.org/wiki/Web_Mercator) is the map
projection used by most online mapping applications such as Google Maps,
OpenStreetMap and others. It is a variation on the standard Mercator
Projection.

### Universal Transverse Mercator

The [Universal Transverse
Mercator](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system)
projection system is actually not a single projection, but a composite
of many Mercator projections, one for each \"zone\", specifically
optimised for that area in order to reduce distortion. UTM is now very
common for hiking maps, and is the projection I have been using for the
maps that I make.

Included in the UTM system is the concept of UTM coordinates. These are
an alternative to using Latitude and Longitude to represent a position
on the map. Instead, you specify the UTM zone, and then the distance (in
meters) East, and the distance (in meters) North from the origin of the
zone. These are also known as \"eastings\" and \"northings\".

An example (from Wikipedia) of this coordinate system could be:

**17N 630084 4833438**

The first word/number **17N** in this coordinate is used to represent
the UTM zone that the point is located in. Unfortunately there are
currently two methods in use for specifying the zone.

The second word/number **630084** is the distance east from the zone
origin in meters.

The third word/number **4833438** is the distance north from a reference
point relating to the zone. When in the Northern Hemisphere, this is the
distance north from the zone origin on the equator. When in the Southern
hemisphere it is the distance north from roughly the south pole.

Method 1:

**17N 630084 4833438**

The **17** designates that the zone is UTM zone column 17. The **N**
designates Northern hemisphere.

Method 2:

**17T 630084 4833438**

The **17** designates that the zone is UTM zone column 17. The **T**
designates which latitude row in the column that the zone is in. In a
sense the T is partially redundant because part of that information is
also encoded in the northing number.

A more detailed/accurate description of the coordinate system is
available on the wikipedia page.

### About Earth Shape Models

In order to project a map of earth onto a flat surface, you need to have
a notion about what exact the shape of the earth is in the form of a
mathematical model. The most basic model for the shape of the earth is
that of a sphere. The Earth is an irregular shape, and not a sphere.
This means that projections using a sphere as the model will, in certain
areas, be less accurate/less useful.

Luckily, most of the irregularities are small and localised, so a better
(than a sphere) model of the Earth\'s shape can be built using an
ellipsoid. These are also known as an [Earth
Ellipoid](https://en.wikipedia.org/wiki/Earth_ellipsoid) or [Reference
Ellipsoid](https://en.wikipedia.org/wiki/Reference_ellipsoid). There are
many many different refererence elipsoids which have been constructed
and defined, but the most common one in use today is defined in the [WGS
84](https://en.wikipedia.org/wiki/World_Geodetic_System) standard, but
the ITRF datum is gaining popularity due to it being an open and
improving standard.

A [Datum](https://en.wikipedia.org/wiki/Geodetic_datum) or Coordinate
Reference System (CRS) is a coordinate system. There are horizontal
datums with models used for locating a point in terms of latitude and
longitude, and there are vertical datums with models used for locating a
point in terms of altitude. You could use a single model to do both, but
there are benefits to using something like a simple ellipsoid for
horizontal location, and a more complicated (and accurate) shape like a
[geoid](https://en.wikipedia.org/wiki/Geoid) for the vertical location.
The models are also callibrated with respect to a particular reference
frame or position.

A reason why you might want a different datum is that an ellipsoid can
be callibrated/made more accurate for a certain area of coverage than a
more general model like WGS 84. In Australia, for topographic maps, we
now use the
[GDA94](http://www.ga.gov.au/scientific-topics/positioning-navigation/geodesy/geodetic-datums/gda)
datum, which in turn uses the [GRS
80](https://en.wikipedia.org/wiki/GRS_80) reference ellipsoid. Sometimes
the difference between the same latitude and longitude represented with
different datums can be hundreds of meters, unacceptable to choose the
wrong one if you\'re trying to find a campsite in the dense fog with
your gps.

There\'s some nice presentations
[here](http://www.quickclose.com.au/stanaway07pres.pdf) and
[here](http://www.members.iinet.net.au/~abbey/WGS84_ITRF_&_GDA94_What_is_the_Difference.pdf)
outlining the differences between GDA94, ITRF and WGS84. The TLDR is
that as time goes on and the tectonic plates shift, the differences
between these coordinate systems increases. As far as I know, WGS84 is a
static datum, meaning it has no model for how the surface of the earth
moves as the tectonic plates slide around. GDA94 is also a static datum,
but this works well for Australia, because mainland Australia is located
on a single plate, and positions relative to each other in GDA94 on
mainland Australia stay the same. Going to a country like New Zealand, a
datum which is dynamic, and takes into account the velocity of the
tectonic plates is required in order for the datum to maintain its
accuracy for longer periods of time.

Coping with the changes due to tectonic plate shifting with respect to
measurements taken using GPS is an interesting/advanced topic, there\'s
a great document about it here at: [Coping With Tectonic
Motion](https://www.ngs.noaa.gov/TOOLS/Htdp/canSurveyor_SnayPearson-CopingWithTectonicMotion_Vol7No9.pdf).
The basic problem is that if you measure a location (such as a mountain
peak) accurately in 1994, and then return there 20 years later, you
could obtain a result which is several meters different. Not huge
problem for Topographic maps in the short term, but definitely something
that surveyors need to worry about.

### Which Shape Model to Use?

I use GDA94 for my Australian maps, because it\'s currently the most
accurate, future proof, and logical choice. This requires that any input
data using a different CRS needs to be transformed in order to be able
to plot it on the GDA94 map

# Map Data

Before you begin making any map, you need a source for the data you\'re
going to use in the map. By data, I mean, the source of information for
all the features to be included in the map. The more detailed, and more
accurate your source of information, the better your map can be
(provided you spend the time figuring out how to present this
information in a sensible manner). There are many freely available
sources of geography data online, but you can also use data you
generate/provide yourself.

## Data Types

There are a number of different data types which can be used in maps,
having an understanding of these data types is important so you can know
what to look for when you set out to construct a map.

### Raster Data

Raster data is stored in regular sized blocks, essentially like pixels
in a digital photograph. For raster data to be useful, it also needs to
be accompanied with some callibration information to allow GIS software
to know where on the planet the data is located, and what the size and
location of the \"pixels\" are.

[GeoTIFF](https://en.wikipedia.org/wiki/GeoTIFF) is a very common
container/format for raster data which packages the data along with the
map callibration data.

### Vector Data

Vector data

## Worldwide

There are a number of good sources of geography data which cover large
portions of the planet. Some of the ones I have used are listed here:

### Open Street Maps

## Creating Your Own Data

### GPS Tracks

### Satellite Photo Overlay
