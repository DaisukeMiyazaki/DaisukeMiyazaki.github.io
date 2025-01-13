module.exports = {
    mode: 'jit',
    content: [
      './_drafts/**/*.html',
      './_includes/**/*.html',
      './_layouts/**/*.html',
      './_posts/*.md',
      './*.md',
      './*.html',
      "./src/**/*.@(js|jsx|ts|tsx)",
    ],
    theme: {
      extend: {
        typography: (theme) => ({
          DEFAULT: {
            css: {
              h1: {
                // color: theme('colors.red.500'),
                // fontWeight: 'bold',
              },
            },
          },
        }),
      },
    },
    plugins: [
      require('@tailwindcss/typography'),
    ],
  }