const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const webpack = require('webpack');

module.exports = (env, argv) => {
  const config = {
    context: __dirname,
    entry: ['./assets/js/index'],

    output: {
      path: path.resolve('./assets/bundles/'),
      filename: '[name]-[hash].js',
    },

    plugins: [
      new CleanWebpackPlugin(),
      new BundleTracker({ filename: './webpack-stats.json' }),
    ],

    module: {
      rules: [
        {
          test: /\.m?jsx?$/,
          exclude: /node_modules/,
          use: [{
            loader: 'babel-loader',
            options: {
              plugins: ['@babel/plugin-transform-react-jsx'],
              presets: ['@babel/preset-env'],
            },
          }],
        },
      ],
    },

    devServer: {
      contentBase: path.join(__dirname, 'assets/bundles/'),
      headers: { "Access-Control-Allow-Origin": "*" },
      port: 3000,
      hot: true,
      inline: true,
      watchContentBase: true,
    },
  };

  // https://thoughtbot.com/blog/setting-up-webpack-for-react-and-hot-module-replacement

  if (argv.$0.match(/webpack-dev-server/)) {
    argv.mode = 'development';
    config.output.publicPath = 'http://localhost:3000/';
    config.plugins.unshift(new webpack.HotModuleReplacementPlugin());
  }

  // We're not currently using it, but the explicitness doesn't hurt.
  if (argv.mode === 'development') {
    config.output.filename = '[name].js';

    config.entry.unshift(
      'webpack-dev-server/client?http://localhost:3000',
      'webpack/hot/only-dev-server',
    );

    config.module.rules[0].use[0].options.plugins.unshift('react-hot-loader/babel');
  }

  return config;
};
