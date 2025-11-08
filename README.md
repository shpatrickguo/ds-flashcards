# DS Flashcards (Flask viewer)

A minimal Flask app to view the flashcards stored in cards/*.md.

Requirements
- Python 3.8+
- Install dependencies:
  - pip install -r requirements.txt

Run locally
1. From repo root:
   - export FLASK_APP=app.py
   - pip install -r requirements.txt
   - python app.py
2. Open http://127.0.0.1:5000

Notes
- The app reads files under the `cards/` directory. Cards must include YAML front matter with `name` and `tags`, and the following Markdown sections:
  - `## Q:` for the question
  - `## Answer (Technical)` for the technical answer
  - `## Answer (Non-Technical)` for the plain-language answer

- The card validator script (`scripts/validate_cards.py`) will help ensure the cards conform to this layout.
