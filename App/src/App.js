import './App.css';
import React, { useState, useEffect} from "react"
//import { hit as Hit} from "/Users/christian/desktop/ML-Blackjack/Back-End/deckL.py"; 

function App() {
  //const hit = () => {
    //Hit(); 
    //console.log()
  //}
  const [data, setData] = useState([{}])
  const stack = 100;
  const bet = 10;
  const dCard1 = "Ten";
  const dCard2 = "Ace";
  const pCard1 = "Ten";
  const pCard2 = "Ace";

  useEffect (() => {
    fetch("/main").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])
  
  return (
    <div className="App">
      <div className = "Header"></div>
        <h1> Welcome to Machine Learning Blackjack</h1>
      
      <div className = "Dealer"></div>
        <h1>Dealer's Hand:</h1>
        <p>{dCard1} {dCard2}</p>
      <div className = "player"></div>
        <p> {pCard1} {pCard2} </p>
        <p>Bet: {bet} </p>
        <button> Hit </button>
        <button> Stay </button>
        <p>Stack: {stack}</p>
    </div>
  );
}

export default App;
