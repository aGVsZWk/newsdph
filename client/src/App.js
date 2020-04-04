import logo from './logo.svg';
import './App.less';
// import './App.css';
import React, {PropTypes} from 'react';
import NavLeft from './components/NavLeft'
import Sider from './components/demos/menuClickAutoClose';
import Header from './components/Header'
import Footer from './components/Footer'
import {Row, Col} from 'antd';

export default class App extends React.Component {
	render() {
		return (<div>
			(<Row className="container">
				<Col span="5" className="nav-left">
					<NavLeft/>
					<Sider></Sider>
				</Col>
				<Col span="19" className="main">
					<Header></Header>
					<Row className="content">
						<Col span={24}>
							{this.props.children}
						</Col>
					</Row>
					<Footer></Footer>
				</Col>
			</Row>)
		</div>);
	}
}

App.propTypes = {};
