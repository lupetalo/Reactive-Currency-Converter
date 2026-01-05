# Reactive Currency Converter

A lightweight, real-time currency converter web application built with [Alpine.js](https://alpinejs.dev/) and styled with [DaisyUI](https://daisyui.com/) + [Tailwind CSS](https://tailwindcss.com/).

## Features

- **Reactive Conversion**: Instantly converts amounts as you type or select currencies.
- **Theming**: Includes 5 built-in themes (Forest, Cupcake, Dark, Light, Cyberpunk).
- **Responsive Design**: Mobile-friendly interface.
- **Local Dependencies**: All assets (CSS, JS) are hosted locally within the project for privacy and reliability. No external CDN requests are made during runtime.

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Run a local server:**
   Because the app loads data from `rates.json` via `$http`, you need a local web server to avoid CORS/security restrictions.

   Using Python:
   ```bash
   python3 -m http.server
   ```

   Using Node.js:
   ```bash
   npx http-server .
   ```

3. **Open in Browser:**
   Navigate to `http://localhost:8000` (or the port shown in your terminal).

## Recent Changes

- **Localized Dependencies**: Switched from CDNs to local assets (`/assets`) for DaisyUI, Tailwind, Theme Change, and Alpine.js. This ensures the app can run without reaching out to third-party servers.
- **Modern Stack**: Migrated from AngularJS to Alpine.js for a lighter, more modern "no-build" reactive experience.

## Tech Stack

- **HTML5**
- **Alpine.js 3.x**
- **Tailwind CSS**
- **DaisyUI**

## Data Updates

The application uses `rates.json` for exchange rates. You can update this file automatically using the included Python script.

**Usage:**
```bash
python3 update_rates.py
```
This script fetches the latest middle exchange rates from the National Bank of Serbia website and updates `rates.json`. It dynamically detects all currencies currently defined in `rates.json` and attempts to fetch their latest rate.
