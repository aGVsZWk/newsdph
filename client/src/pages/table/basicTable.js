import React, {PropTypes, useState} from 'react';
import {Card, Table, Tag, Radio} from 'antd';
import reqwest from 'reqwest';
const {Column, ColumnGroup} = Table

const dataSource = [
	{
		id: '0',
		userName: 'Jack',
		sex: '1',
		state: '1',
		interest: '1'
	}, {
		id: '1',
		userName: 'Jack',
		sex: '1',
		state: '1',
		interest: '1'
	}
]
const columns = [
	{
		"title": 'id',
		"dataIndex": 'id'
	}, {
		"title": '用户名',
		"dataIndex": 'userName'
	}, {
		"title": '性别',
		"dataIndex": 'sex'
	}, {
		"title": 'state',
		"dataIndex": 'state'
	}
]
const data = [
	{
		key: '1',
		firstName: 'John',
		lastName: 'Brown',
		age: 32,
		address: 'New York No. 1 Lake Park',
		tags: ['nice', 'developer']
	}, {
		key: '2',
		firstName: 'Jim',
		lastName: 'Green',
		age: 42,
		address: 'London No. 1 Lake Park',
		tags: ['loser']
	}, {
		key: '3',
		firstName: 'Joe',
		lastName: 'Black',
		age: 32,
		address: 'Sidney No. 1 Lake Park',
		tags: ['cool', 'teacher']
	}
];

const columns2 = [
	{
		title: "姓名",
		dataIndex: "name",
		key: "name",
		render: (item) => (<a>{item}</a>)
	}, {
		title: "年龄",
		dataIndex: "age",
		key: "age"
	}, {
		title: "住址",
		dataIndex: "address",
		key: "address"
	}, {
		title: "Tags",
		key: 'tags',
		dataIndex: "tags",
		render: tags => (<span>{
				tags.map(tag => {
					let color = tag.length > 5
						? "geekblue"
						: "green"
					if (tag === "loser") {
						color = "volcano"
					}
					return (<Tag color={color} key={tag}>
						{tag.toUpperCase()}
					</Tag>)
				})
			}</span>)
	}, {
		title: "Action",
		key: "Action",
		dataIndex: "action",
		render: (text, record, index) => (<span>
			<a>Invite{record.name}</a>
			<a>Delete{text}aaa{index}</a>
		</span>)
	}
]
const dataSource2 = [
	{
		key: 1,
		name: "胡彦斌",
		age: "32",
		address: "西湖区湖底公园1号",
		tags: [
			'nice',
			'develoer',
			'c',
			'd',
			'loser',
			'winner'
		]
	}, {
		key: 2,
		name: "吴彦祖",
		age: 42,
		address: "西湖区湖底公园2号",
		tags: ['a', 'b', 'c', 'd', 'loser']
	}
]

const columns3 = [
	{
		title: 'Name',
		dataIndex: 'name',
		render: text => <a>{text}</a>
	}, {
		title: 'Age',
		dataIndex: 'age'
	}, {
		title: 'Address',
		dataIndex: 'address'
	}
];
const data3 = [
	{
		key: '1',
		name: 'John Brown',
		age: 32,
		address: 'New York No. 1 Lake Park'
	}, {
		key: '2',
		name: 'Jim Green',
		age: 42,
		address: 'London No. 1 Lake Park'
	}, {
		key: '3',
		name: 'Joe Black',
		age: 32,
		address: 'Sidney No. 1 Lake Park'
	}, {
		key: '4',
		name: 'Disabled User',
		age: 99,
		address: 'Sidney No. 1 Lake Park'
	}
];

const columns4 = [
	{
		title: 'Name',
		dataIndex: 'name',
		sorter: true,
		render: name => `${name.first} ${name.last}`,
		width: '20%'
	}, {
		title: 'Gender',
		dataIndex: 'gender',
		filters: [
			{
				text: 'Male',
				value: 'male'
			}, {
				text: 'Female',
				value: 'female'
			}
		],
		width: '20%'
	}, {
		title: 'Email',
		dataIndex: 'email'
	}
]

export default class BasicTable extends React.Component {
	constructor(props) {
		super(props)
		this.state = {
			dataSource: [],
			selectionType: "radio",
			columns: [],
			columns2: [],
			data: [],
			columns3: [],
			data3: [],
			selectedRowKeys: ['3'],
			columns4: [],
			data4: [],
			pagination4: {},
			loading4: false
		}
	}
	componentDidMount() {
		this.fetch()
		this.setState({
			dataSource,
			dataSource2,
			columns,
			columns2,
			data,
			columns3,
			data3,
			columns4
		});
	}

	setSelectionType = (e) => (this.setState({selectionType: e.target.value}))
	onSelectChange = (selectedRowKeys) => {
		console.log(selectedRowKeys);
		this.setState({selectedRowKeys})
	}

	handTableChange = (pagination, filters, sorter) => {
		const pager = {
			...this.state.pagination4
		}
		pager.current = pagination.current
		this.setState({pagination: pager})
		this.fetch({
			results: pagination.pageSize,
			page: pagination.current,
			sortField: sorter.field,
			sortOrder: sorter.order,
			...filters
		})
	}

	fetch = (params = {}) => {
		console.log("params", params)
		this.setState({loading4: true})
		reqwest({
			url: 'https://randomuser.me/api',
			method: 'get',
			data: {
				results: 10,
				...params
			},
			type: 'json'
		}).then(data => {
			console.log(data);
			const pagination4 = {
				...this.state.pagination4
			};
			// Read total count from server
			// pagination.total = data.totalCount;
			pagination4.total = 200;
			this.setState({loading: false, data4: data.results, pagination4});
		});
	};

	render() {
		const selections = [
			Table.SELECTION_ALL,
			Table.SELECTION_INVERT, {
				key: "odd",
				text: "Select Odd Row",
				onSelect: changeableRowKeys => {
					let newSelectedRowKeys = []
					newSelectedRowKeys = changeableRowKeys.filter((key, index) => {
						if (index % 2 !== 0) {
							return false;
						}
						return true
					})
					this.setState({selectedRowKeys: newSelectedRowKeys})
				}
			}
		]

		return (<div>
			<Card title="基础表格">
				<Table columns={this.state.columns} dataSource={this.state.dataSource}></Table>
				<Table columns={this.state.columns2} dataSource={this.state.dataSource2}></Table>
			</Card>
			<Card title="columns">
				<Table dataSource={this.state.data}>
					<ColumnGroup title="Name">
						<Column title="First Name" dataIndex="firstName"></Column>
						<Column title="Last Name" dataIndex="lastName"></Column>
					</ColumnGroup>
					<Column title="Age" dataIndex="age" key="age"/>
					<Column title="Address" dataIndex="address" key="address"/>
					<Column title="Tags" dataIndex="tags" key="tags" render={tags => (<span>
							{
								tags.map(tag => (<Tag color="blue" key={tag}>
									{tag}
								</Tag>))
							}
						</span>)}/>
					<Column title="Action" key="action" render={(text, record) => (<span>
							<a style={{
									marginRight: 16
								}}>Invite {record.lastName}</a>
							<a>Delete</a>
						</span>)}/>
				</Table>
			</Card>
			<Card title="rowSelection">
				<Radio.Group onChange={this.setSelectionType} value={this.state.selectionType}>
					<Radio.Button style={{
							display: "block",
							height: "30px",
							lineHight: "30px"
						}} value="checkbox">checkbox</Radio.Button>
					<Radio.Button style={{
							display: "block",
							height: "30px",
							lineHight: "30px"
						}} value="checkbox" disabled="disabled">checkbox</Radio.Button>
					<Radio style={{
							display: "block",
							height: "30px",
							lineHight: "30px"
						}} value="radio">radio</Radio>
				</Radio.Group>
				<Radio.Group disabled="disabled" value={this.state.selectionType}>
					<Radio.Button value="checkbox">checkbox</Radio.Button>
					<Radio value="radio">radio</Radio>
				</Radio.Group>
				<span>{this.state.selectedRowKeys.length}
					item has been selected</span>
				<Table dataSource={this.state.data3} columns={this.state.columns3} rowSelection={{
						type: this.state.selectionType,
						selectedRowKeys: this.state.selectedRowKeys,
						onChange: this.onSelectChange,
						selections: selections
					}}></Table>
			</Card>
			<Card title="fetch">
				<Table onChange={this.handTableChange} columns={this.state.columns4} dataSource={this.state.data4} rowKey={record => record.login.uuid} pagination={this.state.pagination4} loading={this.state.loading}></Table>
			</Card>
		</div>)
	}
}

BasicTable.propTypes = {};
