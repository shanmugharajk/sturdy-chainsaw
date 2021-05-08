module.exports = {
  purge: ["./src/**/*.{js,jsx,ts,tsx}", "./public/index.html"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        hover: "#2b2a63",
      },
      borderWidth: {
        1: "border-width: 1px",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
