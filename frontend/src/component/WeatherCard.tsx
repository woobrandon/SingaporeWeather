import React from "react";
import { ForecastData } from "../interacesAndTypes"
import styles from "./WeatherCard.module.css";
import thunderstorm from "../assets/thunderstorm.gif";
import humidity from "../assets/humidity.png";
import temperature from "../assets/temperature.png";
import wind from "../assets/wind.png"

const WeatherCard: React.FC<ForecastData> = ({ day, forecast_date, temperature_low, temperature_high, humidity_low, humidity_high, forecast, wind_speed_low, wind_speed_high, wind_direction }) => {

    const weatherTypes = [
        "Fair",
        "Fair (Day)",
        "Fair (Night)",
        "Fair and Warm",
        "Partly Cloudy",
        "Partly Cloudy (Day)",
        "Partly Cloudy (Night)",
        "Cloudy",
        "Hazy",
        "Slightly Hazy",
        "Windy",
        "Mist",
        "Fog",
        "Light Rain",
        "Moderate Rain",
        "Heavy Rain",
        "Passing Showers",
        "Light Showers",
        "Showers",
        "Heavy Showers",
        "Thundery Showers",
        "Heavy Thundery Showers",
        "Heavy Thundery Showers with Gusty Winds"
      ]

    return day ? (
        <div className = {styles.CardBackground}>
            <img src = {thunderstorm} alt = "Background GIF" className = {styles.backgroundGif}/>
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