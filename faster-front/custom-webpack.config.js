const webpack = require('webpack');

module.exports = {
  plugins: [
    new webpack.DefinePlugin({
      $ENV: {
        ENVIRONMENT: JSON.stringify(process.env.ENVIRONMENT),
        CHANNEL_API_URL: JSON.stringify(process.env.CHANNEL_API_URL)
      }
    })
  ]
};
