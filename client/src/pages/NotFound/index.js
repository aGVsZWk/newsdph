import React, {Component} from "react";

class NotFound extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  
  render() {
    return (<div>
      <h2>NotFound界面</h2>
      <img src="/images/404.png" alt="" /></div>);
  }
  
}

export default NotFound;
