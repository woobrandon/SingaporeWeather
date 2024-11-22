import React from 'react';
import styles from "./Home.module.css";
import { SingaporeMap, Header } from '../component';

const Home = () => {
  return (
    <div className = {styles.background}>
        <Header />
        <SingaporeMap />
    </div>
  );
};

export default Home;
