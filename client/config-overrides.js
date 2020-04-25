const {override, addDecoratorsLegacy, fixBabelImports, addWebpackAlias, addLessLoader} = require("customize-cra");
const path = require('path');

const modifyVars = require('./theme/nx.js')

module.exports = override(
	// enable legacy decorators babel plugin
	addDecoratorsLegacy(),

	fixBabelImports('import', {
		libraryName: 'antd',
		libraryDirectory: 'es',
		style: true
	}),

	addWebpackAlias({
		'@': path.resolve(__dirname, 'src')
	}),

	addLessLoader({
		javascriptEnabled: true,
		modifyVars
	})
);
