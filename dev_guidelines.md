# Developer Guidelines

## Project Overview
This project is a reactive currency converter web application. It is a lightweight, single-page application built with AngularJS and styled with Tailwind CSS and DaisyUI.

## Technology Stack
The project relies on Content Delivery Networks (CDNs) for its dependencies. No build step is required.

- **Core**: HTML5
- **Logic**: [AngularJS 1.8.2](https://angularjs.org/)
- **Styling**: 
  - [Tailwind CSS](https://tailwindcss.com/) (via script)
  - [DaisyUI](https://daisyui.com/) (Component library)
- **Utilities**: 
  - [theme-change](https://github.com/saadeghi/theme-change) (Theme switching)
- **Data**: JSON (`rates.json`)

## File Structure

```
/
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
The application logic is contained within the `<script>` tag at the bottom of `index.html` inside the `CurrencyController`.
- **`$scope.rates`**: Stores currency rates.
- **`$scope.amount`**: Stores the amount input.
- **`$scope.convert()`**: Function to calculate conversion.

### Data Management
- Currency rates and symbols are defined in `rates.json`.
- The `default_from` key in `rates.json` sets the initial base currency.

## Deployment
This is a static site. To deploy:
1. Ensure `index.html` and `rates.json` are in the deployment directory.
2. Upload to any static site host (GitHub Pages, Netlify, Vercel, or a standard web server).
