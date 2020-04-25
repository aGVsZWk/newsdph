import CommonHttp from '../http'

const commonHttp = new CommonHttp()
const http = commonHttp.http.bind(commonHttp)



/**
 * 获取用户信息
 * @param params
 */
const getUserInfo = params => http({
    url: 'http://127.0.0.1:8000/user/profile',
    params,
})


export default {
    getUserInfo,
}
