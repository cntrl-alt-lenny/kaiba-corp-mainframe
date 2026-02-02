# Kaiba Corp Mainframe

A Python toolkit for interacting with the Yu-Gi-Oh! YGOProDeck API (v7). The first project focuses on searching cards and downloading images for local use.

## What’s Inside
- `docs/api_reference.md`: Full YGOProDeck API documentation (v7) with cleaned formatting.
- `project_01_card_search/main.py`: Simple CLI to search cards, print stats, and download images locally.

## Quick Start
1. Create and activate a virtual environment (recommended).
2. Install dependencies if needed.
3. Run the card search script:

```bash
python project_01_card_search/main.py
```

## Notes
- Images are downloaded locally to avoid hotlinking.
- The API is rate-limited; cache results where possible.

## License
See `LICENSE`.
