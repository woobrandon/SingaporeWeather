import React from "react";
import { ForecastData } from "../interacesAndTypes"
import styles from "./WeatherCard.module.css";
import thunderstorm from "../assets/thunderstorm.gif";
import cloudy from "../assets/cloudy.gif"
import humidity from "../assets/humidity.png";
import temperature from "../assets/temperature.png";
import wind from "../assets/wind.png"

const WeatherCard: React.FC<{ data: ForecastData }> = ({ data }) => {
    const {
        day,
        forecast_date,
        temperature_low,
        temperature_high,
        humidity_low,
        humidity_high,
        forecast,
        wind_speed_low,
        wind_speed_high,
        wind_direction,
      } = data;

    const weatherTypes: { [key: string]: string } = {
        "Fair": thunderstorm,
        "Fair (Day)": thunderstorm,
        "Fair (Night)": thunderstorm,
        "Fair and Warm": thunderstorm,
        "Partly Cloudy": cloudy,
        "Partly Cloudy (Day)": cloudy,
        "Partly Cloudy (Night)": cloudy,
        "Cloudy": cloudy,
        "Hazy": thunderstorm,
        "Slightly Hazy": thunderstorm,
        "Windy": thunderstorm,
        "Mist": thunderstorm,
        "Fog": thunderstorm,
        "Light Rain": thunderstorm,
        "Moderate Rain": thunderstorm,
        "Heavy Rain": thunderstorm,
        "Passing Showers": thunderstorm,
        "Light Showers": thunderstorm,
        "Showers": thunderstorm,
        "Heavy Showers": thunderstorm,
        "Thundery Showers": thunderstorm,
        "Heavy Thundery Showers": thunderstorm,
        "Heavy Thundery Showers with Gusty Winds": thunderstorm
    };

    return day ? (
        <div className = {styles.CardBackground}>
            <img src = {weatherTypes[forecast]} alt = "Background GIF" className = {styles.backgroundGif}/>
            <p className = {styles.day}>{day}</p>
            <p className = {styles.weather}>{forecast}</p>
            <div className = {styles.forecastInformation}>
                <div className = {styles.informationContainer}>
                    <div className = {styles.imgContainer}>
                        <img src = {temperature} alt = "Temperature Logo" className = {styles.temperatureLogo}/>
                    </div>
                    <p className = {styles.information}>{temperature_low}&deg;C-{temperature_high}&deg;C</p>
                </div>
                <div className = {styles.informationContainer}>
                    <div className = {styles.imgContainer}>
                        <img src = {humidity} alt = "Humidity Logo" className = {styles.humidityLogo}/>
                    </div>
                    <p className = {styles.information}>{humidity_low}%-{humidity_high}%</p>
                </div>
                <div className = {styles.informationContainer}>
                    <div className = {styles.imgContainer}>
                        <img src = {wind} alt = "Wind Logo" className = {styles.windLogo}/>
                    </div>
                    <p className = {styles.information}>{wind_speed_low}km/h-{wind_speed_high}km/h</p>
                </div>
            </div>
        </div>
    ) : (
        <div className = {styles.CardBackground}>No Data Loaded</div>
    )
}

export default WeatherCard;