# GitHub Profile Lookup

A simple Python CLI tool that fetches and displays live profile data for any GitHub user, using the GitHub public API.

## What it does

- Takes a GitHub username as input
- Fetches real-time profile data (name, bio, followers, following, public repos, location, account creation date)
- Handles invalid/non-existent usernames gracefully instead of crashing

## Tech used

- Python
- `requests` library for API calls
- GitHub REST API

## How to run

```bash
pip install requests
python github_profile_lookup.py
```

## What I learned building this

- How to send GET requests to a real API and work with JSON responses
- The importance of checking `response.status_code` before assuming a request succeeded
- That calling `.json()` immediately discards the response object, losing access to `.status_code` — this cost me a bug I had to debug and fix myself