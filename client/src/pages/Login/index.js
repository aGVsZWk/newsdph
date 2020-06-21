import { Alert, Checkbox, Card, Button, Form, Input } from "antd";
import {AlipayCircleOutlined, TaobaoCircleOutlined, WeiboCircleOutlined, UserOutlined, LockOutlined} from "@ant-design/icons";
import React, {Component} from "react";
import "@/css/login.less";

class Login extends Component {
	constructor(props) {
		super(props);
	}

	onFinish = values => {
		console.log("Received values of form: ", values);
	};

	render() {
		return (
			<Card className="login-card" title="CMS 后台登录" extra={<Button type = "danger" > 主页</Button>}>
				<Form name="normal_login" initialValues={{
					remember: true
				}} onFinish={this.onFinish}>
					<Form.Item name="username" rules={[{
						required: true,
						message: "请输入您的用户名!"
					}
					]}>
						<Input prefix={<UserOutlined />} placeholder="Username"/>
					</Form.Item>
					<Form.Item name="password" rules={[{
						required: true,
						message: "请输入您的密码!"
					}
					]}>
						<Input prefix={<LockOutlined />} type="password" placeholder="Password"/>
					</Form.Item>
					<Form.Item>
						<Form.Item name="remember" valuePropName="checked" noStyle="noStyle">
							<Checkbox>记住我</Checkbox>
						</Form.Item>

						<a href="#" className={"forget-password"}>
							忘记密码
						</a>
					</Form.Item>
					<Form.Item>
						<Button type="primary" htmlType="submit">
							登录
						</Button>
						<Button type="primary" className={"register"}>
							注册
						</Button>
					</Form.Item>
				</Form>
			</Card>
		);
	}
}

export default Login;
