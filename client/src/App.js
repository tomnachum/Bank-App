import "./App.css";
import {
  BrowserRouter as Router,
  Route,
  Redirect,
  Switch,
} from "react-router-dom";
import NavBar from "./components/NavBar/NavBar";
import Transactions from "./components/Transactions/Transactions";
import Operations from "./components/Operations/Operations";
import Breakdown from "./components/Breakdown/Breakdown";
import { useState } from "react";

const USER_ID = 0;

function App() {
  const balance = 20;

  return (
    <Router>
      <div className="app">
        <NavBar balance={balance}></NavBar>
        <div className="routes">
          <Switch>
            <Route
              exact
              path="/transactions"
              render={() => <Transactions />}
            ></Route>
            <Route
              exact
              path="/operations"
              render={() => <Operations />}
            ></Route>
            <Route exact path="/breakdown" render={() => <Breakdown />}></Route>
            <Redirect to="/transactions" />
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
