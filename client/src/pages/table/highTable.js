import React, {PropTypes} from 'react';
import {Table, Card, Button} from 'antd'

class highTable extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      sortedInfo: {},
      filteredInfo: {}
    }
  }

  componentDidMount() {

  }
  handleChange = (pagination, filters, sorter) => {
    console.log(1);
    console.log(sorter);
    console.log(filters);
    this.setState({
      filteredInfo: filters,
      sortedInfo: sorter
    });
  }
  setAgeSort = () => {
    this.setState({
      sortedInfo: {
        order: "descend",
        columnKey: "age"
      }
    });
  }
  clearFilters = () => {
    this.setState({
      filteredInfo: {}
    });
  }
  clearAll = () => {
    this.setState({
      filteredInfo: {},
      sortedInfo: {}
    });
  }


  render() {
    const columns = [
      {
        title:"Name",
        dataIndex: "name",
        key:"name",
        filters: [
          {
            text:"张",
            value:"张"
          },
          {
            text:"李",
            value:"李"
          },
          {
            text:"王",
            value:"王"
          }
        ],
        onFilter: (value, record) => record.name.indexOf(value) === 0
      },
      {
        title: "Gender",
        dataIndex:"gender",
        key: "gender",
        filters: [
          {
            text: "男",
            value:"男"
          },
          {
            text:"女",
            value:"女"
          }
        ],
        filteredValue: this.state.filteredInfo.gender || null,      // 受控属性
        onFilter: (value, record) => record.gender === value
      },
      {
        title:"Age",
        dataIndex:"age",
        defaultSortOrder: "descend",
        sorter: (a, b) => a.age - b.age,
        sortOrder: this.state.sortedInfo.columnKey === 'age' && this.state.sortedInfo.order,    // 受控属性
        ellipsis: true,   // 省略号
        key: "age"  // key 必须可少，与 columnKey 绑定
      },
      {
        title:"Address",
        dataIndex:"address",
        key:"address"
      }
  ]
    const dataSource = [
      {id:1, name:"张三", gender:"男", age:"18", address:"地球"},
      {id:2, name:"李四", gender:"男", age:"19", address:"地球"},
      {id:3, name:"王五", gender:"男", age:"18", address:"地球"},
      {id:4, name:"张三", gender:"男", age:"22", address:"地球"},
      {id:5, name:"张三", gender:"男", age:"18", address:"地球"},
      {id:6, name:"张三", gender:"男", age:"18", address:"地球"},
      {id:7, name:"张三", gender:"男", age:"18", address:"地球"},
      {id:8, name:"张三", gender:"男", age:"18", address:"地球"},
      {id:9, name:"张三", gender:"男", age:"18", address:"地球"},
      {id:10, name:"张三", gender:"男", age:"19", address:"地球"},
      {id:11, name:"张三", gender:"女", age:"18", address:"地球"}
    ]
    const onChange = (pagination, filters, sorter, extra) => {
      console.log(pagination)
      console.log(filters)
      console.log(sorter)
      console.log(extra)
    }

    return (<div>
      <Card title="table1">
        <Table columns={columns} dataSource={dataSource} onChange={onChange}></Table>
      </Card>
      <Card title="table2">
        <Button onClick={this.setAgeSort}>Sort age</Button>
        <Button onClick={this.clearFilters}>Clear filters</Button>
        <Button onClick={this.clearAll}>Clear filters and sorters</Button>
        <Table columns={columns} dataSource={dataSource} onChange={this.handleChange} pagination={{pageSize:3}} scroll={{y:70}}></Table>
      </Card>
    </div>);
  }
}

highTable.propTypes = {
};

export default highTable
