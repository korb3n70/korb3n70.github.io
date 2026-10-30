---
title: Giochi
icon: fas fa-gamepad
order: 1
---

Conversioni e remake per **Amiga** e **Commodore 64**, scritti in Assembly.
Si scaricano gratis: niente registrazione, niente negozio di mezzo.

<div class="giochi-elenco">
  {% assign elenco = site.giochi | sort: 'order' %}
  {% for g in elenco %}
    <article class="giochi-scheda card">
      <a href="{{ g.url | relative_url }}">
        {% assign copertina = g.copertina | default: g.schermate[0].file %}
        {% if copertina %}
          <img src="{{ copertina | relative_url }}" alt="{{ g.title }}" loading="lazy">
        {% endif %}
        <div class="giochi-scheda-testo">
          <h2>{{ g.title }}</h2>
          <p class="giochi-scheda-meta">
            {{ g.piattaforma }}
            {% if g.versione %}<span class="gioco-sep">·</span> v{{ g.versione }}{% endif %}
          </p>
          <p class="giochi-scheda-sommario">{{ g.sommario }}</p>
        </div>
      </a>
    </article>
  {% endfor %}

  {% if elenco.size == 0 %}
    <p class="text-muted">Ancora niente da scaricare. Torna a trovarmi.</p>
  {% endif %}
</div>
