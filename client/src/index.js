import React from "react";
import ReactDOM from "react-dom";
import App from "./App";

// antd 中文环境
import zhCN from "antd/es/locale/zh_CN";
import {ConfigProvider} from "antd";

// redux 操作
import { Provider } from 'react-redux'
import store from './store'

// 路由操作
import {BrowserRouter as Router, Route, Switch, Redirect} from "react-router-dom";

import {commonRoutes} from "@/routers";

import "@/css/index.less";
// import '@/css/BlackMusic.scss'

ReactDOM.render(
  <ConfigProvider locale={zhCN}>
    <Provider store={store}>
      <Router>
        <App />
      </Router>
    </Provider>
  </ConfigProvider>,

  document.getElementById(
    "root",
  ),
);
