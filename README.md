# DS Prep

## Practical Interview Prep Order

1. **Coding first** (fastest rejection point).  
   Master LeetCode mediums: arrays/strings, hash maps, two pointers, BFS/DFS, heaps, basic DP.

2. **Interview-proof projects**. Be ready to explain:  
   - Baseline & why  
   - Key metric (not accuracy)  
   - What broke (leakage, imbalance, edge cases)  
   - Production plan (latency, monitoring, retraining)

3. **ML fundamentals** (when + tradeoffs):  
   - Bias/variance fixes  
   - Regularization, calibration, thresholding  
   - Leakage, shift, imbalance  
   - Feature eng vs model complexity  
   - Debugging worse models

4. **Light ML system design**: Practice recommender, fraud detection, text classification, forecasting.  
   Cover: data → training → deployment → monitoring → retraining.

5. **Behavioral**: Prep 3 stories ("model failed," stakeholder work).

**Weekly plan**:  
- 45-60 min/day coding  
- 3x/week ML fundamentals  
- 1 weekend: mock interview + project deep dive


## Requirements
- Python 3.8+
- Install dependencies:
  - pip install -r requirements.txt

## Run locally
1. From repo root:
   - export FLASK_APP=app.py
   - pip install -r requirements.txt
   - python app.py
2. Open http://127.0.0.1:5000

## Notes
- The app reads files under the `cards/` directory. Cards must include YAML front matter with `name` and `tags`, and the following Markdown sections:
  - `## Q:` for the question
  - `## Answer (Technical)` for the technical answer
  - `## Answer (Non-Technical)` for the plain-language answer

- The card validator script (`scripts/validate_cards.py`) will help ensure the cards conform to this layout.
