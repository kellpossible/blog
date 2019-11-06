+++
title = "Linux Laptop"
date = 2018-07-01
slug = "linux-laptop"
draft = true
[taxonomies]
categories = ["Code"]
tags = []
authors = ["Luke Frisken"]
+++

# Android Tablet

## Bluetooth Keyboard

## Termux

# Lenovo Laptop

## Arch-Linux Setup

For a long while now I\'ve been wishing I had a laptop which I could
take with me to do work on the train, and at university. My android
tablet is slow, and while the termux environment lets me get a lot done,
it is also fairly hamstrung; there is no working rust compiler, for
instance. Ideally something second hand, that is easy to fix if it
breaks.

One of my friends who recommended buying a Lenovo laptop for running
linux has a tiling window manager. This concept always intrugued me, as
it appeared to make much better use of the available screen space, and
the keyboard focus makes much better sense on hardware where the mouse
(trackpad) isn\'t really a primary citizen like it is on the desktop.
Also, the x220\'s trackpad is terrible, and the nipple mouse isn\'t much
better, so a keyboard driven interface is always going to be more
efficient.

Another thing that I\'ve been wanting to try out for a while, but have
been unwilling to sacrifice my desktop setup to do, is the wayland
display server. This technology promises to be the future of linux
graphics technology, replacing the convoluted X server with something
that should be more efficient and more secure.

### Lenovo x220

The laptop I ended up buying was the Lenovo x220, second hand. This
laptop has a fairly good reputation for being a solid linux laptop.
There are many guides online on how to install linux on this laptop, and
the ArchLinux guide (TODO: insert link) for this laptop is
comprehensive.

It also has easy access to the components within the laptop, and it\'s
not hard to replace or upgrade them. I will probably purchase some spare
parts, and a new battery soon enough.

It turns out that I\'ve managed to configure almost all the hardware
keyboard actions, which I\'ve very impressed with, and the automatic
standby when closing the lid, and resume upon opening, appears to be
working flawlessly so far.

### WiFi

-   netcfg

### Sway Compositor/Window Manager

Designed to be fully compatible with the i3 window manager config, but
now with support for wayland.

TODO: put config details here for my laptop

Ideally move to the rust \"Way Cooler\" one when it is ready.
