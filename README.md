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
