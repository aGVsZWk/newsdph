import React, {PropTypes} from 'react';
import {
	Form,
	Input,
	Button,
	Checkbox,
	Radio,
	InputNumber,
	Select,
	Switch,
	DatePicker,
	Row,
	Col,
} from 'antd';

class basicForm extends React.Component {
	constructor(props) {
		super(props);
	}

	render() {
		return (<div>
			<Form labelCol={{
					span: 9
				}} wrapperCol={{
					span: 6
				}}>
				<Form.Item label="Username" name="username" rules={[{ required: true, message: '请输入用户名' }]}>
					<Input placeholder="请输入用户名"></Input>
				</Form.Item>

				<Form.Item label="Password" name="password">
					<Input.Password/>
				</Form.Item>
				<Form.Item wrapperCol={{
						span: 6,
						offset: 9
					}}>
					<Row>
						<Col span={14}>
							<Checkbox>Remember me</Checkbox>
						</Col>
						<Col span={8} offset={2}>
							<Checkbox>Fuck me</Checkbox>
						</Col>
					</Row>
				</Form.Item>


				<Form.Item label="性别" rules={[{required:true, message:"请选择性别"}]}>
				<Radio.Group></Radio.Group>
			</Form.Item>


				<Form.Item wrapperCol={{
						span: 2,
						offset: 9
					}}>
					<Button htmlType="submit">Submit</Button>
				</Form.Item>

			</Form>

		</div>);
	}
}

basicForm.propTypes = {};

export default basicForm
