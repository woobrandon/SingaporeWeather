import React, { useEffect, useState } from 'react';
import styles from "./Home.module.css";
import Singapore from "../assets/SingaporeHome.jpg";
import axios from "axios";
import { Header, WeatherCard } from '../component';

interface TemperatureData {
  id: string;
  latitude: number;
  longitude: number;
  name: string;
  temperature: number;
}

interface ForecastData {
  day: string;
  forecast_date: string;
  temperature_low: number;
  temperature_high: number;
  humidity_low: number;
  humidity_high: number;
  forecast_summary: string;
  wind_speed_low: number;
  wind_speed_high: number;
  wind_direction: string;
}

const Home = () => {
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [meanTemperature, setMeanTemperature] = useState<string | null>(null);
  const [weatherForecast, setWeatherForecast] = useState<ForecastData | null>(null);

  useEffect(() => {
    const fetchTemperatureData = async () => {
      setIsLoading(true)
      try {
        const response = await axios.get("http://localhost:5001/temperature");
        console.log('Temperature Response:', response);
        const responseData = response.data
        console.log('Temperature Response data:', responseData);
        setMeanTemperature((responseData.reduce((sum: number, value: TemperatureData) => sum + value.temperature, 0)/responseData.length).toFixed(1));
      } catch (error) {
        console.error("Error processing weather data:", error);
      }
      setIsLoading(false);
    }
    fetchTemperatureData();
  }, [])

  useEffect(() => {
    const fetchForecastData = async () => {
      setIsLoading(true)
      try {
        const response = await axios.get("http://localhost:5001/weather-forecast");
        console.log('Weather Forecast Response:', response);
        const responseData = response.data
        console.log('Weather Forecast Response data:', responseData);
        setWeatherForecast(responseData)
      } catch (error) {
        console.error("Error processing weather data:", error);
      }
      setIsLoading(false);
    }
    fetchForecastData();
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
