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
import Transaction from "./objects/Transaction";

const USER_ID = 0;

function App() {
  const [transactions, setTransactions] = useState([
    {
      id: 0,
      amount: -50,
      vendor: "Chick & Pick",
      date: "2022-10-12 08:27:15",
      categoryId: 2,
      userId: 0,
    },
    {
      id: 1,
      amount: -499.9,
      vendor: "Super Pharm",
      date: "2022-10-29 22:50:58",
      categoryId: 5,
      userId: 0,
    },
    {
      id: 2,
      amount: -3000,
      vendor: "Rent",
      date: "2022-10-20 07:05:13",
      categoryId: 0,
      userId: 0,
    },
    {
      id: 3,
      amount: -279.9,
      vendor: "Lior",
      date: "2022-10-26 22:02:27",
      categoryId: 3,
      userId: 0,
    },
    {
      id: 4,
      amount: -20,
      vendor: "Eged",
      date: "2022-11-08 22:32:22",
      categoryId: 1,
      userId: 0,
    },
    {
      id: 5,
      amount: -489.9,
      vendor: "Agam Liderim",
      date: "2022-10-17 06:37:10",
      categoryId: 6,
      userId: 0,
    },
    {
      id: 6,
      amount: 10000,
      vendor: "CyberArk",
      date: "2022-10-26 12:52:36",
      categoryId: 10,
      userId: 0,
    },
    {
      id: 7,
      amount: -100,
      vendor: "Zer4U",
      date: "2022-11-03 17:02:34",
      categoryId: 7,
      userId: 0,
    },
    {
      id: 8,
      amount: -129.9,
      vendor: "Teder",
      date: "2022-10-14 21:04:13",
      categoryId: 8,
      userId: 0,
    },
    {
      id: 9,
      amount: -70,
      vendor: "Shalvata",
      date: "2022-11-10 07:52:09",
      categoryId: 8,
      userId: 0,
    },
    {
      id: 10,
      amount: 70,
      vendor: "Yossi",
      date: "2022-13-10 08:52:09",
      categoryId: 11,
      userId: 0,
    },
  ]);
  const [categories, setCategories] = useState([
    { id: 0, name: "Housing" },
    { id: 1, name: "Transportation" },
    { id: 2, name: "Food" },
    { id: 3, name: "Utilities" },
    { id: 4, name: "Insurance" },
    { id: 5, name: "Medical & Healthcare" },
    { id: 6, name: "Investing" },
    { id: 7, name: "Gifts" },
    { id: 8, name: "Entertainment" },
    { id: 9, name: "Car" },
    { id: 10, name: "Salary" },
    { id: 11, name: "Bit" },
  ]);

  function getTransactionsObjects() {
    return transactions.map(
      t =>
        new Transaction(
          t.amount,
          t.vendor,
          t.date,
          categories.find(c => c.id === t.categoryId).name
        )
    );
  }

  return (
    <Router>
      <div className="app">
        <NavBar></NavBar>
        <div className="routes">
          <Switch>
            <Route
              exact
              path="/transactions"
              render={() => (
                <Transactions transactions={getTransactionsObjects()} />
              )}
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
