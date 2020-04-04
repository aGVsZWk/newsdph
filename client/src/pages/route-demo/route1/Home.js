import React from 'react'
import {HashRouter, Route, Link, Switch} from 'react-router-dom';

import Main from './Main';
import Topic from './Topic';
import About from './About';

export default class Home extends React.Component {
	render() {
		return (
			<HashRouter>
                <div>
					<ul>
						<li>
							<Link to='/'>Home</Link>
						</li>
						<li>
							<Link to='/about'>About</Link>
						</li>
						<li>
							<Link to='/topic'>Topic</Link>
						</li>
					</ul>
					<hr></hr>
					{/*
					<Route path="/" component={Main}></Route>  // 不加 exact 则会继续向下匹配，多个路由同时加载
					<Route path="/" exact component={Main}></Route>
					<Route path="/topic" component={Topic}></Route>
					<Route path="/about" component={About}></Route>
					*/}
					{/*
						Swtich只加载第一次匹配到的路由，只加载一个路由
					<Switch>
						<Route path="/" component={Main}></Route>
						<Route path="/topic" component={Topic}></Route>
						<Route path="/about" component={About}></Route>
					</Switch>
					*/}
					<Route path="/" exact component={Main}></Route>
					<Route path="/topic" component={Topic}></Route>
					<Route path="/about" component={About}></Route>
				</div>
            </HashRouter>
		);
	}
}
