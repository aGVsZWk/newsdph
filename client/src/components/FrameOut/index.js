import React, {Component} from 'react';
import {Layout, Menu, Breadcrumb} from 'antd';
import {UserOutlined, LaptopOutlined, NotificationOutlined, SettingFilled} from '@ant-design/icons';
import {withRouter} from 'react-router-dom';
import {privateRoutes} from '@/routers';

const {SubMenu} = Menu;
const {Header, Content, Sider} = Layout;

// 左侧菜单只显示一级
const topMenus = privateRoutes.filter((item) => {
	return item.isTop === true
})

// 布局组件，公共的页面部分
/*高阶组件中的withRouter, 作用是将一个组件包裹进Route里面, 然后react-router的三个对象history, location, match就会被放进这个组件的props属性中. */

@withRouter
class FrameOut extends Component {
	constructor(props) {
		super(props);
		this.state = {}
	}

	handleMenuClick = ({ item, key, keyPath, domEvent }) => {
		this.props.history.push(key)
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
							defaultSelectedKeys={topMenus[0].pathname}
							defaultOpenKeys={['sub1']}
							style={{
								height: '100%',
								borderRight: 0
							}}>
						{
							topMenus.map((item) => {
								return (
									<Menu.Item key={item.pathname} onClick={this.handleMenuClick}>{item.title}</Menu.Item >
								)
							})
						}
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
							{this.props.children}
						</Content>
					</Layout>
				</Layout>
			</Layout>
		)
	}
}

export default FrameOut;
