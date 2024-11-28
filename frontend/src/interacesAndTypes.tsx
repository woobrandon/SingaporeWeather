export interface TemperatureData {
    id: string;
    latitude: number;
    longitude: number;
    name: string;
    temperature: number;
  } 

export interface ForecastData {
    day: string;
    forecast_date: string;
    temperature_low: number;
    temperature_high: number;
    humidity_low: number;
    humidity_high: number;
    forecast: string;
    wind_speed_low: number;
    wind_speed_high: number;
    wind_direction: string;
  }