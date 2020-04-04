const createRequestParams = (params) => {
	let newParams = {}
	params && Object.keys(params).forEach((objKey) => {
		const val = params[objKey]
		if (val !== null && val !== '' && val !== undefined) {
			newParams[objKey] = val
		}
	})

	let t = JSON.stringify(newParams)
	return t
}

const createRequestUrl = (url, method, params) => {
	const baseUrl = "http://localhost:2345/api"
	let targetUrl = ''
	if (method === "get") {
		let parasPartOfUrl = ''
		for (var i = 0; i < Object.keys(params).length; i++) {
			parasPartOfUrl += Object.keys(params)[i] + "=" + Object.values(params)[i] + "&"
		}
		parasPartOfUrl = parasPartOfUrl.substr(0, parasPartOfUrl.length - 1)
		targetUrl = baseUrl + url + "?" + parasPartOfUrl
	} else {
		targetUrl = baseUrl + url
	}
	return targetUrl
}

const createRequestConfig = (method, params) => {
	let config = {
		cache: 'no-cache',
		credentials: 'omit',
		headers: {
			"user-agent": "Mozilla/4.0 MDN Example",
			"content-type": "application/json"
		},
		method: method,
		mode: 'cors',
		redirect: 'follow',
		referrer: 'no-referrer',
		body: method === "post"
			? createRequestParams(params)
			: null
	}
	return config
}

const responseInterceptor = (resolve, reject, response) => {
	resolve(response.json())
}

// const request = (url, method, params) => {
// 	return new Promise((resolve, reject) => {
// 		fetch(createRequestUrl(url, method, params), createRequestConfig(method, params)).then(response => response.json()).then(responseData => {
// 			responseInterceptor(responseData)
// 		}).catch((error) => console.log(error))
// 	})
// }

const request = (url, method, params) => {
	return new Promise((resolve, reject) => {
		fetch(createRequestUrl(url, method, params), createRequestConfig(method, params)).then(response => responseInterceptor(resolve, reject, response)).catch((error) => console.log(error))
		// TODO: why can't read data?
	});
}

const http = (url, method, params) => {
	return request(url, method, params)
}

export default http
