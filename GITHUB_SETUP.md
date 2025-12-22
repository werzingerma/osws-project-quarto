# GitHub Setup - Schritt für Schritt

Diese Anleitung führt dich durch das komplette Setup auf GitHub.

---

## 1. Neues Repository erstellen

1. Gehe zu [github.com](https://github.com) und logge dich ein
2. Klicke auf **"+"** (oben rechts) → **"New repository"**
3. Einstellungen:
   - **Repository name:** `osws-project-quarto` (oder dein Wunschname)
   - **Description:** `Open-Source Workflow mit Quarto für wissenschaftliche Berichte`
   - **Visibility:** `Public` (für GitHub Pages kostenlos) oder `Private`
   - **NICHT** "Add a README file" aktivieren (haben wir schon)
4. Klicke **"Create repository"**

---

## 2. Lokales Repository initialisieren und pushen

Öffne ein Terminal im Projektordner und führe aus:

```bash
# Git initialisieren (falls noch nicht geschehen)
git init

# Alle Dateien hinzufügen
git add .

# Ersten Commit erstellen
git commit -m "Initial commit: PRECISION Quarto Workflow"

# Branch auf 'main' setzen
git branch -M main

# Remote hinzufügen (ERSETZE YOUR-USERNAME!)
git remote add origin https://github.com/YOUR-USERNAME/osws-project-quarto.git

# Pushen
git push -u origin main
```

---

## 3. GitHub Pages aktivieren

1. Gehe zu deinem Repository auf GitHub
2. Klicke auf **"Settings"** (Zahnrad-Symbol)
3. Im linken Menü: **"Pages"**
4. Unter **"Build and deployment"**:
   - **Source:** Wähle **"GitHub Actions"**
5. Speichern (automatisch)

---

## 4. GitHub Actions prüfen

1. Gehe zu **"Actions"** Tab in deinem Repository
2. Du solltest den Workflow "Publish Quarto Site" sehen
3. Nach dem ersten Push wird er automatisch ausgeführt
4. Warte 2-5 Minuten bis der Build fertig ist

### Bei Fehlern:

- Klicke auf den fehlgeschlagenen Workflow
- Lies die Fehlermeldung
- Häufige Probleme:
  - Python-Dependencies fehlen → `requirements.txt` prüfen
  - Quarto-Syntax-Fehler → `.qmd` Dateien prüfen

---

## 5. Website aufrufen

Nach erfolgreichem Build ist deine Seite verfügbar unter:

```
https://YOUR-USERNAME.github.io/osws-project-quarto/
```

---

## 6. URLs in Konfiguration anpassen

Ersetze `YOUR-USERNAME` in diesen Dateien durch deinen GitHub-Benutzernamen:

### `_quarto.yml`
```yaml
website:
  site-url: https://YOUR-USERNAME.github.io/osws-project-quarto/
  repo-url: https://github.com/YOUR-USERNAME/osws-project-quarto
```

### `README.md`
Alle Vorkommen von `YOUR-USERNAME` ersetzen.

Nach den Änderungen:
```bash
git add .
git commit -m "Update GitHub URLs"
git push
```

---

## 7. Täglicher Workflow

### Neue Analyse hinzufügen:

```bash
# 1. Änderungen machen (Notebook, .qmd, etc.)

# 2. Status prüfen
git status

# 3. Alle Änderungen hinzufügen
git add .

# 4. Commit mit aussagekräftiger Nachricht
git commit -m "Add: Neue Analyse für Q1/2025"

# 5. Pushen
git push

# 6. GitHub Action läuft automatisch
# 7. Nach 2-5 Min ist die Website aktualisiert
```

### Branches für größere Änderungen:

```bash
# Neuen Branch erstellen
git checkout -b feature/neue-funktion

# Arbeiten...
git add .
git commit -m "WIP: Neue Funktion"

# Branch pushen
git push -u origin feature/neue-funktion

# Auf GitHub: Pull Request erstellen
# Nach Review: Merge in main
```

---

## 8. Optionale Erweiterungen

### Branch Protection aktivieren:

1. **Settings** → **Branches**
2. **"Add branch protection rule"**
3. Branch name pattern: `main`
4. Aktiviere:
   - ✅ Require a pull request before merging
   - ✅ Require status checks to pass before merging

### Secrets für sensible Daten:

Falls du API-Keys oder ähnliches brauchst:

1. **Settings** → **Secrets and variables** → **Actions**
2. **"New repository secret"**
3. Name: z.B. `API_KEY`
4. In GitHub Actions verwenden: `${{ secrets.API_KEY }}`

---

## 9. Troubleshooting

### Problem: "Pages build failed"

**Lösung:**
1. Gehe zu **Actions** → fehlgeschlagener Workflow
2. Klicke auf den Job für Details
3. Lies die Fehlermeldung
4. Häufig: Quarto-Syntax-Fehler in `.qmd` Dateien

### Problem: "404 Not Found" auf der Website

**Lösung:**
1. Prüfe ob Pages auf "GitHub Actions" steht (nicht "Deploy from branch")
2. Warte 5 Minuten nach dem letzten Push
3. Lösche Browser-Cache und lade neu

### Problem: Bilder werden nicht angezeigt

**Lösung:**
- Verwende relative Pfade: `![](../assets/images/bild.png)`
- Prüfe Groß-/Kleinschreibung (Linux ist case-sensitive!)

### Problem: Python-Modul nicht gefunden

**Lösung:**
- Füge das Modul zu `requirements.txt` hinzu
- Committe und pushe

---

## 10. Nützliche Git-Befehle

```bash
# Status anzeigen
git status

# Änderungen anzeigen
git diff

# Letzte Commits anzeigen
git log --oneline -10

# Änderungen verwerfen (VORSICHT!)
git checkout -- dateiname.qmd

# Remote-Änderungen holen
git pull

# Branch wechseln
git checkout branchname

# Alle Branches anzeigen
git branch -a
```

---

## Fertig!

Dein Open-Source Workflow ist jetzt eingerichtet. Bei jedem Push wird die Website automatisch aktualisiert.

**Support:**
- Quarto Docs: [quarto.org/docs](https://quarto.org/docs/)
- GitHub Actions: [docs.github.com/actions](https://docs.github.com/en/actions)
- GitHub Pages: [docs.github.com/pages](https://docs.github.com/en/pages)
