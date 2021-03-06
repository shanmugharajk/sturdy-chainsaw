module.exports = {
  purge: ["./src/**/*.html", "./src/**/*.js"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        hover: "#2b2a63",
      },
      width: {
        13: "3.25rem",
        25: "6.5rem",
      },
      margin: {
        0.5: "0.125rem",
      },
      borderWidth: {
        1: "border-width: 1px",
      },
      outline: {
        thin: "1px solid transparent;",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
