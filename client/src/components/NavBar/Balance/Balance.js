import React from "react";

export default function Balance(props) {
  return (
    <div>
      <strong>Balance: </strong>
      <span className={props.balance >= 0 ? "plus" : "minus"}>
        {props.balance}
      </span>
    </div>
  );
}
