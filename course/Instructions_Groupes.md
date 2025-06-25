# Groupe X – Tests d’intégration automatisés

## Objectif

Mettre en place des tests d’intégration pour valider le bon fonctionnement global de l’API, et les exécuter automatiquement via GitHub Actions.

## Travail attendu

### 1. Mise en place locale

* Créer une suite de tests d’intégration avec `pytest` et `httpx` ou `TestClient`
* Couvrir des scénarios complets (ex : créer une salle + faire une réservation)
* Prévoir un environnement de test propre (utilisation de **SQLite in-memory** ou, si besoin, d'une technologie comme **TestContainers** pour simuler une BDD indépendante)

### 2. Intégration dans la CI

* Ajouter une **GitHub Action** qui exécute les tests d’intégration à chaque push ou PR

### 3. Présentation attendue

* Affichage des résultats de test
* Exemple de fail dans la CI et sa correction

---

**Livrables :**

* Tests d’intégration fonctionnels
* GitHub Action opérationnelle
* Démo ou capture de résultats