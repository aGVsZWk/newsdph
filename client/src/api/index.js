import http from './http';


const getUserList = (params) => {
	return http('/users/all', 'get', params)
}


export default getUserList
