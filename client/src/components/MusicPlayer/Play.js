/**
 * @Author: helei
 * @Date:   2020-08-23
 * @Email:  v_heleihe@tencent.com
 * @Filename: Player.js
 * @Last modified by:   helei
 * @Last modified time: 2020-08-23
 */
import React from 'react';
import {Row, Col, Button} from 'antd';
import PropTypes from 'prop-types';
import '@/css/footer.less'

export default class Play extends React.Component {
	constructor(props) {
		super(props)
	}

	render() {
		return (
			<Row>
				<Col span={8}>
					<Button shape='circle'>
						<svg className='icon' aria-hidden='true'>
							<use xlinkHref='#icon-previous' />
						</svg>
					</Button>
				</Col>

				<Col span={8}>
					<Button shape='circle'>
						<svg className='icon' aria-hidden='true'>
							<use xlinkHref={`#icon-stop`} />
						</svg>
					</Button>
				</Col>

				<Col span={8}>
					<Button shape='circle'>
						<svg className='icon' aria-hidden='true'>
							<use xlinkHref='#icon-next' />
						</svg>
					</Button>
				</Col>
			</Row>
		)
	}
}
