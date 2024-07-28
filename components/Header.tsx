import React from 'react';
import { Link } from 'react-router-dom';

interface HeaderProps {}

const Header: React.FC<HeaderProps> = () => {
  return (
    <header style={{ backgroundColor: '#282c34', padding: '10px', color: 'white', textAlign: 'center' }}>
      <h1>{process.env.REACT_APP_BRANDING_NAME}</h1>
      <nav>
        <ul style={{ listStyle: 'none', display: 'flex', justifyContent: 'center', padding: 0 }}>
          <li style={{ margin: '0 10px' }}>
            <Link to="/" style={{ color: 'white', textDecoration: 'none' }}>
              Home
            </Link>
          </li>
          <li style={{ margin: '0 10px' }}>
            <Link to="/videos" style={{ color: 'white', textDecoration: 'none' }}>
              Videos
            </Link>
          </li>
          <li style={{ margin: '0 10px' }}>
            <Link to="/about" style={{ color: 'white', textDecoration: 'none' }}>
              About
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;