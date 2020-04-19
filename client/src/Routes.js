import React from 'react';
import {HashRouter, Route, Switch, Redirect} from 'react-router-dom';
import {Provider} from 'react-redux';
import {combineReducers} from 'redux';

import App from './pages/App';
import Home from './pages/Home';
import About from './pages/About';
import NotFound from './pages/NotFound';

// import Counter from './pages/CounterPage'
// import Home from './pages/Home'
// import About from './pages/About'
// import NotFound from './pages/NotFound'

import store from './Store.js';

const createElement = (Component, props) => {
	return (<Provider store={store}>
		<Component {...props}/>
	</Provider>);
};


const Routes = () => (<HashRouter createElement={createElement}>
	<Switch>
		<Route path="/" exact render={() => <Redirect to='/home'/>}/>
		<Switch>
			<Route path="/home" component={Home}/>
			<Route path="/about" component={About}/>
			<Route path="/404" component={NotFound}/>
		</Switch>
	</Switch>

</HashRouter>);

export default Routes;
