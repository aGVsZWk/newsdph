import React from 'react'
import {HashRouter, Route, Link, Switch} from 'react-router-dom';


export default class Home extends React.Component {
	render() {
		return (
			<HashRouter>
                <div>
					<ul>
						<li>
							<Link to='/main'>Home</Link>
						</li>
						<li>
							<Link to='/about'>About</Link>
						</li>
						<li>
							<Link to='/topic'>Topic</Link>
						</li>
                        <li>
                            <Link to='/xxx'>xxx</Link>
                        </li>
					</ul>
					{this.props.children}

				</div>
            </HashRouter>
		);
	}
}
