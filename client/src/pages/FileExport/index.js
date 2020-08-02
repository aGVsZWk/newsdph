import React from 'react'
import PropTypes from 'prop-types'
import {Button} from 'antd';
import * as file from '@/api/file'

class FileExport extends React.Component {
	constructor(props) {
		super(props);
		this.state = {}
	}
	exportBtnClick = (e) => {
		this.setState({isLoading: true});
		file.ymarkInfoExport().then((value) => {
			console.log(value);
		}).catch((err) => {
			console.log(err);
		}).finally(() => {
			this.setState({isLoading: false});
		})
	}
	render() {
		return (
			<div>
				<Button onClick={this.exportBtnClick}>导出</Button>
			</div>
	)
}
}

export default FileExport;
