import React from "react";
import styles from "./Header.module.css";
import { useNavigate } from "react-router-dom";
import logo from "../assets/weather_logo.png"

interface HeaderProps {
    className?: string;
}

const Header: React.FC<HeaderProps> = ({ className }) => {
    const navigate = useNavigate();
    const headerItems = [
        { label: "Home", path: "/"},
        { label: "Map", path: "/map"}
    ];

    const navigateTo = (path: string) => {
        navigate(path);
      };
    return (
        <div className = {className}>
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