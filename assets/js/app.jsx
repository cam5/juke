import { hot } from 'react-hot-loader/root';

import React from 'react';
import axios from 'axios';
import Search from './search';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      query: 'billy', artists: [], releases: [], tracks: [],
    };

    this.handleQueryChange = this.handleQueryChange.bind(this);
    this.handleSearchResponse = this.handleSearchResponse.bind(this);
    this.updateQuery = this.updateQuery.bind(this);
    this.componentDidMount = this.componentDidMount.bind(this);
  }

  componentDidMount() {
    const { query } = this.state;

    axios.get(`http://localhost:8000/search/?q=${query}`)
      .then(this.handleSearchResponse);
  }

  handleQueryChange(e) {
    const val = e.target.value;
    axios.get(`http://localhost:8000/search/?q=${val}`)
      .then(this.handleSearchResponse)
      .then(this.updateQuery(val));
  }

  handleSearchResponse(response) {
    const { results } = response.data;
    this.setState({
      artists: results.Artist,
      releases: results.Release,
      tracks: results.Track,
    });
  }

  updateQuery(q) {
    this.setState({ query: q });
  }


  makeListFromState(key, subkeys = ['id', 'name']) {
    const stateKey = this.state[key]; // eslint-disable-line react/destructuring-assignment
    return stateKey.map(d => (<li key={d[subkeys[0]]}>{d[subkeys[1]]}</li>));
  }

  render() {
    const { query } = this.state;
    return (
      <div>
        <Search onQueryChange={this.handleQueryChange} query={query} />
        <h2>Artists</h2>
        <ul>{this.makeListFromState('artists')}</ul>
        <h2>Releases</h2>
        <ul>{this.makeListFromState('releases', ['id', 'title'])}</ul>
        <h2>Tracks</h2>
        <ul>{this.makeListFromState('tracks')}</ul>
      </div>
    );
  }
}

export default hot(App);
