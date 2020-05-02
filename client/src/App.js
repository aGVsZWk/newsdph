import React, {Component} from "react";
import logo from "./logo.svg";
import {Button, Pagination} from "antd";
import {privateRoutes} from "./routers";
import {Route, Switch, Redirect} from "react-router-dom";
import FrameOut from "@/components/FrameOut";

class App extends Component {
  
  constructor(props) {
    super(props);
    // console.log('app', this.props);
    // 只要地址栏的hash变化，listen就会被触发，参数locationd代表当前url地址
    this.props.history.listen((location) => {
      console.log("location", location);
      var pathname = location.pathname;
      var findOne = privateRoutes.find((item) => {
        return item.pathname === pathname;
      });
      console.log("findOne", findOne);
      window.document.title = findOne && findOne.title;
    });
  }
  
  render() {
    // 显示私有的路由  /admin/dashboard 二级路由 (rbac授权)
    return (
      <FrameOut>
        <Switch>
          {
            privateRoutes.map((item, index) => {
              return (
                <Route
                  key={item.pathname}
                  path={item.pathname}
                  render={(rootProps) => {
                    return <item.component {...rootProps} />;
                  }} />
              );
            })
          }
          {/* 1. 配置默认的 /admin 2. not found */}
          <Redirect from='/admin' to={privateRoutes[0].pathname} exact="exact"></Redirect>
          <Redirect to='/404'></Redirect>
        </Switch>
      </FrameOut>
    
    );
  }
}

export default App;
