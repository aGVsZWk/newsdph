import React from 'react'
import {HashRouter, Route, Link} from 'react-router-dom';

export default class Main extends React.Component {
	render() {
		return (<HashRouter>
			<div>
				This is mian page

				<hr></hr>
				<Link to="/home/a">a</Link>
				<hr></hr>

				{this.props.children}
			</div>
		</HashRouter>);
	}
}
