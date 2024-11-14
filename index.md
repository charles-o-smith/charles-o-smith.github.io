---
layout: default
title:  "Charles the fabulist"
---
{% for post in site.posts %}
<h2>{{ post.date | date: "%Y-%m-%d" }} {{ post.title }}</h2>
 {% if post.image %}
<div class="small-grid">
    <div><img src="{{post.image}}" alt="{{page.image-alt}}" class="thumb"></div>
    <div>{{post.excerpt}}
    <a href="{{ post.url }}">Read more...</a>
    </div>
</div>
{% else %}
{{ post.excerpt }}
<a href="{{ post.url }}">Read more...</a>
{% endif %}
<br />
{% endfor %}

## Stories

- [The Giraffe](https://www.midnightchem.org/no-2/the-silver-ring)
- [The Silver Ring](https://www.midnightchem.org/no-2/the-silver-ring)
- [Where Do the Dead Go When the Living Come to Town](wdtdg.md)

