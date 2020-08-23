/**
 * @Author: helei
 * @Date:   2020-08-23
 * @Email:  v_heleihe@tencent.com
 * @Filename: FooterUIUI.js
 * @Last modified by:   helei
 * @Last modified time: 2020-08-23
 */
import React, { Component } from 'react'
import {Row, Col, Slider} from 'antd'
import ReactPlayer from 'react-player';
import {VIDEO_URL, AUDIO_URL} from '@/constants/urls'
import Play from '@/components/MusicPlayer/Play'
import Handle from '@/components/MusicPlayer/Handle'
import Progress from '@/components/MusicPlayer/Progress'
import '@/css/footer.less'

class MusicPlayer extends Component {
	constructor(props) {
		super(props)
		this.state = {
		}
	}


	render() {
		return (
			<div style={{height:'100%', width:'100%'}}>
				<ReactPlayer playing url={AUDIO_URL} />
				<Row justify="space-around" align="middle">
					<Col xxl={2} xl={3} lg={3} md={4} sm={6} xm={7}>
						<Play></Play>
					</Col>

					<Col xxl={20} xl={18} lg={18} md={16} sm={12} xm={10}>
						<Progress></Progress>
					</Col>
					<Col xxl={2} xl={3} lg={3} md={4} sm={6} xm={7}>
						<Handle></Handle>
					</Col>
				</Row>
			</div>
		)
	}

}

export default MusicPlayer
