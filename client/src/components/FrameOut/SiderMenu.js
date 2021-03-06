import React, {Component} from "react";
import {Layout, Menu, Breadcrumb, Row, Col, Dropdown, Avatar, Badge} from "antd";
import {UserOutlined, LaptopOutlined, NotificationOutlined, SettingFilled, DownOutlined} from "@ant-design/icons";
import {Link, Route, Redirect} from 'react-router-dom'
import {BlackMusic} from '@/pages'

const {SubMenu} = Menu;
const {Header, Content, Sider} = Layout;


const SiderMenu = (props) => {
	return (
			<Menu
				mode="inline"
				defaultSelectedKeys={["site_menu0"]}
				style={{
					height: "100%",
					borderRight: 0,
				}}>
				<Menu.Item key='site_menu0'>
					<Link to="/todo">TODO</Link>
				</Menu.Item>
				<Menu.Item key='site_menu1'>
					<Link to="/music">黑云电台</Link>
				</Menu.Item>
				<Menu.Item disabled key={'site_menu2'}>OONE频道</Menu.Item>
				<Menu.Item disabled key={'site_menu3'}>Jere 足球录像</Menu.Item>
				<Menu.Item disabled key={'site_menu4'}>Jere 西甲风云</Menu.Item>
				<Menu.Item disabled key={'site_menu5'}>Jere 欧冠之夜</Menu.Item>
				<Menu.Item disabled key={'site_menu6'}>Jere Die</Menu.Item>
				<Menu.Item disabled key={'site_menu7'}>Jere Live</Menu.Item>
				<Menu.Item disabled key={'site_menu8'}>垃圾 Rock</Menu.Item>
				<Menu.Item disabled key={'site_menu9'}>金属 Rock</Menu.Item>
				<Menu.Item disabled key={'site_menu10'}>Jere 交响曲</Menu.Item>
				<Menu.Item disabled key={'site_menu11'}>Jere 超清壁纸</Menu.Item>
			</Menu>
	)
}


export default SiderMenu
