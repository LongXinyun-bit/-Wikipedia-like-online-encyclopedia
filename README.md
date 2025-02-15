# Wiki-like Encyclopedia Web Application

## Description:
This web application is a lightweight, Wikipedia-style online encyclopedia designed to manage and display user-generated content stored in Markdown format. Users can browse, search, create, and edit encyclopedia entries, with content dynamically rendered as HTML for seamless readability. The platform emphasizes simplicity, usability, and efficient content management.

## Key Features:

- Entry Viewing:

Access entries via /wiki/TITLE, dynamically converting Markdown content to HTML for clean rendering.

Error handling for non-existent entries, displaying a user-friendly error page.

- Index Page:

Lists all entries with hyperlinks for direct navigation to individual entry pages.

- Search Functionality:

- Exact Matches: Redirects users to the entry page if the search query matches an entry title.

- Partial Matches: Displays a list of entries containing the search term as a substring.

- Content Creation:

Users can create new entries with a title and Markdown content.

Validation ensures no duplicate titles exist, preventing overwrites.

- Content Editing:

Edit existing entries via a pre-populated Markdown editor.

Changes are saved to disk, and users are redirected to the updated entry.

- Markdown-to-HTML Conversion:

Utilizes Python-Markdown2 for robust conversion of Markdown syntax (headings, lists, links, etc.) to HTML.

## Technical Stack:

- Backend: Django (Python) for routing, views, and data handling.

- Frontend: HTML/CSS for structure and styling, JavaScript for dynamic interactions.

- Markdown Processing: Python-Markdown2 library.

- Storage: Entries stored as Markdown files, managed via Django’s file-handling utilities.

- Security: CSRF protection, input validation, and error handling.

## Contact:
For inquiries or collaboration opportunities, please reach out via lxyxsc999@163.com.
