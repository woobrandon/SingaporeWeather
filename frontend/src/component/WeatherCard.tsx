import React from "react";
import { ForecastData } from "../interacesAndTypes"
import styles from "./WeatherCard.module.css";

const WeatherCard: React.FC<ForecastData> = ({ day, forecast_date, temperature_low, temperature_high, humidity_low, humidity_high, forecast_summary, wind_speed_low, wind_speed_high, wind_direction }) => {

    return day ? (
        <div className = {styles.CardBackground}>
            <p className = {styles.day}>{day}</p>
            <div className = {styles.forecastInformation}>
                <div className = {styles.informationContainer}>
                    <p className = {styles.informationTitle}>Temperature</p>
                    <p className = {styles.information}>{temperature_low}-{temperature_high}</p>
                </div>
                <div className = {styles.informationContainer}>
                    <p className = {styles.informationTitle}>Humidity</p>
                    <p className = {styles.information}>{humidity_low}-{humidity_high}</p>
                </div>
                <div className = {styles.informationContainer}>
                    <p className = {styles.informationTitle}>Wind Speed</p>
                    <p className = {styles.information}>{wind_speed_low}-{wind_speed_high}</p>
                </div>
            </div>
        </div>
    ) : (
        <div className = {styles.CardBackground}>No Data Loaded</div>
    )
}

export default WeatherCard;