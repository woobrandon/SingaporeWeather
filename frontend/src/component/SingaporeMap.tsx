import React, { useState, useEffect } from "react";
import { APIProvider, Map, MapCameraChangedEvent } from "@vis.gl/react-google-maps";

const SingaporeMap: React.FC = () => {
  const [apiKey, setApiKey] = useState<string | undefined>(undefined);

  useEffect(() => {
    const key = process.env.REACT_APP_GOOGLE_MAP_API_KEY;
    key ? setApiKey(key) : console.warn("No API key found")
  }, [])

  return apiKey ? (
    <APIProvider
      apiKey={apiKey}
      onLoad={() => console.log("Maps API has loaded.")}
    >
      <Map
        defaultZoom={13}

        defaultCenter={{ lat: 1.3521, lng: 103.8198 }}
        style={{ width: "100%", height: "500px" }}
        onCameraChanged={(ev: MapCameraChangedEvent) =>
          console.log("Camera changed:", ev.detail.center, "Zoom:", ev.detail.zoom)
        }
      />
    </APIProvider>
  ) : (
    <div>Map is loading...</div>
  );
};

export default SingaporeMap;