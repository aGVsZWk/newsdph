import React from "react";
import PropTypes from "prop-types";
import {
  Layout,
  Menu,
  Breadcrumb,
  Divider,
  Row,
  Col,
  Tag,
  Table,
  Button,
  Anchor,
  DatePicker,
  Card,
  Select,
  Form,
  Input,
  InputNumber,
} from "antd";
import {UserOutlined, LaptopOutlined, NotificationOutlined} from "@ant-design/icons";
import api from "@/api";
// import '@/style/view-style/table.scss'

const columns = [
  {
    title: "姓名",
    dataIndex: "name",
    key: "name",
    render: text => <Button type='link'>{text}</Button>,
  }, {
    title: "性别",
    dataIndex: "sex",
    key: "sex",
  }, {
    title: "年龄",
    dataIndex: "age",
    key: "age",
  }, {
    title: "生日",
    dataIndex: "birthday",
    key: "birthday",
  }, {
    title: "邮箱",
    dataIndex: "email",
    key: "email",
  }, {
    title: "爱好",
    dataIndex: "hobby",
    key: "hobby",
  }, {
    title: "是否确认",
    dataIndex: "confirmed",
    key: "confirmed",
  }, {
    title: "是否激活",
    dataIndex: "active",
    key: "active",
  }, {
    title: "是否锁定",
    dataIndex: "locked",
    key: "locked",
  }, {
    title: "Tags",
    key: "tags",
    dataIndex: "tags",
    render: tags => (
      <span>
				{
          tags.map(tag => {
            let color = tag.length > 5 ? "geekblue" : "green";
            if (tag === "loser") {
              color = "volcano";
            }
            return (<Tag color={color} key={tag}>
              {tag.toUpperCase()}
            </Tag>);
          })
        }
			</span>
    ),
  }, {
    title: "操作",
    key: "operate",
    render: (text, record) => (
      <span>
				<Button type='link'>修改</Button>
				<Divider type='vertical' />
				<Button type='link'>删除</Button>
			</span>
    ),
  },
];

class Home extends React.Component {
  constructor(props) {
    super(props);
    // 定义初始化状态
    this.state = {
      formData: {},
      tableData: [],
    };
  }
  
  onFinish = (fieldsValues) => {
    const birthRangeValue = fieldsValues["birth"];
    const name = fieldsValues["name"];
    const sex = fieldsValues["sex"];
    const email = fieldsValues["email"];
    const age_lte = fieldsValues["age_lte"];
    const age_gte = fieldsValues["age_gte"];
    const formData = {
      "start_birth": birthRangeValue[0].format("YYYY-MM-DD"),
      "end_birth": birthRangeValue[1].format("YYYY-MM-DD"),
      "name": name,
      "sex": sex,
      "email": email,
      "age_lte": age_lte,
      "age_gte": age_gte,
    };
    this.setState({formData: formData});
    console.log(this.state.formData);
    api.user.getUserInfo(this.state.formData).then((res) => {
      console.log(res);
      if (res.state === 0) {
        console.log("成功");
      }
    }).catch((err) => {
      console.log(err);
    });
  };
  
  render() {
    const formItemLayout = {
      labelCol: {
        xs: {
          span: 24,
        },
        sm: {
          span: 8,
        },
      },
      wrapperCol: {
        xs: {
          span: 10,
        },
        sm: {
          span: 16,
        },
      },
    };
    
    return (<Layout>
      <Layout>
        <Layout.Sider width={200} className="site-layout-background">
          <Menu
            mode="inline"
            defaultSelectedKeys={["1"]}
            defaultOpenKeys={["sub1"]}
            style={{
              height: "100%",
              borderRight: 0,
            }}>
            <Menu.SubMenu key="sub1" title={<span> <UserOutlined />
              subnav 1 </span>}>
              <Menu.Item key="1">option1</Menu.Item>
              <Menu.Item key="2">option2</Menu.Item>
              <Menu.Item key="3">option3</Menu.Item>
              <Menu.Item key="4">option4</Menu.Item>
            </Menu.SubMenu>
            <Menu.SubMenu key="sub2" title={<span> <LaptopOutlined />
              subnav 2 </span>}>
              <Menu.Item key="5">option5</Menu.Item>
              <Menu.Item key="6">option6</Menu.Item>
              <Menu.Item key="7">option7</Menu.Item>
              <Menu.Item key="8">option8</Menu.Item>
            </Menu.SubMenu>
            <Menu.SubMenu key="sub3" title={<span> <NotificationOutlined />
              subnav 3 </span>}>
              <Menu.Item key="9">option9</Menu.Item>
              <Menu.Item key="10">option10</Menu.Item>
              <Menu.Item key="11">option11</Menu.Item>
              <Menu.Item key="12">option12</Menu.Item>
            </Menu.SubMenu>
          </Menu>
        </Layout.Sider>
        <Layout>
          <Breadcrumb style={{
            margin: "16px 0",
          }}>
            <Breadcrumb.Item>Home</Breadcrumb.Item>
            <Breadcrumb.Item>List</Breadcrumb.Item>
            <Breadcrumb.Item>用户信息</Breadcrumb.Item>
          </Breadcrumb>
          <Layout.Content style={{
            padding: 24,
            margin: 0,
            minHeight: 280,
          }}>
            
            <Form {...formItemLayout} layout="inline" onFinish={this.onFinish}>
              <Row gutter={24}>
                <Col span={8}>
                  <Form.Item label="姓名" name="name">
                    <Input placeholder="请输入姓名" style={{
                      width: 200,
                    }} />
                  </Form.Item>
                </Col>
                <Col span={8}>
                  <Form.Item label="性别" name="sex">
                    <Select placeholder="请选择性别" key="sex" style={{
                      width: 200,
                    }}>
                      <Select.Option key="man" value="man">男</Select.Option>
                      <Select.Option key="woman" value="woman">女</Select.Option>
                    </Select>
                  </Form.Item>
                </Col>
                <Col span={8}>
                  <Form.Item label="生日" name="birth">
                    <DatePicker.RangePicker
                      style={{
                        width: 200,
                      }}
                      rules={[{
                        type: "",
                      },
                      ]} />
                  </Form.Item>
                </Col>
                <Col span={8}>
                  <Form.Item label="年龄" style={{
                    marginBottom: 0,
                  }}>
                    <Row>
                      <Col span={8}>
                        <Form.Item style={{
                          display: "inline-block",
                        }} name="age_gte"><InputNumber placeholder="起始年龄" /></Form.Item>
                      </Col>
                      <Col span={8}>
                        <span
                          style={{
                            display: "inline-block",
                            lineHeight: "32px",
                            textAlign: "center",
                          }}>-</span>
                      </Col>
                      <Col span={8}>
                        <Form.Item style={{
                          display: "inline-block",
                        }} name="age_lte"><InputNumber placeholder="结束年龄" /></Form.Item>
                      </Col>
                    </Row>
                  </Form.Item>
                </Col>
                <Col span={8}>
                  <Form.Item label="邮箱" name="email">
                    <Input placeholder="请输入邮箱" />
                  </Form.Item>
                </Col>
                <Col span={8}>
                  <Form.Item label="手机" name="phone">
                    <Input placeholder="请输入手机号" />
                  </Form.Item>
                </Col>
                <Col span={24} style={{
                  textAlign: "right",
                }}>
                  <Button type="primary" htmlType="submit">搜索</Button>
                  <Button style={{margin: "0 8px"}}>清空</Button>
                </Col>
              </Row>
            
            </Form>
            
            <Table columns={columns} dataSource={this.data} />
          </Layout.Content>
        </Layout>
      </Layout>
    </Layout>);
  }
}

export default Home;
