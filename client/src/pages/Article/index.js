import React, {Component} from 'react';
import {Card, Button} from 'antd';
import api from '@/api'

class Article extends Component {
	constructor(props) {
		super(props);
		this.state = {}
	}

	componentWillMount() {
		api.article.getArticles()
		.then((value) => {console.log(value)})
		.catch((err) => {console.log(err)})
	}
	render() {
		return (
			<Card title="文章列表" extra={<Button type="dashed">导出excel</Button>}>
				<p>Card content</p>
				<p>Card content</p>
				<p>Card content</p>
			</Card>

		)
	}

}

export default Article;
