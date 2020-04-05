import {routes} from './routes';
import React, {PropTypes} from 'react';
import {HashRouter, Route, Switch, Redirect} from 'react-router-dom'
import App from '../App';
import NoFound from '../pages/404';

					// {routes.map(item => (
					// <Route key={item.path} path={item.path} exact={item.exact} component={item.component}></Route>
					// ))}
					// <Route component={App}></Route>
                    // <Route component={NoFound}></Route>

import Login from '../views/Login';

export default class IRouter extends React.Component {
	render() {
		return (<HashRouter>
				<Switch>
                    <Route path='/login' component={Login}></Route>

				</Switch>
		</HashRouter>)
	}
}
