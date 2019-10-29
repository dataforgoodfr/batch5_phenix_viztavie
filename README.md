# VizTaVie

Résultat du projet Dataforgood + Phenix.

# Installation
Pour installer les dépendances et lancer les serveurs (webpack: 8080 et express: 4000).
```node
yarn prepare
```

# Lancement
```node
yarn serve
```

# Production

```node
yarn build
```
# Client
Il s'agit d'un projet Vue.JS + TypeScript + Vuex. 
Les autres dépendances principales sont TailwindCSS, Chart.JS et Leaflet. 
Le projet contient également deux fichiers GeoJSON pour les calques régions et départements. Il suffit d'ajouter un fichier GeoJSON dans le dossier ***./client/src/assets*** et d'y ajouter une clé "level" pour qu'il soit ajouté dans la liste des niveaux géographiques disponibles.

```json
./client/src/assets/cantons.geojson.json

{ "type":"FeatureCollection","level":"Cantons","features":[ ... ] }
```

***A noter***: *Object.freeze* est utilisé à de nombreuses reprises dans le store lorsqu'il s'agit d'objets très larges 
qui ne requièrent pas de watchers, ce qui permet d'améliorer drastiquement les performances avec des arrays de 10000+ objets.


***./client/src/store/geography.ts***
```ts
/**
 * Available geo layerings.
 */
public layers: readonly GeoLayer[] = Object.freeze(geoLayers)
```

***./client/src/store/index.ts***
```ts
/**
 * Set all data.
 */
set(state, data: Data) {
  for (let i in data) {
    state[i] = Object.freeze(data[i])
  }
}
```

# Serveur

Le serveur Node est utilisé pour récupérer les données et lancer les scripts python. 
La documentation et les pré-requis de la partie en Python arrivera bientôt.
