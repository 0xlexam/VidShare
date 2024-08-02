import React from 'react';

interface IFooterProps {}

const Footer: React.FC<IFooterProps> = (props) => {
  return (
    <footer>
      <div>
        <ul>
          <li><a href={process.env.REACT_APP_TWITTER_LINK} target="_blank" rel="noopener noreferrer">Twitter</a></li>
          <li><a href={process.env.REACT_APP_FACEBOOK_LINK} target="_blank" rel="noopener noreferrer">Facebook</a></li>
          <li><a href={process.env.REACT_APP_INSTAGRAM_LINK} target="_blank" rel="noopener noreferrer">Instagram</a></li>
        </ul>
      </div>
      <div>
        <p>&copy; {new Date().getFullYear()} VidShare. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;