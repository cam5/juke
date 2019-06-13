const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const config = require('./webpack.config.js')('dev', 'webpack-dev-server');

config.entry.unshift('webpack-dev-server/client?http://localhost:8080/');

const compiler = webpack(config);
const server = new WebpackDevServer(compiler);
server.listen(8080);
