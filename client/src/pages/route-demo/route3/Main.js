import React from 'react'
import {HashRouter, Route, Link} from 'react-router-dom';

export default class Main extends React.Component {
	render() {
		return (<HashRouter>
			<div>
				This is mian page

				<hr></hr>
				<Link to="/main/test-id">嵌套路由1</Link>
				<Link to="/main/456">嵌套路由2</Link>
				<hr></hr>

				{this.props.children}
			</div>
		</HashRouter>);
	}
}
