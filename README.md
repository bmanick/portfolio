# Elegant Architect Portfolio

A high-performance, minimalist portfolio website for a Front-End Architect, built with Vanilla HTML, CSS, and JavaScript.

## Features

*   **Design:** "Midnight Slate" dark theme with glassmorphism accents.
*   **Performance:** Optimized assets, minified build, and zero external framework dependencies (Vanilla JS).
*   **Responsive:** Fully responsive layout with a mobile-friendly sidebar navigation.
*   **Icons:** Integrated RemixIcon and Devicon for consistent and crisp iconography.
*   **Animations:** Subtle scroll-reveal animations and smooth transitions.

## Project Structure

```
portfolio/
├── assets/          # Images, resume, and favicon
├── css/             # Modular CSS files
│   ├── animations.css
│   ├── base.css
│   ├── components.css
│   ├── layout.css
│   ├── style.css    # Main entry point (imports others)
│   └── variables.css
├── js/              # JavaScript files
│   └── main.js
├── build/           # Generated production build (after running build.py)
├── build.py         # Python script to generate optimized build
├── server.py        # Python script to serve the build locally
├── index.html       # Main source HTML
└── README.md        # Project documentation
```

## Getting Started

### Prerequisites

*   Python 3.x (for building and serving)

### Development

To run the source code directly during development:

```bash
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080) in your browser.

### Building for Production

To create an optimized production build (minified HTML, CSS, JS):

```bash
python3 build.py
```

This will create a `build/` directory containing the optimized site.

### Running the Production Build

To serve the optimized build locally:

```bash
python3 server.py
```

Open [http://localhost:8080](http://localhost:8080) in your browser.

## Customization

*   **Theme:** Edit `css/variables.css` to change colors, fonts, and spacing.
*   **Content:** Edit `index.html` to update your profile, experience, and projects.
*   **Icons:** Use [RemixIcon](https://remixicon.com/) class names for UI icons and [Devicon](https://devicon.dev/) for tech stack logos.

## License

MIT
