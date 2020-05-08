import React, {createContext, Component, useState} from "react";
import {AlipayCircleOutlined, TaobaoCircleOutlined, WeiboCircleOutlined} from "@ant-design/icons";
import {Alert, Checkbox, Card, Button} from "antd";
import LoginForm from "./LoginForm";
import styles from "./style.less";
import {Link} from "react-router-dom";

const {Tab, UserName, Password, Mobile, Captcha, Submit} = LoginForm;

const LoginMessage = ({content}) => (
  <Alert style={{
    marginBottom: 24,
  }} message={content} type="error" showIcon="showIcon" />
);

const Login = props => {
  const {userAndlogin = {}, submitting} = props;
  const {status, type: loginType} = userAndlogin;
  const [autoLogin, setAutoLogin] = useState(true);
  const [type, setType] = useState("account");

  const handleSubmit = values => {
    console.log(values);
  };
  // this.props.history.goBack


  return (
    <div className={styles.main}>
      <Card className="login-card" title="CMS 后台登录" extra={<Button type="danger">主页</Button>}>
        <LoginForm onTabChange={setType} activeKey={type} onSubmit={handleSubmit} className="login-form">
          <Tab key="account" tab="账户密码登录">
            {status === "error" && loginType === "account" && !submitting && (
              <LoginMessage content="账户或密码错误（admin/ant.design）" />)}
            <UserName name="userName" placeholder="用户名" rules={[{required: true, message: "请输入用户名!"}]} />
            <Password name="password" placeholder="密码" rules={[{required: true, message: "请输入密码！"}]} />
          </Tab>
          <Tab key="mobile" tab="手机号登录">
            {status === "error" && loginType === "mobile" && !submitting && (<LoginMessage content="验证码错误" />)}
            <Mobile name="mobile" placeholder="手机号"
                    rules={[{required: true, message: "请输入手机号！"}, {pattern: /^1\d{10}$/, message: "手机号格式错误！"}]} />
            <Captcha name="captcha" placeholder="验证码" countDown={120} getCaptchaButtonText="" getCaptchaSecondText="秒"
                     rules={[{required: true, message: "请输入验证码！"}]} />
          </Tab>
          <div>
            <Checkbox checked={autoLogin} onChange={e => setAutoLogin(e.target.checked)}>自动登录</Checkbox>
            <a style={{float: "right"}}>忘记密码</a>
          </div>
          <Submit loading={submitting}>登录</Submit>
          <div className={styles.other}>
            其他登录方式
            <AlipayCircleOutlined className={styles.icon} />
            <TaobaoCircleOutlined className={styles.icon} />
            <WeiboCircleOutlined className={styles.icon} />
            <Link className={styles.register} to="/user/register">注册账户</Link></div>
        </LoginForm>
      </Card>
    </div>
  );
};
export default Login;
