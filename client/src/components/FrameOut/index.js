import React, {Component} from "react";
import {Layout, Menu, Breadcrumb, Row, Col, Dropdown, Avatar, Badge} from "antd";
import {UserOutlined, LaptopOutlined, NotificationOutlined, SettingFilled, DownOutlined} from "@ant-design/icons";
import {Link, Route, Redirect} from 'react-router-dom'
import {BlackMusic} from '@/pages'
import {TodoList} from '@/pages'
import HeaderUI from './header'
import SiderMenuUI from './sider'

const {SubMenu} = Menu;
const {Header, Content, Sider} = Layout;


class FrameOut extends Component {
  constructor(props) {
    super(props)
    this.handleMenuClick = this.handleMenuClick.bind(this)
    this.state = {};
  }

  handleMenuClick({item, key, keyPath, domEvent}){
    this.props.history.push(key);
  }

render() {
  return (
    <Layout style={{
      minHeight: "100%",
    }}>
      <HeaderUI></HeaderUI>
      <Layout>
        <SiderMenuUI></SiderMenuUI>
        {/* 不成文的规范：padding margin 建议是 8 的倍数*/}
        <Layout style={{
            padding: "24px",
        }}>
          <Content
            className="site-layout-background"
            style={{
                padding: 24,
                margin: 0,
                minHeight: 280,
            }}>
            <Route path='/music' component={BlackMusic}></Route>
            <Route path='/todo' component={TodoList}></Route>
          </Content>
        </Layout>
      </Layout>
    </Layout>
)
}
}

export default FrameOut;
