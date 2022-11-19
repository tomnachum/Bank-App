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
import { useEffect, useState } from "react";
import axios from "axios";
import * as c from "./utils/Constants";

function App() {
  const [balance, setBalance] = useState(0);

  async function fetchBalance() {
    const res = await axios.get(
      `${c.SERVER_DOMAIN}${c.USERS}/${c.USER_ID}/${c.BALANCE}`
    );
    const balance = res.data.balance;
    setBalance(balance);
  }

  useEffect(() => {
    fetchBalance();
  }, []);

  return (
    <Router>
      <div className="app">
        <NavBar balance={balance}></NavBar>
        <div className="routes">
          <Switch>
            <Route
              exact
              path="/transactions"
              render={() => <Transactions updateBalance={fetchBalance} />}
            ></Route>
            <Route
              exact
              path="/operations"
              render={() => <Operations updateBalance={fetchBalance} />}
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
