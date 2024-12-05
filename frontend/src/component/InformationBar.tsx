import React from "react"; 
import styles from "./InformationBar.module.css";
import { Bar } from "../InteracesAndTypes";

const InformationBar: React.FC<({ data: Bar })> = ({ data }) => {

    const scaleRange = data.max_value - data.min_value;

    const leftPercent = ((data.min_data - data.min_value) / scaleRange) * 100;
    const rightPercent = ((data.max_value - data.max_data) / scaleRange) * 100;
    const widthPercent = ((data.max_data - data.min_data) / scaleRange) * 100;

    console.log(leftPercent);

    return (
        <div className = {styles.barContainer}>
            <p className = {styles.dataLabel}>{data.min_data}{data.logo}</p>
            <div className = {styles.blackBar} style = {{background: `linear-gradient(to right, ${data.from_colour}, ${data.to_colour}`}}>
                <div className= {styles.GrayBar} style = {{width: `${leftPercent}%`}}></div>
                <div className= {styles.GrayBar} style = {{width: `${rightPercent}%`, left: `${100-rightPercent}%`}}></div>
            </div>
            <p className = {styles.dataLabel}>{data.max_data}{data.logo}</p>
        </div>
    )
}

export default InformationBar
