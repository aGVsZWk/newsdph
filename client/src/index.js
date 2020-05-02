import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import * as serviceWorker from "./serviceWorker";

// antd 中文环境
import zhCN from "antd/es/locale/zh_CN";
import {ConfigProvider} from "antd";

// 路由操作
import {HashRouter as Router, Route, Switch, Redirect} from "react-router-dom";

import {commonRoutes} from "@/routers";

import "@/css/index.less";

ReactDOM.render(
  <ConfigProvider locale={zhCN}>
    {/* Route 路由映射表 1. 公共的 2. 私有的 */}
    <Router>
      <Switch>
        {/* 登录之后才能访问, 授权检测 */}
        {
          <Route path="/admin" render={(rootProps) => {
            return <App {...rootProps} />;
          }}></Route>
        }
        {/* 公共的 */}
        {
          commonRoutes.map((item, index) => {
            return (<Route key={item.pathname} path={item.pathname} component={item.component}></Route>);
          })
        }
        {/* not found 和 默认的 / */}
        <Redirect from="/" to="/admin" exact></Redirect>
        <Redirect to="/404"></Redirect>
      </Switch>
    </Router>
  
  </ConfigProvider>,
  
  document.getElementById(
    "root",
  ),
);

// If you want your app to work offline and load faster, you can change unregister() to register() below. Note this
// comes with some pitfalls. Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
