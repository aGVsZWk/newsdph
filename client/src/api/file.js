import CommonHttp from '@/utils/http'

const commonHttp = new CommonHttp()
const http = commonHttp.http.bind(commonHttp)



/**
 * 导出文件
 * @param params
 */
export const ymarkInfoExport = params => http({
    url: 'http://basedbproduct.noscan.sparta.html5.qq.com/ymark/export',
    params,
})


export const fileListUplaod = (params) => http({
  url: "/user/uploadFileList",
  params,
  method: 'post'
})

export const heartBeat = (params) => http({
  url: "/user/heartBeat",
  params
})
