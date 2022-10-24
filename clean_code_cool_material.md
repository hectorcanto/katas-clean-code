# Interesting links and references

These links point to resources that have been used to create this course `Clean Code and beyond`

## Main material

- 📘 _Clean Code: A Handbook of Agile Software Craftsmanship_ 
  
  (Robert C. Martin, _aka Uncle Bob_, 2009)

- 🌐 [herbertograca.com]()
  (Herberto Graca,  2015-2020)



https://plantuml.com/'

## Relevant blogs

* [Martin's Fowler blog](https://martinfowler.com/), author of Refactoring, among other books
* [CleanCoder](http://blog.cleancoder.com/) Robert C. Martin's blog, author of Clean Code among others
* [Joel on Software](https://www.joelonsoftware.com/) by Joel Spolsky, founder of Stackoverflow and Trello
* [Engineering at Spotify](https://engineering.atspotify.com/)
  * highlighted: Agile organization in tribes, guilds, chapters and squads


### Highlighted articles

- [The transformation priority premise](http://blog.cleancoder.com/uncle-bob/2013/05/27/TheTransformationPriorityPremise.html), by Robert C.Martin
- [The Joel test, 12 steps for better code](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/) by Joel Spolsky
- [The Twelve Factor App](https://12factor.net/) by Adam Wright
- [DevOps tools periodic table](https://digital.ai/devops-tools-periodic-table)
- Object calisthenics
- [Test Desiderata](https://kentbeck.github.io/TestDesiderata/)

## Summaries

[Clean Code summary](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29), by Wojtek Lukaszuk
[Clean Code notes](https://github.com/JuanCrg90/Clean-Code-Notes), by Juan Carlos Ruiz

## Relevant sites

* [Refactoring.guru](https://refactoring.guru/)
  * Refactoring techniques, also design patterns
* [Source Making](https://sourcemaking.com/)
  * Patterns and antipatterns, also refactoring 
* [Refactoring catalog](https://refactoring.com/catalog/)
  * From the book Refactoring, by Martin Fowler 

## Katas

Katas are coding challenges meant to train certain aspects of software design
They are relatively short and some come with a starting point.

Many of them are meant to be repeated over and over, like their namesake Karate's Kata, where
you train a pattern of movements as if it was a simulated fight

- [Clean Code Developer school](https://ccd-school.de/coding-dojo/)
  - Page is in German but exercises are available in English (click the flags)
  - Katas are divided by artifacts: functions, classes, library ...

- [Kata Log](https://kata-log.rocks/)

- [Understand Legacy Code](https://understandlegacycode.com/blog/5-coding-exercises-to-practice-refactoring-legacy-code/)


### Gilded rose

- [Gilded Rose kata at kata-log.rock](https://kata-log.rocks/gilded-rose-kata)
  - remember to NOT modify Item
  - starting points: https://github.com/emilybache/GildedRose-Refactoring-Kata

- Solution (try it by yourself before ever looking at any solution)
  - [Python solution by Hector Canto](https://github.com/hectorcanto/katas-clean-code/tree/feature/gilded-rose/katas)
    - includes tests 


### Bowling Kata

- [Bowling Kata at Codurance](https://www.codurance.com/katalyst/bowling)
  - includes some solutions in Kotlin, Scala ... 
  - [Python solution by Hector Canto](https://github.com/hectorcanto/katas-clean-code/blob/feature/bowling/katas/bowling.py)
    - includes tests 

- Thoughts on it by Robert C. Martin, includes PPT slides
  - [http://butunclebob.com/ArticleS.UncleBob.TheBowlingGameKata]()
    

### Other Kata soultions

* [Kata CSV](https://github.com/hectorcanto/katas-clean-code/blob/main/katas/csv.py)
* [Kata Roman numbers](https://github.com/hectorcanto/katas-clean-code/blob/main/katas/roman_numbers.py)


## Interesting standards and RFC

- [Python Zen](https://peps.python.org/pep-0020/), by Tim Peters, at python.org
- [Semantic versioning 2.0.0](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
- [Json:Api specification](https://jsonapi.org/format/)
  - [Recommendations](https://jsonapi.org/recommendations/)
  - [Drupal JsonAPI module](https://www.drupal.org/docs/core-modules-and-themes/core-modules/jsonapi-module)
- [Health Check Response Format for HTTP APIs, draft 6](https://datatracker.ietf.org/doc/html/draft-inadarei-api-health-check) at IETF
- [RFC 2068, Hypertext Transfer Protocol HTTP/1.1](https://datatracker.ietf.org/doc/rfc2068/) by Roy Fielding et all.
- [HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) at mozilla.org 

## Architecture

* 📄 [Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/)
  (Alistair Cockburn, 2005)

* 📄 [The Onion Architecture](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/)
  (Jeffrey Palermo, 2008)


## Other techniques 

- BDD: 📄 [Introducting BDD](https://dannorth.net/introducing-bdd/) by Dan North
- DDD Hexagonal: [Explicit architecture](https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/) , by Herberto Graça
- Object Calisthenics:
  - [Object Calisthenics](https://williamdurand.fr/2013/06/03/object-calisthenics/) by William Durand
  - [Object Calisthenics, mejora tu diseño orientado a objetos](https://keyvanakbary.com/object-calisthenics-mejora-tu-diseno-orientado-a-objetos/), by Keyvan Akbary
- Extreme Programming
  - [http://www.extremeprogramming.org/when.html]() 

### Own material

This is material I've been building in the past years on related topics

- Keep your repo clean [slides](https://www.slideshare.net/HectorCanto/keep-your-repo-clean)
- Testing
  - Effective testing with Pytest
    - 📄 [slides in English](https://www.slideshare.net/HectorCanto/effective-testing-withpytest)
    - 📄 [slides in Spanish](https://www.slideshare.net/HectorCanto/testing-efectivo-con-pytest)
  - [Tips and tricks for unit tests](https://medium.com/worldsensing-techblog/tips-and-tricks-for-unit-tests-b35af5ba79b1)
- LADR: Light Architecture decision records 
  - 📄 [slides in Spanish](https://www.slideshare.net/HectorCanto/)
  - 🎤 [Podcast Entre Dev y Ops ep.68](https://www.entredevyops.es/podcasts/podcast-68.html)


### Cool tools

- Diagrams as Code: [python-diagrams](https://diagrams.mingrammer.com/), [plantuml](https://plantuml.com/)
- Versioning: [bump2version](https://github.com/c4urself/bump2version)
- Documentation: [Sphinx](https://www.sphinx-doc.org/en/master/glossary.html), [Doxygen](https://doxygen.nl/), [handsdown](https://vemel.github.io/handsdown/)
- Commits and branches: [CommitZen](https://commitizen-tools.github.io/commitizen/), [git-flow](https://nvie.com/posts/a-successful-git-branching-model/)
- APIs: [Open API 3, formerly Swagger](https://swagger.io/specification/)
- Code quality: [Sonarqube](https://www.sonarqube.org/)
- Project templates: [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/)

### Usually recommended books

DISCLAIMER: I haven't read them all, so I can only vouch for some. But they are all
highlighted by the community and are present of several must-read list


* _Test Driven Development: By Example_ (Kent Beck, 2000)
* _The Pragmatic Programmer_ (Andy Hunt and Dave Thomas, 1999)
* _Software Craftsmanship_ (Pete McBreen, 2001)

* _The Mythical Man-Month: Essays on Software Engineering_ (Fred Broks, 1975)
* _The Clean Coder_ (Robert C. Martin, 2011)
 
* _Working Effectively with Legacy Code_ (Michael Feathers, 2004)
* _Refactoring: Improving the Design of Existing Code_ (Martin Fowler, 1999)

* PPP: _Agile Software Development, Principles, Patterns, and Practices_ (Robert C. Martin)
* _Head first design patters_ (Freeman and Robson, 2004)
* _Design Patterns: Elements of Reusable Object-Oriented_  (Gamma, Helm, Johnson and Vlissides, 1995)
* PEAA: _Patterns of Enterprise Application Architecture_ (Martin Fowler, 2003)

* _Domain Driven Design, Tackling Complexity in the Heart of Software_ (Eric Evans, 2003)
* _Domain Driven Design distilled_ (Vaughn Vernon, 2016)
* _Learning Domain-Driven Design: Aligning Software Architecture and Business Strategy_ (Vladik Khononov, 2021)
