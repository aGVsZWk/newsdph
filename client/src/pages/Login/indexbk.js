import React, {Component} from "react";
import {
  Form,
  Input,
  Buttom,
  Card,
  Button,
  Checkbox,
  Row,
  Col,
} from "antd";
import {UserOutlined, LockOutlined} from "@ant-design/icons";

import {withRouter} from "react-router-dom";

import "./index.less";

const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 16,
  },
};
const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 16,
  },
};

const onFinish = values => {
  console.log("Success:", values);
};

const onFinishFailed = errorInfo => {
  console.log("Failed:", errorInfo);
};

@withRouter
class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  
  render() {
    return (
      <Row>
        <Col span={8} offset={8}>
          <Card
            className="my-login-form"
            title="CMS 后台登录"
            extra={<Button type="danger" onClick={
              this.props.history.goBack
            }> 主页</Button>}>
            <Form
              name="normal_login"
              className="login-form"
              initialValues={{
                remember: true,
              }}
              onFinish={onFinish}>
              <Form.Item
                name="username"
                rules={[{
                  required: true,
                  message: "铁憨憨！请输入用户名！",
                },
                ]}>
                <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="用户名" />
              </Form.Item>
              <Form.Item
                name="password"
                rules={[{
                  required: true,
                  message: "铁憨憨！请输入密码!",
                },
                ]}>
                <Input prefix={<LockOutlined className="site-form-item-icon" />} type="password" placeholder="密码" />
              </Form.Item>
              <Form.Item>
                <Form.Item name="remember" valuePropName="checked" noStyle="noStyle">
                  <Checkbox>记住我</Checkbox>
                </Form.Item>
                
                <a style={{
                  float: "right",
                }} href="#">
                  忘记密码
                </a>
              </Form.Item>
              
              <Form.Item>
                <Button type="primary" htmlType="submit" className="login-form-button">
                  登录
                </Button>
              </Form.Item>
            </Form>
          
          </Card>
        </Col>
      
      </Row>
    
    );
  }
  
}

export default Login;
