import './App.css';
import React, { useState, useEffect} from "react"
//import { hit as Hit} from "/Users/christian/desktop/ML-Blackjack/Back-End/deckL.py"; 

function App() {
  
  const [data, setData] = useState([{}])
  const stack = 100;
  const bet = 10;
  const [pHand, setPHand] = useState([" ", " "])
  const [dHand, setDHand] = useState([" ", " "])

  const handleHit = () => {
    console.log("Hit")
  }
  
  const handleStay = () => {
    console.log("Stay")
  }

  useEffect (() => {
    fetch("/deal").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        setPHand(data["Player"])
        setDHand(data["Dealer"])
      }
    )
  }, [])

  return (
    <div className="App">
      <div className = "Header"></div>
        <h1> Welcome to Machine Learning Blackjack</h1>
      
      <div className = "Dealer"></div>
        <h1>Dealer's Hand:</h1>
        <p>{dHand}</p>
      <div className = "player"></div>
        <p> {pHand} </p>
        <p>Bet: {bet} </p>
        <button onClick = {handleHit}> Hit </button>
        <button onClick = {handleStay}> Stay </button>
        <p>Stack: {stack}</p>
    </div>
  );
}

export default App;
