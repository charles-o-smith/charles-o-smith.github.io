---
layout: default
title:  "Charles the fabulist"
---
{% for post in site.posts %}
<h2>{{ post.date | date: "%Y-%m-%d" }} {{ post.title }}</h2>
 {% if post.thumb %}
<div class="small-grid">
    <div><img src="{{post.thumb}}" alt="{{page.thumb-alt}}" class="thumb"></div>
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

- [The Staircase](https://clubchicxulub.com/club-chicxulub-journal-vol-4-limbo/#elementor-toc__heading-anchor-15)
- [The Giraffe](https://www.yourimpossiblevoice.com/the-giraffe)
- [The Silver Ring](https://www.midnightchem.org/no-2/the-silver-ring)
- [Where Do the Dead Go When the Living Come to Town](wdtdg.md)

