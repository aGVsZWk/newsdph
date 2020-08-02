import {message} from "antd";

import axios from "axios";
import basicErrorCodes from "@/constants/basicErrorCodes";

const env = process.env;

/**
 * 错误提示
 */
const errorTip = (msg) => {
  message.error(msg || "后端未返回错误码");
};

/**
 * 重新登录
 */
// function resetLogin() {
//     Vue.$commonDialog({
//         content: '请重新登录！',
//         confirmFunc: () => {
//             store.dispatch('auth/logout')
//         },
//         cancelFunc: () => {},
//     })
// }


class CommonHttp {
  constructor() {
    this.url = "";
    this.params = null;
    this.method = "";
    this.errorCodes = null;
    this.responseAdapter = null;

    this.requestHeaders = "";

    this.withCredentials = false;
    this.headerContentType = "application/json; charset=utf-8";
  }

  /**
   * 生成请求头
   */
  createRequestHeaders() {
    // const token = store.state.auth.token
    this.requestHeaders = {
      "Content-Type": this.headerContentType,
    };
    // if (token && !debug) {
    //     requestHeaders.Authorization = token
    // }
  }

  /**
   * 生成请求参数
   */
  createRequestParams() {
    const params = {};
    this.params && Object.keys(this.params).forEach((objKey) => {
      const val = this.params[objKey];
      if (val !== null && val !== "" && val !== undefined) {
        params[objKey] = val;
      }
    });
    this.params = params;
    // const token = store.state.auth.token

    // if (debug) {
    //     requestParams.token = token
    // }
  }

  requestInterceptor() {
    const {method, url} = this;
    const requestMethod = method === null ? env.REACT_APP_REQUEST_METHOD : method;
    this.requestConfig = {
      url,
      headers: this.requestHeaders,
      method: requestMethod,
      timeout: 1000 * 10,
      withCredentials: this.withCredentials,
      baseURL: env.API_LOCATION,
    };

    if (requestMethod === "get") {
      this.requestConfig.params = this.params;
    }

    if (requestMethod === "post") {
      this.requestConfig.data = this.params;
    }
  }

  /**
   * 处理响应错误
   */
  handleError(reject, resultData) {
    const {errorCodes} = this;
    if (resultData.msg === "TOKEN_INVALID") {
      // resetLogin()
    } else if (resultData.msg === "PERMISSION_DENIED") {
      errorTip("缺少访问权限");
      // store.dispatch('auth/updatePermissions')
    } else {
      const errorCode = resultData.msg;
      const errorText = errorCodes[errorCode] || basicErrorCodes[errorCode] || errorCode;
      errorCodes.dealSelf || errorTip(errorText);
    }
    reject(resultData);
  }

  /**
   * 响应拦截器
   */
  responseInterceptor(resolve, reject, result) {
    const {responseAdapter} = this;
    const resultData = result.data;

    if (result.status === 200) {
      switch (resultData.state) {
        case 0:
          resolve(responseAdapter(resultData));
          break;
        case 1:
          this.handleError(reject, resultData);
          break;
        default:
          errorTip(`未知状态 ${resultData.state}`);
          reject(resultData);
          break;
      }
    } else {
      errorTip(`未知错误 ${result}`);
    }
  }

  initConfig() {
    this.createRequestHeaders();
    this.createRequestParams();
    this.requestInterceptor();
  }

  request() {
    return new Promise((resolve, reject) => {
      axios(this.requestConfig).then((result) => {
        this.responseInterceptor(resolve, reject, result);
      }).catch((error) => {
        errorTip("服务端未响应，请检查网络或稍后重试");
        reject(error);
      });
    });
  }

  http({url, params, method = null, errorCodes = {}, responseAdapter = data => data}) {
    this.url = url;
    this.params = params;
    this.method = method;
    this.errorCodes = errorCodes;
    this.responseAdapter = responseAdapter;

    this.initConfig();
    return this.request();
  }
}

export default CommonHttp;
