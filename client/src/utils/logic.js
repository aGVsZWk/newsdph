import crypto from "crypto";

/**
 * 滚动到指定位置
 * @param targetScroll
 * @param scrollDuration
 * @constructor
 */
let scrollInterval;
let scrollBarWidth;

const scrollToTarget = (targetScroll = 0, scrollDuration = 300) => {
  clearInterval(scrollInterval);
  const html = document.querySelector("html");
  const currentScroll = html.scrollTop;
  const scrollValue = targetScroll - currentScroll;
  const movementInterval = 15; // 每次移动的时间间隔
  const speed = scrollValue / (scrollDuration / movementInterval);
  
  scrollInterval = setInterval(() => {
    html.scrollBy(0, speed);
    const realTimeScroll = html.scrollTop;
    
    if (scrollValue > 0) {
      if (realTimeScroll >= targetScroll) {
        clearInterval(scrollInterval);
        html.scrollTo(0, targetScroll);
      }
    } else if (realTimeScroll <= targetScroll) {
      clearInterval(scrollInterval);
      html.scrollTo(0, targetScroll);
    }
  }, movementInterval);
};

/**
 * 获取到文档顶部、左侧的距离
 * @param target
 * @returns {{top: number, left: number}}
 */
export const distanceDocument = (target) => {
  let top = 0;
  let left = 0;
  let targetEle = target;
  
  while (targetEle.offsetParent) {
    top += target.offsetTop;
    left += target.offsetLeft;
    targetEle = target.offsetParent;
  }
  
  return {
    top,
    left,
  };
};

/**
 * 数字前面补零
 * @param num
 * @param length
 * @returns {string}
 */
const prefixInteger = (num, length) => {
  if (num.toString().length < length) {
    return (Array(length).join("0") + num).slice(-length);
  }
  return num;
};

/**
 * 是否是不为空的对象
 * @param val
 * @returns {boolean}
 */
const isMeaningfulObject = (val) => {
  if (val instanceof Object) {
    return Object.keys(val).length > 0;
  }
  return false;
};

/**
 * 过滤文件路径
 * @param filePath
 * @returns {*}
 */
const filterFilePath = filePath => filePath.replace(/\.\/|\.\.\//g, "").replace(/\.module.js$/, "");

/**
 * 获取 scrollBar 宽度
 * @return {number}
 */
const getScrollBarWidth = () => {
  if (scrollBarWidth !== undefined) return scrollBarWidth;
  const outer = document.createElement("div");
  outer.style.visibility = "hidden";
  outer.style.width = "100px";
  outer.style.position = "absolute";
  outer.style.top = "-9999px";
  outer.style.overflow = "scroll";
  document.body.appendChild(outer);
  
  const inner = document.createElement("div");
  inner.style.width = "100%";
  outer.appendChild(inner);
  
  const widthWithScroll = outer.offsetWidth;
  const widthNoScroll = inner.offsetWidth;
  scrollBarWidth = widthWithScroll - widthNoScroll;
  
  return scrollBarWidth;
};
/**
 * 获取cookie
 * @param {*} cookieName
 */
const getCookie = (cookieName) => {
  const allCookies = document.cookie;
  let value = "";
  
  // 索引长度，开始索引的位置
  let cookiePos = allCookies.indexOf(cookieName);
  
  // 如果找到了索引，就代表cookie存在,否则不存在
  if (cookiePos !== -1) {
    // 把cookie_pos放在值的开始，只要给值加1即可
    // 计算取cookie值得开始索引，加的1为“=”
    cookiePos = cookiePos + cookieName.length + 1;
    // 计算取cookie值得结束索引
    let cookieEnd = allCookies.indexOf(";", cookiePos);
    
    if (cookieEnd === -1) {
      cookieEnd = allCookies.length;
    }
    // 得到想要的cookie的值
    value = unescape(allCookies.substring(cookiePos, cookieEnd));
  }
  return value;
};

/**
 * 生成随机密码
 * @param {*} min
 * @param {*} max
 */
const createPassword = (min, max) => {
  // 可以生成随机密码的相关数组
  const num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
  const english = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
  const ENGLISH = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
  const special = ["-", "_", "#"];
  const config = num.concat(english).concat(ENGLISH).concat(special);
  
  // 随机从数组中抽出一个数值
  function getOne(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
  }
  
  // 先放入一个必须存在的
  const arr = [];
  arr.push(getOne(num));
  arr.push(getOne(english));
  arr.push(getOne(ENGLISH));
  arr.push(getOne(special));
  
  // 获取需要生成的长度
  const len = min + Math.floor(Math.random() * ((max - min) + 1));
  
  for (let i = 4; i < len; i++) {
    // 从数组里面抽出一个
    arr.push(config[Math.floor(Math.random() * config.length)]);
  }
  
  // 乱序
  const newArr = [];
  for (let j = 0; j < len; j++) {
    newArr.push(arr.splice(Math.random() * arr.length, 1)[0]);
  }
  return newArr.join("");
};

/**
 * 使用md5加密
 * @param {*} value
 */
const encryptWithMd5 = (value) => {
  const md5 = crypto.createHash("md5");
  md5.update(value);
  return md5.digest("hex");
};


/**
 * 密码验证方法
 * @param {*} str
 */
const passwordValidate = (rule, str, callback) => {
  const rC = {
    lW: "[a-z]", // 小写字母
    uW: "[A-Z]", // 大写字母
    nW: "[0-9]", // 汉字
    sW: "[\\u0020-\\u002F\\u003A-\\u0040\\u005B-\\u0060\\u007B-\\u007E]", // 特殊字符
  };
  
  function Reg(strs, rStr) {
    const reg = new RegExp(rStr);
    if (reg.test(strs)) {
      return true;
    }
    return false;
  }
  
  if (str.length < 8 || str.length > 16) {
    callback(new Error("密码长度应在8 - 16个字符之间"));
  } else {
    const tR = {
      l: Reg(str, rC.lW),
      u: Reg(str, rC.uW),
      n: Reg(str, rC.nW),
      s: Reg(str, rC.sW),
    };
    if ((tR.l && tR.u && tR.n) || (tR.l && tR.u && tR.s) || (tR.s && tR.u && tR.n) || (tR.s && tR.l && tR.n)) {
      // 密码符合要求
      callback();
    } else {
      callback(new Error("密码必须含有\"小写字母\"、\"大写字母\"、\"数字\"、\"特殊符号\"中的任意三种"));
    }
  }
};

/**
 * 通过身份证号获取生日
 * @param {*} idCard
 */
const getBirthdayByIdCard = (idCard) => {
  let birthday = "";
  if (idCard != null && idCard !== "") {
    if (idCard.length === 15) {
      birthday = `19${idCard.substr(6, 6)}`;
    } else if (idCard.length === 18) {
      birthday = idCard.substr(6, 8);
    }
    
    birthday = birthday.replace(/(.{4})(.{2})/, "$1-$2-");
  }
  return birthday;
};

/**
 * 检查实例 data 数据是否有修改
 * @param {*} vueIns
 */
const checkInsDataIsChanged = vueIns => !vueIns.$lodash.isEqual(vueIns.$data, vueIns.$options.data.apply(vueIns));

/**
 * 重置实例 data 数据
 * @param {*} vueIns
 */
const resetInsData = (vueIns) => {
  if (checkInsDataIsChanged(vueIns)) {
    Object.assign(vueIns.$data, vueIns.$options.data.apply(vueIns));
  }
};


export default {
  scrollToTarget,
  prefixInteger,
  isMeaningfulObject,
  filterFilePath,
  getScrollBarWidth,
  getCookie,
  encryptWithMd5,
  createPassword,
  passwordValidate,
  getBirthdayByIdCard,
  checkInsDataIsChanged,
  resetInsData,
};
