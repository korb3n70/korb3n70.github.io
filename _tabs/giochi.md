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
      {% assign copertina = g.copertina | default: g.schermate[0].file %}
      {% if copertina %}
        <img src="{{ copertina | relative_url }}" alt="{{ g.title }}" loading="lazy">
      {% endif %}
      <div class="giochi-scheda-testo">
        {%- comment -%}
          Il link avvolge SOLO testo. Avvolgendo anche l'immagine, Chirpy ci
          infila dentro il proprio <a class="popup"> per l'ingranditore: due
          <a> annidati, che il browser risolve chiudendo quello esterno, e il
          collegamento alla scheda resta vuoto. Era il motivo per cui l'elenco
          sembrava slegato dalle pagine dei giochi.
        {%- endcomment -%}
        <h2><a href="{{ g.url | relative_url }}">{{ g.title }}</a></h2>
        <p class="giochi-scheda-meta">
          {% if g.versione %}v{{ g.versione }}{% endif %}
          {% if g.versione and g.data_versione %}<span class="gioco-sep">&middot;</span>{% endif %}
          {% if g.data_versione %}{{ g.data_versione | date: "%d/%m/%Y" }}{% endif %}
        </p>
        <p class="giochi-scheda-vai">
          <a href="{{ g.url | relative_url }}">Scheda e download &rarr;</a>
        </p>
      </div>
    </article>
  {% endfor %}

  {% if elenco.size == 0 %}
    <p class="text-muted">Ancora niente da scaricare. Torna a trovarmi.</p>
  {% endif %}
</div>
