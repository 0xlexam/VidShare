import React from 'react';
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Route,
  Switch
} from 'react-router-dom';

const API_URL = process.env.REACT_APP_API_URL;

import './styles/App.css';

import HomePage from './components/HomePage';
import VideoDetailPage from './components/VideoDetailPage';
import NotFoundAccessException from './components/NotFoundPage';

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={HomePage} />
        <Route path="/video/:id" component={VideoDetailPage} />
        <Route component={NotFoundPage} />
      </Switch>
    </Router>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));