const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  entry: {
    theme: "./src/index.js",
    bootstrap: "./src/bootstrap/_bootstrap.js",
    fontawesome: "./src/_fontawesome.js",
  },
  output: {
    filename: "js/[name].js",
    path: path.resolve(__dirname, "yummy_sphinx_theme/static")
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "css/[name].css"
    })
  ],
  externals: {
    jquery: "jQuery",
  },
  module: {
    rules: [
      {
        test: require.resolve("./src/index.js"),
        use: "imports-loader"
      },
      {
        test: /\.s[ac]ss$/i,
        use: [
          "style-loader",
          MiniCssExtractPlugin.loader,
          "css-loader",
          {
            loader: "postcss-loader",
            options: {
              ident: 'postcss',
              plugins: function() {
                return [require("precss"), require("autoprefixer")];
              }
            }
          },
          "sass-loader"
        ]
      }
    ]
  }
};
