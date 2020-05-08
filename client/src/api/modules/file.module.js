import CommonHttp from '../http'

const commonHttp = new CommonHttp()
const http = commonHttp.http.bind(commonHttp)



/**
 * 导出文件
 * @param params
 */
const ymarkInfoExport = params => http({
    url: 'http://basedbproduct.noscan.sparta.html5.qq.com/ymark/export',
    params,
})


export default {
    ymarkInfoExport,
}
