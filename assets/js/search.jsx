import React from 'react';

function Search(props) {
  const { query, onQueryChange } = props;
  return (
    <div>
      <label htmlFor="search">Search:</label>
      <input type="text" id="poo" value={query} onChange={onQueryChange} />
    </div>
  )
}

export default Search;
