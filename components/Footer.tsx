import React from 'react';

interface IFooterProps {}

const Footer: React.FC<IFooterProps> = (props) => {
  const renderSocialMediaLink = (name: string, url?: string) => {
    if (!url) {
      console.error(`Error: ${name} link is not defined in the environment variables.`);
      return null;
    }

    return (
      <li>
        <a href={url} target="_blank" rel="noopener noreferrer">{name}</a>
      </li>
    );
  };

  return (
    <footer>
      <div>
        <ul>
          {renderSocialMediaLink('Twitter', process.env.REACT_APP_TWITTER_LINK)}
          {renderSocialMediaLink('Facebook', process.env.REACT_APP_FACEBOOK_LINK)}
          {renderSocialMediaLink('Instagram', process.env.REACT_APP_INSTAGRAM_LINK)}
        </ul>
      </div>
      <div>
        <p>&copy; {new Date().getFullYear()} VidShare. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;