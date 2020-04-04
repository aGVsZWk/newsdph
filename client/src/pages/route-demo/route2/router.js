import React from 'react'
import PropTypes from 'prop-types'
import {HashRouter as Router, Route, Link} from 'react-router-dom';
import Home from './Home';
import Main from '../route2/Main'
import About from '../route2/About'
import Topic from '../route2/Topic'

class IRouter extends React.Component {
	render() {
		return (<Router>
			<Home>
				<Route path="/home" render={() => (<Main>
						<Route path="/home/a" component={About}></Route>
					</Main>)}></Route>
				<Route path="/topic" component={Topic}></Route>
				<Route path="/about" component={About}></Route>
			</Home>
		</Router>)
	}
}

export default IRouter;
