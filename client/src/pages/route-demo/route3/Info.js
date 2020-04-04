import React from 'react'
import {HashRouter, Route, Link} from 'react-router-dom';

export default class About extends React.Component {
	render() {
		return (
			<HashRouter>
                <div>
					测试动态路由
					<br></br>
					{this.props.match.params.mainId}
				</div>
            </HashRouter>
		);
	}
}
