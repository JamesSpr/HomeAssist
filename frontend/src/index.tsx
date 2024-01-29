import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ReactDOM from 'react-dom/client';
import App from './App';


const root = ReactDOM.createRoot(
    document.getElementById("app") as HTMLElement
);

root.render(
    <React.StrictMode>
        <BrowserRouter>
            <Routes>
                <Route path="/*" element={<App />}/>
            </Routes>
        </BrowserRouter>
    </React.StrictMode>
);
