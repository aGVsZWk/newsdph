import http from './http';


const getUserList = (params) => {
	return http('/users/all', 'get', params)
}

const login = (data) => {
    return http('/auth/login', 'post', data)
}

export default login
