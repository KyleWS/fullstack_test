// IS MY INDENTATION OFF?
var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
	// Main directory locations
	context: __dirname,
	entry: './assets/js/index', 
	// Locations for the bundle, and naming convetions
	output: {
		path: path.resolve('./assets/bundles/'),
		filename: '[name]-[hash].js',
	},
	plugins: [
		// Extra goodies we can throw in to webpack
		new BundleTracker({filename: './webpack-stats.json'}),
		// Makes jquery available in every module
		new webpack.ProvidePlugin({
			$: 'jquery',
			jQuery: 'jquery',
			'window.jQuery': 'jquery'
		})
	],
	module: {
		loaders: [
			// User loader on .js and .jsx
			{
				test: /\.jsx?$/,
				exclude: /node_modules/,
				loader: 'babel-loader',
				query: {
					// Specify react
					presets: ['react']
				}
			}
		]
	},
	resolve: {
		moduleExtensions: ['node_modules'],
		extensions: ['', '.js', '.jsx']
	}
}
