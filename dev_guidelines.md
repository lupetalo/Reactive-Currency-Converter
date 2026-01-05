# Developer Guidelines

## Project Overview
This project is a reactive currency converter web application. It is a lightweight, single-page application built with AngularJS and styled with Tailwind CSS and DaisyUI.

## Technology Stack
The project relies on local assets stored in the `assets/` directory. No build step is required.

- **Core**: HTML5
- **Logic**: [Alpine.js](https://alpinejs.dev/) (Local)
- **Styling**: 
  - [Tailwind CSS](https://tailwindcss.com/) (Local script)
  - [DaisyUI](https://daisyui.com/) (Local component library)
- **Utilities**: 
  - Custom alpine-based theme switcher (defaults to **Dark** theme)
- **Data**: JSON (`rates.json`)

## File Structure

```
/
├── assets/         # Local dependencies (CSS, JS)
├── index.html      # Main application file (HTML + JS Controller)
├── rates.json      # Configuration file for currency rates and symbols
└── ...
```

## Development Workflow

### Prerequisites
- A text editor (VS Code recommended).
- A local web server to serve the static files (required for `$http` requests to `rates.json` due to CORS/Clickjacking protections in some browsers when opening files directly).

### Running Locally
1. Open the project folder in your terminal.
2. Start a simple HTTP server.
   e.g., using Python:
   ```bash
   python3 -m http.server
   ```
   or using Node.js `http-server`:
   ```bash
   npx http-server .
   ```
3. Navigate to `http://localhost:8000` (or the port specified by your server).

### Javascript Logic
The application logic is contained within the `<script>` tag at the bottom of `index.html` using [Alpine.js](https://alpinejs.dev/).
- **`x-data="currencyConverter()"`**: Initialize the component state.
- **`init()`**: Fetches rates from `rates.json`.
- **`convert()`**: Function to calculate conversion.

### Data Management
- Currency rates and symbols are defined in `rates.json`.
- The `default_from` key in `rates.json` sets the initial base currency.

### Automation
- `update_rates.py`: A Python script to fetch the latest rates from the National Bank of Serbia.
  - Run with `python3 update_rates.py`.
  - It reads `rates.json` to identify which currencies to update.
  - If you add a new currency to `rates.json`, this script will automatically attempt to fetch its rate next time it runs (provided the currency code exists on the NBS page).

## Deployment
This is a static site. To deploy:
1. Ensure `index.html` and `rates.json` are in the deployment directory.
2. Upload to any static site host (GitHub Pages, Netlify, Vercel, or a standard web server).
