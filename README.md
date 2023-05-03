<div align="center">
  <h1>Ohjelmistokehityksen seminaarityö</h1>
  </div>
  
## Johdanto
Seminaarityön aiheena oli tehdä tutoriaaliin perustuva matopeli, jota tekoäly oppii pelaamaan, käyttäen Python-ohjelmointikieltä ja siihen kuuluvia teknologioita. Seminaarityö on tutoriaaliin perustuva ja käyttää valmista matopelin, sekä koneoppimismallin koodia, jota seminaarityössä muokattiin. Tutoriaali on Patrick Loeberin tekemä ja löytyy neliosaisena sarjana YouTubesta: 

<a href="https://www.youtube.com/watch?v=PJl4iabBEz0&list=PLqnslRFeH2UrDh7vUmJ60YrmWd64mTTKV">’Teach AI To Play Snake – Reinforcement Learning Tutorial With Py-Torch and Pygame’.</a>
  
Työn tavoitteena oli oppia tuntemaan perusteet koneoppimisesta ja kokeilla niitä käytännössä sekä luoda näiden funktioille testejä.
  
## Teknologiat
Työssä käytetyt teknologiat:

- Anaconda
- Pygame
- PyTorch
- Pytest

## Anaconda
Paketinhallintatyökalu, jonka avulla luotiin varsinainen projektitiedosto
## Pygame
Matopeli luotiin käyttämällä Pygame-pelikirjastoa. Matopelin alkuperäinen koodi löytyy Patrick Loeberin GitHubista:

<a href="https://github.com/patrickloeber/snake-ai-pytorch">Tästä linkistä</a>

Omassa versiossani matopelistä lisäsin ominaisuudet, kuten: toisen omenan, mahdollisuuden liikkua seinien läpi sekä satunnaisesti uusiin peleihin generoituvat "vihollispalikat", joihin osuminen päättää pelin. Lisäsin myös omat laskurit punaiselle sekä vihreälle omenalle.

## PyTorch
Koneoppimismallin luomiseen käytetty työkalu. Alkuperäinen koodi löytyy Patrick Loeberin GitHubista, ylempää samaisesta linkistä. ^

## Pytest
Lopuksi luotiin muutamia testejä pelin ja koneoppimismallin funktioille käyttämällä Pytest-testausrunkoa

### Arkkitehtuurikaavio
<img width="720" alt="arkkitehtuurikaavio" src="https://user-images.githubusercontent.com/94442657/235981480-f35ed149-1791-4fe8-9d82-884b102f2a8a.png">
Lähde: <a href="https://www.youtube.com/watch?v=PJl4iabBEz0&t=424s">Tutorial</a>
<p></p>
Koodipuu:

<img width="323" alt="koodirunko" src="https://user-images.githubusercontent.com/94442657/235983703-b6c1123f-b7cb-48e0-bd91-3d3282f869f4.png">

## Yhteenveto
Työ oli kokonaisuudessaan yksinkertainen, että haastava sillä käytettyjä teknologioita ja uusia asioita oli paljon. Vaikka työ olikin tutoriaaliin perustuva, haasteita silti kohdattiin ja tunteja niiden korjaamiseen upposi. Suurimpia haasteita olivat mm. testien luominen, sekä madon opettaminen syömään molempia omenoita vain yhden sijasta.

Projekti sujui kaikin puolin hyvin ja eteni aikataulussa. Odotukset haastavuudessa olivat korkealla, mutta loppujen lopuksi käytetyt teknologiat ja niiden käyttäminen olivat kohtuullisen yksinkertaista. 
