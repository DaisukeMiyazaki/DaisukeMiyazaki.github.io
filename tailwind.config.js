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
          light: "#F5F6F8", // Obsidianライトテーマの背景色に近い色
          dark: "#1E2028", // Obsidianダークテーマの背景色（より深い濃紺がかった黒）
          link: "#3B82F6", // 既存のリンク色
          "link-dark": "#60A5FA", // 既存のダークモードリンク色
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
