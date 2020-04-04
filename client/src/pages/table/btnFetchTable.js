import React, {PropTypes} from 'react';
import {
	Table,
	Card,
	Divider,
	Button,
	Select,
	Input
} from 'antd';
import getUserList from '../../api';

const columns = [
	{
		title: "姓名",
		dataIndex: "name",
		key: "name"
	}, {
		title: "性别",
		dataIndex: "gender",
		key: "gender"
	}, {
		title: "年龄",
		dataIndex: "age",
		key: "age"
	}, {
		title: "地址",
		dataIndex: "address",
		key: "address"
	}
]

class btnFetchTable extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			columns,
			klass: [
				{
					title: "1班",
					id: "1"
				}, {
					title: "2班",
					id: "2"
				}, {
					title: "不限",
					id: ''
				}

			],
			classId: '',
			name: '',
			data: null,
			response: null,
			pagination: {}
			// pagination: {
			// 	current: 1,
			// 	pageSize: 2,
			// 	total: 5,
			// 	totalPages: 1
			// }
		}
	}

	handleSubmitClick = (event) => {
		getUserList({classId: this.state.classId, name: this.state.name}).then((response) => {
			console.log(response.data);
			this.setState({data: response.data, pagination: response.pagination})
		})
	}

	handleKlassChange = (value) => {
		this.setState({classId: value})
	}

	handleInputName = (event) => {
		this.setState({name: event.target.value})
	}

	handleTableChange = (pagination, filters, sorter) => {
		getUserList({
			classId: this.state.classId,
			name: this.state.name,
			...pagination
		}).then((response) => {
			this.setState({data: response.data, pagination: response.pagination})
		})
	}

	componentWillMount() {
		getUserList({}).then((response) => {
			console.log(response.data);
			this.setState({data: response.data, pagination: response.pagination})
		})
	}

	render() {
		return (<div>
			<Card title="表格按钮联动">
				<span style={{
						marginRight: "10px"
					}}>班级</span>
				<Select style={{
						marginRight: "50px",
						width: "10%"
					}} onChange={this.handleKlassChange}>
					{this.state.klass.map((item) => (<Select.Option value={item.id}>{item.title}</Select.Option>))}
				</Select>
				<span style={{
						marginRight: "10px"
					}}>名字</span>
				<Input style={{
						width: "10%"
					}} onChange={this.handleInputName}></Input>
				<Button onClick={this.handleSubmitClick} style={{
						float: "right"
					}}>查询</Button>
				<Divider></Divider>
				<Table columns={this.state.columns} dataSource={this.state.data} pagination={this.state.pagination} onChange={this.handleTableChange}></Table>
			</Card>
		</div>);
	}
}

btnFetchTable.propTypes = {};

export default btnFetchTable
