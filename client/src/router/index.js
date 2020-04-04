import {routes} from './routes';
import React, {PropTypes} from 'react';
import {HashRouter, Route, Switch, Redirect} from 'react-router-dom'
import App from '../App';
import NoFound from '../pages/404';

export default class IRouter extends React.Component {
	render() {
		return (<HashRouter>
			<App>
				<Switch>
					{routes.map(item => (
					<Route key={item.path} path={item.path} exact={item.exact} component={item.component}></Route>
					))}
                    <Route component={NoFound}></Route>
				</Switch>
			</App>
		</HashRouter>)
	}
}
