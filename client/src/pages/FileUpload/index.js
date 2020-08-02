import React, {Component, Fragment} from 'react';

import { Upload, message, Button } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import * as file from '@/api/file'


class FileUpload extends Component {
  constructor(props) {
    super(props);
    this.state = {
    }
  }

  componentWillMount(){
    const env = process.env;
    console.log(env);
    file
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
      action: 'http://127.0.0.1:8000/user/uploadFiles',
      // headers: {
      //   authorization: 'authorization-text',
      // },
      "multiple": true,
      // "accept": ['.mif', '.mid'],
      "showUploadList": true,
      // "withCredentials": true,
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
      <Fragment>
        <Upload {...props}>
          <Button>
            <UploadOutlined /> Click to Upload
          </Button>
        </Upload>
        <Upload>

        </Upload>
      </Fragment>
    )
  }

}

export default FileUpload;
