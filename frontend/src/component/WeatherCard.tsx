import React, { useRef } from "react";
import { ForecastData } from "../InteracesAndTypes"
import styles from "./WeatherCard.module.css";
import thunderstorm from "../assets/thunderstorm.gif";
import cloudy from "../assets/cloudy.gif"
import humidity from "../assets/humidity.png";
import temperature from "../assets/temperature.png";
import wind from "../assets/wind.png"
import InformationBar from "./InformationBar"

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
            <div className = {styles.forecastInformation}>
                <div className = {styles.titleContainer}>
                    <p className = {styles.day}>{day}</p>
                    <p className = {styles.weather}>{forecast}</p>
                </div>
                <InformationBar 
                data = {{
                    min_value: 20,
                    min_data: temperature_low,
                    max_value: 40,
                    max_data: temperature_high,
                    logo: "\u00B0C",
                    from_colour: "rgb(255, 199, 108)",
                    to_colour: "rgb(255, 75, 75)"
                }}/>
                <InformationBar 
                data = {{
                    min_value: 0,
                    min_data: humidity_low,
                    max_value: 100,
                    max_data: humidity_high,
                    logo: "%",
                    from_colour: "rgb(71, 221, 255)",
                    to_colour: "rgb(0, 60, 255)"
                }}/>
                <InformationBar 
                data = {{
                    min_value: 0,
                    min_data: wind_speed_low,
                    max_value: 30,
                    max_data: wind_speed_high,
                    logo: "km/h",
                    from_colour: "rgb(169, 255, 145)",
                    to_colour: "rgb(0, 255, 38)"
                }}/>
            </div>
        </div>
    ) : (
        <div className = {styles.CardBackground}>No Data Loaded</div>
    )
}

export default WeatherCard;