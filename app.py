#!/usr/bin/env python3
import os
import re
from flask import Flask, render_template, abort, url_for, redirect
import yaml
import markdown

APP_ROOT = os.path.dirname(__file__)
CARDS_DIR = os.path.join(APP_ROOT, 'cards')

app = Flask(__name__, template_folder='templates', static_folder='static')

def load_cards():
    cards = []
    if not os.path.isdir(CARDS_DIR):
        return cards
    for fname in sorted(os.listdir(CARDS_DIR)):
        if not fname.endswith('.md'):
            continue
        path = os.path.join(CARDS_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                txt = f.read()
        except Exception:
            continue

        # parse YAML front matter
        m = re.match(r'^---\n(.*?)\n---\n', txt, re.S)
        fm = {}
        body = txt
        if m:
            fm_text = m.group(1)
            try:
                fm = yaml.safe_load(fm_text) or {}
            except Exception:
                fm = {}
            body = txt[m.end():]

        # extract sections by header
        def extract_section(header):
            # Accept headers like "## Q:" or "## Q: ..." etc.
            pat = r'##\s+' + re.escape(header) + r'\s*(.*?)\n(?=##\s+|$)'
            mm = re.search(pat, body, re.S)
            return mm.group(1).strip() if mm else ''

        question = extract_section('Q:')
        answer_tech = extract_section('Answer (Technical)')
        answer_non = extract_section('Answer (Non-Technical)')

        slug = os.path.splitext(fname)[0]
        tags = fm.get('tags', '')
        if isinstance(tags, str):
            tags_list = [t.strip() for t in tags.split(',') if t.strip()]
        elif isinstance(tags, list):
            tags_list = tags
        else:
            tags_list = []

        cards.append({
            'slug': slug,
            'filename': fname,
            'name': fm.get('name', slug),
            'tags': tags_list,
            'question_md': question,
            'answer_tech_md': answer_tech,
            'answer_non_md': answer_non,
        })

    return cards

@app.route('/')
def index():
    cards = load_cards()
    return render_template('index.html', cards=cards)

@app.route('/card/')
def first_card_redirect():
    cards = load_cards()
    if not cards:
        abort(404)
    return redirect(url_for('show_card', slug=cards[0]['slug']))

@app.route('/card/<slug>')
def show_card(slug):
    cards = load_cards()
    card = next((c for c in cards if c['slug'] == slug), None)
    if not card:
        abort(404)

    # Render markdown to HTML
    md = markdown.Markdown(extensions=['fenced_code', 'tables'])
    card_html = {
        'question': md.convert(card['question_md'] or ''),
    }
    # reset markdown instance between conversions
    md.reset()
    card_html['answer_tech'] = md.convert(card['answer_tech_md'] or '')
    md.reset()
    card_html['answer_non'] = md.convert(card['answer_non_md'] or '')

    # determine navigation
    slugs = [c['slug'] for c in cards]
    idx = slugs.index(slug)
    prev_slug = slugs[idx - 1] if idx > 0 else None
    next_slug = slugs[idx + 1] if idx < len(slugs) - 1 else None

    return render_template('card.html', card=card, card_html=card_html,
                           prev_slug=prev_slug, next_slug=next_slug)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
