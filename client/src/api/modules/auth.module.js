import CommonHttp from "../http";
import CommonHttpForm from "../httpForm";

const commonHttp = new CommonHttp();
const http = commonHttp.http.bind(commonHttp);


/**
 * 登录
 * @param params
 */
const commonHttpForm = new CommonHttpForm();
const login = params => commonHttpForm.http({
  url: "/login",
  params,
  errorCodes: {dealSelf: true},
});

/**
 * 登出
 * @param params
 */
const logout = params => http({
  url: "/logout",
  params,
});


export default {
  login,
  logout,
};
