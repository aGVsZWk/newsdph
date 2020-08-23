/**
* @Author: helei
* @Date:   2020-08-23
* @Email:  v_heleihe@tencent.com
* @Filename: Handle.js
 * @Last modified by:   helei
 * @Last modified time: 2020-08-24
*/
import React, { Component } from 'react'
import {Row, Col, Slider, Popover, Button} from 'antd';
import '@/css/footer.less'


class Handle extends Component {
	constructor(props) {
		super(props)
		this.state = {
		}
	}
	render() {
		return (
			<Row>
				<Col span={8}>
					<Popover
						content={
							<div className='h100'>
								<Slider vertical min={0} max={1} step={0.1} value={0.3} defaultValue={0.3} tipFormatter={null} />
							</div>
						}
					>
						<Button shape='circle'>
							<svg className="icon" aria-hidden="true">
								<use xlinkHref={`#icon-volume-min`} />
							</svg>
						</Button>
					</Popover>
				</Col>

				<Col span={8}>
					<Button shape='circle'>
						<svg className="icon" aria-hidden="true">
							<use xlinkHref={`#icon-shuffle`} />
						</svg>
					</Button>
				</Col>

				<Col span={8}>
					<Button shape='circle' >
						<svg className='icon' aria-hidden='true'>
							<use xlinkHref='#icon-music-list' />
						</svg>
					</Button>
				</Col>
			</Row>
		)
	}
}

export default Handle
