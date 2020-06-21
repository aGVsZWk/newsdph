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


const fileListUplaod = (params) => http({
  url: "/user/uploadFileList",
  params,
  method: 'post'
})

const heartBeat = (params) => http({
  url: "http://127.0.0.1:8000/user/heartBeat",
  params
})

export default {
    ymarkInfoExport,
    fileListUplaod,
    heartBeat
}
