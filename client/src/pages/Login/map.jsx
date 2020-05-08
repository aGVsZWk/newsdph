import {LockTwoTone, MailTwoTone, MobileTwoTone, UserOutlined} from "@ant-design/icons";
import React from "react";
import styles from "./index.less";

export default {
  UserName: {
    props: {
      size: "large",
      id: "userName",
      prefix: (
        <UserOutlined
          style={{
            color: "#1890ff",
          }}
          className={styles.prefixIcon}
        />
      ),
      placeholder: "admin",
    },
    rules: [
      {
        required: true,
        message: "瓜娃子！请输入用户名！！！",
      },
    ],
  },
  Password: {
    props: {
      size: "large",
      prefix: <LockTwoTone className={styles.prefixIcon} />,
      type: "password",
      id: "password",
      placeholder: "888888",
    },
    rules: [
      {
        required: true,
        message: "瓜娃子！请输入密码！！！",
      },
    ],
  },
  Mobile: {
    props: {
      size: "large",
      prefix: <MobileTwoTone className={styles.prefixIcon} />,
      placeholder: "mobile number",
    },
    rules: [
      {
        required: true,
        message: "瓜娃子！请输入手机号！！！",
      },
      {
        pattern: /^1\d{10}$/,
        message: "手机号格式错误!",
      },
    ],
  },
  Captcha: {
    props: {
      size: "large",
      prefix: <MailTwoTone className={styles.prefixIcon} />,
      placeholder: "captcha",
    },
    rules: [
      {
        required: true,
        message: "瓜娃子，请输入验证码！！！",
      },
    ],
  },
};
