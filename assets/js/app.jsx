import { hot } from 'react-hot-loader/root';
import React from 'react';
import PropTypes from 'prop-types';
import { HashRouter as Router, Route, Link } from 'react-router-dom';
import axios from 'axios';
import 'uikit';
import 'uikit/dist/css/uikit.css';
import Search from './search';
import Playlist from './playlist';
import Artist from './artist-detail';
import Release from './release-detail';


function SearchResults(props) {
  const { artists, releases, tracks } = props;
  return (
    <div>
      <h2>Artists</h2>
      <ul>{artists}</ul>

      <h2>Releases</h2>
      <ul>{releases}</ul>

      <h2>Tracks</h2>
      <ul>{tracks}</ul>
    </div>
  );
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      query: 'billy', artists: [], releases: [], tracks: [], playlist: [],
    };

    this.handleQueryChange = this.handleQueryChange.bind(this);
    this.handleSearchResponse = this.handleSearchResponse.bind(this);
    this.appendSearchResponse = this.appendSearchResponse.bind(this);
    this.updateQuery = this.updateQuery.bind(this);
    this.componentDidMount = this.componentDidMount.bind(this);
    this.addTrackToPlaylist = this.addTrackToPlaylist.bind(this);
    this.removeTrackFromPlaylist = this.removeTrackFromPlaylist.bind(this);
    this.renderTrack = this.renderTrack.bind(this);
  }

  componentDidMount() {
    const { query } = this.state;

    axios.get(`http://localhost:8000/search/?q=${query}`)
      .then(this.handleSearchResponse);
  }

  handleQueryChange(e) {
    const val = e.target.value;
    axios.get(`http://localhost:8000/search/?q=${val}`)
      .then(this.updateQuery(val))
      .then(this.handleSearchResponse)
      .then(
        () => axios.get(`http://localhost:8000/search/external/?q=${val}`)
          .then(response => this.appendSearchResponse(response)),
      );
  }

  handleSearchResponse(response) {
    const { results } = response.data;
    this.setState({
      artists: results.Artist,
      releases: results.Release,
      tracks: results.Track,
    });
  }

  appendSearchResponse(response) {
    const results = response.data;
    this.setState((prevState) => {
      results.Artist.map(a => prevState.artists.push(a));
      results.Release.map(r => prevState.releases.push(r));
      results.Tracks.map(t => prevState.tracks.push(t));

      return prevState;
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
        inPlaylist = playlist.find(t => t.mbid === d.mbid);
      }

      return (
        <li {...htmlAttrs}>
          <Link to={`/${key}/${d.id}`}>{d[valKey]}</Link>
          {key === 'tracks' && !inPlaylist && <button type="button" onClick={handleAddClick}>+</button>}
        </li>
      );
    });
  }

  addTrackToPlaylist(track) {
    this.setState((prevState) => {
      if (!prevState.playlist.find(t => t.mbid === track.mbid)) prevState.playlist.push(track);
      return { prevState };
    });
  }

  removeTrackFromPlaylist(track) {
    const { playlist } = this.state;
    this.setState({ playlist: playlist.filter(t => t.mbid !== track.mbid) });
  }

  renderTrack(track) {
    const { playlist } = this.state;
    const handleAddClick = () => this.addTrackToPlaylist(track);
    let inPlaylist = false;

    if (track && playlist.length > 0) inPlaylist = playlist.find(t => t.mbid === track.mbid);

    return (
      <span>
        {track.name || track.title}
        {!inPlaylist && <button type="button" onClick={handleAddClick}>+</button>}
      </span>
    );
  }

  render() {
    const { query, playlist, tracks } = this.state;
    return (
      <div className="uk-grid" data-uk-grid>
        <div className="uk-width-1-3">
          <Search onQueryChange={this.handleQueryChange} query={query} />

          <Router basname="/playlist/">
            <Route
              exact
              path="/"
              render={() => (
                <SearchResults
                  artists={this.makeListFromState('artists')}
                  releases={this.makeListFromState('releases', ['mbid', 'title'])}
                  tracks={tracks.map(t => (<li key={t.mbid}>{ this.renderTrack(t) }</li>))}
                />
              )}
            />

            <Route
              exact
              path="/artists/:artistId"
              render={props => (
                <div>
                  <div className="uk-margin">
                    <Link to="/">&larr; Back</Link>
                  </div>
                  <Artist id={props.match.params.artistId} onRenderTrack={this.renderTrack} />
                </div>
              )}
            />

            <Route
              exact
              path="/releases/:releaseId"
              render={props => (
                <div>
                  <div className="uk-margin">
                    <Link to="/">&larr; Back</Link>
                  </div>
                  <Release id={props.match.params.releaseId} onRenderTrack={this.renderTrack} />
                </div>
              )}
            />
          </Router>
        </div>
        <div className="uk-width-2-3">
          Playlist state data lives here.
          <Playlist tracks={playlist} onTrackDelete={this.removeTrackFromPlaylist} />
        </div>
      </div>
    );
  }
}

SearchResults.propTypes = {
  artists: PropTypes.arrayOf(PropTypes.object).isRequired,
  releases: PropTypes.arrayOf(PropTypes.object).isRequired,
  tracks: PropTypes.arrayOf(PropTypes.object).isRequired,
};

export default hot(App);
