import React from 'react';

function Search(props) {
  const { query, onQueryChange } = props;
  return (
    <div className="uk-form uk-form-horizontal">
      <label className="uk-form-label" htmlFor="search">Search:</label>
      <div className="uk-form-controls">
        <input type="text" id="poo" className="uk-input" value={query} onChange={onQueryChange} />
      </div>
    </div>
  )
}

export default Search;
