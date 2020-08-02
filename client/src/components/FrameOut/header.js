import React, { Component } from 'react';
import {Link, Route, Redirect} from 'react-router-dom'
import {Layout, Row, Col, Dropdown, Avatar, Badge} from "antd";
import {UserOutlined, LaptopOutlined, NotificationOutlined, SettingFilled, DownOutlined} from "@ant-design/icons";
import HeaderAvatarDropUI from './headerAvatarDrop'

const {Header} = Layout;

const HeaderUI = (props) => {
	return (
		<Header>
			<Row>
				<Col span={8}>
					<h2><Link to="/" style={{ color: "#fff"}}>Jerenme</Link></h2>
				</Col>
				<Col span={3} offset={13}>
					<div style={{
						color: "#fff",
					}}>
						<Dropdown overlay={HeaderAvatarDropUI}>
							<Badge count={25}>
								<div style={{
									color: "#fff",
								}}>
									<Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />
									欢迎您 游客 !
									<DownOutlined />
								</div>
							</Badge>
						</Dropdown>
					</div>
				</Col>
			</Row>
		</Header>
	)
}

export default HeaderUI
