import React, { Component } from 'react';

import { Upload, message, Button } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import api from '@/api'


class FileUpload extends Component {
  constructor(props) {
    super(props);
    this.state = {
    }
  }

  componentWillMount(){
    api.file
    .heartBeat()
    .then((res) => {
      console.log(res)
    })
    .catch((err) => {
      console.log(err)
    })
    .finally(() => {
      this.setState({
        isLoading: false
      });
    })
  }

  render() {
    const props = {
      name: 'file',
      action: 'https://127.0.0.1:8000/user/uploadFileList',
      // headers: {
      //   authorization: 'authorization-text',
      // },
      "multiple": true,
      // "accept": ['.mif', '.mid'],
      "showUploadList": true,
      "withCredentials": true,
      onChange(info) {
        if (info.file.status !== 'uploading') {
          console.log(info.file, info.fileList);
        }
        if (info.file.status === 'done') {
          message.success(`${info.file.name} file uploaded successfully`);
        } else if (info.file.status === 'error') {
          message.error(`${info.file.name} file upload failed.`);
        }
      },
    };

    return (
      <Upload {...props}>
        <Button>
          <UploadOutlined /> Click to Upload
        </Button>
      </Upload>
    )
  }

}

export default FileUpload;