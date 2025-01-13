module.exports = {
    plugins: [
      require('tailwindcss'),
      require('autoprefixer'),
    require("tailwindcss/nesting"),
    require("tailwindcss"),
      ...(process.env.JEKYLL_ENV == 'production'
        ? [require('cssnano')({ preset: 'default' })]
        : [])
    ]
  }
  