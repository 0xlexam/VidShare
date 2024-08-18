import React, { useState, useEffect } from "react";

interface VideoDetails {
  id: string;
  title: string;
  description: string;
  url: string;
  likes: number; // added likes
  dislikes: number; // added dislikes
}

interface Comment {
  id: string;
  videoId: string;
  text: string;
}

interface VideoInfoProps {
  videoId: string;
}

const VideoInfo: React.FC<VideoInfoProps> = ({ videoId }) => {
  const [videoDetails, setVideoDetails] = useState<VideoDetails | null>(null);
  const [comments, setComments] = useState<Comment[]>([]);
  const [newCommentText, setNewCommentText] = useState("");

  useEffect(() => {
    fetchVideoDetails();
    fetchComments();
  }, [videoId]);

  const fetchVideoDetails = async () => {
    const response = await fetch(`${process.env.REACT_APP_API_URL}/videos/${videoId}`);
    const data = await response.json();
    setVideoDetails(data);
  };

  const fetchComments = async () => {
    const response = await fetch(`${process.env.REACT_APP_API_URL}/comments/${videoId}`);
    const data = await response.json();
    setComments(data);
  };

  const handleNewCommentSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await fetch(`${process.env.REACT_APP_API_URL}/comments`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ videoId, text: newCommentText }),
    });
    if (response.ok) {
      fetchComments();
      setNewCommentText("");
    }
  };

  // Function to handle likes and dislikes
  const handleReaction = async (type: "like" | "dislike") => {
    // Using PATCH method to update only specific fields
    const response = await fetch(`${process.env.REACT_APP_API_URL}/videos/${videoId}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ [type]: videoDetails ? videoDetails[type] + 1 : 1 }),
    });
    if (response.ok) {
      fetchVideoDetails(); // Refresh the video details to show updated likes or dislikes
    }
  };

  return (
    <div>
      {videoDetails && (
        <div>
          <h2>{videoDetails.title}</h2>
          <p>{videoDetails.description}</p>
          <video src={videoDetails.url} controls />
          <div>Likes: {videoDetails.likes} Dislikes: {videoDetails.dislikes}</div>
          <button onClick={() => handleReaction("like")}>Like</button>
          <button onClick={() => handleReaction("dislike")}>Dislike</button>
        </div>
      )}
      <h3>Comments</h3>
      <div>
        {comments.map((comment) => (
          <div key={comment.id}>{comment.text}</div>
        ))}
      </div>
      <form onSubmit={handleNewCommentSubmit}>
        <textarea
          value={newCommentText}
          onChange={(e) => setNewCommentText(e.target.value)}
          placeholder="Add a comment..."
          required
        ></textarea>
        <button type="submit">Submit Comment</button>
      </form>
    </div>
  );
};

export default VideoInfo;