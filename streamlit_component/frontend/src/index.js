import React from "react"
import ReactDOM from "react-dom"
import MyComponent from "./MyComponent"
import MyGameComp from "./MyGameComp"

ReactDOM.render(
  <React.StrictMode>
    <MyComponent />
    <MyGameComp />

  </React.StrictMode>,
  document.getElementById("root")
)