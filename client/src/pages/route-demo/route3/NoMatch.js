import React, {PropTypes} from 'react';

export default class NoMatch extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (<div>404 No pages</div>);
  }
}

NoMatch.propTypes = {
};
