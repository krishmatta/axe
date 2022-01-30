# axe &middot; ![Python Application](https://github.com/krishxmatta/axe/actions/workflows/python-app.yml/badge.svg)

axe is a command line tool that provides information from any Wikipedia page straight to your terminal. It can be used to either provide information from a specified page, or to provide information from a random page.

## Usage
axe has two main functionalities: querying information from a specified Wikipedia page, and querying information from a random Wikipedia page. In either case, axe will print out the first paragraph found in the Wikipedia page.

To get information from a specific page, use the `search` subcommand followed by the title of the page you want to query: `axe search <page-title>`.

To get information from a random page, use the `random` subcommand: `axe random`.
