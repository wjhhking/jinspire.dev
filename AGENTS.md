Agent Notes for jinspire.dev

Scope
- This file documents working conventions for the entire repo.

Layouts & UI
- Home page uses layout `home`; post pages use layout `post`.
- Social icons (LinkedIn/X) appear only on the Home header.
- Post pages expose a Catalog FAB that appears after scrolling past the header (scroll‑aware) and aligns with the content column. Avoid adding the catalog to the Home page.

Do / Don’t
- Do not commit generated output: `_site/` is excluded. Keep PRs focused on source files.
- Keep changes minimal and consistent with existing styles; prefer small, focused patches.
- Prefer `rg` for searches and read files in small chunks.
- Avoid introducing long helper files; refactor if a file grows too large.

Local Dev
- Serve locally with `bundle exec jekyll serve`.
- RubyGems 3.2.3+ and Bundler `~> 2.4` recommended for Ruby 2.6; modern Ruby via `rbenv` encouraged.

Commit Hygiene
- Use imperative, concise commit messages describing the user‑visible change.

