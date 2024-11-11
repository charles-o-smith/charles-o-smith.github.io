---
layout: default
title:  "Charles the fabulist"
---


Howdy, I'm Charles. I'm working on a collection of fariy tales.

{% for post in site.posts %}
<h2>{{ post.date | date: "%Y-%m-%d" }} {{ post.title }}</h2>
{{ post.excerpt }}
<a href="{{ post.url }}">Read more...</a>
<br />
<br />
{% endfor %}

## Stories

- [The Silver Ring](https://www.midnightchem.org/no-2/the-silver-ring)
- [Where Do the Dead Go When the Living Come to Town](wdtdg.md)

