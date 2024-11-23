import React from 'react';
import { Header, SingaporeMap } from "../component"
import styles from "./Map.module.css"

const Map = () => {
    return (
      <div className = {styles.background}>
          <Header className = {styles.header}/>
          <SingaporeMap />
      </div>
    );
  };
  
  export default Map;