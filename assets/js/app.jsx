import { hot } from 'react-hot-loader/root';
import React from 'react';
import axios from 'axios';
import 'uikit';
import 'uikit/dist/css/uikit.css';
import Search from './search';
import Playlist from './playlist';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      query: 'billy', artists: [], releases: [], tracks: [], playlist: [],
    };

    this.handleQueryChange = this.handleQueryChange.bind(this);
    this.handleSearchResponse = this.handleSearchResponse.bind(this);
    this.updateQuery = this.updateQuery.bind(this);
    this.componentDidMount = this.componentDidMount.bind(this);
    this.addTrackToPlaylist = this.addTrackToPlaylist.bind(this);
    this.removeTrackFromPlaylist = this.removeTrackFromPlaylist.bind(this);
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
    const { playlist } = this.state;
    const stateKey = this.state[key]; // eslint-disable-line react/destructuring-assignment
    const [attrKey, valKey] = subkeys;

    return stateKey.map((d) => {
      const htmlAttrs = { key: d[attrKey] };
      const handleAddClick = () => this.addTrackToPlaylist(d);
      let inPlaylist = false;

      // Flag to allow "Add" button.
      if (key === 'tracks' && typeof d !== 'undefined' && playlist.length > 0) {
        inPlaylist = playlist.find(t => t.id === d.id);
      }

      return (
        <li {...htmlAttrs}>
          {d[valKey]}
          {key === 'tracks' && !inPlaylist && <button type="button" onClick={handleAddClick}>+</button>}
        </li>
      );
    });
  }

  addTrackToPlaylist(track) {
    this.setState((prevState) => {
      if (!prevState.playlist.find(t => t.id === track.id)) prevState.playlist.push(track);
      return { prevState };
    });
  }

  removeTrackFromPlaylist(track) {
    const { playlist } = this.state;
    this.setState({ playlist: playlist.filter(t => t.id !== track.id) });
  }

  render() {
    const { query, playlist } = this.state;
    return (
      <div className="uk-grid" data-uk-grid>
        <div className="uk-width-1-3">
          <Search onQueryChange={this.handleQueryChange} query={query} />
          <h2>Artists</h2>
          <ul>{this.makeListFromState('artists')}</ul>
          <h2>Releases</h2>
          <ul>{this.makeListFromState('releases', ['id', 'title'])}</ul>
          <h2>Tracks</h2>
          <ul>{this.makeListFromState('tracks')}</ul>
        </div>
        <div className="uk-width-2-3">
          Playlist state data lives here.
          <Playlist tracks={playlist} onTrackDelete={this.removeTrackFromPlaylist} />
        </div>
      </div>
    );
  }
}

export default hot(App);
