import React, {Component} from "react";
import {Layout, Menu, Breadcrumb, Row, Col, Dropdown, Avatar, Badge} from "antd";
import {UserOutlined, LaptopOutlined, NotificationOutlined, SettingFilled, DownOutlined} from "@ant-design/icons";
import {Link, Route, Redirect} from 'react-router-dom'
import {BlackMusic} from '@/pages'
import HeaderUI from './header'

const {SubMenu} = Menu;
const {Header, Content, Sider} = Layout;


const HeaderAvatarDropUI = (props) => (
    <Menu>
      <Menu.Item key="/admin/notify">
        <div>
          <Badge dot>通知中心</Badge>
        </div>
      </Menu.Item>
      <Menu.Item key="/admin/setting">
        <div>
          個人設置
        </div>
      </Menu.Item>
      <Menu.Item key="/login">
        <div>
          退出
        </div>
      </Menu.Item>
    </Menu>
);

export default HeaderAvatarDropUI
