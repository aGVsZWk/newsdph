import React, {Component} from "react";
import {Card, Button, Modal} from "antd";
import * as article from "@/api/article";

class Article extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  componentWillMount() {
    this.setState({isLoading: true});
    // Promise 存在 1：then 2：catch 3：finally
    article.getArticles()
    .then((value) => {
      console.log(value);
    })
    .catch((err) => {
      console.log(err);
    })
    .finally(() => {
      this.setState({isLoading: false});
    });
  }

  editHandler = (record) => {
    console.log(record);
    Modal.confirm({
      // title: '标题',
      content: `删除【${record.id}】？此操作不可逆，谨慎操作！`,
      onCancel: () => console.log("用户取消了"),
      onOk: () => console.log("用户确认了"),
    });
  };
  goHandler = (record) => {
    // push, goBack, listen
    this.props.history.push("/admin/dashboard/");
  };
  backHandler = (record) => {
    this.props.history.goBack();
  };

  render() {
    let record = {
      id: 1,
    };
    return (
      <Card title="文章列表" extra={<Button type="dashed"> 导出excel</Button>}>
        <p>Card content</p>
        <p>Card content</p>
        <p>Card content</p>
        <Button onClick={this.editHandler.bind(this, record)}>Modal</Button>
        <Button onClick={this.goHandler.bind(this, record)}>Go</Button>
        <Button onClick={this.backHandler.bind(this, record)}>Back</Button>
      </Card>
  );
}
}

export default Article;
