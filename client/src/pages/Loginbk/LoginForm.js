import React, {Component} from "react";
import {Tabs, Form} from "antd";
import LoginSubmit from "./LoginSubmit";
import LoginItem from "./LoginItem";
import LoginTab from "./LoginTab";
import styles from "./index.less";
import useMergeValue from "use-merge-value";
import LoginContext from "./LoginContext";


class LoginForm extends Component{
  constructor(props) {
    super (props);
    this.state = {
      tabs: [],
      active: null,
      type: ""
    }
  }
  setTabs = (id) => {
    this.setState([...this.state.tabs, id]);
  }
  setActive = () =>{
    this.setState({active: true});
  }
  setType = (activeKey) => {
    this.setState({type:this.props.activeKey});
  }

  render(){
    const {className} = this.props;
    const TabChildren = [];
    const otherChildren = [];

    React.Children.forEach(this.props.children, child => {
      if(!child){
        return;
      }
      if(child.type.typeName === "LoginTab"){
        TabChildren.push(child);
      } else{
        otherChildren.push(child);
      }
    });

    return (
      <div className={[className, styles.login].join(" ")}><Form form={this.props.form} onFinish={values => {
        if(this.props.onSubmit){
          this.props.onSubmit(values);
        }
      }}>{this.state.tabs.length ? (
        <React.Fragment><Tabs animated={false} className={styles.tabs} activeKey={this.state.type} onChange={activeKey => {
          this.setType(activeKey);
        }}>{TabChildren}</Tabs>{otherChildren}</React.Fragment>) : (this.props.children)}</Form>
      </div>
    );
  }
}





LoginForm.Tab = LoginTab;
LoginForm.Submit = LoginSubmit;
LoginForm.UserName = LoginItem.UserName;
LoginForm.Password = LoginItem.Password;
LoginForm.Mobile = LoginItem.Mobile;
LoginForm.Captcha = LoginItem.Captcha;
export default LoginForm;