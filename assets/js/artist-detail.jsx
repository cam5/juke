import React from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';
import Pluralize from 'react-pluralize';
import Release from './release-detail';

class Artist extends React.PureComponent {
  constructor(props) {
    super(props);
    this.state = {
      artist: {},
      releases: [],
    };
  }

  componentDidMount() {
    const { id } = this.props;

    axios.get(`http://localhost:8000/releases/?artist=${id}`)
      .then(response => this.setState({
        releases: response.data.results,
        releaseCount: response.data.count,
      }));

    axios.get(`http://localhost:8000/artists/${id}`)
      .then(response => this.setState({ artist: response.data }));
  }

  render() {
    const { artist, releases, releaseCount } = this.state;
    const { onRenderTrack } = this.props;
    return (
      <div>
        <h3>{ artist.name }</h3>
        <div>
          <Pluralize singular="release" count={releaseCount} zero="No releases" />
        </div>
        { releases.map(r => (<Release key={r.mbid} data={r} onRenderTrack={onRenderTrack} />)) }
      </div>
    );
  }
}

Artist.propTypes = {
  id: PropTypes.string.isRequired,
  onRenderTrack: PropTypes.func,
};

Artist.defaultProps = {
  onRenderTrack: t => t.name,
};

export default Artist;
