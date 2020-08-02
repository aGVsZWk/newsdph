import CommonHttp from "./http";

class HttpForm extends CommonHttp {
  constructor(props) {
    super(props);
    // this.withCredentials = true
    this.headerContentType = "application/x-www-form-urlencoded";
  }

  createRequestParams() {
    let data = "";
    Object.keys(this.params).forEach((objKey) => {
      data += `${encodeURIComponent(objKey)}=${encodeURIComponent(this.params[objKey])}&`;
    });
    this.params = data.slice(0, -1);
  }
}

export class HttpFormMultipart extends CommonHttp {
  constructor() {
    super();
    // this.withCredentials = true
    this.headerContentType = "multipart/form-data";
  }

  createRequestParams() {
    const formData = new FormData();
    Object.keys(this.params).forEach((objKey) => {
      formData.append(objKey, this.params[objKey]);
    });
    this.params = formData;
  }
}

export default HttpForm;
