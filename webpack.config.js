const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  mode: 'development',
  context: __dirname,
  entry: './assets/js/index',

  output: {
    path: path.resolve('./assets/bundles/'),
    filename: '[name]-[hash].js',
  },

  plugins: [
    new BundleTracker({ filename: './webpack-stats.json' }),
  ],

  module: {
    rules: [
      {
        test: /\.m?jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            plugins: ['@babel/plugin-transform-react-jsx'],
            presets: ['@babel/preset-env'],
          },
        },
      },
    ],
  },
};
