// import {Button, Form} from "antd";
// import React from "react";
// import styles from "./index.less";
//
// const FormItem = Form.Item;
//
// const LoginSubmit = ({className, ...rest}) => {
//
//   return (
//     <FormItem>
//       <Button size="large" className={"sumbit "+className} type="primary" htmlType="submit" {...rest} />
//     </FormItem>
//   );
// };
//
// export default LoginSubmit;



// aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
import {Button, Form} from "antd";
import React, {Component} from "react";

class LoginSubmit extends Component{
  render(){
    const FormItem = Form.Item;

    return (
      <FormItem>
        <Button size="large" className={"sumbit "+this.props.className} type="primary" htmlType="submit" {...this.props.rest} />
      </FormItem>
    );
  }
}

export default LoginSubmit;