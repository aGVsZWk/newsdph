import React, {Component} from 'react';
import logo from './logo.svg';
import {Button, Pagination,} from 'antd'
import {privateRoutes} from './routers';
import {Route, Switch, Redirect} from 'react-router-dom';
import FrameOut from '@/components/FrameOut'

class App extends Component {
	render() {
		// 显示私有的路由  /admin/dashboard 二级路由 (rbac授权)
		// <Switch>
		// 	{
		// 		privateRoutes.map((item, index) => {
		// 			return (
		// 				<Route
		// 					key={item.pathname}
		// 					path={item.pathname}
		// 					render={(rootProps) => {
		// 						return <item.component {...rootProps}/>
		// 					}} />
		// 			)
		// 		})
		// 	}
		// 	{/* 1. 配置默认的 /admin 2. not found */}
		// 	<Redirect from='/admin' to={privateRoutes[0].pathname} exact="exact"></Redirect>
		// 	<Redirect to='/404'></Redirect>
		// </Switch>
		return (
			<FrameOut></FrameOut>

		)
	}
}
export default App;
