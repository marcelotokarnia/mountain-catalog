// This is a karma config file. For more details see
//   http://karma-runner.github.io/0.13/config/configuration-file.html
// we are also using it with karma-webpack
//   https://github.com/webpack/karma-webpack

var webpackConfig = require('./webpack.test.config')

module.exports = function (config) {
  config.set({
    // to run in additional browsers:
    // 1. install corresponding karma launcher
    //    http://karma-runner.github.io/0.13/config/browsers.html
    // 2. add it to the `browsers` array below.
    browsers: ['PhantomJS'],
    frameworks: ['mocha', 'sinon-chai', 'phantomjs-shim'],
    reporters: ['spec'],
    logLevel: config.LOG_INFO,
    loggers: [
      {type: 'console'},
    ],
    browserConsoleLogOptions: {
      level: '',
      terminal: true,
    },
    colors: true,
    files: [
      '../../node_modules/babel-polyfill/dist/polyfill.js',
      './specs/**/*.spec.js',
    ],
    preprocessors: {
      './specs/**/*.spec.js': ['webpack', 'sourcemap'],
    },
    webpack: webpackConfig,
    webpackMiddleware: {
      stats: 'errors-only',
    },
    port: 9876,
    autoWatch: true,
    singleRun: true,
    concurrency: Infinity,
  })
}
