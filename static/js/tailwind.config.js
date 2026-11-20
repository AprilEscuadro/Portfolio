/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./templates/**/*.html", "./static/js/**/*.js"],
    corePlugins: { preflight: false },
    theme: {
        extend: {
            screens: { sm: "621px", md: "901px" },
            colors: {
                cream: "#f8efd9", paper: "#fff8e8", ink: "#213c34", rust: "#a95635",
                gold: "#c6a56b", sand: "#e8dfc6", line: "#e3d4b5", muted: "#8b785a",
                green: { DEFAULT: "#123f38", light: "#285d4e" },
            },
            fontFamily: {
                serif: ['"Playfair Display"', "serif"],
                sans: ['"DM Sans"', "sans-serif"],
            },
        },
    },
};