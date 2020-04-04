import React, {PropTypes} from 'react';

import {
	Row,
	Col,
	Badge,
	Avatar,
	Dropdown,
	Menu
} from 'antd'
import {GithubOutlined, BellOutlined, EditOutlined, SettingOutlined, LogoutOutlined} from '@ant-design/icons'
import './index.css'

class Header extends React.Component {
	constructor(props) {
		super(props);
	}
	menu = (<Menu>
		<Menu.ItemGroup title='用户设置'>
			<Menu.Divider/>
			<Menu.Item>
				<span>
					<EditOutlined/>
					个人设置
				</span>
			</Menu.Item>
			<Menu.Item>
				<span>
					<SettingOutlined theme='filled'/>
					系统设置
				</span>
			</Menu.Item>
		</Menu.ItemGroup>
		<Menu.Divider/>
		<Menu.Item>
			<span>
				<LogoutOutlined/>
				退出登录
			</span>
		</Menu.Item>
	</Menu>)
	render() {
		return (<div>
			<Row className="header">
				<Col span={4} className="header-left">
					<div className="mr">BikeSharing
					</div>
				</Col>
				<Col span={20} className="header-right">
					<div className="mr"><GithubOutlined/></div>

					<div className="mr"><BellOutlined/></div>
					<div className="mr">
						<Dropdown overlay={this.menu}>
							<Avatar icon="user" src="./avatar.jpg" alt="avatar" style={{
									cursor: "pointer"
								}}></Avatar>
						</Dropdown>

					</div>
				</Col>

			</Row>

		</div>);
	}
}

Header.propTypes = {};

export default Header
