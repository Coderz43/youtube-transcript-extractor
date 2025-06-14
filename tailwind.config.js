/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#6e76ff',
          foreground: '#ffffff',
        },
      },
    },
  },
  plugins: [],
  darkMode: 'class',
};