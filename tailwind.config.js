/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/templates/*.html', // Include all HTML files in the templates directory
    './app/static/**/*.js',      // Include all JS files in the static directory
    './app/**/*.py',             // Include all Python files in the app directory
    './app/static/*.css'      // Include all CSS files in the static directory
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}