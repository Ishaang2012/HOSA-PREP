# HOSA Prep site (name TBD)

Static site: no build step and no server needed. Open `index.html` in a browser, or host the folder anywhere (GitHub Pages, Netlify, Vercel).

## Files
- `index.html`: page shell
- `css/styles.css`: all styling (light and dark themes)
- `js/app.js`: routing and the three study modes. Set the site name in `SITE_NAME` at the top.
- `data/events.js`: the 64 HOSA events for 2026–27, built from the official guidelines (format, test plan, official references, guideline link). Leaves out Recognition, Middle School-only and Academic Testing Center events.
- `data/content.js`: summaries, tests and flashcards, keyed by event id

## Adding content for an event
Add an entry to `window.CONTENT` in `data/content.js` using the event's `id` from `events.js`.
`medical-terminology` is a complete example. Events without an entry show "Coming soon."

- **summaries**: chapters for each official reference, keyed by the book's position in that event's `books` list in `events.js`
- **tests**: `easy`, `medium`, `hard` arrays of questions (`answer` is the index of the correct option). Put them in `data/tests/<event-id>.js` and add a `<script>` tag for it in `index.html`. A test only opens once it has exactly the real test's length (`testQuestions` in `events.js`, 50 for every 2026–27 event).
- **quizzes**: chapter quizzes, one per 3 chapters of a book, keyed by the book's position in `books`: `{ 0: [ { chapters: [1, 2, 3], questions: [...] } ] }`. Put them in `data/quizzes/<event-id>.js` and add a `<script>` tag for it in `index.html`.
- **flashcards**: an array of sections, each with its own `cards`
- **guide** (events without a written test): how the event runs, the official rubric points, tips, common mistakes, and a prep checklist that saves in the browser. Write `tools/guides/<event_id>.py` (see the docstring in `tools/build_guides.py`) and run `python3 tools/build_guides.py <event-id>`. The builder checks that each rubric adds up to the total printed on the official rating sheet, writes `data/guides/<event-id>.js` and adds the `<script>` tag.

Tests and flashcards are written as Python in `tools/content/<event_id>.py` and built with `python3 tools/build_content.py <event-id>`, which checks question counts against the official test plan.
