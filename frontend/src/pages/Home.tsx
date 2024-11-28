import React, { useEffect, useState } from 'react';
import styles from "./Home.module.css";
import Singapore from "../assets/SingaporeHome.jpg";
import axios from "axios";
import { Header, WeatherCard } from '../component';

interface WeatherData {
  id: string;
  latitude: number;
  longitude: number;
  name: string;
  temperature: number;
}

const Home = () => {
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [temperatureData, setTemperatureData] = useState<WeatherData[]>([])
  const [meanTemperature, setMeanTemperature] = useState<string | null>(null)

  useEffect(() => {
    const fetchWeatherData = async () => {
      setIsLoading(true)
      try {
        const response = await axios.get("http://localhost:5001/temperature");
        console.log('Response:', response);
        const responseData = response.data
        console.log('Response data:', responseData);
        setTemperatureData(responseData);
        setMeanTemperature((responseData.reduce((sum: number, value: WeatherData) => sum + value.temperature, 0)/responseData.length).toFixed(1));
      } catch (error) {
        console.error("Error processing weather data:", error);
      }
      setIsLoading(false);
    }
    fetchWeatherData();
  }, [])

  
  return (
    <div className = {styles.background}>
        <Header className = {styles.header}/>
        <div className = {styles.body}>
          <div className = {styles.SingaporeMapContainer}>
            <img src = {Singapore} alt = "Singapore"/>
            <div className = {styles.imgTop}>
              <h1 className = {styles.CountryName}>Singapore</h1>
              <div className = {styles.weatherInformationContainer}>
                <div className = {styles.meanTemperatureContainer}>
                  <div className = {styles.meanTemperature}>{meanTemperature}</div>
                  <div className = {styles.degreeLogo}>°C</div>
                </div>
              </div>
            </div>
            <div className = {styles.WeatherCardsContainer}>
              <WeatherCard/>
              <WeatherCard/>
              <WeatherCard/>
              <WeatherCard/>
            </div>
          </div>
        </div>
    </div>
  );
};

export default Home;
