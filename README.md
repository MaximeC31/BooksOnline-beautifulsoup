# 📚 Books Online Scraper

> Pipeline ETL pour extraire, transformer et charger les données de **books.toscrape.com**

---

## Démarrage Rapide

### Créer l'environnement virtuel

```bash
python3 -m venv venv
```

### Activer l'environnement

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Exécution

```bash
python main.py
```

### Résultats

- **CSV** → `output/data/` _(un fichier par catégorie)_
- **Images** → `output/images/` _(couvertures des livres)_

---

## Désactivation de l'environnement

```bash
deactivate
```
