module.exports = {
  // If use as web app
  // publicPath: "",

  outputDir: "web_builded",
  transpileDependencies: ["vuetify"],
  productionSourceMap: process.env.NODE_ENV != "production",

  configureWebpack: {
    devtool: process.env.NODE_ENV === "development" ? "source-map" : false,
  },
};
