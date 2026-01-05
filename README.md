# Reactive Currency Converter

A lightweight, real-time currency converter web application built with [AngularJS](https://angularjs.org/) and styled with [DaisyUI](https://daisyui.com/) + [Tailwind CSS](https://tailwindcss.com/).

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

- **Localized Dependencies**: Switched from CDNs to local assets (`/assets`) for DaisyUI, Tailwind, Theme Change, and AngularJS. This ensures the app can run without reaching out to third-party servers.

## Tech Stack

- **HTML5**
- **AngularJS 1.8.2**
- **Tailwind CSS**
- **DaisyUI**
