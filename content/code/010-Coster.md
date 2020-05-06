+++
title = "Introducing Coster"
date = 2020-05-10
slug = "introducing-coster"
draft = true
[taxonomies]
categories = ["Code"]
tags = ["rust", "yew"]
authors = ["Luke Frisken"]
+++

For the past couple of months, mostly in a COVID lock-down induced frenzy, I've been hacking away at a personal project using the Rust programming language to produce a self-hosted website for sharing costs between friends/group members. I wanted to support multiple currencies, make it easy to translate to other languages, support off-line/synchronisation, no dependencies and easy to install/run (distribute as a single binary). As an extra challenge I decided to develop both the back-end and the front-end in Rust with shared libraries between them, making use of the language's excellent support for WebAssembly.

https://github.com/yewstack/yew/issues/830 