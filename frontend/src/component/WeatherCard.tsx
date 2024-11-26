import React from "react";
import styles from "./WeatherCard.module.css";

interface WeatherCardProps {
    className?: string;
}

const WeatherCard: React.FC<WeatherCardProps> = ({ className }) => {

    
    return (
        <div className = {className}>
            <div className = {styles.CardBackground}>
                weather card
            </div>
        </div>
    )
}

export default WeatherCard;