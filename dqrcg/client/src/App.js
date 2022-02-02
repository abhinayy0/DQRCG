import NavBar from "./components/Navbar";
import Home from "./components/Home";
import React, { useState, useEffect } from "react";
import ShowDetail from "./components/Loader";
import config from "./config";

import Login from "./components/Login";

function App() {
  const [showForm, setshowForm] = useState(false);

  function checkApi() {
    fetch(config.BASE_URL)
      .then((res) => {
        if (res.ok) {
          setshowForm(true);
        }
      })
      .catch((err) => {
        setshowForm(false);
        setTimeout(() => {
          checkApi();
        }, 5000);
      });
  }

  useEffect(() => {
    checkApi();
  }, []);

  return (
    <div className="App">
      <NavBar />
      {!showForm && <ShowDetail />}
      {showForm && <Home showForm="true" />}
    </div>
  );
}

export default App;
