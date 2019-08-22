import React from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';

class Release extends React.Component {
  constructor(props) {
    super(props);
    this.state = { data: { tracks: [] } };
  }

  componentDidMount() {
    const { id, data } = this.props;

    if (Object.keys(data).length) this.setState({ data });

    if (id && (!data || Object.keys(data).length === 0)) {
      axios.get(`http://localhost:8000/releases/${id}/`)
        .then(response => this.setState({ data: response.data }));
    }
  }

  render() {
    const { data } = this.state;
    const { onRenderTrack } = this.props;
    return (
      <div>
        <h4>{data.title}</h4>
        <ol>
          { data.tracks.map(t => (<li key={t.id}>{onRenderTrack(t)}</li>)) }
        </ol>
      </div>
    );
  }
}

Release.propTypes = {
  id: PropTypes.string,
  data: PropTypes.shape({
    id: PropTypes.number,
    title: PropTypes.string,
    artist: PropTypes.string,
    date: PropTypes.string,
    country: PropTypes.string,
    label: PropTypes.string,
    catalogue_number: PropTypes.string,
    barcode: PropTypes.string,
    status: PropTypes.string,
    mbid: PropTypes.string,
    tracks: PropTypes.array,
  }),
  onRenderTrack: PropTypes.func,
};

Release.defaultProps = {
  id: null,
  data: {},
  onRenderTrack: t => t.name,
};

export default Release;
