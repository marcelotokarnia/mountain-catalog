const path = require('path')
const webpack = require('webpack')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const { VueLoaderPlugin } = require('vue-loader')


module.exports = {
  context: path.resolve(__dirname),
  entry: {
    build: './src/index.ts',
    styles: './src/styles.global.ts'
  },
  output: {
    filename: '[name].js',
    path: path.join(__dirname, '/dist'),
    publicPath: '/dist/',
  },
  resolve: {
    extensions: ['.js', '.ts', '.json', '.vue'],
    alias: {
      '@src': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@locales': path.resolve(__dirname, './src/locales'),
      '@typings': path.resolve(__dirname, './typings'),
      '@queries': path.resolve(__dirname, './src/queries'),
      '@mutations': path.resolve(__dirname, './src/mutations'),
      'vue$': 'vue/dist/vue.esm.js'
    }
  },
  module: {
    rules: [
      {
        test: /\.styl(us)?$/,
        loader: 'vue-style-loader!css-loader!stylus-loader?paths=node_modules/bootstrap-stylus/stylus/'
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        options: {
          presets: ['es2015'],
        },
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
            js: {
              loader: 'babel-loader',
              options: {
                presets: ['stage-2']
              }
            },
          }
          // other vue-loader options go here
        }
      },
      {
        test: /\.d\.ts$/,
        loader: 'ignore-loader',
      },
      {
        test: /\.tsx?$/,
        loader: 'ts-loader',
        exclude: /node_modules|\.d\.ts$/,
        options: {
          appendTsSuffixTo: [/\.vue$/],
        }
      },
      {
        loader: 'graphql-tag/loader',
        test: /\.(graphql|gql)$/,
      },
      {
        test: /\.scss$/,
        use: [
          'vue-style-loader',
          'css-loader',
          {
            loader: 'sass-loader',
            options: {
              data: '$color: red;'
            }
          }
        ]
      },
      {
        test: /\.css$/,
        use: ['vue-style-loader', 'css-loader']
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      }
    ]
  },
  plugins: [
    new VueLoaderPlugin(),
    new CopyWebpackPlugin([
      { from: 'assets/images/*', to: 'images/[name].[ext]' },
      { from: 'assets/js/*', to: 'js/[name].[ext]' },
      { from: 'assets/css/*', to: 'css/[name].[ext]' },
      { from: 'assets/icons/*', to: 'icons/[name].[ext]' },
      { from: 'assets/favicon.png', to: '[name].[ext]' },
    ]),
  ],
  devServer: {
    historyApiFallback: true,
    noInfo: true
  },
  performance: {
    hints: false
  },
  devtool: '#eval-source-map'
}

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map'
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: true,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ])
}