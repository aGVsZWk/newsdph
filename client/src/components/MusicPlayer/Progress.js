/**
* @Author: helei
* @Date:   2020-08-23
* @Email:  v_heleihe@tencent.com
* @Filename: Progress.js
 * @Last modified by:   helei
 * @Last modified time: 2020-08-23
*/
import React from 'react';
import {Row, Col, Slider} from 'antd';
import PropTypes from 'prop-types';
import '@/css/footer.less'

export default class Player extends React.Component {
	constructor(props) {
		super(props)
	}

	tipFormatter(value) {
		let min = Math.floor(value / 60);
		let sec = Math.floor(value % 60);

		min = min > 9 ? min : `0${min}`;
		sec = sec > 9 ? sec : `0${sec}`;

		return `${min}:${sec}`;
	}
	
	render() {
		return (
			<Row justify="space-around" align="middle">
				<Col className="text-right" span={1}>
					<span>{this.tipFormatter(250)}</span>
				</Col>
				<Col span={22}>
					<Slider min={0} step={1} value={30} max={40} />
				</Col>
				<Col className='text-left' span={1}>
					<span>{this.tipFormatter(800)}</span>
				</Col>
			</Row>
		)
	}
}
