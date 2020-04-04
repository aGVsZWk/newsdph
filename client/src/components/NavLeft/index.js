import React, {PropTypes} from 'react';
import menuConfig from '../../config/menuConfig';
import {Menu, Button, Icon, Switch} from 'antd';
import {NavLink} from 'react-router-dom';
import {ContainerOutlined, SmileOutlined, MenuUnfoldOutlined, MenuFoldOutlined} from '@ant-design/icons'
import './index.scss'

const {SubMenu, Item, ItemGroup} = Menu;

class NavLeft extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			collapsed: false,
			theme: "dark",
			mode: "inline",
            openKeys: []
		}
	}
	rootSubMenuKeys = menuConfig.filter((item) => (item.key && item.children)).map((item) =>(item.key))

	componentWillMount() {
		const menuTreeNode = this.renderMenu(menuConfig)
		this.setState({menuTreeNode});
	}

	onOpenChange = openKeys => {
		const latestOpenKey = openKeys.find( key=> this.state.openKeys.indexOf(key) === -1)
		if (this.rootSubMenuKeys.indexOf(latestOpenKey)===-1) {
			this.setState({
				openKeys
			});
		} else {
			this.setState({
				openKeys: latestOpenKey? [latestOpenKey]: []
			});
		}
	}

	changeCollapsed = () => (this.setState({
		collapsed: !this.state.collapsed
	}))

	changeTheme = (value) => (this.setState({
		theme: value
			? "light"
			: "dark"
	}))

	changeLayoutMode = (value) => {
		this.setState({
			mode: value
				? "vertical"
				: "inline"
		});
	}

	renderMenu = (data) => {
		return data.map((item) => {
			if (item.children) {
				return (
				// <ItemGroup title={item.title} key={item.key}>
				// 	{this.renderMenu(item.children)}
				// </ItemGroup>
				<SubMenu key={item.key} title={<span> < SmileOutlined />< span > {
						item.title
					}
					</span>
			</span>}>
					{this.renderMenu(item.children)}
				</SubMenu>)
			}
			return <Item title={item.title} key={item.key} disabled={item.disabled}><ContainerOutlined/>
                <NavLink to={item.key}>{item.title}</NavLink>
			</Item>;
		})
	}
	// {this.state.collapsed ? MenuFoldOutlined: MenuUnfoldOutlined}
	render() {
		return (<div>
			<div className="logo">
				<img src="/assets/logo-ant.svg" alt=""/>
				<h1>BikeSharing</h1>
			</div>
			<Button onClick={this.changeCollapsed} type="primary">{
					this.state.collapsed
						? <MenuFoldOutlined/>
						: <MenuUnfoldOutlined/>
				}
			</Button>
			<Switch checkedChildren={"light"} unCheckedChildren={"dark"} style={{
					marginLeft: "1vh"
				}} onChange={this.changeTheme} checked={this.state.theme === "light"}/>
			<Switch checkedChildren={"inline"} unCheckedChildren={"vertical"} style={{
					marginLeft: "1vh"
				}} onChange={this.changeLayoutMode} checked={this.state.mode === "vertical"}/>

			<Menu theme={this.state.theme} mode={this.state.mode} defaultSelectedKeys={['/home']} defaultOpenKeys={['/form']} inlineCollapsed={this.state.collapsed} onOpenChange={this.onOpenChange} openKeys={this.state.openKeys}>
				{this.renderMenu(menuConfig)}
			</Menu>

		</div>)
	}
}

export default NavLeft
