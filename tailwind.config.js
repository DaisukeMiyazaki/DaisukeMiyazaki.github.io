module.exports = {
  mode: "jit",
  darkMode: "class",
  content: [
    "./_drafts/**/*.html",
    "./_includes/**/*.html",
    "./_layouts/**/*.html",
    "./_posts/*.md",
    "./*.md",
    "./*.html",
    "./src/**/*.@(js|jsx|ts|tsx)",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          light: "#FFFFFF", // bg-whiteと同じ
          dark: "#1F2937", // bg-gray-800と同じ
          link: "#3B82F6", // text-blue-500と同じ
          "link-dark": "#60A5FA", // text-blue-400と同じ（ダークモード用）
        },
      },
      typography: (theme) => ({
        DEFAULT: {
          css: {
            h1: {
              // color: theme('colors.red.500'),
              // fontWeight: 'bold',
            },
          },
        },
        dark: {
          css: {
            color: theme("colors.gray.300"),
            '[class~="lead"]': {
              color: theme("colors.gray.400"),
            },
            a: { color: theme("colors.primary.link-dark") },
            h1: { color: theme("colors.white") },
            h2: { color: theme("colors.white") },
            h3: { color: theme("colors.white") },
            blockquote: {
              borderLeftColor: theme("colors.gray.700"),
              color: theme("colors.gray.300"),
            },
            hr: { borderColor: theme("colors.gray.700") },
            strong: { color: theme("colors.gray.100") },
            li: {
              "&::before": {
                backgroundColor: theme("colors.gray.700"),
              },
            },
          },
        },
      }),
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
