import logic from "./logic.module";

const context = require.context("./", false, /\.module.js$/);
const files = context.keys();
const utils = {};

files.forEach((filePath) => {
  const fileName = logic.filterFilePath(filePath);
  utils[`${fileName}`] = context(filePath).default;
});

utils.install = (Vue) => {
  files.forEach((filePath) => {
    const fileName = logic.filterFilePath(filePath);
    Vue.prototype[`$${fileName}`] = context(filePath).default;
  });
};

export default utils;
