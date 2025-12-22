# PRECISION Open-Source Workflow mit Quarto

[![Quarto Publish](https://github.com/YOUR-USERNAME/osws-project-quarto/actions/workflows/publish.yml/badge.svg)](https://github.com/YOUR-USERNAME/osws-project-quarto/actions/workflows/publish.yml)

Ein vollständig open-source Workflow für wissenschaftliche Berichte und Analysen im PRECISION-Projekt.

## Features

- **Automatisierte Berichtserstellung** - Von Jupyter Notebook zum fertigen Report
- **Einheitliches Design** - PRECISION Corporate Template
- **Versionskontrolle** - Git-basierter Workflow
- **Automatisches Deployment** - GitHub Actions + GitHub Pages
- **100% Open Source** - Alle Tools frei verfügbar

## Schnellstart

### 1. Repository klonen

```bash
git clone https://github.com/YOUR-USERNAME/osws-project-quarto.git
cd osws-project-quarto
```

### 2. Python-Umgebung einrichten

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Quarto installieren

Download von [quarto.org](https://quarto.org/docs/get-started/)

### 4. Lokal entwickeln

```bash
quarto preview
```

## Projektstruktur

```
osws-project-quarto/
├── .github/
│   └── workflows/
│       └── publish.yml      # GitHub Actions Workflow
├── assets/
│   ├── css/                 # PRECISION Styles
│   └── images/              # Logos, Grafiken
├── data/
│   └── sample/              # Beispieldaten
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_statistical_analysis.ipynb
│   └── 03_visualization.ipynb
├── reports/
│   ├── beispiel-analyse.qmd
│   └── patient-statistics.qmd
├── _quarto.yml              # Quarto Konfiguration
├── index.qmd                # Startseite
├── guide.qmd                # Anleitung
├── requirements.txt         # Python Dependencies
└── README.md
```

## Workflow

```
Jupyter Notebook → .qmd Datei → git push → GitHub Action → GitHub Pages
```

1. **Analyse** in Jupyter Notebook durchführen
2. **Ergebnisse** in Quarto-Dokument (.qmd) integrieren
3. **Commit & Push** zu GitHub
4. **Automatisch** wird die Website neu gebaut und deployed

## Neuen Bericht erstellen

1. Erstelle eine neue `.qmd` Datei in `reports/`:

```yaml
---
title: "Mein Bericht"
author: "Name"
date: today
format:
  html:
    code-fold: true
---
```

2. Füge den Bericht zu `_quarto.yml` hinzu
3. Committe und pushe die Änderungen

## Open Source Stack

| Komponente | Tool | Lizenz |
|------------|------|--------|
| Dokumentation | [Quarto](https://quarto.org) | MIT |
| Versionskontrolle | Git | GPL-2.0 |
| Hosting | GitHub Pages | Kostenlos |
| CI/CD | GitHub Actions | Kostenlos |
| Analyse | Python, Jupyter | BSD/MIT |

## Lokale Entwicklung

### Einzelne Datei rendern

```bash
quarto render reports/beispiel-analyse.qmd
```

### Ganzes Projekt bauen

```bash
quarto render
```

### PDF erstellen

```bash
quarto render reports/beispiel-analyse.qmd --to pdf
```

## GitHub Setup

### 1. Repository erstellen

Erstelle ein neues Repository auf GitHub.

### 2. Code pushen

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/osws-project-quarto.git
git push -u origin main
```

### 3. GitHub Pages aktivieren

1. Gehe zu **Settings** → **Pages**
2. Unter **Source** wähle **GitHub Actions**
3. Speichern

### 4. Warten

Nach dem ersten Push dauert es 2-5 Minuten, bis die Seite unter `https://YOUR-USERNAME.github.io/osws-project-quarto/` verfügbar ist.

## Beitragende

PRECISION Team

## Lizenz

MIT License - siehe [LICENSE](LICENSE) Datei.
