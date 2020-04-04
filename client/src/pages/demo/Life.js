import React, {PropTypes} from 'react';
import Child from './Child';
import {Button, Input} from 'antd';


class Life extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count : 0
    }
  }


  handleAdd = () => {
    this.setState({
      count: this.state.count + 1
    })
  }

  render() {
    let style = {
      padding: 50
    }
    return (
      <div style={style}>
      	<p>React生命周期</p>
      	<Button onClick={this.handleAdd}>点我+1</Button>
        <Input></Input>
      	<p>{this.state.count}</p>
        <Child name="Jack"></Child>
      </div>
    );
  }
}

Life.propTypes = {
};

export default Life
