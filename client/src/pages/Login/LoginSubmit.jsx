import {Button, Form} from "antd";
import React from "react";
import styles from "./index.less";

const FormItem = Form.Item;

const LoginSubmit = ({className, ...rest}) => {
  console.log("a", styles.login-form, className);
  const clsString = [styles.submit, className].join(" ");
  console.log("clsString", clsString);
  return (
    <FormItem>
      <Button size="large" className={clsString} type="primary" htmlType="submit" {...rest} />
    </FormItem>
  );
};

export default LoginSubmit;
