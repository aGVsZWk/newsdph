import React, {PropTypes} from 'react'

class FetchDemo extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			error: null,
			isLoaded: false,
			id: "999"
		};
	}

	fetchUrl() {
		// 1. fetch(url) ==> Promise(Response)
		fetch("https://api.apiopen.top/getAllUrl").then(function(response) {
			return response.json()
		}).then(function(myJson) {
			console.log(myJson);
		})
	}

	fetchWithRequest() {
		// 2. fetch(url, Request)
		const url = "http://www.liulongbin.top:3005/api/addproduct"
		const data = JSON.stringify({name: "ccc"})
		const requestConfig = {
			body: data,
			cache: 'no-cache',
			credentials: 'omit',
			headers: {
				"user-agent": "Mozilla/4.0 MDN Example",
				"content-type": "application/json"
			},
			method: 'post',
			mode: 'cors',
			redirect: 'follow',
			referrer: 'no-referrer'
		}
		fetch(url, requestConfig)
			.then(res => res.json())
			.then(data => {
				// this.setState({id: data.id})
				console.log(data)
			})
			.catch(error => console.log(error))
	}
	fetchWithParams(id) {
		const url = "http://www.liulongbin.top:3005/api/delproduct/" + id
		console.log(url);
		// fetch(url).then(res => res).then(response => console.log(response)).catch(error => console.log(error))
	}
	componentDidMount() {
		this.fetchWithRequest()
		console.log(this.state.id);
		this.fetchWithParams(this.state.id)
	}

	render() {
		const {error, isLoaded, items} = this.state;
		if (error) {
			return <div>Error: {error.message}</div>;
		} else if (!isLoaded) {
			return <div>Loading...</div>;
		} else {
			return (<ul>
				{
					items.map(item => (<li key={item.name}>
						{item.name}
						{item.price}
					</li>))
				}
			</ul>);
		}
	}
}

FetchDemo.propTypes = {};

export default FetchDemo
