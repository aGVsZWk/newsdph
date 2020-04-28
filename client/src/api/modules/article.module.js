import CommonHttp from '../http'

const commonHttp = new CommonHttp()
const http = commonHttp.http.bind(commonHttp)

/**
 * 获取文章列表
 * @param params
 */
const getArticles = params => http({
    url: 'http://rap2.taobao.org:38080/app/mock/252652/api/articles/',
    params,
})


export default {
    getArticles,
}
