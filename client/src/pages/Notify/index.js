import React, {Component} from 'react';
import {Card, Button, List, Avatar} from 'antd'

const data = [
  {
    title: 'Ant Design Title 1',
  },
  {
    title: 'Ant Design Title 2',
  },
  {
    title: 'Ant Design Title 3',
  },
  {
    title: 'Ant Design Title 4',
  },
];

class Notify extends Component {
	constructor(props) {
		super(props);
		this.state = {}
	}
	render() {
		return (<div>
			<Card title="通知中心" extra={<Button> 全部標記為已讀</Button>}>

					<List
	     itemLayout="horizontal"
	     dataSource={data}
	     renderItem={item => (
	       <List.Item extra={<Button>標記為已讀</Button>}>
	         <List.Item.Meta
	           avatar={<Avatar src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png" />}
	           title={<a href="https://ant.design">{item.title}</a>}
	           description="Ant Design, a design language for background applications, is refined by Ant UED Team"
	         />
	       </List.Item>
	     )}
	   />,
			</Card>

		</div>);
	}

}

export default Notify;
