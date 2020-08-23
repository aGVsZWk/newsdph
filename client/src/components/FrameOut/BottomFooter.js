/**
* @Author: helei
* @Date:   2020-08-23
* @Email:  v_heleihe@tencent.com
* @Filename: FooterUIUI.js
 * @Last modified by:   helei
 * @Last modified time: 2020-08-23
*/
import React, { Component } from 'react'
import {Layout} from 'antd'
import MusicPlayer from '@/components/MusicPlayer'


const {Footer} = Layout

class BottomFooter extends Component {
	constructor(props) {
		super(props)
		this.state = {
		}
	}

	render() {
		return (
			<Footer>
				<MusicPlayer></MusicPlayer>
			</Footer>
		)
	}

}

export default BottomFooter
