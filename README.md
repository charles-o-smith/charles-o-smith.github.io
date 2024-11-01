Howdy, I'm Charles. I'm working on a collection of fariy tlales.

{% for post in site.posts %}
<h2>{{ post.date | date: "%Y-%m-%d" }} {{ post.title }}</h2>
{{ post.excerpt }}
<a href="{{ post.url }}">Read more...</a>
<br />
<br />
{% endfor %}

## Stories

- [Where Do the Dead Go When the Living Come to Town](wdtdg.md)
