import utils from "../utils";

const context = require.context("./modules/", false, /\.module.js$/);
const files = context.keys();

export default files.reduce((acc, filePath) => {
  const fileName = utils.logic.filterFilePath(filePath);
  acc[fileName] = context(filePath).default;
  return acc;
}, {});
