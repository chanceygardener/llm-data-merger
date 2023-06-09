import LlmAggregatorApp from './components/llmAggregator';
import React, { useState, useEffect } from 'react';

import styles from './App.css';


const Login = () => {
  // janky simple password protection, just to not make it too too easy
  // for people to overuse my openai credits... Acknowledged that someone
  // could if they really wanted to.

  const [isVerified, setIsVerified] = useState(false);
  const [userEnteredWrong, setUserEnteredWrong] = useState(false);
  const [inputPassword, setInputPassword] = useState(null);




  async function digestMessage(message) {
    const encoder = new TextEncoder();
    const data = encoder.encode(message);
    const digest = await crypto.subtle.digest('SHA-256', data);
    const hash = Array.prototype.map.call(new Uint8Array(digest),
      x => (('00' + x.toString(16)).slice(-2))).join('')
    return hash;
  }

  const checkPw = (e) => {
    console.log(`Submission`);
    e.preventDefault();
    const pwHash = "31d75eb41aeca360be964b5b7012b279c4f822ee4c4144b265ba14da77513548";
    const userInput = document.getElementById("password").value;
    console.log(`User input is: ${userInput}`);
    digestMessage(userInput).then((inputHash) => {
      console.log(`input hash is ${JSON.stringify(inputHash)}`);
      if (inputHash === pwHash) {
        setIsVerified(true);
      } else {
        setUserEnteredWrong(true);
      }
    });
  }


  return (
    <>
      {isVerified ? <LlmAggregatorApp /> : (
        <form onSubmit={checkPw}>
          {userEnteredWrong ? <p>Incorrect password</p> : <></>}
          <input type="text" id="password" name="password" />
          <div className={styles.PasswordSubmit}>
            <button className={styles.Button}>
              Enter the password Ian provided you.
            </button>
          </div >
        </form>)}
    </>
  )

}

function App() {
  return (
    <div className="App">
      <Login />
    </div>
  );
}

export default App;
