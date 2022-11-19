import React from "react";
import "./Operations.css";
import InsertTransaction from "./InsertTransaction/InsertTransaction";

export default function Operations(props) {
  return (
    <div>
      <InsertTransaction
        updateBalance={props.updateBalance}
      ></InsertTransaction>
    </div>
  );
}
