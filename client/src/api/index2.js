import CommonHttp from './http'

const commonHttp = new CommonHttp()
const http = commonHttp.http.bind(commonHttp)

export default {
	getUserList(params) {
		return http('/users/all', 'post', params)
	}
}
