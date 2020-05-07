import {Tabs, Form} from "antd";
import React, {useState} from "react";
import useMergeValue from "use-merge-value";
import LoginContext from "./LoginContext";
import LoginItem from "./LoginItem";
import LoginSubmit from "./LoginSubmit";
import LoginTab from "./LoginTab";
import styles from "./index.less";

const LoginForm = props => {
  const {className} = props;
  const [tabs, setTabs] = useState([]);
  const [active, setActive] = useState();
  const TabChildren = [];
  const otherChildren = [];
  const [type, setType] = useMergeValue("", {
    value: props.activeKey,
    onChange: props.onTabChange,
  });

  React.Children.forEach(props.children, child => {
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
    <LoginContext.Provider value={{
      tabUtil: {
        addTab: id => {
          setTabs([...tabs, id]);
        }, removeTab: id => {
          setTabs(tabs.filter(currentId => currentId !== id));
        },
      }, updateActive: activeItem => {
        if(active[type]){
          active[type].push(activeItem);
        } else{
          active[type] = [activeItem];
        }
        setActive(active);
      },
    }}>
      <div className={[className, styles.login].join(" ")}><Form form={props.form} onFinish={values => {
        if(props.onSubmit){
          props.onSubmit(values);
        }
      }}>{tabs.length ? (
        <React.Fragment><Tabs animated={false} className={styles.tabs} activeKey={type} onChange={activeKey => {
          setType(activeKey);
        }}>{TabChildren}</Tabs>{otherChildren}</React.Fragment>) : (props.children)}</Form></div>
    </LoginContext.Provider>);
};
LoginForm.Tab = LoginTab;
LoginForm.Submit = LoginSubmit;
LoginForm.UserName = LoginItem.UserName;
LoginForm.Password = LoginItem.Password;
LoginForm.Mobile = LoginItem.Mobile;
LoginForm.Captcha = LoginItem.Captcha;
export default LoginForm;