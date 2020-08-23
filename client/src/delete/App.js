// import React, {Component} from "react";
// import {Route, Switch, Redirect} from "react-router-dom";
// import FrameOut from "@/components/FrameOut";
//
// class App extends Component {
//
//   constructor(props) {
//     super(props)
//   }
//
//   render() {
//     // 显示私有的路由  /admin/dashboard 二级路由 (rbac授权)
//     return (
//       <FrameOut>
//       </FrameOut>
//       );
//     }
//   }
//
// export default App;

import React, { useState } from 'react';
import { Form, Input, Button, Radio } from 'antd';

const FormLayoutDemo = () => {
  const [form] = Form.useForm();
  const [formLayout, setFormLayout] = useState('horizontal');

  const onFormLayoutChange = ({ layout }) => {
    setFormLayout(layout);
  };

  const formItemLayout =
    formLayout === 'horizontal'
      ? {
        labelCol: {
            span: 4,
        },
        wrapperCol: {
            span: 14,
        },
      }
      : null;
  const buttonItemLayout =
    formLayout === 'horizontal'
      ? {
        wrapperCol: {
            span: 14,
            offset: 4,
        },
      }
      : null;
  return (
    <>
      <Form
        {...formItemLayout}
        layout={formLayout}
        form={form}
        initialValues={{
          layout: formLayout,
        }}
        onValuesChange={onFormLayoutChange}
      >
        <Form.Item label="Form Layout" name="layout">
          <Radio.Group value={formLayout}>
            <Radio.Button value="horizontal">Horizontal</Radio.Button>
            <Radio.Button value="vertical">Vertical</Radio.Button>
            <Radio.Button value="inline">Inline</Radio.Button>
          </Radio.Group>
        </Form.Item>
        <Form.Item label="Field A">
          <Input placeholder="input placeholder" />
        </Form.Item>
        <Form.Item label="Field B">
          <Input placeholder="input placeholder" />
        </Form.Item>
        <Form.Item {...buttonItemLayout}>
          <Button type="primary">Submit</Button>
        </Form.Item>
      </Form>
    </>
  );
};

export default FormLayoutDemo;
