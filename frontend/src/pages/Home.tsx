import React from 'react';
import styles from "./Home.module.css";
import Singapore from "../assets/SingaporeHome.jpg"
import { Header } from '../component';

const Home = () => {
  return (
    <div className = {styles.background}>
        <Header className = {styles.header}/>
        <div className = {styles.body}>
          <div className = {styles.SingaporeMapContainer}>
            <img src = {Singapore} alt = "Singapore"/>
            <h1 className = {styles.CountryName}>Singapore</h1>
          </div>
        </div>
    </div>
  );
};

export default Home;
