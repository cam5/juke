import React from 'react';

class Search extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <input type="text" value={this.props.query} onChange={this.props.onQueryChange} />
    )
  }
}

export default Search;
