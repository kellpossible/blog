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

Different methods of transferring information between the client and the server. Graphql requires defining types at least twice. Once in the message and once in the code. https://github.com/davidpdrsn/juniper-from-schema looks like it at least partially eliminates one definition, the one in the server.

It seems like this second definition is unavoidable, there is a whole bunch of boilerplate overhead involved with providing a graphql api. It may also be that I also need to provide different methods for marshalling from the rust objects to graphql objects and back again. It's seeming like it may just be better to do this directly in web sockets, the downside is not being able to benefit from the https infrastructure for secure communication. The other alternative is just using regular `REST` requests and message bodies consisting of serialized json objects. It seems like https://github.com/google/tarpc is designed as a potential solution for this problem.
