import React from "react";
import styles from "./Header.module.css";
import { useNavigate } from "react-router-dom";
import logo from "../assets/weather_logo.png"

const Header = () => {
    const navigate = useNavigate();
    const headerItems = [
        { label: "Home", path: "/"},
    ];

    const navigateTo = (path: string) => {
        navigate(path);
      };
    return (
        <div>
            <header className={styles.header}>
                <img src = {logo} className = {styles.headerLogo} alt = "logo"/>
                <div className = {styles.appButton}>
                    {headerItems.map((headerItem) => (
                        <div onClick={() => navigateTo(headerItem.path)} className = {styles.headerButton}>
                            {headerItem.label}
                        </div>
                    ))}
                </div>
            </header>
        </div>
    )
}

export default Header