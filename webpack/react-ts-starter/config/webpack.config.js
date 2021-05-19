const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const ForkTsCheckerWebpackPlugin = require("fork-ts-checker-webpack-plugin");

// == env utils ==
const env = (name) => name === (process.env.NODE_ENV || "development");

const isProd = () => env("production");

const ifProd = (t, f) => (isProd() ? t : f);

// == paths ==
const dist = path.resolve(__dirname, "..", "./dist");
const context = path.resolve(__dirname, "..", "./src");
const configFile = "../tsconfig.json";
const main = process.env.MAIN_ENTRY || "./index.tsx";

module.exports = {
  context,

  entry: main,

  output: {
    path: dist,
    filename: ifProd("[name].[chunkhash].js", "[name].js"),
    chunkFilename: ifProd("[name].[chunkhash].js", "[name].js"),
  },

  resolve: {
    extensions: [".tsx", ".ts", ".js"],
    alias: {
      "~": ".",
    },
  },

  module: {
    rules: [
      {
        test: /\.(ts|js)x?$/,
        exclude: /node_modules/,
        use: [
          {
            loader: "babel-loader",
          },
        ],
      },
    ],
  },

  mode: "development",

  plugins: [
    // Does the type checking since babel only compiles to Javscript.
    new ForkTsCheckerWebpackPlugin({
      typescript: {
        configFile,
      },
    }),

    // injects the bundle.js file
    new HtmlWebpackPlugin({
      template: "index.html",
      favicon: "favicon.ico",
    }),
  ],

  devtool: ifProd(undefined, "eval-cheap-module-source-map"),
};
