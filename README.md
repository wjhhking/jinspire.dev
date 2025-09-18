# Jinspire

Writing about curiosity, insights, and reflection.

## About Jin Wu
- AI-first builder, writer, and ex-Google engineer now crafting products at startup speed.
- Documenting the journey in both English and Chinese, from vibe coding experiments to founder life.
- Exploring how humans and AI collaborate, sharing what works (and what does not) in practice.

## Site Quickstart
- Run `bundle exec jekyll serve` to preview locally.
- Posts live in `_posts/`, layouts in `_layouts/`, assets in `assets/`, and configuration in `_config.yml`.

## Terminology
- Home page: `http://127.0.0.1:4000/` (layout `home`).
- Post page: `http://127.0.0.1:4000/YYYY/MM/DD/slug.html` (layout `post`).

## UI Conventions
- Social icons (L/X) show only on the Home header.
- Post pages have a scroll‑aware Catalog FAB that appears after the hero header and aligns with the content column.
- `_site/` is generated and not tracked.

## Local Dev Environment
- Ruby: 2.6.x works; modern Ruby via `rbenv` recommended.
- RubyGems: 3.2.3+ recommended to silence Bundler warning.
- Bundler: `~> 2.4` with Ruby 2.6.

Upgrade commands (system Ruby):
```
sudo gem update --system 3.2.3
sudo gem install bundler -v '~> 2.4' --no-document
bundle install
```

Optional (recommended) with rbenv:
```
brew install rbenv ruby-build
rbenv install 3.2.2 && rbenv local 3.2.2
gem update --system && gem install bundler jekyll --no-document
bundle install
```

## Agent Notes
- Prefer `rg` for code or text searches; stay concise when responding.
- Keep the home header clean—surface socials via the icons, not text blocks.
- Share any notable insights or issues you encounter while working in the repo.
