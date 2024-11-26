import React from 'react';
import styles from "./Home.module.css";
import Singapore from "../assets/SingaporeHome.jpg"
import { Header, WeatherCard } from '../component';

const Home = () => {
  return (
    <div className = {styles.background}>
        <Header className = {styles.header}/>
        <div className = {styles.body}>
          <div className = {styles.SingaporeMapContainer}>
            <img src = {Singapore} alt = "Singapore"/>
            <h1 className = {styles.CountryName}>Singapore</h1>
            <div className = {styles.WeatherCardsContainer}>
              <WeatherCard className = {styles.WeatherCard}/>
              <WeatherCard className = {styles.WeatherCard}/>
              <WeatherCard className = {styles.WeatherCard}/>
              <WeatherCard className = {styles.WeatherCard}/>
            </div>
          </div>
        </div>
    </div>
  );
};

export default Home;
