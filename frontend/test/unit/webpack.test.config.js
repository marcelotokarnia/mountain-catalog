const merge = require('webpack-merge')
const webpack = require('webpack')
const webpackDevConfig = require('../../webpack.config')

const webpackConfig = merge(webpackDevConfig, {
  mode: 'development',
})

delete webpackConfig.entry

module.exports = webpackConfig