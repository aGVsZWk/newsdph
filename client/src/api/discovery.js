import CommonHttp from '@/utils/http'

const env = process.env;

const commonHttp = new CommonHttp(env.REACT_APP_API_LOCATION)
const http = commonHttp.http.bind(commonHttp)

// 获取轮播图列表
export const getBannerList = () => {
  return http({
    url: '/banner',
  })
}

// 获取推荐歌单
export const getRecommendlist = ({ limit = 10 } = {}) => {
  return http({
    url: '/personalized',
    method: 'get',
    params: {
      limit,
    },
  })
}

// 获取最新音乐
export const getNewsong = () => {
  return http({
    url: '/personalized/newsong',
    method: 'get',
  })
}

// 获取推荐MV
export const getMv = () => {
  return http({
    url: '/personalized/mv',
    method: 'get',
  })
}

// 获取音乐的url
export const getSongUrl = ({ id }) => {
  return http({
    url: '/song/url',
    method: 'get',
    params: {
      id,
    },
  })
}
