import React from 'react';
import PropTypes from 'prop-types';

class Search extends React.PureComponent {
  render() {
    const { query, onQueryChange } = this.props;
    const domId = 'search';

    return (
      <div className="uk-form uk-form-horizontal">
        <label className="uk-form-label" htmlFor={domId}>Search:</label>
        <div className="uk-form-controls">
          <input type="text" id={domId} className="uk-input" value={query} onChange={onQueryChange} />
        </div>
      </div>
    );
  }
}

Search.propTypes = {
  query: PropTypes.string.isRequired,
  onQueryChange: PropTypes.func.isRequired,
};

export default Search;
