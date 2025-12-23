# DOCX Reference Template erstellen

Um ein Word-Template für Quarto zu erstellen:

## Schritt 1: Basis-Template generieren

```bash
quarto pandoc -o templates/precision-reference.docx --print-default-data-file reference.docx
```

## Schritt 2: Template in Word anpassen

Öffne `templates/precision-reference.docx` in Microsoft Word und passe die Styles an:

### Zu ändernde Styles:

| Style Name | Anpassung |
|------------|-----------|
| Title | Schrift: Arial 24pt, Farbe: #005a8c |
| Heading 1 | Schrift: Arial 16pt Bold, Farbe: #005a8c |
| Heading 2 | Schrift: Arial 14pt Bold, Farbe: #007cb0 |
| Heading 3 | Schrift: Arial 12pt Bold, Farbe: #00a0d2 |
| Normal | Schrift: Arial 11pt, Zeilenabstand 1.5 |
| First Paragraph | Wie Normal, kein Einzug |
| Body Text | Wie Normal |
| Table Grid | Rahmen: #005a8c |

### Header/Footer hinzufügen:

1. Einfügen → Kopfzeile → PRECISION Logo links
2. Einfügen → Fußzeile → Seitenzahl rechts

### Speichern:

Speichere als `precision-reference.docx` im `templates/` Ordner.

## Schritt 3: Testen

```bash
quarto render reports/beispiel-analyse.qmd --to docx --reference-doc templates/precision-reference.docx
```
