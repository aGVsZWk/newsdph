import React, {Component} from "react";

class DashBoard extends Component {
	constructor(props) {
		super(props);
		this.state = {
			a: 10,
			b: 20
		};
	}

	render() {
		return (
			<div>
				<h2>DashBoard界面</h2>
			</div>
		);
	}
}

export default DashBoard;
