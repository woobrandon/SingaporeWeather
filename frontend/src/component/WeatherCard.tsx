import React from "react";
import styles from "./WeatherCard.module.css";

interface WeatherCardProps {
    className?: string;
    temperature?: number;
}

const WeatherCard: React.FC<WeatherCardProps> = ({ className, temperature }) => {

    
    return temperature ? (
        <div className = {styles.CardBackground}>
            {temperature}
        </div>
    ) : (
        <div className = {styles.CardBackground}>No Data Loaded</div>
    )
}

export default WeatherCard;