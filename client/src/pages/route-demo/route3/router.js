import React from 'react'
import PropTypes from 'prop-types'
import {HashRouter as Router, Route, Link, Switch} from 'react-router-dom';
import Home from './Home';
import Main from './Main'
import Topic from './Topic'
import Info from './Info'
import About from './About'
import NoMatch from './NoMatch';

class IRouter extends React.Component {
	render() {
		return (<Router>
			<Home>
				<Switch>
				<Route path="/main" render={() => (<Main>
						<Route path="/main/:mainId" component={Info}></Route>
					</Main>)}></Route>
				<Route path="/topic" component={Topic}></Route>
				<Route path="/about" component={About}></Route>
				<Route component={NoMatch}></Route>
				</Switch>
			</Home>
		</Router>)
	}
}

export default IRouter;
