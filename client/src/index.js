import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import './style/common.scss'
import 'antd/dist/antd.css'
// import App from './App';
import App from './pages/demo/Life';

import * as serviceWorker from './serviceWorker';
// import Router from './pages/route-demo/route2/router'
// import Router from './pages/route-demo/route3/router'
import IRouter from './router';

ReactDOM.render(<IRouter/>, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
