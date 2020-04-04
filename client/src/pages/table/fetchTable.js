import React, {PropTypes} from 'react';
import {Table} from 'antd';

const columns = [
	{
		title: "姓名",
		dataIndex: "name",
		key: "name"
	}, {
		title: "性别",
		dataIndex: "gender",
		key: "gender"
	}, {
		title: "年龄",
		dataIndex: "age",
		key: "age"
	}, {
		title: "地址",
		dataIndex: "address",
		key: "address"
	}
]

class fetchTable extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			data: [],
			columns: [],
			pagination: {
				current: null,		// 默认页码，传空由后端控制
				pageSize: null,		// 默认页显示数量，传空由后端控制
				total: null,
				totalPages: null,
			}
		}
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
		const baseUrl = "http://localhost:2345/api"
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
		this.setState({
			data: data.data,
			pagination: data.pagination
		})
	}

	getData(url, method, params) {
		fetch(this.createRequestUrl(url, method, params), this.createRequestConfig(method, params)).then(response => response.json()).then(responseData => {
			this.responseInterceptor(responseData)
		}).catch((error) => console.log(error))
	}
	componentWillMount() {
		this.setState({columns})
		this.getData("/users/all", "post", {
			...this.state.pagination
			// filterField:"gender",
			// filterCondition: "gt",
			// filterValue:"男",
			// orderField:"-age",
		})
	}


	handleTableChange = (pagination, filters, sorter) => {
		// console.log(pagination, filters, sorter);
		// const pager = {...this.state.pagination}
		// pager.current = pagination.current
		// this.setState({
		// 	pagination: pager
		// })

		this.getData('/users/all', 'post', {
			...pagination,
			...filters,
			...sorter
		})
	}

	render() {
		return (<div>
			<Table columns={this.state.columns} dataSource={this.state.data} onChange={this.handleTableChange} rowKey={this.state.data.id} pagination={this.state.pagination}></Table>
		</div>);
	}
}

fetchTable.propTypes = {};

export default fetchTable
