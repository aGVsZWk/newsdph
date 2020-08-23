import React, { Component } from 'react';
import {Link, Route, Redirect} from 'react-router-dom'
import {Layout, Row, Col, Dropdown, Avatar, Badge} from "antd";
import {UserOutlined, LaptopOutlined, NotificationOutlined, SettingFilled, DownOutlined} from "@ant-design/icons";
import '@/css/header.less'
import {LOGO_URL, AVATAR_URL} from '@/constants/urls'
import urls from '@/constants'

const {Header} = Layout;
const TopHeader = (props) => {
	return (
		<Header className='top'>
			<Row>
				<Col span={1}>
					<img height="40px" src="./logo.svg"></img>
				</Col>
				<Col span={7}>
					<h2><Link to="/" className='title'>艺术是灵魂之药</Link></h2>
				</Col>
				<Col span={3} offset={13}>
					<div>
						<Dropdown overlay={props.dropDown}>
							<Badge count={25}>
								<div className='avatar'>
									<Avatar src={AVATAR_URL} />
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

export default TopHeader
