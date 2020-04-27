const webpack = require('webpack');

// URL loader to resolve data-urls at build time
const urlLoader = {
  test: /\.(png|jpg|woff|woff2|eot|ttf|svg)$/,
  loader: 'url-loader?limit=100000'
}

const fileLoader = {
    test: /\.(png|jpg)$/,
    loader: "file-loader?name=[name].[ext]&outputPath=/demo/images/&publicPath=images/",
}

const config = {
    entry:  __dirname + '/demo/index.js',
    output: {
        path: __dirname + '/demo/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css'],
         alias: {
            leaflet_css: __dirname + '/node_modules/leaflet/dist/leaflet.css',
            geosearch_css: __dirname + '/css/leaflet-geosearch_custom.css',
            style_css: __dirname + '/css/style.css',
            countries_geojson: __dirname + '/js/geojson/countries_simp_repair.json',
        }
    },
    module: {
        rules: [
          {
            test: /\.css$/,
            use: ['style-loader', 'css-loader'],
          },
          fileLoader,
        ],
    },
};
module.exports = config;
