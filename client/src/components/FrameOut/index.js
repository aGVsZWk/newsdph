import React, {Component} from 'react';
import {Layout, Menu, Breadcrumb} from 'antd';
import {UserOutlined, LaptopOutlined, NotificationOutlined, SettingFilled} from '@ant-design/icons';

const {SubMenu} = Menu;
const {Header, Content, Sider} = Layout;

// 布局组件，公共的页面部分
class FrameOut extends Component {
	constructor(props) {
		super(props);
		this.state = {}
	}

	render() {
		return (
			<Layout style={{minHeight: '100%'}}>
				<Header className="header">
					<div className="logo"/>
					<h2 style={{color: "#fff"}}>CMS 管理系统</h2>
				</Header>
				<Layout>
					<Sider width={200} className="site-layout-background">
						<Menu
							mode="inline"
							defaultSelectedKeys={['1']}
							defaultOpenKeys={['sub1']}
							style={{
								height: '100%',
								borderRight: 0
							}}>
							<Menu.Item key="1"><SettingFilled />系统设置</Menu.Item>
							<Menu.Item key="2"><LaptopOutlined />文章管理</Menu.Item>
						</Menu>
					</Sider>
					{/* 不成文的规范：padding margin 建议是 8 的倍数*/}
					<Layout style={{
							padding: '24px'
						}}>

						<Content
							className="site-layout-background"
							style={{
								padding: 24,
								margin: 0,
								minHeight: 280,
							}}>
							Content
						</Content>
					</Layout>
				</Layout>
			</Layout>
		)
	}
}

export default FrameOut;
