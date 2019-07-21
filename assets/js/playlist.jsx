import React from 'react';
import PropTypes from 'prop-types';

function Playlist(props) {
  const { tracks, onTrackDelete } = props;
  return (
    <ul>
      {tracks.map(t => (
        <li key={t.id}>
          {t.name}
          <button type="button" onClick={() => onTrackDelete(t)}>&times;</button>
        </li>
      ))}
    </ul>
  );
}

Playlist.propTypes = {
  tracks: PropTypes.arrayOf(PropTypes.object).isRequired,
  onTrackDelete: PropTypes.func.isRequired,
};

export default Playlist;
