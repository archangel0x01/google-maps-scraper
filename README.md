# Google Maps Scraper

This repository contains a Python script that scrapes business names and phone numbers from Google Maps search results. It automates the process of extracting this information by utilizing cookies from your preferred browser.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Features

- Scrapes Google Maps for business names and phone numbers.
- Supports multiple browsers for cookie extraction:
  - Chrome
  - Firefox
  - Edge
  - Opera
  - Brave
  - Vivaldi
- Outputs data in a readable JSON format.

## Prerequisites

- Python 3.6 or higher
- Supported browser installed (from the list above)
- Logged into Google Maps on the selected browser

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/archangel0x01/google-maps-scraper.git
   cd google-maps-scraper
   ```
2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Follow the steps below to use the scraper:
1. Go to https://maps.google.com/ and search for your term (e.g., "restaurants near me").

2. Scroll to the end of the page to ensure all desired listings are loaded.

3. Open Developer Tools (Ctrl + Shift + I on Windows) and go to the "Console" tab.

4. Copy and paste the following code in the console, then press Enter:

```bash
const links = Array.from(document.querySelectorAll('a'));
const placeLinks = links
    .filter(link => link.href.startsWith('https://www.google.com/maps/place/'))
    .map(link => link.href);

const uniquePlaceLinks = [...new Set(placeLinks)];

console.log('Found ' + uniquePlaceLinks.length + ' unique place links:');
console.log(uniquePlaceLinks);

copy(uniquePlaceLinks);
console.log('Links have been copied to clipboard!');
```
This will copy all the place links to your clipboard.

5. Back in your local project directory, open (or create) links.json and paste the copied array into links.json. For example:

```bash
[
    "https://www.google.com/maps/place/...",
    "https://www.google.com/maps/place/...",
    "... more links ..."
]
```
6. Run the Python script:
```bash
python3 google_maps_scraper.py
```
8. Follow the prompt to select which browser cookies you want to use (the browser where you are logged in to Google).

9. The script will then process each link in links.json, extract the name and phone number, and append the results to output.json.

After completion, it will print each extracted entry in JSON format in the console.
