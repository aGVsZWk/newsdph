import React, {Component} from "react";
import {Route, Switch, Redirect} from "react-router-dom";
import FrameOut from "@/components/FrameOut";

class App extends Component {

  constructor(props) {
    super(props)
  }

  render() {
    // 显示私有的路由  /admin/dashboard 二级路由 (rbac授权)
    return (
      <FrameOut>
        
      </FrameOut>
      );
    }
  }

  export default App;
