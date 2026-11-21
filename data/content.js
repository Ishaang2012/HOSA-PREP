/*
 * Study content, keyed by event id (see data/events.js).
 *
 * Shape of one event:
 * {
 *   summaries: {
 *     <bookIndex>: [ { number, title, summary: [ "paragraph", ... ], keyPoints: [ "..." ] } ]
 *   },                     // bookIndex = position of the book in that event's `books` list
 *   tests: {             // usually in its own file: data/tests/<event-id>.js
 *     easy:   [ { q, options: [..4], answer: <index>, explanation, topic } ],
 *     medium: [ ... ],     // each level must have exactly the event's testQuestions (50)
 *     hard:   [ ... ],     // before the site opens it
 *   },
 *   flashcards: [
 *     { section: "Prefixes", description: "...", cards: [ { front, back } ] }
 *   ]
 * }
 *
 * Events or books with no entry here show a "coming soon" state.
 */
// Chapter summaries and quizzes now come from tools/books/ (built into data/books/<event>.js).
window.CONTENT = window.CONTENT || {};
