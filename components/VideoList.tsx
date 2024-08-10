import React, { useEffect, useState } from 'react';

interface Video {
  id: string;
  title: string;
  description: string;
  url: string;
}

const VideoList: React.FC = () => {
  const [videos, setVideos] = useState<Video[]>([]);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/videos`)
      .then(response => response.json())
      .then(data => setVideos(data))
      .catch(error => console.error('There was an error fetching the videos:', error));
  }, []);

  return (
    <div>
      <h2>Video List</h2>
      <ul>
        {videos.map((video) => (
          <li key={video.id}>
            <h3>{video.title}</h3>
            <p>{video.description}</p>
            <a href={`/videos/${video.id}`}>Watch</a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default VideoList;