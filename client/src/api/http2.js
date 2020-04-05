class CommonHttp {
    constructor() {
    }

    createRequestParams(params) {
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

    createRequestUrl(url, method, params) {
        const baseUrl = "http://127.0.0.1:8000"
        let targetUrl = ''
        if (method === "get"){
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


    createRequestConfig(method, params) {
        let config = {
            // body: data,
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
            // params: method === "get"
            // 	? this.createRequestParams(params)
            // 	: null,
            // data: method === "get"
            // 	? this.createRequestParams(params)
            // 	: null
            body: method === "post" ? this.createRequestParams(params): null
        }
        return config
    }

    responseInterceptor(data){
        console.log(data);
    }

    request(url, method, params) {
        return new Promise((resolve, reject) => {
            fetch(this.createRequestUrl(url, method, params), this.createRequestConfig(method, params)).then(response => response.json()).then(responseData => {
                this.responseInterceptor(responseData)
            }).catch((error) => console.log(error))
        })
    }

    http(url, method, params){
        return this.request(url, method, params)
    }
}

export default CommonHttp;
